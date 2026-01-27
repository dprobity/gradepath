import streamlit as st
import pandas as pd
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
        course = c1.selectbox("Select Course", ["CHEM 101", "PHYS 202", "MATH 301", "ENGL 102"])
        folder = c2.selectbox("Target Folder", ["Syllabus", "Assignments", "Lecture Notes", "Exams/Quizzes"])
        
        # File Uploader
        uploaded_files = st.file_uploader(
            "Drag and drop PDFs, PPTX, or DOCX files", 
            type=["pdf", "pptx", "docx"],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            st.info(f"Ready to ingest {len(uploaded_files)} file(s) into **{course} / {folder}**")
            
            if st.button("🚀 Process Materials", type="primary"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simulation of Docling/Ingestion pipeline
                status_text.text("Step 1/3: Converting documents with Docling...")
                time.sleep(0.8)
                progress_bar.progress(33)
                
                status_text.text("Step 2/3: Extracting schedule dates & key concepts...")
                time.sleep(0.8)
                progress_bar.progress(66)
                
                status_text.text("Step 3/3: Generating embeddings & updating Vector DB...")
                time.sleep(0.8)
                progress_bar.progress(100)
                
                st.success(f"Successfully ingested {len(uploaded_files)} documents! Calendar updated with 4 new dates.")

with col_right:
    st.subheader("Recent Activity")
    
    # Mock Activity Feed
    activities = [
        {"action": "Extracted Schedule", "file": "Syllabus_CHEM101.pdf", "time": "2 mins ago", "status": "✅ Success"},
        {"action": "Vectorized Notes", "file": "Week3_Thermodynamics.pptx", "time": "1 hour ago", "status": "✅ Success"},
        {"action": "Failed Upload", "file": "Corrupted_Lab.docx", "time": "Yesterday", "status": "❌ Error"},
    ]
    
    for act in activities:
        with st.container(border=True):
            st.markdown(f"**{act['action']}**")
            st.caption(f"{act['file']} • {act['time']}")
            if "Success" in act['status']:
                st.markdown(f":green[{act['status']}]")
            else:
                st.markdown(f":red[{act['status']}]")

st.markdown("### 📋 Ingested Documents Inventory")
data = {
    "Course": ["CHEM 101", "PHYS 202", "CHEM 101", "MATH 301"],
    "Document Name": ["Fall2025_Syllabus.pdf", "Lecture_04_Kinematics.pptx", "Lab_Safety_Guide.pdf", "Homework_2.docx"],
    "Category": ["Syllabus", "Lecture Notes", "Reference", "Assignments"],
    "Extracted Items": ["14 Dates, 2 Policies", "5 Key Concepts", "12 Rules", "4 Problems"],
    "Date Added": ["Aug 24, 2025", "Sept 10, 2025", "Aug 26, 2025", "Sept 12, 2025"]
}
st.dataframe(pd.DataFrame(data), use_container_width=True)