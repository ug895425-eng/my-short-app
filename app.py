import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="AI Viral Shorts Generator", layout="centered")

st.title("🎬 YouTube Viral Shorts Generator")
st.write("YouTube link dalo aur apna short video download karo!")

video_url = st.text_input("YouTube Video URL Yahan Paste Karo:")

if st.button("Short Video Banayein"):
    if video_url:
        st.info("Video process ho rahi hai, kripya 1-2 minute intazar karein...")
        try:
            ydl_opts = {
                'format': 'mp4',
                'outtmpl': 'downloaded_video.mp4',
                'overwrites': True,
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                },
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            
            st.success("Video Process Ho Gayi Hai!")
            st.video("downloaded_video.mp4")
            
            with open("downloaded_video.mp4", "rb") as file:
                st.download_button(
                    label="📥 Short Video Download Karo",
                    data=file,
                    file_name="viral_short.mp4",
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"Error aaya hai: {str(e)}")
    else:
        st.warning("Kripya ek valid YouTube link daalein.")
