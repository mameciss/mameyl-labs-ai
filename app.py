from openai import OpenAI
import streamlit as st
import pandas as pd
if "messages" not in st.session_state:
    st.session_state.messages = []
st.set_page_config(
    page_title="Mameyl Labs AI",
    page_icon="✨",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# =========================
# STYLE
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

.hero-card, .tool-card, .output-box {
    background: rgba(17,24,39,0.88);
    border: 1px solid rgba(255,255,255,0.10);
    padding: 24px;
    border-radius: 18px;
    margin-bottom: 18px;
}

.output-box {
    border-left: 5px solid #8B5CF6;
    color: #E5E7EB;
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
</style>
""", unsafe_allow_html=True)


# =========================
# IA FUNCTION
# =========================
def ask_ai(system_prompt, user_prompt):
    with st.spinner("L'IA réfléchit..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8
        )
    return response.choices[0].message.content


# =========================
# SIDEBAR
# =========================
st.sidebar.title("✨ IA de Mameyl Labs")
st.sidebar.markdown("### Plateforme de productivité IA")

page = st.sidebar.radio(
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

st.sidebar.info("Plateforme d'assistant IA moderne construite avec Python et Streamlit.")


# =========================
# DASHBOARD
# =========================
if page == "Tableau de bord":
    st.title("✨ Tableau de bord")

    st.markdown("""
<div class="hero-card">
<h2>Mameyl Labs AI</h2>
<p>Plateforme IA pour marketing, contenu, stratégie commerciale, résumé et productivité.</p>
</div>
""", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Requêtes IA", "1 284", "+32%")
    col2.metric("Contenus générés", "642", "+21%")
    col3.metric("Idées business", "118", "+14%")
    col4.metric("Score productivité", "91%", "+9%")

    st.markdown("## Modules IA")

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
            "Assistant conversationnel avec mémoire",
            "Campagnes, hooks, stratégie réseaux sociaux",
            "Vente, fidélisation, scripts clients",
            "Légendes, scripts, emails, descriptions",
            "Résumé clair et structuré",
            "Statistiques et performance"
        ],
        "Statut": [
            "Actif",
            "Actif",
            "Actif",
            "Actif",
            "Actif",
            "Bêta"
        ]
    })

    st.dataframe(modules, use_container_width=True)


# =========================
# CHAT IA AVEC MÉMOIRE
# =========================
elif page == "Chat IA":
    st.title("🤖 Chat IA Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": "Tu es un assistant IA professionnel spécialisé en business, marketing, productivité et entrepreneuriat. Réponds toujours clairement en français."
            }
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**Vous :** {msg['content']}")
        elif msg["role"] == "assistant":
            st.markdown(f"""
<div class="output-box">
<strong>IA :</strong><br><br>{msg['content']}
</div>
""", unsafe_allow_html=True)

    user_message = st.text_area("Votre message")

    if st.button("Envoyer") and user_message.strip():
        st.session_state.messages.append({"role": "user", "content": user_message})

        with st.spinner("L'IA répond..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                temperature=0.8
            )

        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

    if st.button("Effacer la conversation"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": "Tu es un assistant IA professionnel spécialisé en business, marketing, productivité et entrepreneuriat. Réponds toujours clairement en français."
            }
        ]
        st.rerun()


# =========================
# MARKETING IA
# =========================
elif page == "Marketing IA":
    st.title("📈 Générateur Marketing IA")

    marque = st.text_input("Nom de la marque ou du produit")
    plateforme = st.selectbox("Plateforme", ["Instagram", "TikTok", "Facebook", "LinkedIn"])
    ton = st.selectbox("Ton", ["Premium", "Amical", "Professionnel", "Audacieux", "Luxe"])
    objectif = st.text_area("Objectif marketing")

    if st.button("Générer une stratégie marketing"):
        prompt = f"""
Marque/produit : {marque}
Plateforme : {plateforme}
Ton : {ton}
Objectif : {objectif}

Crée une vraie stratégie marketing complète, concrète et exploitable.
Inclure :
- objectif de campagne
- concept créatif
- audience cible
- 5 hooks
- 3 idées de publications
- 2 idées de vidéos
- CTA
- calendrier de publication sur 7 jours
- conseils pour améliorer la conversion
"""

        reply = ask_ai(
            "Tu es un expert marketing digital premium spécialisé en réseaux sociaux, branding, campagnes et conversion.",
            prompt
        )

        st.markdown(f"""
<div class="output-box">
{reply}
</div>
""", unsafe_allow_html=True)


# =========================
# IA COMMERCIALE
# =========================
elif page == "IA commerciale":
    st.title("💼 Assistant IA Commercial")

    industrie = st.selectbox("Industrie", ["Beauté", "Technologie", "E-commerce", "Mode", "Éducation", "Services"])
    demande = st.text_area("Objectif commercial ou demande")

    if st.button("Générer une stratégie commerciale"):
        prompt = f"""
Industrie : {industrie}
Demande : {demande}

Réponds comme un expert commercial.
Selon la demande, produis une réponse adaptée :
- stratégie de vente
- fidélisation
- script WhatsApp
- gestion des objections
- closing
- acquisition client
- offres promotionnelles

La réponse doit être concrète, utile, prête à utiliser.
"""

        reply = ask_ai(
            "Tu es un directeur commercial IA spécialisé en ventes, fidélisation, acquisition client, scripts WhatsApp et conversion.",
            prompt
        )

        st.markdown(f"""
<div class="output-box">
{reply}
</div>
""", unsafe_allow_html=True)


# =========================
# IA DE CONTENU
# =========================
elif page == "IA de contenu":
    st.title("✍️ Générateur de contenu IA")

    type_contenu = st.selectbox(
        "Type de contenu",
        [
            "Légende Instagram",
            "Script TikTok",
            "Email marketing",
            "Description produit",
            "Texte publicitaire",
            "Post Facebook"
        ]
    )

    sujet = st.text_input("Sujet")
    ton = st.selectbox("Ton du contenu", ["Premium", "Simple", "Émotionnel", "Professionnel", "Viral"])

    if st.button("Générer du contenu"):
        prompt = f"""
Type de contenu : {type_contenu}
Sujet : {sujet}
Ton : {ton}

Crée le contenu directement.
Ne donne pas des conseils.
Ne dis pas quoi faire.
Écris le texte final prêt à publier ou utiliser.
Ajoute CTA et hashtags si pertinent.
"""

        reply = ask_ai(
            "Tu es un créateur de contenu expert en beauté, business, réseaux sociaux, storytelling et copywriting.",
            prompt
        )

        st.markdown(f"""
<div class="output-box">
{reply}
</div>
""", unsafe_allow_html=True)


# =========================
# RÉSUMÉ
# =========================
elif page == "Résumé":
    st.title("🧠 Résumeur intelligent")

    texte = st.text_area("Collez le texte à résumer")
    style = st.selectbox("Style de résumé", ["Court", "Détaillé", "En 3 points", "Professionnel"])

    if st.button("Résumer"):
        prompt = f"""
Texte à résumer :
{texte}

Style demandé : {style}

Fais un vrai résumé clair du texte.
Garde seulement les idées importantes.
Ne parle pas du résumé : produis directement le résumé.
"""

        reply = ask_ai(
            "Tu es un expert en synthèse, résumé professionnel et clarification de texte.",
            prompt
        )

        st.markdown(f"""
<div class="output-box">
<strong>Résumé :</strong><br><br>
{reply}
</div>
""", unsafe_allow_html=True)


# =========================
# ANALYTIQUE
# =========================
elif page == "Analytique":
    st.title("📊 Analytique IA")

    data = pd.DataFrame({
        "Mois": ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"],
        "Requêtes IA": [120, 240, 310, 460, 620, 850],
        "Contenus générés": [80, 160, 220, 330, 470, 642]
    })

    st.line_chart(data.set_index("Mois"))

    col1, col2, col3 = st.columns(3)
    col1.metric("Croissance", "+42%")
    col2.metric("Meilleur module", "Marketing IA")
    col3.metric("Gain productivité moyen", "31%")

    st.success("Forte croissance d'utilisation détectée.")


st.markdown("---")
st.caption("Mameyl Labs AI — Plateforme de productivité IA construite avec Python et Streamlit.")