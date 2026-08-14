import streamlit as st

st.set_page_config(page_title="CareerPilot AI", page_icon="🚀", layout="wide")

if "profile" not in st.session_state:
    st.session_state.profile = {}
if "resume" not in st.session_state:
    st.session_state.resume = {}
if "interview_score" not in st.session_state:
    st.session_state.interview_score = 0

st.markdown("""
<style>
.main {background: #f7f9fc;}
.hero {
    padding: 32px;
    border-radius: 20px;
    background: linear-gradient(135deg,#111827,#374151);
    color: white;
    margin-bottom: 25px;
}
.card {
    padding: 22px;
    border-radius: 16px;
    background: white;
    border: 1px solid #e5e7eb;
    min-height: 150px;
}
.small {color:#6b7280;font-size:14px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🚀 CareerPilot AI</h1>
<h3>Your AI Career Assistant</h3>
<p>Create a professional resume • Practice interviews • Find relevant jobs</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Your Career Dashboard")

profile = st.session_state.profile
resume = st.session_state.resume

c1, c2, c3, c4 = st.columns(4)
c1.metric("Profile", "Ready" if profile else "Not created")
c2.metric("Resume", "Generated" if resume else "Not generated")
c3.metric("Interview Score", f"{st.session_state.interview_score}%")
c4.metric("Job Match", "82%" if profile else "--")

st.markdown("### What would you like to do?")

a, b, c = st.columns(3)

with a:
    st.markdown('<div class="card"><h3>📄 Resume Creation</h3><p>Create an ATS-friendly resume from your education, skills, projects and experience.</p></div>', unsafe_allow_html=True)
    st.page_link("pages/1_Resume_Creation.py", label="Open Resume Builder", icon="📄")

with b:
    st.markdown('<div class="card"><h3>🎤 Interview Preparation</h3><p>Practice technical, HR and behavioral questions and receive AI-style feedback.</p></div>', unsafe_allow_html=True)
    st.page_link("pages/2_Interview_Preparation.py", label="Start Interview", icon="🎤")

with c:
    st.markdown('<div class="card"><h3>💼 Job Search</h3><p>Find and rank jobs according to your skills and target role.</p></div>', unsafe_allow_html=True)
    st.page_link("pages/3_Job_Search.py", label="Search Jobs", icon="💼")

st.markdown("---")
st.info("Demo version: the AI logic is implemented locally so you can run the project without an API key. Replace the demo functions with your preferred LLM/job API later.")
