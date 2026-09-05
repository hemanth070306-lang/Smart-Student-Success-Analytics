import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Student Success Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef2ff, #f8fafc, #fdf4ff);
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main title */

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    background: linear-gradient(
        90deg,
        #4f46e5,
        #7c3aed,
        #db2777
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Section headings */

.section-title {
    font-size: 30px;
    font-weight: 800;
    color: #1e293b;
    margin-top: 15px;
}

/* Cards */

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 8px 25px rgba(0,0,0,0.07);
    margin-bottom: 20px;
}

.card h3 {
    color: #4f46e5;
}

/* Experiment card */

.exp-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border-left: 6px solid #6366f1;
    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

/* Hero */

.hero {
    background: linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed,
        #db2777
    );
    padding: 45px;
    border-radius: 25px;
    color: white;
    text-align: center;
    box-shadow: 0 15px 40px rgba(79,70,229,0.25);
}

.hero-title {
    font-size: 42px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 18px;
    opacity: 0.9;
}

/* Metric cards */

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 7px 20px rgba(0,0,0,0.06);
}

.metric-number {
    font-size: 32px;
    font-weight: 800;
    color: #4f46e5;
}

.metric-label {
    color: #64748b;
    font-size: 14px;
}

/* Information boxes */

.info {
    background: #eff6ff;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #3b82f6;
}

.success {
    background: #ecfdf5;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #10b981;
}

.warning {
    background: #fffbeb;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #f59e0b;
}

.danger {
    background: #fef2f2;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #ef4444;
}

/* Footer */

