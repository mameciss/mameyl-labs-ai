import streamlit as st

st.set_page_config(
    page_title="Mameyl Labs AI",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #050816;
    color: white;
}

h1, h2, h3 {
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #0B1120;
}

[data-testid="stSidebar"] * {
    color: white;
}

.stButton>button {
    background-color: #7C3AED;
    color: white;
    border-radius: 10px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.title("✨ Mameyl Labs AI")
st.subheader("AI Assistant Platform")

st.write("""
Welcome to Mameyl Labs AI.

This platform demonstrates AI-powered business and productivity tools built with Python and Streamlit.
""")

st.info("AI features will be added progressively.")

col1, col2, col3 = st.columns(3)

col1.metric("AI Requests", "128", "+24%")
col2.metric("Generated Ideas", "87", "+18%")
col3.metric("Automation Tasks", "42", "+12%")

st.markdown("---")

st.header("AI Tools")

tool = st.selectbox(
    "Choose an AI tool",
    [
        "Marketing Idea Generator",
        "Business Assistant",
        "Content Generator",
        "Text Summarizer"
    ]
)

user_input = st.text_area("Enter your text or idea")

if st.button("Generate"):
    st.success(f"{tool} executed successfully.")

    st.write("Example AI response:")
    
    st.write("""
    This is a simulated AI-generated response.
    Future versions will integrate real AI APIs and automation workflows.
    """)