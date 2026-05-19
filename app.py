from openai import OpenAI
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Mameyl Labs AI",
    page_icon="✨",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {
            "role": "system",
            "content": "Tu es un assistant IA professionnel spécialisé en business, marketing, productivité, entrepreneuriat, e-commerce, création de contenu et automatisation. Réponds toujours clairement en français."
        }
    ]

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #050816 0%, #0B1120 45%, #111827 100%);
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #050816;
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: white;
}

h1, h2, h3 {
    color: white;
    font-weight: 800;
}

.stButton>button {
    background: linear-gradient(135deg, #7C3AED, #2563EB);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.7rem 1.3rem;
    font-weight: 700;
}

.output-box {
    background: rgba(15, 23, 42, 0.95);
    border-left: 5px solid #8B5CF6;
    border-radius: 18px;
    padding: 24px;
    margin-top: 20px;
    line-height: 1.7;
    color: white;
}

.hero {
    background: linear-gradient(135deg, #2E1065, #172554);
    padding: 50px;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 30px;
}

[data-testid="stMetric"] {
    background: transparent;
}

textarea, input, select {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


def ask_ai(prompt, system_prompt="Tu es un assistant IA professionnel. Réponds clairement en français."):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


with st.sidebar:
    st.title("✨ IA de Mameyl Labs")
    st.markdown("### Plateforme de productivité IA")

    page = st.radio(
        "Navigation",
        [
            "Tableau de bord",
            "Chat IA",
            "Marketing IA",
            "IA commerciale",
            "IA de contenu",
            "Résumé",
            "Analytique"
        ]
    )

    st.markdown("""
    <div style="background:#0f2a4a;padding:18px;border-radius:12px;margin-top:25px;">
    Plateforme d'assistant IA moderne construite avec Python et Streamlit.
    </div>
    """, unsafe_allow_html=True)


if page == "Tableau de bord":
    st.markdown("""
    <div class="hero">
        <h1>✨ IA de Mameyl Labs</h1>
        <h2>Plateforme d'assistant IA moderne</h2>
        <p>Une plateforme de productivité IA conçue pour le business, le marketing, le contenu, l'automatisation et l'aide à la décision.</p>
    </div>
    """, unsafe_allow_html=True)

    st.header("Présentation de la plateforme")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Requêtes IA", "1 284", "+32%")
    col2.metric("Résultats générés", "642", "+21%")
    col3.metric("Idées d'automatisation", "118", "+14%")
    col4.metric("Score de productivité", "91%", "+9%")

    st.header("Modules d'IA")

    modules = pd.DataFrame({
        "Module": [
            "Chat IA",
            "Marketing IA",
            "IA commerciale",
            "IA de contenu",
            "Résumé",
            "Analytique"
        ],
        "Objectif": [
            "Assistant conversationnel",
            "Stratégies marketing et campagnes",
            "Recommandations business et ventes",
            "Légendes, emails et descriptions",
            "Résumé de textes et documents",
            "Suivi d'utilisation et performance"
        ],
        "Statut": [
            "Actif",
            "Actif",
            "Actif",
            "Actif",
            "Actif",
            "Beta"
        ]
    })

    st.dataframe(modules, use_container_width=True)


elif page == "Chat IA":
    st.title("🤖 Chat IA Assistant")

    for message in st.session_state.chat_messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    prompt = st.chat_input("Écrivez votre message...")

    if prompt:

        st.session_state.chat_messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("✨ Génération en cours..."):

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.chat_messages
            )

            ai_response = response.choices[0].message.content

        st.session_state.chat_messages.append(
            {"role": "assistant", "content": ai_response}
        )

        with st.chat_message("assistant"):
            st.markdown(ai_response)

        st.rerun()

    if st.button("Effacer la conversation"):

        st.session_state.chat_messages = [
            {
                "role": "system",
                "content": "Tu es un assistant IA professionnel spécialisé en business, marketing, productivité, entrepreneuriat, e-commerce, création de contenu et automatisation. Réponds toujours clairement en français."
            }
        ]

        st.rerun()
elif page == "Marketing IA":
    st.title("📈 Générateur de stratégie marketing IA")

    product = st.text_input("Nom de la marque ou du produit")
    platform = st.selectbox("Plateforme", ["Instagram", "TikTok", "Facebook", "LinkedIn", "WhatsApp"])
    tone = st.selectbox("Ton", ["Premium", "Simple", "Luxe", "Professionnel", "Amical", "Audacieux"])
    goal = st.text_area("Objectif marketing")

    if st.button("Générer une stratégie marketing"):
        prompt = f"""
        Crée une stratégie marketing complète pour :
        Produit ou marque : {product}
        Plateforme : {platform}
        Ton : {tone}
        Objectif : {goal}

        Donne :
        - concept de campagne
        - idées de contenu
        - hooks
        - calendrier simple
        - CTA
        - recommandations concrètes
        """

        with st.spinner("Génération de la stratégie marketing..."):
            result = ask_ai(prompt)

        st.markdown(f"""
        <div class="output-box">
        {result}
        </div>
        """, unsafe_allow_html=True)


elif page == "IA commerciale":
    st.title("💼 Assistant IA Commercial")

    industry = st.selectbox("Industrie", ["Beauté", "E-commerce", "Technologie", "Éducation", "Livraison", "Mode"])
    request = st.text_area("Objectif commercial ou demande")

    if st.button("Générer une stratégie commerciale"):
        prompt = f"""
        Tu es un expert en stratégie commerciale.
        Industrie : {industry}
        Demande : {request}

        Donne :
        - stratégie de vente
        - acquisition client
        - script WhatsApp
        - gestion des objections
        - closing
        - offres promotionnelles intelligentes
        - KPIs à suivre
        """

        with st.spinner("Génération de la stratégie commerciale..."):
            result = ask_ai(prompt)

        st.markdown(f"""
        <div class="output-box">
        {result}
        </div>
        """, unsafe_allow_html=True)


elif page == "IA de contenu":
    st.title("✍️ Générateur de contenu IA")

    content_type = st.selectbox(
        "Type de contenu",
        ["Légende Instagram", "Post LinkedIn", "Email", "Description produit", "Script TikTok", "Message WhatsApp"]
    )

    topic = st.text_input("Sujet")
    tone = st.selectbox("Ton du contenu", ["Simple", "Premium", "Professionnel", "Émotionnel", "Luxe", "Viral"])

    if st.button("Générer du contenu"):
        prompt = f"""
        Crée un contenu de type : {content_type}
        Sujet : {topic}
        Ton : {tone}

        Le contenu doit être clair, professionnel, engageant et adapté à la plateforme.
        Ajoute un CTA si pertinent.
        """

        with st.spinner("Création du contenu..."):
            result = ask_ai(prompt)

        st.markdown(f"""
        <div class="output-box">
        {result}
        </div>
        """, unsafe_allow_html=True)


elif page == "Résumé":
    st.title("🧠 Résumeur intelligent")

    text = st.text_area("Collez le texte à résumer", height=220)
    style = st.selectbox("Style de résumé", ["Court", "En 3 points", "Professionnel", "Très détaillé"])

    if st.button("Résumer") and text.strip():
        prompt = f"""
        Résume le texte suivant en français.

        Style demandé : {style}

        Texte :
        {text}

        Le résumé doit être clair, structuré et utile.
        """

        with st.spinner("Résumé en cours..."):
            result = ask_ai(prompt)

        st.markdown(f"""
        <div class="output-box">
        <strong>Résumé :</strong><br><br>
        {result}
        </div>
        """, unsafe_allow_html=True)


elif page == "Analytique":
    st.title("📊 Analytique IA")

    data = pd.DataFrame({
        "Mois": ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"],
        "Requêtes IA": [120, 240, 310, 460, 620, 850],
        "Résultats générés": [80, 160, 220, 330, 470, 640]
    })

    st.line_chart(data.set_index("Mois"))

    col1, col2, col3 = st.columns(3)
    col1.metric("Croissance", "+42%")
    col2.metric("Meilleur module", "Marketing IA")
    col3.metric("Gain moyen", "31%")

    st.success("Forte croissance de l'utilisation de l'IA détectée.")


st.markdown("""
<hr>
<p style="color:gray;">
Mameyl Labs AI — Plateforme de productivité IA construite avec Python, Streamlit et OpenAI.
</p>
""", unsafe_allow_html=True)