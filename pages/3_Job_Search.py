import streamlit as st
import os
import re

from dotenv import load_dotenv
from google import genai


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv(override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
else:
    client = None


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Job Search",
    page_icon="💼",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "resume_text" not in st.session_state:
    st.session_state["resume_text"] = ""

if "target_role" not in st.session_state:
    st.session_state["target_role"] = ""

if "job_analysis" not in st.session_state:
    st.session_state["job_analysis"] = ""


# ============================================================
# HEADER
# ============================================================

st.title("💼 Job Search")

st.write(
    "Find relevant job opportunities based on your "
    "skills, resume and career goals."
)


# ============================================================
# LOAD RESUME
# ============================================================

resume_text = st.session_state.get(
    "resume_text",
    ""
)

saved_target_role = st.session_state.get(
    "target_role",
    ""
)


# ============================================================
# SEARCH DETAILS
# ============================================================

st.subheader("🔎 Job Search Preferences")

target_role = st.text_input(
    "Job Role",
    value=saved_target_role,
    placeholder="Example: Machine Learning Engineer"
)

location = st.text_input(
    "Preferred Location",
    placeholder="Example: Chennai, Bangalore, Remote"
)

experience_level = st.selectbox(
    "Experience Level",
    [
        "Any",
        "Internship",
        "Fresher",
        "Entry Level",
        "1-3 Years",
        "3-5 Years"
    ]
)

remote_option = st.selectbox(
    "Work Preference",
    [
        "Any",
        "Remote",
        "Hybrid",
        "On-site"
    ]
)


# Save target role

st.session_state["target_role"] = target_role


# ============================================================
# RESUME STATUS
# ============================================================

st.subheader("📄 Candidate Profile")

if resume_text.strip():

    st.success(
        f"✅ Resume loaded — {len(resume_text.split())} words"
    )

else:

    st.warning(
        "⚠️ No resume found. Upload and analyze your resume "
        "from the Resume Creation page first."
    )


# ============================================================
# JOB SEARCH LINKS
# ============================================================

def create_job_search_links(
    role,
    location,
    experience
):

    role_encoded = role.replace(" ", "+")
    location_encoded = location.replace(" ", "+")

    links = {

        "LinkedIn Jobs":
            f"https://www.linkedin.com/jobs/search/"
            f"?keywords={role_encoded}"
            f"&location={location_encoded}",

        "Indeed":
            f"https://www.indeed.com/jobs"
            f"?q={role_encoded}"
            f"&l={location_encoded}",

        "Naukri":
            f"https://www.naukri.com/"
            f"{role.lower().replace(' ', '-')}-jobs"
    }

    return links


# ============================================================
# GEMINI JOB MATCHING
# ============================================================

def analyze_job_match(
    resume_text,
    target_role,
    job_description
):

    if client is None:

        return (
            "❌ Gemini API key is not configured."
        )

    prompt = f"""
You are CareerPilot AI, an expert career advisor.

Analyze how well the candidate matches the job.

TARGET ROLE:
{target_role}

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME:
-------------------------
{resume_text}
-------------------------

Perform a detailed skill-gap analysis.

Return:

## 🎯 Overall Match Score

Give a score from 0 to 100.

## ✅ Matching Skills

List skills the candidate has that are relevant
to the job.

## ❌ Missing Skills

List important skills required by the job that are
not clearly present in the resume.

## ⭐ Strong Matches

Identify the strongest areas of the candidate.

## ⚠️ Skill Gaps

Explain the most important gaps.

## 📚 Recommended Learning

Recommend specific skills or technologies the
candidate should learn.

## 💡 Application Advice

Give 3 practical suggestions for applying to this job.

IMPORTANT:
- Use only information supported by the resume.
- Do not invent candidate skills.
- Clearly distinguish existing skills from recommended skills.
"""


    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        if response.text:

            return response.text

        return "❌ Gemini returned an empty response."

    except Exception as error:

        return f"❌ Job analysis failed: {error}"


# ============================================================
# JOB SEARCH
# ============================================================

st.divider()

st.subheader("🚀 Search Relevant Jobs")


if st.button(
    "🔍 Find Relevant Jobs",
    type="primary",
    use_container_width=True
):

    if not target_role.strip():

        st.error(
            "Please enter a job role."
        )

    elif not location.strip():

        st.error(
            "Please enter a preferred location."
        )

    elif not resume_text.strip():

        st.error(
            "Please upload and analyze your resume "
            "from the Resume Creation page first."
        )

    else:

        links = create_job_search_links(
            target_role,
            location,
            experience_level
        )

        st.subheader("🌐 Job Search Platforms")

        for platform, url in links.items():

            st.markdown(
                f"### 🔗 [{platform}]({url})"
            )

        st.info(
            "These links open job-search pages using "
            "your selected role and location."
        )


# ============================================================
# JOB DESCRIPTION MATCHING
# ============================================================

st.divider()

st.subheader("🤖 AI Job Match Analyzer")

job_description = st.text_area(
    "Paste a Job Description",
    placeholder=(
        "Paste the job description here to calculate "
        "how well your resume matches the job..."
    ),
    height=250
)


if st.button(
    "🎯 Analyze Job Match",
    use_container_width=True
):

    if not resume_text.strip():

        st.error(
            "Please upload and analyze your resume first."
        )

    elif not target_role.strip():

        st.error(
            "Please enter the target job role."
        )

    elif not job_description.strip():

        st.error(
            "Please paste a job description."
        )

    else:

        with st.spinner(
            "🤖 Gemini is analyzing your job match..."
        ):

            result = analyze_job_match(
                resume_text=resume_text,
                target_role=target_role,
                job_description=job_description
            )

        st.session_state[
            "job_analysis"
        ] = result


# ============================================================
# DISPLAY MATCH ANALYSIS
# ============================================================

if st.session_state.get(
    "job_analysis",
    ""
).strip():

    st.divider()

    st.subheader(
        "📊 AI Job Match Analysis"
    )

    st.markdown(
        st.session_state[
            "job_analysis"
        ]
    )


# ============================================================
# CAREER GAP
# ============================================================

if st.session_state.get(
    "job_analysis",
    ""
).strip():

    st.divider()

    st.subheader(
        "📈 Career Gap Analysis"
    )

    st.info(
        "Use the Missing Skills and Recommended Learning "
        "sections above to identify the skills you should "
        "develop for your target role."
    )