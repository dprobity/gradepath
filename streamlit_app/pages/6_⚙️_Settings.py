import streamlit as st
import os

# Now this import works because Home.py fixed the path!
try:
    from services.calendar import CalendarService
except ImportError:
    st.error("⚠️ System Error: Run the app using 'streamlit run streamlit_app/Home.py'")
    st.stop()

st.set_page_config(page_title="Settings | GradePath", page_icon="⚙️", layout="wide")
st.title("⚙️ Settings")

# 1. Profile Section
st.subheader("👤 Account")
with st.container(border=True):
    c1, c2 = st.columns(2)
    c1.text_input("Full Name", "Zachary Grooves")
    c2.text_input("Institution", "University of Alabama")
    c1.text_input("Major", "Chemical Engineering")
    c2.selectbox("Year", ["Freshman", "Sophomore", "Junior", "Senior"])

# 2. Connections Section
st.subheader("🔌 Connections (MCP Tools)")
st.caption("Manage external data sources for the AI agents.")

# Initialize Service
cal_service = None
try:
    cal_service = CalendarService()
except Exception:
    pass # Fail silently if keys are missing

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 📅 Google Calendar")
        
        # Check connection status
        if cal_service and cal_service.is_connected:
            st.success("✅ Connected as Student")
            st.caption("Status: Synced (Real-time)")
            
            if st.button("Disconnect Calendar"):
                if os.path.exists("token.json"):
                    os.remove("token.json")
                    st.rerun()
        else:
            st.warning("❌ Not Connected")
            st.markdown("Connect to allow GradePath to schedule exams.")
            
            # THE "SSO" BUTTON logic
            if st.button("🔗 Connect with Google", type="primary"):
                if cal_service:
                    try:
                        cal_service.connect() # Triggers the browser popup
                        st.success("Successfully connected!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Connection failed: {e}")
                else:
                    st.error("Service not available. Check credentials.json.")

    with st.container(border=True):
        st.markdown("### 🎓 Learning Management System")
        st.toggle("Canvas / Blackboard", value=True)
        st.caption("Status: ✅ Synced (2h ago)")

with col2:
    with st.container(border=True):
        st.markdown("### 📧 Email")
        st.toggle("University Email", value=True)
        st.caption("Status: ✅ Synced (10m ago)")
        
    with st.container(border=True):
        st.markdown("### ☁️ Cloud Storage")
        st.toggle("Google Drive / OneDrive", value=False)
        st.caption("Status: ❌ Not Connected")

# 3. Security Section
st.subheader("🔒 Security & Privacy")
with st.container(border=True):
    st.checkbox("Enable Two-Factor Authentication (2FA)", value=True)
    st.checkbox("Allow AI to read course emails", value=True)
    st.checkbox("Allow AI to add events to calendar", value=True)
    
    st.markdown("---")
    c1, c2 = st.columns([1, 4])
    c1.button("🗑️ Clear Memory", type="secondary")
    c2.button("🚪 Log Out", type="primary")