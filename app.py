import streamlit as st
import joblib
import base64

# Load model
model = joblib.load("sleep_study_model.pkl")

# Page Config
st.set_page_config(page_title="Should I Sleep or Study?", page_icon="😴", layout="centered")

# Custom Banner
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>📚 Should I Sleep or Study? 😴</h1>
    <p style='text-align: center; font-size: 18px;'>A smart decision assistant before your next exam!</p>
""", unsafe_allow_html=True)

# Sidebar Instructions
st.sidebar.title("🧾 About This App")
st.sidebar.info("""
This app predicts whether you should **sleep** or **study** based on your current state using a regression model trained on synthetic data.

Move the sliders to reflect your condition. You'll get a score and a friendly recommendation.
""")

# Inputs
st.markdown("### 📋 Your Inputs")

col1, col2 = st.columns(2)

with col1:
    sleep = st.slider("🛏️ Sleep hours (last 3 days)", 6, 24, 15)
    difficulty = st.slider("📘 Subject difficulty (1–10)", 1, 10, 5)
    exam_days = st.slider("🗓️ Days before exam", 0, 15, 5)
    confidence = st.slider("💪 Confidence level (1–10)", 1, 10, 5)

with col2:
    past_score = st.slider("📊 Past exam score (%)", 40, 100, 70)
    coffee = st.slider("☕ Coffee intake (cups)", 0, 5, 1)
    stress = st.slider("😰 Stress level (1–10)", 1, 10, 5)
    distraction = st.slider("📱 Distraction index (0–10)", 0.0, 10.0, 5.0)

# Prediction
input_data = [[sleep, difficulty, exam_days, confidence, past_score, coffee, stress, distraction]]
score = model.predict(input_data)[0]

# Display score
st.markdown("### 🧠 Sleep-Study Score")
st.metric(label="Decision Score", value=f"{score:.2f}")

# Recommendation
if score > 0.6:
    st.markdown("### ✅ Recommendation: **Sleep 😴**")
    st.success("You seem exhausted or stressed. Take rest and come back stronger!")
elif score < 0.4:
    st.markdown("### ✅ Recommendation: **Study 📖**")
    st.success("You're well rested and confident. It's time to hit the books!")
else:
    st.markdown("### 🤔 Recommendation: **Balanced**")
    st.info("Maybe take a short nap and then study. You’re somewhere in between.")

# Footer
st.markdown("""
    <hr style="margin-top:40px;">
    <div style='text-align: center; font-size: 14px; color: gray;'>
        Made with ❤️ using Streamlit | Project by Shriyanshi
    </div>
""", unsafe_allow_html=True)
