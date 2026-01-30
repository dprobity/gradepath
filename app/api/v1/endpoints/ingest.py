from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from ingestion.processor import SyllabusProcessor
import shutil
import os

router = APIRouter(prefix="/ingest", tags=["ingestion"])

@router.post("/upload")
async def upload_syllabus(
    course_id: str = Form(...),
    folder: str = Form("syllabus"),
    file: UploadFile = File(...)
):
    """
    Uploads a syllabus file, extracts events for Calendar (MCP), 
    and indexes content for RAG (VectorStore).
    """
    # 1. Save uploaded file temporarily
    upload_dir = ".data/uploads"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = f"{upload_dir}/{file.filename}"
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File save failed: {e}")
    
    # 2. Process with MCP pipeline
    try:
        processor = SyllabusProcessor()
        
        # SIMPLIFIED TEXT EXTRACTION (Direct read, PyMuPDF added in Phase 2)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        
        result = processor.process_syllabus(text, course_id, folder)
        
        return {
            "status": "success",
            "message": f"✅ Added {result['events_added']} calendar events, stored {result['chunks_stored']} chunks",
            "course_id": course_id,
            "events": result["calendar_results"][:3]  # Return preview of created events
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {e}")
