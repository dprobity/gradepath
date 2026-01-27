import streamlit as st
import pandas as pd

st.set_page_config(page_title="Overview | GradePath", page_icon="📊", layout="wide")

# -- PPT MATCHING HEADER --
st.title("Overview")
st.markdown("Your academic compass for Fall 2025")

# -- MAIN BANNER (PPT: Dark Blue Background) --
# We simulate the PPT's "Current Status" banner using custom HTML/CSS injection
st.markdown("""
<div style="background-color: #312E81; color: white; padding: 30px; border-radius: 15px; margin-bottom: 25px;">
    <span style="background-color: rgba(255,255,255,0.2); padding: 5px 10px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">CURRENT STATUS</span>
    <h2 style="margin-top: 15px; color: white;">You are on track, Alex.</h2>
    <p style="font-size: 1.1em; opacity: 0.9;">Based on your current trajectory, you are projected to maintain a <strong>3.8 GPA</strong>. Your next high-effort week starts in 4 days.</p>
    <div style="display: flex; justify-content: flex-end; margin-top: 20px;">
        <div style="text-align: center; margin-left: 40px;">
            <h1 style="margin: 0; color: white;">4</h1>
            <span style="font-size: 0.8em; opacity: 0.8;">DEADLINES</span>
        </div>
        <div style="text-align: center; margin-left: 40px;">
            <h1 style="margin: 0; color: white;">12<span style="font-size:0.5em">h</span></h1>
            <span style="font-size: 0.8em; opacity: 0.8;">STUDY LOAD</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# -- TWO COLUMN LAYOUT (High Priority vs Risk Monitor) --
col_high, col_risk = st.columns([2, 1])

with col_high:
    st.subheader("⚡ High Priority")
    st.caption("Sorted by Impact")
    
    # Task Card 1 (Urgent)
    with st.container(border=True):
        c1, c2 = st.columns([0.8, 0.2])
        with c1:
            st.markdown("**:orange[DUE TOMORROW]** • CHEM 101")
            st.markdown("### Lab Report: Chemical Kinetics")
            st.caption("Weighted 15% of final grade. Estimated effort: 2h.")
        with c2:
            st.markdown("⚠️", help="High Urgency")
            
    # Task Card 2 (Upcoming)
    with st.container(border=True):
        c1, c2 = st.columns([0.8, 0.2])
        with c1:
            st.markdown("**:blue[UPCOMING]** • PHYS 202")
            st.markdown("### Midterm Review Set")
            st.caption("Study block scheduled for Saturday. Impact: High.")
        with c2:
            st.markdown("▶️", help="Start Task")

with col_risk:
    st.subheader("Risk Monitor")
    
    with st.container(border=True):
        r1, r2 = st.columns([1, 1])
        r1.markdown("**MATH 301**")
        r2.markdown(":red[**AT RISK**]")
        
        st.progress(0.78, text="Current: 78% (C+)")
        st.caption("Goal: 85% (B)")
        st.markdown("You need a **92%** on the next quiz to get back on track.")
        st.button("View Recovery Scenarios", use_container_width=True)
        
    with st.container(border=True):
        r1, r2 = st.columns([0.2, 0.8])
        r1.image("https://placehold.co/40x40/green/white.png?text=A", width=40)
        r2.markdown("**CHEM 101**\nGrade: 94% (A)")
        st.success("↗ Trending upward vs last week")

st.markdown("---")

# -- DETAILED VIEW EXPANDER --
with st.expander("🔍 View Detailed Dashboard (Tasks, Full Grades, AI Summary)", expanded=False):
    st.markdown("### 📊 Detailed Dashboard")
    
    d_col1, d_col2 = st.columns([1, 1])
    
    with d_col1:
        st.subheader("Today's Task List")
        tasks = [
            {"done": False, "task": "Submit CHEM 101 Lab", "due": "11:59 PM"},
            {"done": True, "task": "Read PHYS 202 Ch. 4", "due": "2:00 PM"},
            {"done": False, "task": "Email Prof. about extension", "due": "ASAP"},
        ]
        for t in tasks:
            st.checkbox(f"{t['task']} ({t['due']})", value=t['done'])
            
    with d_col2:
        st.subheader("🧠 AI Weekly Summary")
        st.info("""
        **Analysis:** You have a heavy reading load this week for PHYS 202. 
        **Strategy:** I suggest breaking the reading into 30-minute blocks on Tuesday/Thursday.
        **Note:** Your CHEM 101 lab report typically takes 3 hours; start by Wednesday evening.
        """)
        
        st.subheader("Detailed Grades")
        g_col1, g_col2, g_col3 = st.columns(3)
        g_col1.metric("CHEM 101", "94%", "+2%")
        g_col2.metric("PHYS 202", "88%", "0%")
        g_col3.metric("MATH 301", "78%", "-4%")