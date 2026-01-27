import streamlit as st

st.set_page_config(page_title="Chat | GradePath", page_icon="💬", layout="wide")

st.title("💬 Chat & Planner")

# Initialize chat history mock
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "user", "content": "Help me plan my week based on my deadlines."},
        {"role": "assistant", "content": "Here is a plan for your week. I've checked your assignments and exams. I suggest dedicating Tuesday afternoon to your project proposal and Wednesday evening to midterm study."}
    ]

# Layout: Chat on left (larger), Context on right (sidebar-like column)
col_chat, col_context = st.columns([3, 1])

with col_chat:
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask about grades, docs, or schedule..."):
        # Add user message to state
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Mock AI Response
        response = f"**[Mock Response]** I received your query: *'{prompt}'*. \n\nI would typically query the Vector DB for context and use the Planner Agent to answer this."
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

with col_context:
    st.subheader("Active Context")
    
    course = st.selectbox("Current Focus", ["Global (All)", "CHEM 101", "PHYS 202", "MATH 201"])
    
    st.markdown("---")
    st.markdown("**🔍 Relevant Documents**")
    st.caption("Syllabus_v2.pdf (p. 4)")
    st.caption("Lab_Safety_Guidelines.docx")
    
    st.markdown("---")
    st.markdown("**⏳ Next Deadlines**")
    st.warning("CS 301 Proposal (Tomorrow)")
    
    st.markdown("---")
    st.markdown("**🧠 Recent Memories**")
    st.info("User prefers studying in 25m Pomodoro blocks.")