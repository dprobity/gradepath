import streamlit as st
import pandas as pd
import requests
import time

st.set_page_config(page_title="Ingestion | GradePath", page_icon="📥", layout="wide")

st.markdown("## 📥 Course Ingestion")
st.markdown("Upload documents to build your AI Knowledge Base. Extract schedules, assignments, and concepts automatically.")

# Layout: Ingestion Form (Left) vs. Recent Activity (Right)
col_left, col_right = st.columns([2, 1])

with col_left:
    with st.container(border=True):
        st.subheader("Add New Material")
        
        # Course & Folder Selection
        c1, c2 = st.columns(2)
        # Using keys to access these values in session state if needed
        course_id = c1.selectbox(
            "Select Course", 
            ["chem101", "phys202", "math301", "engl102"], 
            key="active_course"
        )
        folder_type = c2.selectbox(
            "Target Folder", 
            ["syllabus", "assignments", "notes"], 
            key="folder_type"
        )
        
        # File Uploader
        uploaded_file = st.file_uploader(
            "Upload Syllabus or Course PDF", 
            type=["pdf", "txt", "md"],
            accept_multiple_files=False # Prototype: Single file for clarity
        )
        
        if uploaded_file:
            st.info(f"Ready to ingest into **{course_id} / {folder_type}**")
            
            # REAL BACKEND CONNECTION
            if st.button("🚀 Process Syllabus → Calendar + AI", type="primary"):
                with st.spinner("Extracting events → Triggering MCP Calendar Tool → Indexing for AI..."):
                    
                    # 1. Prepare Request to FastAPI
                    try:
                        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                        data = {
                            "course_id": course_id,
                            "folder": folder_type
                        }
                        
                        # 2. Call the Ingestion Endpoint
                        response = requests.post(
                            "http://localhost:8000/api/v1/ingest/upload", 
                            files=files, 
                            data=data, 
                            timeout=30
                        )
                        
                        # 3. Handle Response
                        if response.status_code == 200:
                            result = response.json()
                            
                            st.success(result["message"])
                            st.balloons()
                            
                            # 4. Show MCP Tool Output (Calendar Events)
                            if result.get("events"):
                                with st.expander("🗓️ MCP Calendar Tool Logs (Events Created)", expanded=True):
                                    for event in result["events"]:
                                        st.markdown(f"**✅ [MCP] Created Event:** `{event['title']}`")
                                        st.caption(f"Date Extraction: {event['timestamp']}")
                                        st.divider()
                            
                        else:
                            st.error(f"❌ Server Error: {response.text}")
                            
                    except requests.exceptions.ConnectionError:
                         st.error("❌ Could not connect to backend. Is `uvicorn app.main:app` running?")
                    except Exception as e:
                        st.error(f"❌ An error occurred: {e}")

with col_right:
    st.subheader("Recent Activity")
    
    # Mock Activity Feed (You can connect this to sqlite later)
    activities = [
        {"action": "MCP Calendar Tool", "file": "Triggered via Syllabus", "time": "Just now", "status": "✅ Active"},
        {"action": "Vectorized Notes", "file": "Week3_Thermodynamics.pptx", "time": "1 hour ago", "status": "✅ Success"},
        {"action": "Failed Upload", "file": "Corrupted_Lab.docx", "time": "Yesterday", "status": "❌ Error"},
    ]
    
    for act in activities:
        with st.container(border=True):
            st.markdown(f"**{act['action']}**")
            st.caption(f"{act['file']} • {act['time']}")
            if "Success" in act['status'] or "Active" in act['status']:
                st.markdown(f":green[{act['status']}]")
            else:
                st.markdown(f":red[{act['status']}]")

st.markdown("### 📋 Ingested Documents Inventory")
# Static data for now, but ready to be replaced with VectorStore.list_documents()
data = {
    "Course": ["CHEM 101", "PHYS 202", "CHEM 101", "MATH 301"],
    "Document Name": ["Fall2025_Syllabus.pdf", "Lecture_04_Kinematics.pptx", "Lab_Safety_Guide.pdf", "Homework_2.docx"],
    "Category": ["Syllabus", "Lecture Notes", "Reference", "Assignments"],
    "Extracted Items": ["14 Dates, 2 Policies", "5 Key Concepts", "12 Rules", "4 Problems"],
    "Date Added": ["Aug 24, 2025", "Sept 10, 2025", "Aug 26, 2025", "Sept 12, 2025"]
}
st.dataframe(pd.DataFrame(data), use_container_width=True)