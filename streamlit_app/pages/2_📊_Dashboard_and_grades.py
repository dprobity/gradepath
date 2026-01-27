import streamlit as st

st.set_page_config(page_title="Dashboard | GradePath", page_icon="📊", layout="wide")

st.title("📊 Today's Dashboard")
st.markdown(f"**{st.session_state.get('user_name', 'Student')}** | {st.session_state.get('institution', 'University of Alabama')}")

col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    st.subheader("✅ Today's Tasks")
    
    # Mock Task Data
    task_container = st.container(border=True)
    task_container.checkbox("Submit Lab Report 3 (CHEM 101)", value=False)
    task_container.checkbox("Read Chapter 4: Thermodynamics (PHYS 202)", value=False)
    task_container.checkbox("Email Prof. Richards re: Extension", value=True)
    
    st.subheader("📅 Upcoming Deadlines")
    deadlines = [
        {"task": "Project Proposal", "course": "CS 301", "due": "Tomorrow, 11:59 PM", "urgent": True},
        {"task": "Midterm Exam", "course": "HIST 102", "due": "Oct 17 (3 days)", "urgent": False},
        {"task": "Problem Set 4", "course": "MATH 201", "due": "Oct 20 (6 days)", "urgent": False},
    ]
    
    for item in deadlines:
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            c1.markdown(f"**{item['task']}**")
            c1.caption(item['course'])
            if item['urgent']:
                c2.error(item['due'])
            else:
                c2.info(item['due'])

with col_right:
    st.subheader("🤖 AI Summary of my Week")
    st.info(
        """
        **Analysis:** You have a moderate workload this week with a major deadline on Friday. 
        Focus on your **CHEM 101 Lab Report** today. 
        
        **Suggestion:** Plan study sessions for your History midterm on Thursday afternoon. 
        I noticed you missed a reading for Physics; should I add that to your tasks?
        """, icon="🧠"
    )
    
    st.subheader("📈 Grades Snapshot")
    
    # Metric Row 1
    m1, m2 = st.columns(2)
    m1.metric(label="CHEM 101", value="92%", delta="A")
    m2.metric(label="PHYS 202", value="85%", delta="-2%")
    
    # Metric Row 2
    m3, m4 = st.columns(2)
    m3.metric(label="MATH 201", value="78%", delta="C+")
    m4.metric(label="CS 301", value="95%", delta="A+")