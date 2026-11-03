import streamlit as st
import re
from collections import Counter

st.set_page_config(
    page_title="Text Analyzer Lab",
    page_icon="📝",
    layout="centered"
)

# Design
st.markdown("""
<style>
.stApp {
    background-color: #F3EDFF;
}
h1 {
    color: #7654C8;
    text-align: center;
}
.stTextArea textarea {
    background-color: white !important;
    color: #222222 !important;
    cursor: text !important;
    opacity: 1 !important;
}
.stButton button {
    background-color: #7654C8;
    color: white;
    border-radius: 10px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("📝 TEXT ANALYZER LAB")
st.write("Enter your text below and analyze it.")

# Text input
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

text = st.text_area(
    "Write your text here:",
    key="input_text",
    height=200,
    placeholder="Start typing here...",
    disabled=False
)

# Buttons
col1, col2 = st.columns(2)

with col1:
    analyze = st.button("Analyze Text")

with col2:
    clear = st.button("Clear")

if clear:
    st.session_state.input_text = ""
    st.rerun()

if analyze:
    text = st.session_state.input_text

    if not text.strip():
        st.warning("Please enter some text.")

    else:
        words = re.findall(r"\b\w+\b", text)
        words = [word.lower() for word in words]

        characters = len(text)
        word_count = len(words)
        unique_words = set(words)
        frequency = Counter(words)

        st.divider()
        st.subheader("📊 FINAL REPORT")

        st.metric("Total Characters", characters)
        st.metric("Total Words", word_count)
        st.metric("Unique Words", len(unique_words))

        st.subheader("Unique Word List")
        for word in sorted(unique_words):
            st.write(f"• {word}")

        st.subheader("Most Frequent Words")
        for word, count in frequency.most_common():
            st.write(f"• {word}: {count} times")
