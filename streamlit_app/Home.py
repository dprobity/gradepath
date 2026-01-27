import streamlit as st

st.set_page_config(
    page_title="GradePath",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to match the PPT visual style (Clean white, Indigo/Blue accent)
st.markdown("""
    <style>
        .stApp {
            background-color: #F8F9FA;
        }
        .main-header {
            font-family: 'Inter', sans-serif;
            color: #1E3A8A; /* PPT dark blue */
            font-weight: 700;
        }
        .stButton>button {
            background-color: #2563EB; /* PPT primary blue */
            color: white;
            border-radius: 8px;
            font-weight: 600;
        }
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([1, 1])

with col1:
    st.image("https://placehold.co/100x100/2563EB/FFFFFF.png?text=GP", width=80) # Placeholder logo
    st.markdown("<h1 class='main-header'>GradePath</h1>", unsafe_allow_html=True)
    st.subheader("Your Academic Compass for Fall 2025")
    
    st.markdown("""
    **GradePath** unifies your academic life.
    * **Ingest** syllabi and slides to build a course knowledge base.
    * **Visualize** your progress with the Grade Scenarios dashboard.
    * **Plan** with an AI-optimized schedule.
    * **Chat** with an assistant that knows your specific course materials.
    """)
    
    if st.button("Go to Overview →"):
        st.switch_page("pages/2_📊_Overview.py")

with col2:
    st.info("👋 **Welcome, Alex.** \n\nYou have **3 high-priority tasks** due in the next 48 hours. Your `CHEM 101` grade is trending upward.")

st.divider()
st.caption("v0.1.0 Prototype | Powered by LangGraph & Streamlit")