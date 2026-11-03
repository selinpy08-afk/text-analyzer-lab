import streamlit as st
import re
from collections import Counter

st.set_page_config(
    page_title="Text Analyzer Lab",
    page_icon="📝"
)

st.markdown("""
<style>
.stApp {
    background-color: #F3EDFF;
}
h1 {
    color: #7654C8;
    text-align: center;
}
.stButton button {
    background-color: #7654C8;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("TEXT ANALYZER LAB")

st.subheader("Enter Your Text:")

def clear_text():
    st.session_state.user_text = ""

if "user_text" not in st.session_state:
    st.session_state.user_text = ""

text = st.text_area(
    "Write your text:",
    key="user_text",
    height=180
)

col1, col2 = st.columns(2)

with col1:
    analyze = st.button("Analyze Text")

with col2:
    st.button("Clear", on_click=clear_text)

if analyze:

    if not text.strip():
        st.warning("Please enter some text.")

    else:
        characters = len(text)

        words = re.findall(r"\b\w+\b", text)

        word_count = len(words)

        words = [word.lower() for word in words]

        unique_words = set(words)

        frequency = Counter(words)

        st.subheader("===== FINAL REPORT =====")

        st.write("Total Characters:", characters)

        st.write("Total Words:", word_count)

        st.write("Unique Words:", len(unique_words))

        st.subheader("Unique Word List")

        for word in sorted(unique_words):
            st.write("-", word)

        st.subheader("Most Frequent Words")

        for word, count in frequency.most_common():
            st.write(f"{word}: {count} times")
