from storage.vector import VectorStore
from tools.mcp_calendar import create_calendar_event
from typing import List, Dict, Any
import re
import os

class SyllabusProcessor:
    def __init__(self):
        self.vector_store = VectorStore()
    
    def process_syllabus(self, text: str, course_id: str, folder: str = "syllabus") -> Dict[str, Any]:
        """
        Orchestrates the syllabus ingestion pipeline:
        1. Extract Events (Regex)
        2. Call MCP Calendar Tool
        3. Chunk & Store in Vector DB
        """
        # 1. Extract structured events
        events = self._extract_events(text)
        
        # 2. Create MCP calendar events
        calendar_results = []
        for event in events:
            # MCP Tool Call
            result = create_calendar_event(
                course_id=course_id,
                title=event["title"],
                raw_date=event["raw_date"]
            )
            calendar_results.append(result)
        
        # 3. Create RAG chunks
        chunks = self._create_chunks(text, course_id, folder)
        self.vector_store.store_chunks(course_id, chunks)
        
        return {
            "status": "success",
            "events_found": len(events),
            "events_added": len(calendar_results),
            "chunks_stored": len(chunks),
            "calendar_results": calendar_results
        }
    
    def _extract_events(self, text: str) -> List[Dict]:
        """Extract due dates, exams, office hours via regex"""
        patterns = [
            r'(lab|report|assignment|hw|problem set).*?(due|submit).*?(fri|thu|jan 30|jan 31)',
            r'(midterm|exam|test|final).*?(jan|feb|mar|thu|fri)',
            r'(office hours?|oh).*?(mon|tue|wed|thu|fri).*?(\d+[:\s]\d+)(am|pm)'
        ]
        events = []
        seen = set()
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE | re.DOTALL)
            for match in matches:
                clean_match = match.group(0).strip().replace('\n', ' ')
                if clean_match not in seen:
                    events.append({
                        "title": clean_match[:60], # Truncate for title
                        "raw_date": clean_match,
                        "type": self._classify_event(clean_match)
                    })
                    seen.add(clean_match)
                    
        return events[:8]  # Limit to top 8 to prevent noise
    
    def _create_chunks(self, text: str, course_id: str, folder: str) -> List[Dict]:
        """Simple paragraph-based chunking"""
        # Split by double newline to get paragraphs
        raw_chunks = [c.strip() for c in text.split('\n\n') if len(c.strip()) > 30]
        
        return [{
            "text": chunk[:800],
            "metadata": {
                "course_id": course_id, 
                "folder": folder, 
                "type": "syllabus",
                "source": "ingestion_pipeline"
            }
        } for chunk in raw_chunks[:15]] # Limit chunks for prototype
    
    def _classify_event(self, text: str) -> str:
        text_lower = text.lower()
        if 'lab' in text_lower or 'report' in text_lower:
            return 'assignment'
        if 'midterm' in text_lower or 'exam' in text_lower:
            return 'exam'
        return 'office_hours'