import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Ingestion | GradePath", page_icon="📥", layout="wide")

st.title("📥 Ingestion & Materials")
st.markdown("Upload course documents or sync with external tools to build your personal knowledge base.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Manual Upload")
    uploaded_files = st.file_uploader(
        "Upload Course PDFs, Slides, or Assignments", 
        type=["pdf", "docx", "pptx"], 
        accept_multiple_files=True
    )
    
    st.write("OR")
    
    lms_link = st.text_input("Paste specific LMS Assignment Link (Canvas/Blackboard)")
    
    if st.button("🚀 Ingest Materials", type="primary"):
        if uploaded_files or lms_link:
            st.success("Ingestion agent triggered! (Stub)")
        else:
            st.error("Please provide a file or link.")

with col2:
    st.subheader("Active Data Sources")
    st.markdown("Status of your **MCP Tool Connectors**:")
    
    st.checkbox("🎓 Canvas LMS", value=True, disabled=True, help="Connected via API Token")
    st.checkbox("📧 University Email", value=True, disabled=True, help="Connected via OAuth")
    st.checkbox("📅 Calendar", value=True, disabled=True)
    st.checkbox("☁️ Google Drive", value=False, disabled=True)
    
    st.caption("Manage connections in Settings.")

st.divider()

st.subheader("📚 Recently Ingested Documents")
# Mock Data for Chemical Engineering Student
data = {
    "Course": ["CHEM 101", "PHYS 202", "MATH 201", "CHEM 101", "Global"],
    "Type": ["Syllabus", "Lecture Slides", "Assignment", "Lab Report", "Email"],
    "Source": ["Upload", "Canvas", "Canvas", "Drive", "Outlook"],
    "Date": ["2023-10-01", "2023-10-03", "2023-10-05", "2023-10-06", "2023-10-07"],
    "Status": ["✅ Vectorized", "✅ Vectorized", "✅ Vectorized", "🔄 Processing", "✅ Vectorized"]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True, hide_index=True)