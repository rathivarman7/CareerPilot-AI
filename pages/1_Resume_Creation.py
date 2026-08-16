import streamlit as st
import re
from io import BytesIO

from pypdf import PdfReader
from docx import Document


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="CareerPilot AI - Resume Creation",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Creation & Analysis")
st.write(
    "Upload your resume, select a target role, and analyze your "
    "resume for skills, ATS readiness, and career gaps."
)

st.divider()


# ---------------------------------------------------------
# SKILL DATABASE
# ---------------------------------------------------------

SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "TypeScript",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Node.js",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "NLP",
    "Natural Language Processing",
    "Computer Vision",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Power BI",
    "Tableau",
    "Excel",
    "AWS",
    "Azure",
    "Google Cloud",
    "Docker",
    "Kubernetes",
    "Git",
    "GitHub",
    "Linux",
    "FastAPI",
    "Flask",
    "Django",
    "Streamlit",
    "R",
    "Data Science",
    "Data Analytics",
]


# ---------------------------------------------------------
# RESUME TEXT EXTRACTION
# ---------------------------------------------------------

def extract_pdf_text(uploaded_file):
    """Extract text from a PDF resume."""

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx_text(uploaded_file):
    """Extract text from a DOCX resume."""

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text


def extract_resume_text(uploaded_file):

    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    try:

        if file_name.endswith(".pdf"):
            return extract_pdf_text(uploaded_file)

        elif file_name.endswith(".docx"):
            return extract_docx_text(uploaded_file)

        else:
            return ""

    except Exception as error:

        st.error(f"Unable to read the resume: {error}")

        return ""


# ---------------------------------------------------------
# SKILL EXTRACTION
# ---------------------------------------------------------

def extract_skills(text):

    detected_skills = []

    text_lower = text.lower()

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):

            detected_skills.append(skill)

    return sorted(
        list(set(detected_skills)),
        key=str.lower
    )


# ---------------------------------------------------------
# BASIC RESUME ANALYSIS
# ---------------------------------------------------------

def analyze_resume(text):

    text_lower = text.lower()

    sections = {
        "Education": [
            "education",
            "academic",
            "degree",
            "bachelor",
            "master"
        ],

        "Experience": [
            "experience",
            "work experience",
            "employment",
            "internship"
        ],

        "Projects": [
            "projects",
            "project"
        ],

        "Skills": [
            "skills",
            "technical skills",
            "technologies"
        ],

        "Certifications": [
            "certification",
            "certifications"
        ]
    }

    section_results = {}

    for section, keywords in sections.items():

        found = any(
            keyword in text_lower
            for keyword in keywords
        )

        section_results[section] = found

    return section_results


# ---------------------------------------------------------
# ATS SCORE
# ---------------------------------------------------------

def calculate_ats_score(text, target_role, skills, sections):

    score = 0

    text_lower = text.lower()

    # Resume length
    word_count = len(text.split())

    if word_count >= 300:
        score += 20

    elif word_count >= 150:
        score += 15

    elif word_count >= 75:
        score += 10

    # Skills
    if len(skills) >= 8:
        score += 25

    elif len(skills) >= 5:
        score += 20

    elif len(skills) >= 3:
        score += 15

    elif len(skills) >= 1:
        score += 10

    # Target role relevance
    if target_role.strip():

        role_words = [
            word.lower()
            for word in re.findall(
                r"[A-Za-z]+",
                target_role
            )
            if len(word) > 2
        ]

        matched_role_words = sum(
            word in text_lower
            for word in role_words
        )

        if role_words:

            role_score = (
                matched_role_words / len(role_words)
            ) * 20

            score += int(role_score)

    # Resume sections
    section_score = sum(sections.values())

    score += min(section_score * 5, 25)

    return min(score, 100)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "resume_skills" not in st.session_state:
    st.session_state.resume_skills = []

if "resume_analysis" not in st.session_state:
    st.session_state.resume_analysis = {}

if "ats_score" not in st.session_state:
    st.session_state.ats_score = 0


# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------

st.subheader("1️⃣ Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload PDF or DOCX",
    type=["pdf", "docx"]
)

