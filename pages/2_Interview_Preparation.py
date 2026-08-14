import streamlit as st

st.set_page_config(page_title="Interview Preparation", page_icon="🎤", layout="wide")

st.title("🎤 Interview Preparation")
st.caption("Practice questions based on your target role and profile.")

profile = st.session_state.get("profile", {})
default_role = profile.get("target_role", "")

role = st.text_input("Target Role", value=default_role, placeholder="e.g. Data Scientist")
difficulty = st.select_slider("Difficulty", options=["Beginner", "Intermediate", "Advanced"], value="Intermediate")
category = st.selectbox("Question Type", ["Technical", "HR", "Behavioral", "Mixed"])

question_bank = {
    "Technical": [
        "Explain the difference between supervised and unsupervised learning.",
        "What is overfitting and how can you reduce it?",
        "Explain precision, recall and F1-score.",
        "What is a REST API and where would you use it?"
    ],
    "HR": [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths and weaknesses?",
        "Where do you see yourself in five years?"
    ],
    "Behavioral": [
        "Tell me about a difficult project and how you solved it.",
        "Describe a time when you worked in a team.",
        "Tell me about a failure and what you learned from it.",
        "How do you handle a tight deadline?"
    ]
}

if category == "Mixed":
    questions = question_bank["Technical"][:2] + question_bank["HR"][:1] + question_bank["Behavioral"][:1]
else:
    questions = question_bank[category]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

q = questions[st.session_state.q_index % len(questions)]

st.markdown("### Current Question")
st.info(q)

answer = st.text_area("Your Answer", height=180, placeholder="Type your interview answer here...")

if st.button("🤖 Evaluate Answer", use_container_width=True):
    words = len(answer.split())
    if words < 10:
        score = 45
        feedback = "Your answer is too short. Add a specific example and explain your reasoning."
    elif words < 40:
        score = 72
        feedback = "Good start. Improve it by adding a concrete example, measurable result and clearer structure."
    else:
        score = 88
        feedback = "Strong answer. Keep it concise and use the STAR structure for behavioral questions."

    st.session_state.interview_score = score
    st.success(f"AI Evaluation Score: {score}%")
    st.progress(score / 100)
    st.write("**Feedback:**", feedback)

    st.markdown("#### Evaluation")
    a,b,c = st.columns(3)
    a.metric("Relevance", f"{min(95, score+3)}%")
    b.metric("Clarity", f"{max(50, score-4)}%")
    c.metric("Completeness", f"{max(50, score-7)}%")

if st.button("➡️ Next Question"):
    st.session_state.q_index += 1
    st.rerun()

st.markdown("---")
st.subheader("💡 Interview Tip")
st.write("For behavioral questions, use **STAR: Situation → Task → Action → Result**.")
