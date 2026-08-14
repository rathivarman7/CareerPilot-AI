import streamlit as st

st.set_page_config(page_title="Job Search", page_icon="💼", layout="wide")

st.title("💼 Relevant Job Search")
st.caption("Find jobs that match your profile. This demo uses sample job data; connect a permitted job API for live listings.")

profile = st.session_state.get("profile", {})

roles = [
    "Machine Learning Engineer",
    "Data Scientist",
    "Python Developer",
    "NLP Engineer",
    "AI Engineer",
    "Software Engineer"
]

role = st.selectbox("Search Role", roles, index=roles.index(profile.get("target_role")) if profile.get("target_role") in roles else 0)
location = st.text_input("Preferred Location", value="India")
remote = st.selectbox("Work Mode", ["Any", "Remote", "Hybrid", "On-site"])

jobs = [
    {"title":"Junior Machine Learning Engineer","company":"TechNova","location":"Bengaluru","mode":"Hybrid","skills":["Python","Machine Learning","SQL","TensorFlow"],"score":0},
    {"title":"AI Engineer","company":"InnovateAI","location":"Chennai","mode":"On-site","skills":["Python","NLP","Machine Learning","Docker"],"score":0},
    {"title":"Data Scientist","company":"DataWorks","location":"Hyderabad","mode":"Remote","skills":["Python","SQL","Statistics","Machine Learning"],"score":0},
    {"title":"Python Developer","company":"CloudSoft","location":"Pune","mode":"Hybrid","skills":["Python","FastAPI","SQL","Git"],"score":0},
    {"title":"NLP Engineer","company":"LanguageLabs","location":"Remote","mode":"Remote","skills":["Python","NLP","Transformers","PyTorch"],"score":0},
]

user_skills = {s.lower() for s in profile.get("skills", [])}

if st.button("🔎 Find Matching Jobs", use_container_width=True):
    results = []
    for job in jobs:
        role_match = role.lower().split()[0] in job["title"].lower() or role.lower() in job["title"].lower()
        skill_hits = sum(1 for s in job["skills"] if s.lower() in user_skills)
        skill_score = skill_hits / len(job["skills"]) * 100

        score = skill_score
        if role_match:
            score += 15
        if remote != "Any" and remote == job["mode"]:
            score += 10

        job["score"] = min(100, round(score))
        results.append(job)

    results.sort(key=lambda x: x["score"], reverse=True)

    st.subheader("Recommended Jobs")

    for job in results:
        with st.container(border=True):
            c1,c2 = st.columns([4,1])
            with c1:
                st.markdown(f"### {job['title']}")
                st.write(f"**{job['company']}** • {job['location']} • {job['mode']}")
                st.write("Required skills:", ", ".join(job["skills"]))
            with c2:
                st.metric("Match", f"{job['score']}%")
                st.button("View Job", key=job["title"])

    if results:
        best = results[0]
        missing = [s for s in best["skills"] if s.lower() not in user_skills]
        st.markdown("---")
        st.subheader("🎯 Career Gap Analysis")
        if missing:
            st.warning("Skills to improve: " + ", ".join(missing))
        else:
            st.success("You already have all listed skills for the top matching job.")

st.info("For production use, connect this page to a legitimate job-search API or licensed job data source rather than scraping websites without permission.")