target_role = st.text_input(
    "🎯 Target Job Role",
    placeholder="Example: Machine Learning Engineer"
)


# ---------------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------------

if st.button(
    "🔍 Analyze Resume",
    type="primary",
    use_container_width=True
):

    if uploaded_file is None:

        st.warning(
            "Please upload a PDF or DOCX resume."
        )

    elif not target_role.strip():

        st.warning(
            "Please enter your target job role."
        )

    else:

        with st.spinner(
            "Analyzing your resume..."
        ):

            resume_text = extract_resume_text(
                uploaded_file
            )

            if not resume_text.strip():

                st.error(
                    "No readable text was found in the resume."
                )

            else:

                skills = extract_skills(
                    resume_text
                )

                analysis = analyze_resume(
                    resume_text
                )

                ats_score = calculate_ats_score(
                    resume_text,
                    target_role,
                    skills,
                    analysis
                )

                st.session_state.resume_text = resume_text
                st.session_state.resume_skills = skills
                st.session_state.resume_analysis = analysis
                st.session_state.ats_score = ats_score

                st.success(
                    "Resume analysis completed!"
                )


# ---------------------------------------------------------
# RESULTS
# ---------------------------------------------------------

if st.session_state.resume_text:

    st.divider()

    st.subheader("2️⃣ Resume Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "ATS Score",
            f"{st.session_state.ats_score}%"
        )

    with col2:

        word_count = len(
            st.session_state.resume_text.split()
        )

        st.metric(
            "Resume Words",
            word_count
        )

    with col3:

        st.metric(
            "Skills Detected",
            len(
                st.session_state.resume_skills
            )
        )


    # -----------------------------------------------------
    # SKILLS
    # -----------------------------------------------------

    st.subheader("🛠️ Detected Skills")

    if st.session_state.resume_skills:

        skill_text = " • ".join(
            st.session_state.resume_skills
        )

        st.success(skill_text)

    else:

        st.warning(
            "No recognized technical skills were detected."
        )


    # -----------------------------------------------------
    # SECTIONS
    # -----------------------------------------------------

    st.subheader("📑 Resume Sections")

    section_columns = st.columns(5)

    for column, (section, found) in zip(
        section_columns,
        st.session_state.resume_analysis.items()
    ):

        with column:

            if found:

                st.success(
                    f"✓ {section}"
                )

            else:

                st.error(
                    f"✗ {section}"
                )


    # -----------------------------------------------------
    # RECOMMENDATIONS
    # -----------------------------------------------------

    st.subheader("💡 Improvement Suggestions")

    recommendations = []

    if st.session_state.ats_score < 70:

        recommendations.append(
            "Improve ATS compatibility by adding relevant "
            "keywords from your target job description."
        )

    if len(st.session_state.resume_skills) < 5:

        recommendations.append(
            "Add more relevant technical skills that you "
            "actually possess."
        )

    if not st.session_state.resume_analysis.get(
        "Projects",
        False
    ):

        recommendations.append(
            "Add a Projects section with measurable outcomes."
        )

    if not st.session_state.resume_analysis.get(
        "Experience",
        False
    ):

        recommendations.append(
            "Add internship, work, or relevant practical experience."
        )

    if not st.session_state.resume_analysis.get(
        "Certifications",
        False
    ):

        recommendations.append(
            "Add relevant certifications if you have them."
        )

    if not recommendations:

        recommendations.append(
            "Your resume has a good basic structure. "
            "Next, optimize it specifically for the target job description."
        )

    for recommendation in recommendations:

        st.info(
            f"💡 {recommendation}"
        )


    # -----------------------------------------------------
    # RESUME TEXT
    # -----------------------------------------------------

    with st.expander(
        "📄 View Extracted Resume Text"
    ):

        st.text_area(
            "Extracted Text",
            st.session_state.resume_text,
            height=350
        )


    # -----------------------------------------------------
    # DOWNLOAD EXTRACTED TEXT
    # -----------------------------------------------------

    text_bytes = (
        st.session_state.resume_text
        .encode("utf-8")
    )

    st.download_button(
        label="⬇️ Download Extracted Resume Text",
        data=text_bytes,
        file_name="careerpilot_resume_text.txt",
        mime="text/plain"
)