.footer {
    text-align: center;
    color: #64748b;
    padding: 30px;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATASETS
# ============================================================

try:

    students = pd.read_csv(
        "dataset/student_details.csv"
    )

    academic = pd.read_csv(
        "dataset/academic_performance.csv"
    )

    learning = pd.read_csv(
        "dataset/learning_behavior.csv"
    )

    activity = pd.read_csv(
        "dataset/activity_log.csv"
    )

    final_data = pd.read_csv(
        "output/final_student_success_dataset.csv"
    )

except Exception as e:

    st.error("❌ Dataset loading failed.")

    st.code(str(e))

    st.stop()


# ============================================================
# CLEAN DATA FOR DISPLAY
# ============================================================

final_data = final_data.copy()

numeric_columns = [
    "attendance",
    "assignment_score",
    "internal_marks",
    "external_marks",
    "study_hours",
    "online_hours",
    "library_visits",
    "practice_tests",
    "sleep_hours",
    "test_score",
    "total_marks",
    "average_score"
]

for col in numeric_columns:

    if col in final_data.columns:

        final_data[col] = pd.to_numeric(
            final_data[col],
            errors="coerce"
        )


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.markdown(
    """
    <div style="text-align:center;">
        <div style="font-size:55px;">🎓</div>
        <h2>SSSA</h2>
        <p>Student Success Analytics</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📚 Project Navigation",
    [
        "🏠 Home",
        "👤 Student Profile",
        "📂 Experiment 1 - Read CSV",
        "🔍 Experiment 2 - Data Exploration",
        "🩹 Experiment 3 - Missing Values",
        "🧹 Experiment 4 - Duplicates",
        "🔄 Experiment 5 - Datatype Conversion",
        "🔗 Experiment 6 - Merge & Concatenate",
        "📏 Experiment 7 - Scaling",
        "🔤 Experiment 8 - Encoding",
        "📦 Experiment 9 - Binning",
        "📊 Overall Analytics",
        "🏆 Student Insights"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Project Technologies**

    🐍 Python  
    🐼 Pandas  
    📊 Matplotlib  
    🤖 Scikit-learn  
    🌐 Streamlit
    """
)


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="hero">'
        '<div class="hero-title">'
        '🎓 SMART STUDENT SUCCESS ANALYTICS'
        '</div>'
        '<div class="hero-subtitle">'
        'A Comprehensive Data Wrangling and Learning Behavior Analysis System'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("")

    st.markdown(
        """
        <div class="card">

        <h2>📌 Project Overview</h2>

        <p>
        Smart Student Success Analytics is a comprehensive data
        wrangling and student analytics system developed to
        transform raw student data into clean, structured and
        analysis-ready information.
        </p>

        <p>
        The project integrates academic performance,
        attendance, learning behavior and student activity
        data using nine major Data Wrangling techniques.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # Metrics

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.markdown(
            """
            <div class="metric-card">
            <div class="metric-number">150</div>
            <div class="metric-label">STUDENTS</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="metric-card">
            <div class="metric-number">4</div>
            <div class="metric-label">DATASETS</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="metric-card">
            <div class="metric-number">9</div>
            <div class="metric-label">EXPERIMENTS</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:

        st.markdown(
            """
            <div class="metric-card">
            <div class="metric-number">38</div>
            <div class="metric-label">FINAL FEATURES</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("")

    # Pipeline

    st.markdown(
        '<div class="section-title">🔄 Data Processing Pipeline</div>',
        unsafe_allow_html=True
    )

    st.info(
        """
        📂 Raw CSV Data
        ↓
        🔍 Data Exploration
        ↓
        🩹 Missing Value Handling
        ↓
        🧹 Duplicate Cleaning
        ↓
        🔄 Datatype Conversion
        ↓
        🔗 Dataset Integration
        ↓
        📏 Scaling
        ↓
        🔤 Encoding
        ↓
        📦 Binning & Transformation
        ↓
        📊 Analytics
        ↓
        🎓 Student Insights
        """
    )

    st.markdown(
        """
        <div class="success">

        <h3>✨ Custom Dataset</h3>

        This project uses a custom-generated student dataset
        specifically created for this Data Wrangling project.
        It is not directly copied from a common Kaggle dataset.

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# STUDENT PROFILE
# ============================================================

elif page == "👤 Student Profile":

    st.markdown(
        '<div class="main-title">👤 Student Profile</div>',
        unsafe_allow_html=True
    )

    student_ids = sorted(
        final_data["student_id"].dropna().unique()
    )

    selected_id = st.selectbox(
        "🔎 Select Student ID",
        student_ids
    )

    student_rows = final_data[
        final_data["student_id"] == selected_id
    ]

    student = student_rows.iloc[0]

    st.markdown(
        f"""
        <div class="hero">

        <div class="hero-title">
        🎓 {student["student_id"]}
        </div>

        <div class="hero-subtitle">
        {student["name"]} • {student["branch"]} • Year {student["year"]}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📊 Performance Snapshot")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Average Score",
            f"{student['average_score']:.2f}"
        )

    with c2:
        st.metric(
            "Attendance",
            f"{student['attendance']:.1f}%"
        )

    with c3:
        st.metric(
            "Study Hours",
            f"{student['study_hours']:.1f}"
        )

    with c4:

        score = student["test_score"]

        if pd.notna(score):
            score_text = f"{score:.1f}"
        else:
            score_text = "N/A"

        st.metric(
            "Test Score",
            score_text
        )

    # Personal information

    st.markdown("### 👤 Personal Information")

    personal = pd.DataFrame({
        "Field": [
            "Name",
            "Gender",
            "Age",
            "Branch",
            "Year",
            "City"
        ],
        "Value": [
            student["name"],
            student["gender"],
            student["age"],
            student["branch"],
            student["year"],
            student["city"]
        ]
    })

    st.dataframe(
        personal,
        use_container_width=True,
        hide_index=True
    )

    # Academic

    st.markdown("### 📚 Academic Performance")

    academic_profile = pd.DataFrame({
        "Metric": [
            "Attendance",
            "Assignment Score",
            "Internal Marks",
            "External Marks",
            "Total Marks",
            "Average Score",
            "Performance Category"
        ],
        "Value": [
            student["attendance"],
            student["assignment_score"],
            student["internal_marks"],
            student["external_marks"],
            student["total_marks"],
            student["average_score"],
            student["performance_category"]
        ]
    })

    st.dataframe(
        academic_profile,
        use_container_width=True,
        hide_index=True
    )

    # Learning

    st.markdown("### 🧠 Learning Behavior")

    learning_profile = pd.DataFrame({
        "Metric": [
            "Study Hours",
            "Online Hours",
            "Library Visits",
            "Practice Tests",
            "Sleep Hours",
            "Preferred Resource",
            "Study Mode"
        ],
        "Value": [
            student["study_hours"],
            student["online_hours"],
            student["library_visits"],
            student["practice_tests"],
            student["sleep_hours"],
            student["preferred_resource"],
            student["study_mode"]
        ]
    })

    st.dataframe(
        learning_profile,
        use_container_width=True,
        hide_index=True
    )

    # Chart

    st.markdown("### 📈 Academic Score Breakdown")

    subjects = [
        "Assignment",
        "Internal",
        "External"
    ]

    scores = [
        student["assignment_score"],
        student["internal_marks"],
        student["external_marks"]
    ]

    fig, ax = plt.subplots(figsize=(9, 4))

    ax.bar(
        subjects,
        scores
    )

    ax.set_ylim(0, 100)

    ax.set_ylabel("Score")

    ax.set_title(
        "Academic Performance Breakdown"
    )

    ax.grid(
        axis="y",
        alpha=0.2
    )

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# EXPERIMENT 1
# ============================================================

elif page == "📂 Experiment 1 - Read CSV":

    st.markdown(
        '<div class="main-title">'
        'Experiment 1 — Reading CSV Data'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="exp-card">

        <h2>📂 Objective</h2>

        Read student information from a CSV file using
        the Pandas library and display the dataset.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.code(
        """
import pandas as pd

data = pd.read_csv(
    "dataset/student_details.csv"
)

print(data.head())
print(data.tail())
        """,
        language="python"
    )

    st.markdown("### 📊 Dataset Preview")

    st.dataframe(
        students.head(10),
        use_container_width=True
    )

    st.markdown("### 🔚 Last Records")

    st.dataframe(
        students.tail(5),
        use_container_width=True
    )

    st.success(
        "✅ CSV file was successfully loaded and displayed."
    )


# ============================================================
# EXPERIMENT 2
# ============================================================

elif page == "🔍 Experiment 2 - Data Exploration":

    st.markdown(
        '<div class="main-title">'
        'Experiment 2 — Dataset Exploration'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="exp-card">

        <h2>🔍 Objective</h2>

        Explore the structure, size, datatypes and
        statistical characteristics of the dataset.

        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Rows",
            students.shape[0]
        )

    with c2:
        st.metric(
            "Columns",
            students.shape[1]
        )

    with c3:
        st.metric(
            "Missing Values",
            int(students.isnull().sum().sum())
        )

    st.markdown("### 📋 Dataset Information")

    st.dataframe(
        pd.DataFrame({
            "Column": students.columns,
            "Datatype": students.dtypes.astype(str),
            "Non-Null Values": students.notnull().sum().values,
            "Missing Values": students.isnull().sum().values
        }),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 📊 Descriptive Statistics")

    st.dataframe(
        students.describe(
            include="all"
        ).transpose(),
        use_container_width=True
    )

    st.success(
        "✅ Dataset structure and statistical information explored successfully."
    )


# ============================================================
# EXPERIMENT 3
# ============================================================

elif page == "🩹 Experiment 3 - Missing Values":

    st.markdown(
        '<div class="main-title">'
        'Experiment 3 — Missing Value Handling'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="exp-card">

        <h2>🩹 Objective</h2>

        Identify missing values and handle them using
        appropriate data-cleaning techniques.

        </div>
        """,
        unsafe_allow_html=True
    )

    missing_before = students.isnull().sum()

    st.markdown("### 🔎 Missing Values Before Handling")

    st.dataframe(
        missing_before.rename(
            "Missing Values"
        ),
        use_container_width=True
    )

    cleaned = students.copy()

    cleaned["gender"] = cleaned["gender"].fillna(
        "Unknown"
    )

    cleaned["city"] = cleaned["city"].fillna(
        "Unknown"
    )

    st.markdown("### 🧹 Missing Values After Handling")

    st.dataframe(
        cleaned.isnull().sum().rename(
            "Missing Values"
        ),
        use_container_width=True
    )

    st.success(
        "✅ Missing categorical values were handled successfully."
    )


# ============================================================
# EXPERIMENT 4
# ============================================================

elif page == "🧹 Experiment 4 - Duplicates":

    st.markdown(
        '<div class="main-title">'
        'Experiment 4 — Duplicate & Inconsistent Records'
        '</div>',
        unsafe_allow_html=True
    )

    duplicate_count = students.duplicated().sum()

    st.metric(
        "🔁 Duplicate Records Detected",
        duplicate_count
    )

    st.markdown("### 🔎 Duplicate Records")

    if duplicate_count > 0:

        st.dataframe(
            students[
                students.duplicated()
            ],
            use_container_width=True
        )

    cleaned = students.drop_duplicates()

    st.markdown("### 🧹 Cleaning Operations")

    st.code(
        """
data = data.drop_duplicates()

data["gender"] = (
    data["gender"]
    .str.strip()
    .str.title()
)

data["branch"] = (
    data["branch"]
    .str.strip()
    .str.upper()
)

data["city"] = (
    data["city"]
    .str.strip()
    .str.title()
)
        """,
        language="python"
    )

    st.metric(
        "Records After Cleaning",
        len(cleaned)
    )

    st.success(
        "✅ Duplicate and inconsistent records cleaned successfully."
    )


# ============================================================
# EXPERIMENT 5
# ============================================================

elif page == "🔄 Experiment 5 - Datatype Conversion":

    st.markdown(
        '<div class="main-title">'
        'Experiment 5 — Datatype Conversion & Formatting'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="exp-card">

        <h2>🔄 Objective</h2>

        Convert columns into suitable datatypes and
        standardize text and date formats.

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📥 Original Activity Data")

    st.dataframe(
        activity.head(10),
        use_container_width=True
    )

    converted = activity.copy()

    converted["test_date"] = pd.to_datetime(
        converted["test_date"],
        errors="coerce"
    )

    converted["test_score"] = pd.to_numeric(
        converted["test_score"],
        errors="coerce"
    )

    converted["study_mode"] = (
        converted["study_mode"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    converted["remarks"] = (
        converted["remarks"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    st.markdown("### 🔄 Converted Datatypes")

    st.dataframe(
        pd.DataFrame({
            "Column": converted.columns,
            "Datatype": converted.dtypes.astype(str)
        }),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### 📊 Converted Data")

    st.dataframe(
        converted.head(10),
        use_container_width=True
    )

    st.success(
        "✅ Datatype conversion and formatting completed."
    )


# ============================================================
# EXPERIMENT 6
# ============================================================

elif page == "🔗 Experiment 6 - Merge & Concatenate":

    st.markdown(
        '<div class="main-title">'
        'Experiment 6 — Merge, Join & Concatenate'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="exp-card">

        <h2>🔗 Objective</h2>

        Combine multiple datasets using a common key
        and demonstrate dataset concatenation.

        <br><br>

        <b>Common Key:</b> student_id

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📂 Datasets")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Student Details",
            f"{students.shape[0]} × {students.shape[1]}"
        )

    with c2:
        st.metric(
            "Academic",
            f"{academic.shape[0]} × {academic.shape[1]}"
        )

    with c3:
        st.metric(
            "Learning",
            f"{learning.shape[0]} × {learning.shape[1]}"
        )

    with c4:
        st.metric(
            "Activity",
            f"{activity.shape[0]} × {activity.shape[1]}"
        )

    merged = pd.merge(
        students.drop_duplicates(),
        academic.drop_duplicates(),
        on="student_id",
        how="inner"
    )

    merged = pd.merge(
        merged,
        learning.drop_duplicates(),
        on="student_id",
        how="inner"
    )

    merged = pd.merge(
        merged,
        activity.drop_duplicates(),
        on="student_id",
        how="left"
    )

    st.markdown("### 🔗 Final Merged Dataset")

    st.dataframe(
        merged.head(10),
        use_container_width=True
    )

    st.metric(
        "Merged Dataset Shape",
        f"{merged.shape[0]} × {merged.shape[1]}"
    )

    concatenated = pd.concat(
        [
            students.drop_duplicates(),
            academic.drop_duplicates()
        ],
        axis=0,
        ignore_index=True
    )

    st.markdown("### ➕ Concatenated Dataset")

    st.metric(
        "Concatenated Shape",
        f"{concatenated.shape[0]} × {concatenated.shape[1]}"
    )

    st.success(
        "✅ Multiple datasets successfully merged and concatenated."
    )


# ============================================================
# EXPERIMENT 7
# ============================================================

elif page == "📏 Experiment 7 - Scaling":

    st.markdown(
        '<div class="main-title">'
        'Experiment 7 — Normalization & Standardization'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="exp-card">

        <h2>📏 Objective</h2>

        Transform numerical features to comparable scales
        using Min-Max Normalization and Standardization.

        </div>
        """,
        unsafe_allow_html=True
    )

    features = [
        "attendance",
        "assignment_score",
        "internal_marks",
        "external_marks",
        "study_hours"
    ]

    scale_data = final_data[features].copy()

    scale_data = scale_data.fillna(
        scale_data.median()
    )

    from sklearn.preprocessing import (
        MinMaxScaler,
        StandardScaler
    )

    minmax = MinMaxScaler()

    normalized = pd.DataFrame(
        minmax.fit_transform(scale_data),
        columns=features
    )

    standard = StandardScaler()

    standardized = pd.DataFrame(
        standard.fit_transform(scale_data),
        columns=features
    )

    st.markdown("### 📊 Original Numerical Data")

    st.dataframe(
        scale_data.head(10),
        use_container_width=True
    )

    st.markdown("### 📏 Min-Max Normalized Data")

    st.dataframe(
        normalized.head(10),
        use_container_width=True
    )

    st.markdown("### 📐 Standardized Data")

    st.dataframe(
        standardized.head(10),
        use_container_width=True
    )

    st.success(
        "✅ Normalization and standardization completed successfully."
    )


# ============================================================
# EXPERIMENT 8
# ============================================================

elif page == "🔤 Experiment 8 - Encoding":

    st.markdown(
        '<div class="main-title">'
        'Experiment 8 — Label & One-Hot Encoding'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="exp-card">

        <h2>🔤 Objective</h2>

        Convert categorical variables into numerical
        representations suitable for analysis and machine learning.

        </div>
        """,
        unsafe_allow_html=True
    )

    from sklearn.preprocessing import LabelEncoder

    encoded = final_data.copy()

    encoder = LabelEncoder()

    encoded["gender_encoded"] = encoder.fit_transform(
        encoded["gender"].fillna("Unknown")
    )

    st.markdown("### 🔢 Label Encoding")

    st.dataframe(
        encoded[
            [
                "gender",
                "gender_encoded"
            ]
        ].head(15),
        use_container_width=True
    )

    one_hot = pd.get_dummies(
        encoded,
        columns=[
            "branch",
            "preferred_resource",
            "study_mode"
        ],
        dtype=int
    )

    st.markdown("### 🔲 One-Hot Encoded Data")

    st.dataframe(
        one_hot.head(10),
        use_container_width=True
    )

    st.metric(
        "Encoded Dataset Shape",
        f"{one_hot.shape[0]} × {one_hot.shape[1]}"
    )

    st.success(
        "✅ Label encoding and one-hot encoding completed."
    )


# ============================================================
# EXPERIMENT 9
# ============================================================

elif page == "📦 Experiment 9 - Binning":

    st.markdown(
        '<div class="main-title">'
        'Experiment 9 — Binning, Transformation & Discretization'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="exp-card">

        <h2>📦 Objective</h2>

        Convert continuous numerical values into meaningful
        categories and apply mathematical transformation.

        </div>
        """,
        unsafe_allow_html=True
    )

    bin_data = final_data.copy()

    bin_data["attendance_category"] = pd.cut(
        bin_data["attendance"],
        bins=[
            0,
            60,
            75,
            90,
            100
        ],
        labels=[
            "Low",
            "Average",
            "Good",
            "Excellent"
        ]
    )

    bin_data["study_hours_log"] = np.log1p(
        bin_data["study_hours"]
    )

    bin_data["study_level"] = pd.cut(
        bin_data["study_hours"],
        bins=[
            -1,
            2,
            5,
            8,
            20
        ],
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

    st.markdown("### 📊 Binning Results")

    st.dataframe(
        bin_data[
            [
                "student_id",
                "attendance",
                "attendance_category",
                "study_hours",
                "study_hours_log",
                "study_level"
            ]
        ].head(15),
        use_container_width=True
    )

    st.markdown("### 📊 Attendance Categories")

    attendance_counts = (
        bin_data["attendance_category"]
        .value_counts()
    )

    st.bar_chart(
        attendance_counts
    )

    st.markdown("### 📚 Study Level Distribution")

    study_counts = (
        bin_data["study_level"]
        .value_counts()
    )

    st.bar_chart(
        study_counts
    )

    st.success(
        "✅ Binning, transformation and discretization completed."
    )


# ============================================================
# OVERALL ANALYTICS
# ============================================================

elif page == "📊 Overall Analytics":

    st.markdown(
        '<div class="main-title">'
        '📊 Overall Student Analytics'
        '</div>',
        unsafe_allow_html=True
    )

    # Metrics

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "👨‍🎓 Students",
            len(final_data)
        )

    with c2:

        st.metric(
            "📈 Average Score",
            f"{final_data['average_score'].mean():.2f}"
        )

    with c3:

        st.metric(
            "🕒 Average Attendance",
            f"{final_data['attendance'].mean():.2f}%"
        )

    with c4:

        st.metric(
            "📚 Avg Study Hours",
            f"{final_data['study_hours'].mean():.2f}"
        )

    # Branch

    st.markdown("### 🏫 Branch-wise Performance")

    branch_performance = (
        final_data
        .groupby(
            "branch",
            observed=True
        )["average_score"]
        .mean()
        .sort_values(
            ascending=False
        )
    )

    st.bar_chart(
        branch_performance
    )

    # Study vs score

    st.markdown("### 📚 Study Hours vs Average Score")

    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.scatter(
        final_data["study_hours"],
        final_data["average_score"]
    )

    ax.set_xlabel(
        "Study Hours"
    )

    ax.set_ylabel(
        "Average Score"
    )

    ax.set_title(
        "Study Hours vs Average Score"
    )

    ax.grid(
        alpha=0.2
    )

    st.pyplot(fig)

    plt.close(fig)

    # Attendance

    st.markdown("### 🕒 Attendance vs Average Score")

    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.scatter(
        final_data["attendance"],
        final_data["average_score"]
    )

    ax.set_xlabel(
        "Attendance (%)"
    )

    ax.set_ylabel(
        "Average Score"
    )

    ax.set_title(
        "Attendance vs Average Score"
    )

    ax.grid(
        alpha=0.2
    )

    st.pyplot(fig)

    plt.close(fig)


# ============================================================
# STUDENT INSIGHTS
# ============================================================

elif page == "🏆 Student Insights":

    st.markdown(
        '<div class="main-title">'
        '🏆 Student Performance Insights'
        '</div>',
        unsafe_allow_html=True
    )

    # Top students

    st.markdown("### 🥇 Top 10 Students")

    top_students = (
        final_data
        .sort_values(
            by="average_score",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_students[
            [
                "student_id",
                "name",
                "branch",
                "attendance",
                "average_score",
                "performance_category"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    # At risk

    st.markdown(
        "### ⚠️ Students Needing Improvement"
    )

    at_risk = final_data[
        (
            final_data["average_score"] < 60
        )
        |
        (
            final_data["attendance"] < 60
        )
    ]

    st.metric(
        "Students Needing Improvement",
        len(at_risk)
    )

    st.dataframe(
        at_risk[
            [
                "student_id",
                "name",
                "branch",
                "attendance",
                "average_score",
                "performance_category"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    # Performance categories

    st.markdown(
        "### 📊 Performance Category Distribution"
    )

    category_counts = (
        final_data[
            "performance_category"
        ]
        .value_counts()
    )

    st.bar_chart(
        category_counts
    )

    # Branch table

    st.markdown(
        "### 🏫 Branch Performance"
    )

    branch_performance = (
        final_data
        .groupby(
            "branch",
            observed=True
        )["average_score"]
        .mean()
        .sort_values(
            ascending=False
        )
    )

    st.dataframe(
        branch_performance.rename(
            "Average Score"
        ),
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🎓 <b>Smart Student Success Analytics</b>

    <br><br>

    Data Wrangling • Academic Analytics • Learning Behavior • Student Insights

    <br><br>

    Built with Python • Pandas • Scikit-learn • Streamlit

    </div>
    """,
    unsafe_allow_html=True
)