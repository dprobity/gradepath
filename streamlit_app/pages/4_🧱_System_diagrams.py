import streamlit as st
import os

st.set_page_config(page_title="Architecture | GradePath", page_icon="🧱", layout="wide")

st.title("🧱 System Architecture")
st.markdown("Visualizing the GradePath backend, agent graphs, and data flow.")

tabs = st.tabs(["High Level Journey", "Backend & Agents"])

# Helper to load images safely
def show_image_or_placeholder(path, caption):
    if os.path.exists(path):
        st.image(path, caption=caption, use_column_width=True)
    else:
        st.warning(f"Image not found at {path}. Please add the architecture diagrams to the 'assets' folder.")
        st.code(f"Placeholder for: {caption}")

with tabs[0]:
    st.header("User Journey & Data Flow")
    st.markdown("From student interaction to backend ingestion and LLM processing.")
    show_image_or_placeholder("streamlit_app/assets/user_journey.png", "System Overview Diagram")

with tabs[1]:
    st.header("Backend Architecture")
    st.markdown("FastAPI, LangGraph Agents, MCP Tools, and Vector Persistence.")
    show_image_or_placeholder("streamlit_app/assets/backend_arch.png", "Backend Architecture Diagram")