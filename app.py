import streamlit as st

st.set_page_config(page_title="AI Viral Shorts Generator", layout="centered")

st.title("🎬 YouTube Viral Shorts Generator")
st.write("YouTube link dalo aur aasani se video dekho!")

video_url = st.text_input("YouTube Video URL Yahan Paste Karo:")

if st.button("Video Dekhein / Chalaayein"):
    if video_url:
        try:
            st.success("Ye lo aapki video taiyar hai!")
            st.video(video_url)
        except Exception as e:
            st.error(f"Error aaya hai: {str(e)}")
    else:
        st.warning("Kripya ek valid YouTube link daalein.")
