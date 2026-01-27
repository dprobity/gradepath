import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(os.getcwd())
DATA_DIR = BASE_DIR / ".data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Vector Store Settings
VECTOR_DB_PATH = str(DATA_DIR / "chroma_db")
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
VECTOR_DIMENSION = 384

# Memory Store Settings
MEMORY_DB_PATH = f"sqlite:///{DATA_DIR}/gradepath_memory.db"
MEMORY_TABLE_NAME = "student_memory"

# Collection Naming Convention
def get_collection_name(course_id: str) -> str:
    """Format course ID into a valid Chroma collection name."""
    clean_name = course_id.lower().replace(" ", "_")
    return f"gradepath_{clean_name}"