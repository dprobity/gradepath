import streamlit as st

st.set_page_config(page_title="Settings | GradePath", page_icon="⚙️", layout="wide")

st.title("⚙️ Settings")

# Profile Section
st.subheader("👤 Account")
with st.container(border=True):
    c1, c2 = st.columns(2)
    c1.text_input("Full Name", "Alex Chen")
    c2.text_input("Institution", "University of Alabama")
    c1.text_input("Major", "Chemical Engineering")
    c2.selectbox("Year", ["Freshman", "Sophomore", "Junior", "Senior"])

# Integrations Section (MCP Tools)
st.subheader("🔌 Connections (MCP Tools)")
st.caption("Manage external data sources for the AI agents.")

cols = st.columns(2)

with cols[0]:
    with st.container(border=True):
        st.markdown("### 🎓 Learning Management System")
        st.toggle("Canvas / Blackboard", value=True)
        st.caption("Status: ✅ Synced (2h ago)")
        
    with st.container(border=True):
        st.markdown("### 📅 Calendar")
        st.toggle("Google Calendar / Outlook", value=True)
        st.caption("Status: ✅ Synced (Real-time)")

with cols[1]:
    with st.container(border=True):
        st.markdown("### 📧 Email")
        st.toggle("University Email", value=True)
        st.caption("Status: ✅ Synced (10m ago)")
        
    with st.container(border=True):
        st.markdown("### ☁️ Cloud Storage")
        st.toggle("Google Drive / OneDrive", value=False)
        st.caption("Status: ❌ Not Connected")

# Security Section
st.subheader("🔒 Security & Privacy")
with st.container(border=True):
    st.checkbox("Enable Two-Factor Authentication (2FA)", value=True)
    st.checkbox("Allow AI to read course emails", value=True)
    st.checkbox("Allow AI to add events to calendar", value=True)
    
    st.markdown("---")
    st.button("🗑️ Clear AI Memory Cache", type="secondary")
    st.button("🚪 Log Out", type="primary")