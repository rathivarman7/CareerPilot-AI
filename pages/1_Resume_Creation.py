import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Resume Creation", page_icon="📄", layout="wide")

st.title("📄 Resume Creation")
st.caption("Build an ATS-friendly resume using your profile information.")

with st.form("resume_form"):
    left, right = st.columns(2)
    with left:
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        location = st.text_input("Location")
        education = st.text_area("Education", placeholder="B.E. Computer Science, ABC College, 2026")
    with right:
        target_role = st.text_input("Target Job Role", placeholder="Machine Learning Engineer")
        skills = st.text_area("Skills", placeholder="Python, SQL, Machine Learning, NLP")
        projects = st.text_area("Projects", placeholder="AI Career Assistant - built using Python and Streamlit")
        experience = st.text_area("Experience / Internship")
        certifications = st.text_area("Certifications")
    submitted = st.form_submit_button("✨ Generate Resume", use_container_width=True)

if submitted:
    if not name or not target_role or not skills:
        st.error("Please enter at least your name, target role and skills.")
    else:
        skill_list = [x.strip() for x in skills.split(",") if x.strip()]
        summary = f"Motivated {target_role} candidate with skills in {', '.join(skill_list[:5])}. Interested in applying technical knowledge to real-world projects and continuously improving professional skills."

        st.session_state.profile = {
            "name": name, "email": email, "phone": phone, "location": location,
            "education": education, "target_role": target_role, "skills": skill_list,
            "projects": projects, "experience": experience, "certifications": certifications
        }
        st.session_state.resume = {"summary": summary, "skills": skill_list}

        st.success("Resume generated successfully!")

profile = st.session_state.get("profile", {})
if profile:
    st.markdown("---")
    st.subheader("Resume Preview")

    resume_text = f"""# {profile.get('name','')}
**{profile.get('target_role','')}**

{profile.get('email','')} | {profile.get('phone','')} | {profile.get('location','')}

## Professional Summary
{st.session_state.resume.get('summary','')}

## Skills
{', '.join(profile.get('skills', []))}

## Education
{profile.get('education','')}

## Projects
{profile.get('projects','')}

## Experience
{profile.get('experience','')}

## Certifications
{profile.get('certifications','')}
"""
    st.markdown(resume_text)

    score = min(98, 55 + len(profile.get("skills", []))*5 + (10 if profile.get("projects") else 0) + (10 if profile.get("experience") else 0))
    st.metric("Estimated ATS Readiness", f"{score}%")

    st.download_button(
        "⬇️ Download Resume",
        data=resume_text,
        file_name="careerpilot_resume.md",
        mime="text/markdown",
        use_container_width=True
    )
