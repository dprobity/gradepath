from typing import Dict, Any
try:
    from mcp.server import ToolSchema, tool
except ImportError:
    # Fallback/Mock for prototype if mcp library isn't installed
    def tool():
        return lambda func: func
    class ToolSchema:
        pass

@tool()
def create_calendar_event(course_id: str, title: str, raw_date: str) -> Dict[str, Any]:
    """Create Google Calendar event from syllabus extraction.
    
    Args:
        course_id: chem101, phys202
        title: Lab Report 1, Midterm Exam
        raw_date: due Friday Jan 30 at 5pm
    
    Returns:
        {"status": "success", "event_id": "abc123"}
    """
    # Placeholder MCP implementation (Real MCP server wiring happens in Phase 2)
    # This acts as the "Tool Executor"
    print(f"🗓️ MCP Calendar Tool Triggered: [{course_id}] {title} on {raw_date}")
    
    return {
        "status": "success", 
        "event_id": f"{course_id}_{title[:10].replace(' ', '_')}",
        "title": title,
        "course_id": course_id,
        "timestamp": raw_date
    }

# Export tool schema for the Agent (if needed later)
calendar_tools = [
    # create_calendar_event.schema() # Uncomment if using full MCP SDK
]