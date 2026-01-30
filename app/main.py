from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import ingest

# Initialize FastAPI application
app = FastAPI(
    title="GradePath API",
    description=(
        "Backend API for GradePath, a student productivity AI system. "
        "Powers LangGraph agents, MCP-style tools, and RAG workflows "
        "for course management and student assistance."
    ),
    version="0.1.0",
)

# CORS Configuration
# Allow requests from local Streamlit and future React frontend
origins = [
    "http://localhost:8501",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------------------
# API Router Configuration
# ------------------------------------------------------------------------------

api_router = APIRouter()

# TODO: Import and include domain-specific routers from app.api.v1
# These modules will handle specific business logic for GradePath.

# from app.api.v1 import auth, dashboard, chat, ingest

# api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
# api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
# api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
# api_router.include_router(ingest.router, prefix="/ingest", tags=["ingest"])

# Mount the main v1 router
app.include_router(api_router, prefix="/api/v1")
app.include_router(ingest.router, prefix="/api/v1")


# ------------------------------------------------------------------------------
# Health Check
# ------------------------------------------------------------------------------

@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """
    Simple health check to ensure the API is reachable.
    """
    return {"status": "ok"}