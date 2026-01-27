import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import uuid
from typing import List, Dict, Any, Optional
import logging
from .config import VECTOR_DB_PATH, EMBEDDING_MODEL_NAME, get_collection_name

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VectorStore:
    """
    Manages per-course vector embeddings using ChromaDB.
    Handles embedding generation, storage, and semantic retrieval.
    """

    def __init__(self):
        """Initialize ChromaDB client and load the embedding model."""
        logger.info(f"Initializing VectorStore at {VECTOR_DB_PATH}")
        
        # persistent client
        self.client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
        
        # Load embedding model (384 dim)
        # Note: In production, consider moving model loading to a singleton or dependency injection
        logger.info(f"Loading embedding model: {EMBEDDING_MODEL_NAME}")
        self.model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    def _get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for a list of texts."""
        embeddings = self.model.encode(texts)
        return embeddings.tolist()

    def ensure_course_collection(self, course_id: str) -> chromadb.Collection:
        """
        Get or create a Chroma collection for a specific course.
        
        Args:
            course_id: e.g., "chem101"
        """
        collection_name = get_collection_name(course_id)
        try:
            return self.client.get_or_create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"}
            )
        except Exception as e:
            logger.error(f"Failed to ensure collection for {course_id}: {e}")
            raise

    def store_chunks(self, course_id: str, chunks: List[Dict[str, Any]]) -> bool:
        """
        Embed and store document chunks in the course collection.

        Args:
            course_id: The course identifier (e.g., "chem101").
            chunks: List of dicts, each must have "text" and "metadata".
                    Example: [{"text": "...", "metadata": {"source": "syllabus.pdf"}}]
        """
        if not chunks:
            return False

        try:
            collection = self.ensure_course_collection(course_id)
            
            texts = [chunk["text"] for chunk in chunks]
            metadatas = [chunk.get("metadata", {}) for chunk in chunks]
            ids = [str(uuid.uuid4()) for _ in chunks]

            # Generate embeddings
            embeddings = self._get_embeddings(texts)

            # Add to Chroma
            collection.add(
                documents=texts,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
            logger.info(f"Stored {len(chunks)} chunks for course {course_id}")
            return True

        except Exception as e:
            logger.error(f"Error storing chunks for {course_id}: {e}")
            return False

    def retrieve_chunks(
        self, 
        course_id: str, 
        query: str, 
        k: int = 5, 
        filter_metadata: Optional[Dict] = None
    ) -> List[Dict[str, Any]]:
        """
        Perform semantic search for a query within a course.

        Args:
            course_id: The course to search within.
            query: The user's question or search phrase.
            k: Number of results to return.
            filter_metadata: Optional ChromaDB filter dict (e.g., {"type": "syllabus"}).

        Returns:
            List of dicts containing 'text', 'metadata', and 'score'.
        """
        try:
            collection = self.ensure_course_collection(course_id)
            query_embedding = self._get_embeddings([query])

            results = collection.query(
                query_embeddings=query_embedding,
                n_results=k,
                where=filter_metadata
            )

            # Format results into a clean list of dicts
            formatted_results = []
            if results['documents']:
                for i in range(len(results['documents'][0])):
                    formatted_results.append({
                        "text": results['documents'][0][i],
                        "metadata": results['metadatas'][0][i] if results['metadatas'] else {},
                        "id": results['ids'][0][i],
                        "distance": results['distances'][0][i] if results['distances'] else 0.0
                    })
            
            return formatted_results

        except Exception as e:
            logger.error(f"Error retrieving chunks for {course_id}: {e}")
            return []

    def list_collections(self) -> List[str]:
        """List all active course collections."""
        return [c.name for c in self.client.list_collections()]