import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Mameyl Labs AI",
    page_icon="✨",
    layout="wide"
)

# =========================
# STYLE PREMIUM
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #050816 0%, #0B1120 45%, #111827 100%);
    color: white;
}

[data-testid="stSidebar"] {
    background: #050816;
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: white;
}

h1, h2, h3 {
    color: white;
    font-weight: 800;
}

p, li, label {
    color: #D1D5DB;
}

.hero-card {
    background: linear-gradient(135deg, rgba(124,58,237,0.25), rgba(37,99,235,0.18));
    border: 1px solid rgba(255,255,255,0.12);
    padding: 35px;
    border-radius: 24px;
    box-shadow: 0 20px 45px rgba(0,0,0,0.35);
}

.tool-card {
    background: rgba(17,24,39,0.86);
    border: 1px solid rgba(255,255,255,0.10);
    padding: 24px;
    border-radius: 20px;
    margin-bottom: 18px;
}

.output-box {
    background: #111827;
    border-left: 5px solid #8B5CF6;
    padding: 22px;
    border-radius: 14px;
    color: #E5E7EB;
}

[data-testid="metric-container"] {
    background: rgba(17,24,39,0.88);
    border: 1px solid rgba(255,255,255,0.12);
    padding: 18px;
    border-radius: 18px;
}

.stButton>button {
    background: linear-gradient(90deg, #7C3AED, #2563EB);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.7rem 1.2rem;
    font-weight: 700;
}

.stTextArea textarea, .stTextInput input {
    background-color: #0B1120;
    color: white;
    border-radius: 12px;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #0B1120;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("✨ Mameyl Labs AI")
st.sidebar.markdown("### AI Productivity Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "AI Chat",
        "Marketing AI",
        "Business AI",
        "Content AI",
        "Summarizer",
        "Analytics"
    ]
)

st.sidebar.info("Modern AI assistant platform built with Python and Streamlit.")

# =========================
# SIMULATED DATA
# =========================
ideas = [
    "Launch a short-form video campaign focused on transformation and storytelling.",
    "Create a premium brand positioning strategy with emotional product benefits.",
    "Build a weekly content calendar with educational, social proof and product posts.",
    "Use customer pain points to create targeted captions and campaign hooks.",
    "Develop a launch campaign with teasers, testimonials and limited-time offers."
]

business_strategies = [
    "Focus on customer retention through personalized follow-ups and loyalty offers.",
    "Automate repetitive communication tasks to save operational time.",
    "Track product performance weekly to identify best sellers and slow movers.",
    "Use data dashboards to guide inventory and marketing decisions.",
    "Build strong brand consistency across website, social media and customer support."
]

# =========================
# DASHBOARD
# =========================
if page == "Dashboard":
    st.markdown("""
<div class="hero-card">
<h1>✨ Mameyl Labs AI</h1>
<h3>Modern AI Assistant Platform</h3>
<p>
A premium AI productivity platform designed for business, content creation,
marketing strategy, automation and intelligent decision support.
</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("## Platform Overview")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("AI Requests", "1,284", "+32%")
    col2.metric("Generated Outputs", "642", "+21%")
    col3.metric("Automation Ideas", "118", "+14%")
    col4.metric("Productivity Score", "91%", "+9%")

    st.markdown("## AI Modules")

    modules = pd.DataFrame({
        "Module": [
            "AI Chat",
            "Marketing AI",
            "Business AI",
            "Content AI",
            "Summarizer",
            "Analytics"
        ],
        "Purpose": [
            "Conversational assistant",
            "Campaign ideas and hooks",
            "Business recommendations",
            "Captions, emails and descriptions",
            "Text and notes summarization",
            "AI usage and productivity metrics"
        ],
        "Status": [
            "Active",
            "Active",
            "Active",
            "Active",
            "Active",
            "Beta"
        ]
    })

    st.dataframe(modules, use_container_width=True)

# =========================
# AI CHAT
# =========================
elif page == "AI Chat":
    st.title("🤖 AI Chat Assistant")

    st.markdown("""
<div class="tool-card">
Ask a question and receive a simulated AI response.  
This module is designed to later connect with a real AI API.
</div>
""", unsafe_allow_html=True)

    question = st.text_area("Your message")

    if st.button("Send"):
        st.markdown("""
<div class="output-box">
<strong>AI Response:</strong><br><br>
This is a simulated AI assistant response. In a production version, this module
would connect to an AI API to provide contextual and intelligent answers.
</div>
""", unsafe_allow_html=True)

# =========================
# MARKETING AI
# =========================
elif page == "Marketing AI":
    st.title("📈 Marketing AI Generator")

    product = st.text_input("Product or business name")
    platform = st.selectbox("Platform", ["Instagram", "TikTok", "Facebook", "LinkedIn"])
    tone = st.selectbox("Tone", ["Premium", "Friendly", "Professional", "Bold", "Luxury"])

    if st.button("Generate Marketing Ideas"):
        st.markdown(f"""
<div class="output-box">
<strong>Marketing idea for {product} on {platform}:</strong><br><br>
{random.choice(ideas)}<br><br>
Tone selected: <strong>{tone}</strong>
</div>
""", unsafe_allow_html=True)

# =========================
# BUSINESS AI
# =========================
elif page == "Business AI":
    st.title("💼 Business Strategy AI")

    industry = st.selectbox("Industry", ["Beauty", "Technology", "E-commerce", "Fashion", "Education", "Services"])
    goal = st.text_area("Business goal")

    if st.button("Generate Strategy"):
        st.markdown(f"""
<div class="output-box">
<strong>Strategic recommendation for {industry}:</strong><br><br>
{random.choice(business_strategies)}<br><br>
Suggested next step: create measurable KPIs and track progress weekly.
</div>
""", unsafe_allow_html=True)

# =========================
# CONTENT AI
# =========================
elif page == "Content AI":
    st.title("✍️ Content AI Generator")

    content_type = st.selectbox(
        "Content type",
        ["Instagram Caption", "LinkedIn Post", "Marketing Email", "Product Description", "Ad Copy"]
    )

    topic = st.text_input("Topic")

    if st.button("Generate Content"):
        st.markdown(f"""
<div class="output-box">
<strong>{content_type} about {topic}</strong><br><br>
Create content that is clear, engaging and aligned with the brand voice.
Highlight the value, benefits and emotional connection with the audience.
</div>
""", unsafe_allow_html=True)

# =========================
# SUMMARIZER
# =========================
elif page == "Summarizer":
    st.title("🧠 Smart Summarizer")

    text = st.text_area("Paste text to summarize")

    if st.button("Summarize"):
        st.markdown("""
<div class="output-box">
<strong>Summary:</strong><br><br>
This text highlights key ideas and can be transformed into a shorter,
clearer and more actionable summary for business or productivity use.
</div>
""", unsafe_allow_html=True)

# =========================
# ANALYTICS
# =========================
elif page == "Analytics":
    st.title("📊 AI Usage Analytics")

    data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "AI Requests": [120, 240, 310, 460, 620, 850],
        "Generated Outputs": [80, 160, 220, 330, 470, 642]
    })

    st.line_chart(data.set_index("Month"))

    col1, col2, col3 = st.columns(3)
    col1.metric("Growth", "+42%")
    col2.metric("Best Module", "Marketing AI")
    col3.metric("Avg Productivity Gain", "31%")

    st.success("Strong AI usage growth detected.")

st.markdown("---")
st.caption("Mameyl Labs AI — Simulated AI productivity platform built with Python and Streamlit.")