import streamlit as st
import os

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
    page_title="Interview Preparation",
    page_icon="🎤",
    layout="wide"
)


# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================

if "resume_text" not in st.session_state:
    st.session_state["resume_text"] = ""

if "target_role" not in st.session_state:
    st.session_state["target_role"] = ""

if "job_description" not in st.session_state:
    st.session_state["job_description"] = ""

if "interview_questions" not in st.session_state:
    st.session_state["interview_questions"] = ""


# ============================================================
# HEADER
# ============================================================

st.title("🎤 Interview Preparation")

st.write(
    "Prepare for your interview using your resume, "
    "target job role and job description."
)


# ============================================================
# LOAD DATA FROM RESUME CREATION
# ============================================================

resume_text = st.session_state.get(
    "resume_text",
    ""
)

saved_target_role = st.session_state.get(
    "target_role",
    ""
)

saved_job_description = st.session_state.get(
    "job_description",
    ""
)


# ============================================================
# INTERVIEW DETAILS
# ============================================================

st.subheader("🎯 Interview Details")

target_role = st.text_input(
    "Target Job Role",
    value=saved_target_role,
    placeholder="Example: Machine Learning Engineer"
)

job_description = st.text_area(
    "Job Description (Optional)",
    value=saved_job_description,
    placeholder="Paste the job description here...",
    height=180
)


# Save updated values to session state

st.session_state["target_role"] = target_role

st.session_state["job_description"] = job_description


# ============================================================
# RESUME STATUS
# ============================================================

st.subheader("📄 Candidate Resume")

if resume_text.strip():

    word_count = len(resume_text.split())

    st.success(
        f"✅ Resume loaded successfully — {word_count} words"
    )

    with st.expander("📄 View Extracted Resume"):

        st.text(resume_text[:5000])

        if len(resume_text) > 5000:

            st.caption(
                "Only the first 5000 characters are displayed."
            )

else:

    st.warning(
        "⚠️ No resume found."
    )

    st.info(
        "Please go to the Resume Creation page, "
        "upload your resume and click Analyze Resume "
        "before starting interview preparation."
    )


# ============================================================
# GEMINI FUNCTION
# ============================================================

def generate_interview_questions(
    resume_text,
    target_role,
    job_description
):

    if client is None:

        return (
            "❌ Gemini API key is not configured. "
            "Please check your .env file."
        )

    if not resume_text.strip():

        return "❌ Resume text is empty."

    if not target_role.strip():

        return "❌ Target job role is empty."


    prompt = f"""
You are CareerPilot AI, an expert technical interviewer
and career preparation assistant.

Your task is to create a personalized interview preparation
set for the candidate.

============================================================
TARGET JOB ROLE
============================================================

{target_role}

============================================================
JOB DESCRIPTION
============================================================

{job_description if job_description.strip() else "No job description provided."}

============================================================
CANDIDATE RESUME
============================================================

{resume_text}

============================================================
INTERVIEW QUESTION REQUIREMENTS
============================================================

Generate questions in the following six categories.

### 1. Technical Questions

Generate 3 questions related to the technical skills
required for the target role.

### 2. HR Questions

Generate 3 common HR interview questions relevant to
the candidate and target role.

### 3. Behavioral Questions

Generate 3 behavioral questions that test:

- Problem solving
- Teamwork
- Leadership
- Adaptability
- Communication

### 4. Resume-Based Questions

Generate 3 questions directly related to information
present in the candidate's resume.

### 5. Project-Based Questions

Generate 3 questions about projects mentioned in the resume.

### 6. Role-Specific Questions

Generate 3 questions that an interviewer would realistically
ask for the target job role.

============================================================
IMPORTANT RULES
============================================================

1. Use the candidate's actual resume as the primary source.

2. Do NOT invent:
   - Projects
   - Skills
   - Certifications
   - Education
   - Work experience
   - Achievements

3. If something is not present in the resume, do not claim
   that the candidate has it.

4. Questions can test knowledge that is required for the
   target role even if the candidate does not currently
   have that skill.

5. Resume-based questions must be based strictly on the
   provided resume.

6. Project questions must refer to actual projects in the
   resume.

7. Make the questions realistic and suitable for an actual
   interview.

============================================================
OUTPUT FORMAT
============================================================

# 🎯 Interview Preparation

## 1. 💻 Technical Questions

### Question 1
...

### Question 2
...

### Question 3
...

## 2. 👔 HR Questions

### Question 1
...

### Question 2
...

### Question 3
...

## 3. 🧠 Behavioral Questions

### Question 1
...

### Question 2
...

### Question 3
...

## 4. 📄 Resume-Based Questions

### Question 1
...

### Question 2
...

### Question 3
...

## 5. 🚀 Project-Based Questions

### Question 1
...

### Question 2
...

### Question 3
...

## 6. 🎯 Role-Specific Questions

### Question 1
...

### Question 2
...

### Question 3
...

## ⭐ Preparation Tips

Provide 5 short preparation tips specifically for this
candidate and target role.
"""


    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        if response.text:

            return response.text

        return (
            "❌ Gemini returned an empty response."
        )

    except Exception as error:

        return (
            f"❌ Question generation failed:\n\n{error}"
        )


# ============================================================
# GENERATE INTERVIEW QUESTIONS
# ============================================================

st.divider()

st.subheader("🤖 AI Interview Question Generator")


if st.button(
    "✨ Generate Interview Questions",
    type="primary",
    use_container_width=True
):

    # --------------------------------------------------------
    # Validation
    # --------------------------------------------------------

    if not target_role.strip():

        st.error(
            "❌ Please enter your target job role."
        )

    elif not resume_text.strip():

        st.error(
            "❌ Resume text is not available. "
            "Please upload and analyze your resume "
            "from the Resume Creation page first."
        )

    else:

        # ----------------------------------------------------
        # Generate questions
        # ----------------------------------------------------

        with st.spinner(
            "🤖 Gemini is preparing your personalized interview..."
        ):

            questions = generate_interview_questions(
                resume_text=resume_text,
                target_role=target_role,
                job_description=job_description
            )

        st.session_state[
            "interview_questions"
        ] = questions


# ============================================================
# DISPLAY GENERATED QUESTIONS
# ============================================================

if st.session_state.get(
    "interview_questions",
    ""
).strip():

    st.divider()

    st.subheader(
        "📋 Your Personalized Interview Questions"
    )

    st.markdown(
        st.session_state[
            "interview_questions"
        ]
    )


# ============================================================
# CLEAR QUESTIONS
# ============================================================

if st.session_state.get(
    "interview_questions",
    ""
).strip():

    st.divider()

    if st.button(
        "🗑️ Clear Interview Questions"
    ):

        st.session_state[
            "interview_questions"
        ] = ""

        st.rerun()