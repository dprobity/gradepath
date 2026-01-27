import streamlit as st
import datetime

st.set_page_config(page_title="Schedule | GradePath", page_icon="📅", layout="wide")

st.title("Smart Schedule")
st.markdown("Your academic compass for Spring 2026")

# Controls
c1, c2, c3 = st.columns([1, 1, 4])
view_mode = c1.radio("View", ["Day", "Week"], horizontal=True)
date_sel = c2.date_input("Date", datetime.date(2026, 1, 22))
c3.button("🔄 Re-Optimize Plan", help="AI will reshuffle study blocks based on deadlines")

st.markdown("---")

# Week View Mockup (Grid Layout)
if view_mode == "Week":
    cols = st.columns(5)
    days = ["MON 22", "TUE 23", "WED 24", "THU 25", "FRI 26"]
    
    # Monday
    with cols[0]:
        st.markdown(f"**{days[0]}**")
        st.info("**CHEM 101 Lecture**\n\n9:00 - 10:30")
        st.success("**Study: Bio Lab**\n\n12:00 - 1:00\n\n✅ Done")
        
    # Tuesday
    with cols[1]:
        st.markdown(f"**{days[1]}**")
        st.info("**CHEM 101 Lab**\n\n9:00 - 12:00")
        
    # Wednesday
    with cols[2]:
        st.markdown(f"**{days[2]}**")
        st.info("**PHYS 202 Lecture**\n\n9:00 - 10:30")
        
    # Thursday
    with cols[3]:
        st.markdown(f"**{days[3]}**")
        st.warning("**Calc Review**\n\n10:00 - 11:00\n\n⚠️ Missed")
        st.markdown("""
        <div style="background-color: #E0E7FF; padding: 10px; border-radius: 8px; border-left: 4px solid #4F46E5;">
            <strong>Draft History Paper</strong><br>
            <span style="font-size: 0.8em; color: #4F46E5;">High Focus</span><br>
            1:00 - 2:30 PM
        </div>
        """, unsafe_allow_html=True)
        
    # Friday
    with cols[4]:
        st.markdown(f"**{days[4]}**")
        st.markdown("""
        <div style="border: 2px dashed #ccc; padding: 20px; border-radius: 8px; text-align: center; color: #888;">
            Free Slot
        </div>
        """, unsafe_allow_html=True)

else:
    st.write("Day view placeholder.")

st.markdown("---")
st.caption("ℹ️ 'Lecture' events extracted from **Spring2026_Syllabus.pdf**")