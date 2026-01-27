from sqlalchemy import create_engine, Column, String, Integer, DateTime, JSON, Text
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from typing import List, Dict, Any, Optional
import json
import logging
from .config import MEMORY_DB_PATH, MEMORY_TABLE_NAME

# Configure logging
logger = logging.getLogger(__name__)

# SQLAlchemy Base
Base = declarative_base()

class StudentMemoryModel(Base):
    """SQLAlchemy model for student memory table."""
    __tablename__ = MEMORY_TABLE_NAME

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, index=True, nullable=False)
    course_id = Column(String, index=True, nullable=True) # Nullable for global context
    memory_type = Column(String, nullable=False) # e.g., 'chat', 'plan', 'preference'
    payload = Column(JSON, nullable=False) # Stores the actual content/summary
    created_at = Column(DateTime, default=datetime.utcnow)

class MemoryStore:
    """
    Manages persistent student memory using SQLite and SQLAlchemy.
    Stores chat history, user preferences, and study plans.
    """

    def __init__(self, db_url: str = MEMORY_DB_PATH):
        """Initialize DB engine and create tables."""
        logger.info(f"Initializing MemoryStore at {db_url}")
        
        self.engine = create_engine(
            db_url, 
            connect_args={"check_same_thread": False} # Needed for SQLite with FastAPI
        )
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def append_memory(
        self, 
        user_id: str, 
        memory_type: str, 
        payload: Dict[str, Any], 
        course_id: Optional[str] = None
    ) -> bool:
        """
        Save a new memory entry.

        Args:
            user_id: ID of the student.
            memory_type: Category (e.g., 'chat_history', 'user_preference').
            payload: Dictionary containing the data.
            course_id: Optional course context.
        """
        session = self.SessionLocal()
        try:
            memory_entry = StudentMemoryModel(
                user_id=user_id,
                course_id=course_id,
                memory_type=memory_type,
                payload=payload,
                created_at=datetime.utcnow()
            )
            session.add(memory_entry)
            session.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to append memory: {e}")
            session.rollback()
            return False
        finally:
            session.close()

    def get_recent_memory(
        self, 
        user_id: str, 
        limit: int = 10, 
        memory_type: Optional[str] = None,
        course_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve recent memory entries.

        Args:
            user_id: ID of the student.
            limit: Number of entries to retrieve.
            memory_type: Filter by type (optional).
            course_id: Filter by course (optional).

        Returns:
            List of dicts containing the payload and metadata.
        """
        session = self.SessionLocal()
        try:
            query = session.query(StudentMemoryModel).filter(StudentMemoryModel.user_id == user_id)

            if memory_type:
                query = query.filter(StudentMemoryModel.memory_type == memory_type)
            
            if course_id:
                query = query.filter(StudentMemoryModel.course_id == course_id)

            # Get latest first
            results = query.order_by(StudentMemoryModel.created_at.desc()).limit(limit).all()

            # Format output
            memories = []
            for row in results:
                memories.append({
                    "id": row.id,
                    "type": row.memory_type,
                    "course_id": row.course_id,
                    "payload": row.payload,
                    "created_at": row.created_at.isoformat()
                })
            
            # Return reversed (oldest first) for chat context reconstruction
            return memories[::-1] 

        except Exception as e:
            logger.error(f"Failed to retrieve memory: {e}")
            return []
        finally:
            session.close()
            
    def clear_memory(self, user_id: str):
        """Debug utility to clear a user's memory."""
        session = self.SessionLocal()
        try:
            session.query(StudentMemoryModel).filter(StudentMemoryModel.user_id == user_id).delete()
            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()