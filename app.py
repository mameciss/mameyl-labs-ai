import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Mameyl Labs AI",
    page_icon="✨",
    layout="wide"
)

# =========================
# PREMIUM CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #050816;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #0B1120;
}

[data-testid="stSidebar"] * {
    color: white;
}

h1, h2, h3 {
    color: white;
    font-weight: 700;
}

.metric-card {
    background: linear-gradient(135deg, #111827, #1F2937);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #1F2937;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.35);
}

.ai-box {
    background: #111827;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #1F2937;
    margin-top: 15px;
}

.stButton>button {
    background: linear-gradient(90deg,#7C3AED,#2563EB);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.7rem 1.2rem;
    font-weight: 600;
}

.stTextArea textarea {
    background-color: #111827;
    color: white;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("✨ Mameyl Labs AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Accueil",
        "Marketing AI",
        "Business AI",
        "Content Generator",
        "Analytics"
    ]
)

st.sidebar.info(
    "AI productivity platform built with Python and Streamlit."
)

# =========================
# HOME
# =========================

if page == "Accueil":

    st.title("✨ Mameyl Labs AI")
    st.subheader("AI Assistant Platform")

    st.markdown("""
AI-powered productivity platform focused on:
- marketing
- analytics
- automation
- business intelligence
- content generation
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Requests", "128", "+24%")

    with col2:
        st.metric("Generated Ideas", "87", "+18%")

    with col3:
        st.metric("Automation Tasks", "42", "+12%")

    st.markdown("---")

    st.header("🚀 Platform Features")

    features = pd.DataFrame({
        "Feature": [
            "Marketing AI",
            "Business Analytics",
            "Content Generator",
            "AI Insights",
            "Automation"
        ],
        "Status": [
            "Active",
            "Active",
            "Active",
            "Beta",
            "Coming Soon"
        ]
    })

    st.dataframe(features, use_container_width=True)

# =========================
# MARKETING AI
# =========================

elif page == "Marketing AI":

    st.title("📈 Marketing AI Generator")

    business = st.text_input("Business or Product")

    platform = st.selectbox(
        "Platform",
        ["Instagram", "LinkedIn", "TikTok", "Facebook"]
    )

    if st.button("Generate Marketing Idea"):

        ideas = [
            f"Create a premium {platform} campaign for {business}.",
            f"Launch a before/after storytelling strategy for {business}.",
            f"Build influencer collaborations around {business}.",
            f"Create educational short-form content for {business}.",
            f"Develop a luxury branding campaign for {business}."
        ]

        st.success(random.choice(ideas))

# =========================
# BUSINESS AI
# =========================

elif page == "Business AI":

    st.title("💼 Business Strategy AI")

    industry = st.selectbox(
        "Industry",
        [
            "Beauty",
            "Technology",
            "E-commerce",
            "Fashion",
            "Education"
        ]
    )

    goal = st.text_area("Business Goal")

    if st.button("Generate Strategy"):

        st.markdown(f"""
### Strategic Recommendations for {industry}

- Improve digital positioning
- Focus on customer retention
- Develop automation workflows
- Optimize analytics dashboards
- Increase social media engagement
- Build AI-assisted productivity systems
""")

# =========================
# CONTENT GENERATOR
# =========================

elif page == "Content Generator":

    st.title("✍️ AI Content Generator")

    content_type = st.selectbox(
        "Content Type",
        [
            "Instagram Caption",
            "LinkedIn Post",
            "Marketing Email",
            "Product Description"
        ]
    )

    topic = st.text_input("Topic")

    if st.button("Generate Content"):

        st.markdown(f"""
### Generated {content_type}

🚀 Premium content idea for **{topic}**

This AI-generated content is designed to improve engagement,
branding and audience growth while maintaining a modern
and professional communication style.
""")

# =========================
# ANALYTICS
# =========================

elif page == "Analytics":

    st.title("📊 AI Analytics Dashboard")

    analytics = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Users": [120, 180, 260, 320, 410]
    })

    st.line_chart(
        analytics.set_index("Month")
    )

    st.metric(
        "Monthly Growth",
        "+42%"
    )

    st.success(
        "Strong user growth detected."
    )