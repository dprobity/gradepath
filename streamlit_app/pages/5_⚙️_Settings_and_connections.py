import streamlit as st

st.set_page_config(page_title="Settings | GradePath", page_icon="⚙️", layout="wide")

st.title("⚙️ Settings & Connections")

col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 User Profile")
    with st.container(border=True):
        st.text_input("Full Name", value="David Amobi Emehelu")
        st.text_input("Institution", value="University of Alabama")
        st.selectbox("Major", ["Chemical Engineering", "Computer Science", "Physics"])
        st.selectbox("Academic Year", ["Freshman", "Sophomore", "Junior", "Senior", "Graduate"])
        if st.button("Save Profile"):
            st.toast("Profile updated!")

    st.subheader("🔒 Security & Privacy")
    with st.container(border=True):
        st.checkbox("Enable Two-Factor Authentication (2FA)", value=True)
        st.checkbox("Allow AI to draft emails (requires review)", value=True)
        st.checkbox("Allow AI to auto-send emails (Trusted contacts only)", value=False)
        st.button("Clear Vector Memory", type="primary")

with col2:
    st.subheader("🔌 MCP Tool Integrations")
    st.markdown("Manage permissions for external data sources.")
    
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        c1.markdown("**Canvas / Blackboard LMS**")
        c2.toggle("Connected", value=True)
        st.caption("Last synced: 2 hours ago")
        
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        c1.markdown("**University Email** (Outlook/Gmail)")
        c2.toggle("Connected", value=True)
        
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        c1.markdown("**Calendar**")
        c2.toggle("Connected", value=True)
        
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        c1.markdown("**Cloud Storage** (Drive/OneDrive)")
        c2.toggle("Connected", value=False)