import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------------
       GLOBAL
    ------------------------------------------------------- */

    .stApp {
        background: linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2ff 50%,
            #f8fafc 100%
        );
    }

    .main {
        padding-top: 2rem;
    }


    /* -------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------- */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #111827 0%,
            #1e293b 100%
        );
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    .sidebar-brand {
        text-align: center;
        padding: 20px 5px;
    }

    .sidebar-brand-icon {
        font-size: 42px;
        margin-bottom: 5px;
    }

    .sidebar-brand-title {
        font-size: 24px;
        font-weight: 700;
    }

    .sidebar-brand-subtitle {
        font-size: 13px;
        color: #cbd5e1;
        margin-top: 6px;
    }

    .sidebar-divider {
        border: none;
        border-top: 1px solid #475569;
        margin: 20px 0;
    }


    /* -------------------------------------------------------
       HERO SECTION
       ------------------------------------------------------- */

    .hero {
        background: linear-gradient(
            135deg,
            #111827 0%,
            #1e1b4b 50%,
            #312e81 100%
        );

        border-radius: 22px;
        padding: 55px 40px;
        text-align: center;

        box-shadow:
            0 20px 50px rgba(15, 23, 42, 0.20);

        margin-bottom: 35px;
    }

    .hero-icon {
        font-size: 55px;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        color: white;
        margin-bottom: 15px;
    }

    .hero-title span {
        color: #a5b4fc;
    }

    .hero-subtitle {
        max-width: 750px;
        margin: auto;

        font-size: 18px;
        line-height: 1.7;

        color: #cbd5e1;
    }


    /* -------------------------------------------------------
       SECTION TITLE
       ------------------------------------------------------- */

    .section-title {
        font-size: 28px;
        font-weight: 750;
        color: #111827;
        margin-top: 30px;
        margin-bottom: 20px;
    }


    /* -------------------------------------------------------
       FEATURE CARDS
       ------------------------------------------------------- */

    .card-container {
        display: flex;
        gap: 22px;
        margin-top: 20px;
        margin-bottom: 35px;
    }

    .feature-card {
        flex: 1;

        background: white;

        border-radius: 18px;

        padding: 30px 25px;

        min-height: 220px;

        border: 1px solid #e2e8f0;

        box-shadow:
            0 10px 30px rgba(15, 23, 42, 0.08);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px);

        box-shadow:
            0 18px 40px rgba(15, 23, 42, 0.14);
    }

    .card-icon {
        font-size: 42px;
        margin-bottom: 15px;
    }

    .card-title {
        font-size: 22px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 10px;
    }

    .card-text {
        color: #64748b;
        font-size: 15px;
        line-height: 1.6;
    }


    /* -------------------------------------------------------
       WORKFLOW
       ------------------------------------------------------- */

    .workflow {
        background: white;

        border-radius: 20px;

        padding: 30px;

        border: 1px solid #e2e8f0;

        box-shadow:
            0 10px 30px rgba(15, 23, 42, 0.07);

        margin-top: 25px;
    }

    .workflow-title {
        font-size: 24px;
        font-weight: 700;
        color: #111827;
        text-align: center;
        margin-bottom: 25px;
    }

    .workflow-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
    }

    .workflow-step {
        background: #eef2ff;

        color: #312e81;

        border-radius: 14px;

        padding: 15px 20px;

        text-align: center;

        font-weight: 650;

        min-width: 150px;
    }

    .workflow-arrow {
        font-size: 24px;
        color: #6366f1;
        font-weight: bold;
    }


    /* -------------------------------------------------------
       STATS
       ------------------------------------------------------- */

    .stats-container {
        display: flex;
        gap: 20px;
        margin-top: 30px;
    }

    .stat-card {
        flex: 1;

        background: white;

        border-radius: 16px;

        padding: 25px;

        text-align: center;

        border: 1px solid #e2e8f0;

        box-shadow:
            0 8px 25px rgba(15, 23, 42, 0.06);
    }

    .stat-number {
        font-size: 32px;
        font-weight: 800;
        color: #4f46e5;
    }

    .stat-label {
        font-size: 14px;
        color: #64748b;
        margin-top: 5px;
    }


    /* -------------------------------------------------------
       FOOTER
       ------------------------------------------------------- */

    .footer {
        text-align: center;

        margin-top: 50px;
        padding: 25px;

        color: #64748b;

        font-size: 14px;

        border-top: 1px solid #e2e8f0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """<div class="sidebar-brand">
<div class="sidebar-brand-icon">🚀</div>
<div class="sidebar-brand-title">CareerPilot AI</div>
<div class="sidebar-brand-subtitle">Your AI-powered career assistant</div>
</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        '<hr class="sidebar-divider">',
        unsafe_allow_html=True
    )

    st.markdown(
        "### 📌 Career Tools"
    )

    st.page_link(
        "pages/1_Resume_Creation.py",
        label="📄 Resume Creation",
        icon="📄"
    )

    st.page_link(
        "pages/2_Interview_Preparation.py",
        label="🎤 Interview Preparation",
        icon="🎤"
    )

    st.page_link(
        "pages/3_Job_Search.py",
        label="💼 Job Search",
        icon="💼"
    )

    st.markdown(
        '<hr class="sidebar-divider">',
        unsafe_allow_html=True
    )

    st.markdown(
        "### 📊 Your Progress"
    )

    resume_loaded = bool(
        st.session_state.get(
            "resume_text",
            ""
        )
    )

    if resume_loaded:

        st.success(
            "📄 Resume Loaded"
        )

    else:

        st.info(
            "📄 Resume Not Loaded"
        )

    st.markdown(
        '<hr class="sidebar-divider">',
        unsafe_allow_html=True
    )

    st.caption(
        "CareerPilot AI © 2026"
    )


# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """<div class="hero">
<div class="hero-icon">🚀</div>
<div class="hero-title">Welcome to <span>CareerPilot AI</span></div>
<div class="hero-subtitle">Your intelligent career assistant for creating professional resumes, preparing for interviews, and discovering relevant job opportunities.</div>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# WELCOME
# ============================================================

st.markdown(
    """<div class="section-title">🚀 Your Career Journey Starts Here</div>""",
    unsafe_allow_html=True
)


# ============================================================
# FEATURE CARDS
# ============================================================

st.markdown(
    """<div class="card-container">
<div class="feature-card">
<div class="card-icon">📄</div>
<div class="card-title">Resume Creation</div>
<div class="card-text">Upload your resume, analyze your strengths and weaknesses, and get AI-powered recommendations to improve your resume.</div>
</div>
<div class="feature-card">
<div class="card-icon">🎤</div>
<div class="card-title">Interview Preparation</div>
<div class="card-text">Generate personalized technical, HR, behavioral, resume-based and project-based interview questions.</div>
</div>
<div class="feature-card">
<div class="card-icon">💼</div>
<div class="card-title">Job Search</div>
<div class="card-text">Discover relevant job opportunities based on your skills, target role, experience and preferred location.</div>
</div>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# NAVIGATION BUTTONS
# ============================================================

st.markdown(
    """<div class="section-title">🛠️ Start Using CareerPilot</div>""",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


with col1:

    st.page_link(
        "pages/1_Resume_Creation.py",
        label="📄 Create / Analyze Resume",
        icon="📄",
        use_container_width=True
    )


with col2:

    st.page_link(
        "pages/2_Interview_Preparation.py",
        label="🎤 Prepare for Interview",
        icon="🎤",
        use_container_width=True
    )


with col3:

    st.page_link(
        "pages/3_Job_Search.py",
        label="💼 Search Relevant Jobs",
        icon="💼",
        use_container_width=True
    )


# ============================================================
# WORKFLOW
# ============================================================

st.markdown(
    """<div class="workflow">
<div class="workflow-title">🔄 How CareerPilot AI Works</div>
<div class="workflow-container">
<div class="workflow-step">👤 User Profile</div>
<div class="workflow-arrow">→</div>
<div class="workflow-step">📄 Resume</div>
<div class="workflow-arrow">→</div>
<div class="workflow-step">🤖 AI Analysis</div>
<div class="workflow-arrow">→</div>
<div class="workflow-step">🎤 Interview</div>
<div class="workflow-arrow">→</div>
<div class="workflow-step">💼 Job Matching</div>
<div class="workflow-arrow">→</div>
<div class="workflow-step">📈 Career Growth</div>
</div>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# STATISTICS / FEATURES
# ============================================================

st.markdown(
    """<div class="section-title">⭐ CareerPilot Features</div>""",
    unsafe_allow_html=True
)

st.markdown(
    """<div class="stats-container">
<div class="stat-card">
<div class="stat-number">01</div>
<div class="stat-label">AI Resume Analysis</div>
</div>
<div class="stat-card">
<div class="stat-number">02</div>
<div class="stat-label">Interview Preparation</div>
</div>
<div class="stat-card">
<div class="stat-number">03</div>
<div class="stat-label">Intelligent Job Matching</div>
</div>
<div class="stat-card">
<div class="stat-number">AI</div>
<div class="stat-label">Powered Career Guidance</div>
</div>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# CAREER ASSISTANT INFORMATION
# ============================================================

st.markdown(
    """<div class="workflow">
<div class="workflow-title">🤖 What CareerPilot AI Can Do</div>
<p><strong>📄 Resume Analysis:</strong> Analyze your resume and identify strengths, weaknesses, missing skills and ATS keywords.</p>
<p><strong>🎤 Interview Preparation:</strong> Generate interview questions based on your resume, target role and job description.</p>
<p><strong>💼 Job Search:</strong> Find relevant job opportunities based on your target role, skills and preferred location.</p>
<p><strong>📈 Career Gap Analysis:</strong> Identify missing skills and receive recommendations for improving your career profile.</p>
</div>""",
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """<div class="footer">
🚀 <strong>CareerPilot AI</strong>
<br>
AI-powered Resume Creation • Interview Preparation • Job Search
<br><br>
Built with Python, Streamlit and Gemini AI
</div>""",
    unsafe_allow_html=True
)