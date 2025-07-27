import streamlit as st
import os



# --------- CONSTANTS ---------
NAME = "ABC"
TAGLINE = "Python Developer | Data Engineer | ETL Expert"
EMAIL = "Your_email@gmail.com"
LINKEDIN = "https://linkedin.com/in/your_id"
GITHUB = "https://github.com/username"
RESUME_PATH = "Resume.pdf"

# --------- CONFIG ---------
st.set_page_config(page_title=f"{NAME} | Portfolio", layout="wide", page_icon="🐍")
# ----- DARK MODE TOGGLE -----
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

def toggle_theme():
    st.session_state["dark_mode"] = not st.session_state["dark_mode"]



projects = [
    {
        "title": "Data Pipeline Framework",
        "description": "A modular ETL framework built in Python for ingesting, transforming, and validating data using SQL and Pandas.",
        "tech": ["Python", "SQL", "Airflow", "DuckDB"],
        "link": "https://github.com/yourusername/data-pipeline-framework"
    },
    {
        "title": "Streamlit Data Explorer",
        "description": "A lightweight Streamlit tool for exploring CSV, Parquet, and Excel files visually with charts and profiling.",
        "tech": ["Streamlit", "Pandas", "Plotly"],
        "link": "https://github.com/yourusername/data-explorer"
    },
    {
        "title": "Data Quality Validator",
        "description": "Checks nulls, duplicates, schema mismatches across datasets and generates a quality score report.",
        "tech": ["Python", "Pandas", "Great Expectations"],
        "link": "https://github.com/yourusername/data-quality-validator"
    },
    {
        "title": "DuckDB SQL Tester",
        "description": "A simple local app to test SQL logic using DuckDB in-memory engine with support for joins, filters, and CTEs.",
        "tech": ["DuckDB", "SQL", "Streamlit"],
        "link": "https://github.com/yourusername/duckdb-sql-tester"
    },
    {
        "title": "Synthetic Data Generator",
        "description": "Generate realistic fake datasets for testing or demos using Faker, with custom schema support.",
        "tech": ["Python", "Faker", "Streamlit"],
        "link": "https://github.com/yourusername/synthetic-data-generator"
    }
]


PERSONAL_PROJECTS=[
    {
        "title": "🧾 ETL Log Analyzer",
        "description": "Streamlit app to inspect, search, and debug ETL logs using DuckDB.",
        "tech": "Python, DuckDB, Pandas",
        "link": "private repo"
    },
]

# --------- LOAD CUSTOM STYLE ---------


# Load correct theme CSS
if st.session_state["dark_mode"]:
    css_file = "dark.css"
else:
    css_file = "style.css"

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# --------- SIDEBAR NAV ---------
st.sidebar.title("⚙️ Explore")
page = st.sidebar.radio("Explore ", ["🏠 **About Me**", "📁 **Professional Experience**", "🛠️ **Skills**", "📬 **Contact**"],label_visibility = "collapsed")


# --------- NAVBAR ---------
st.markdown(f"""
    <div class='navbar'>
        <div class='nav-left'>
            <h1>{NAME}</h1>
            <p>{TAGLINE}</p>
        </div>
        <div class='nav-right'>
            <a href="{LINKEDIN}" target="_blank">LinkedIn</a>
            <a href="{GITHUB}" target="_blank">GitHub</a>
            <a href="mailto:{EMAIL}">Email</a>
""", unsafe_allow_html=True)



if os.path.exists(RESUME_PATH):
    with open(RESUME_PATH, "rb") as pdf_file:
        st.sidebar.text('')
        st.sidebar.text('')
        st.sidebar.text('')
        st.sidebar.markdown("## 📄Download Resume")
        st.sidebar.download_button("Download",
                                    data=pdf_file,
                                    file_name="Resume.pdf", 
                                    mime="application/pdf", 
                                    use_container_width=True,
                                    type="primary"
                                    )

st.markdown("</div></div><hr>", unsafe_allow_html=True)

# --------- PAGE ROUTES ---------
if page.startswith("🏠"):
    st.balloons()
    st.header("👋 Hello there")
    st.write("""
    I'm a Python developer with a strong Data Engineering background. I specialize in:
    - Building reliable ETL workflows
    - Designing scalable data pipelines
    - Creating interactive tools using Python, Streamlit & SQL.
    """)
    # st.image("https://source.unsplash.com/1600x500/?data,technology", use_container_width=True)

elif page.startswith("📁"):
    st.subheader("🚀 Professional Experience")
    for proj in projects:
        st.markdown(f"""
        <div class="project-card">
            <h4>{proj['title']}</h4>
            <i>{proj['description']} </i>
            <p><b>Tech Stack:</b> {proj['tech']}</p>
            <a class="button" href="{proj['link']}" target="_blank">🔗 View on GitHub</a>

        </div>
        """, unsafe_allow_html=True)

    st.subheader(" Personal Project")
    for proj in PERSONAL_PROJECTS:
        st.markdown(f"""
        <div class="project-card-personal">
            <h4>{proj['title']}</h4>
            <i>{proj['description']} </i>
            <p><b>Tech Stack:</b> {proj['tech']}</p>
            <a class="button" href="{proj['link']}" target="_blank">🔗 View on GitHub</a>

        </div>
        """, unsafe_allow_html=True)


elif page.startswith("🛠️"):
    st.header("🛠️ Skills")
    st.markdown("""
    <ul class="skills">
        <li><b>Languages:</b> Python ,SQL ,Bash</li>
        <li><b>Frameworks:</b> Airflow, Streamlit, Pandas, PySpark</li>
        <li><b>Databases:</b> Snowflake, DuckDB, PostgreSQL</li>
        <li><b>Tools:</b> Git, Docker, VS Code, Jupyter</li>
    </ul>
    """, unsafe_allow_html=True)

    
elif page.startswith("📬"):
    st.header("📬 Contact Me")
    st.markdown(f"""
    Want to work together or have a question?
    - 📧 Email: [{EMAIL}](mailto:{EMAIL})
    - 💼 LinkedIn: [Profile]({LINKEDIN})
    - 🐍 GitHub: [Repo]({GITHUB})
    """)

    st.write('')
    with st.form("contact_form"):
        name = st.text_input(":blue[Your Name]")
        email = st.text_input(":blue[Your Email]")
        message = st.text_area(":blue[Your Message]")
        submitted = st.form_submit_button("Send",type='primary')

        if submitted:
            st.success("Message sent! (This is a placeholder — integrate with FormSubmit or backend)")
# Theme switch button

st.sidebar.text('')
st.sidebar.markdown("## 🌓 Theme")
if st.sidebar.button("Toggle Dark Mode"):
    toggle_theme()
