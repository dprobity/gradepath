import streamlit as st

st.set_page_config(page_title="Materials | GradePath", page_icon="📚", layout="wide")

st.title("Knowledge Base")
st.markdown("Your academic compass for Spring 2026")

col_tree, col_content = st.columns([1, 2])

with col_tree:
    st.subheader("Course Materials")
    with st.container(border=True):
        st.markdown("📂 **SPRING 2026**")
        
        # CHEM 101 Section (Expanded)
        with st.expander("🧪 CHEM 101", expanded=True):
            st.markdown("📄 Syllabus & Intro")
            st.markdown("📂 **Week 4: Chemical Kinetics**", help="Current Selection")
            st.markdown("📄 Week 5: Thermodynamics")
            
        # PHYS 202 Section
        with st.expander("🔭 PHYS 202"):
            st.markdown("📄 Syllabus")
            st.markdown("📄 Lecture Slides")

        # MATH 301 Section
        with st.expander("📐 MATH 301"):
            st.markdown("📄 Problem Sets")

    st.button("📄 Upload Material", use_container_width=True)

with col_content:
    # Selected File Header
    with st.container(border=True):
        c1, c2 = st.columns([0.8, 0.2])
        c1.markdown("📕 **Week_4_Lecture_Slides.pdf**")
        c1.caption("Added 3 days ago • 2.4 MB")
        c2.success("✅ AI Indexed")
    
    # AI Analysis Card
    st.markdown("""
    <div style="background-color: #F8F9FA; padding: 20px; border-radius: 10px; border: 1px solid #E5E7EB; margin-top: 10px;">
        <div style="display: flex; align-items: start; gap: 15px;">
            <div style="background-color: #4F46E5; color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center;">🤖</div>
            <div>
                <strong>I've analyzed the Chemical Kinetics slides. Key concepts identified:</strong>
                <ul>
                    <li>Reaction Rates & Rate Laws</li>
                    <li>Collision Theory</li>
                    <li>Activation Energy & Catalysts</li>
                </ul>
                <p>What would you like to do?</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Actions
    c1, c2, c3 = st.columns([1, 1, 3])
    c1.button("📝 Quiz me", use_container_width=True)
    c2.button("📄 Summarize", use_container_width=True)
    
    # Chat Input Stub
    st.text_input("", placeholder="Ask a question about this file...", key="doc_chat")