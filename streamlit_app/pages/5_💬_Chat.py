import streamlit as st

st.set_page_config(page_title="Chat | GradePath", page_icon="💬", layout="wide")

st.title("💬 Academic Assistant")

# Context Selector
col1, col2 = st.columns([1, 3])
with col1:
    context = st.selectbox(
        "Chat Context", 
        ["Global (All Courses)", "CHEM 101", "PHYS 202", "MATH 301"],
        help="Select a specific course to narrow down the AI's knowledge base."
    )
    
    st.markdown("---")
    st.caption("Suggested Prompts:")
    if context == "CHEM 101":
        st.button("Explain Rate Laws")
        st.button("Draft Lab Abstract")
    else:
        st.button("What's due this week?")
        st.button("Summarize recent emails")

with col2:
    # Mock Chat History
    messages = [
        {"role": "user", "content": "I'm struggling with the concept of Activation Energy in Chem. Can you explain it simply?"},
        {"role": "assistant", "content": "Think of **Activation Energy** like a hill a ball has to roll over to get to the other side.\n\nEven if the reaction releases energy overall (like the ball rolling down a hill), it needs an initial 'push' to get over the hump. Catalysts lower this hump, making it easier for the reaction to happen."},
        {"role": "user", "content": "Does the catalyst get used up?"},
        {"role": "assistant", "content": "No, that's the key part! A catalyst lowers the activation energy but is **not consumed** in the reaction. It emerges unchanged at the end."}
    ]

    # Render Chat
    for msg in messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # Chat Input
    if prompt := st.chat_input("Ask follow-up..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown("*(AI is thinking... backend not connected)*")