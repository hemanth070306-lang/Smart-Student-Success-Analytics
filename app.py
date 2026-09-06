import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import BeautifulSoup

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Student Success Analytics",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
}

.hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 700;
}

.hero p {
    font-size: 18px;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

students = pd.read_csv("dataset/student_details.csv")
academic = pd.read_csv("dataset/academic_performance.csv")
learning = pd.read_csv("dataset/learning_behavior.csv")
activity = pd.read_csv("dataset/activity_log.csv")

final_data = pd.read_csv(
    "output/final_student_success_dataset.csv"
)


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.title("📚 Project Navigation")

page = st.sidebar.radio(
    "Select Section",
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
        "🌐 Experiment 10 - Web Scraping",
        "📊 Overall Analytics",
        "🏆 Student Insights"
    ]
)


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🎓 Smart Student Success Analytics</h1>
        <p>
        A Comprehensive Data Wrangling and Learning Behavior
        Analysis System
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📌 Project Overview</div>',
        unsafe_allow_html=True
    )

    st.write("""
    This project combines all ten Data Wrangling experiments into
    one complete student analytics system.

    The system processes student academic performance, attendance,
    study habits, online learning, library visits, practice tests,
    sleep hours and learning preferences.
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👨‍🎓 Students", len(final_data))

    with col2:
        st.metric("📊 Features", len(final_data.columns))

    with col3:
        st.metric("🧪 Experiments", 10)

    with col4:
        st.metric("📁 Datasets", 4)

    st.markdown(
        '<div class="section-title">🧪 Experiments Included</div>',
        unsafe_allow_html=True
    )

    experiments = [
        "1️⃣ Read and display CSV data",
        "2️⃣ Dataset exploration",
        "3️⃣ Missing value handling",
        "4️⃣ Duplicate and inconsistent record cleaning",
        "5️⃣ Datatype conversion and formatting",
        "6️⃣ Merge, join and concatenate",
        "7️⃣ Normalization and standardization",
        "8️⃣ Label encoding and one-hot encoding",
        "9️⃣ Data binning and transformation",
        "🔟 Web scraping using Requests and BeautifulSoup"
    ]

    for exp in experiments:
        st.write("✅", exp)


# =========================================================
# STUDENT PROFILE
# =========================================================

elif page == "👤 Student Profile":

    st.markdown(
        '<div class="section-title">👤 Individual Student Analysis</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Select one particular Student ID below and click "
        "'Analyze Student' to view their complete analysis."
    )

    student_ids = sorted(
        final_data["student_id"].dropna().unique()
    )

    selected_id = st.selectbox(
        "🎓 Select Student ID",
        student_ids
    )

    analyze = st.button(
        "🔍 Analyze Student",
        type="primary",
        use_container_width=True
    )

    if analyze:

        student = final_data[
            final_data["student_id"] == selected_id
        ]

        if student.empty:

            st.error("Student ID not found.")

        else:

            student = student.iloc[0]

            st.success(
                f"Analysis generated successfully for {selected_id}"
            )

            st.markdown(
                f"""
                <div class="hero">
                    <h1>🎓 {student['name']}</h1>
                    <p>Student ID: {student['student_id']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # =================================================
            # PERSONAL INFORMATION
            # =================================================

            st.markdown(
                '<div class="section-title">👤 Personal Information</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Student ID", student["student_id"])

            with col2:
                st.metric("Age", student["age"])

            with col3:
                st.metric("Gender", student["gender"])

            with col4:
                st.metric("Year", student["year"])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Branch", student["branch"])

            with col2:
                st.metric("City", student["city"])

            with col3:
                st.metric(
                    "Preferred Resource",
                    student["preferred_resource"]
                )

            # =================================================
            # ACADEMIC PERFORMANCE
            # =================================================

            st.markdown(
                '<div class="section-title">📚 Academic Performance</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Attendance",
                    f"{student['attendance']:.1f}%"
                )

            with col2:
                st.metric(
                    "Assignment Score",
                    f"{student['assignment_score']:.1f}"
                )

            with col3:
                st.metric(
                    "Internal Marks",
                    f"{student['internal_marks']:.1f}"
                )

            with col4:
                st.metric(
                    "External Marks",
                    f"{student['external_marks']:.1f}"
                )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Marks",
                    f"{student['total_marks']:.1f}"
                )

            with col2:
                st.metric(
                    "Average Score",
                    f"{student['average_score']:.2f}"
                )

            with col3:
                st.metric(
                    "Performance",
                    str(student["performance_category"])
                )

            # =================================================
            # LEARNING BEHAVIOR
            # =================================================

            st.markdown(
                '<div class="section-title">📖 Learning Behavior</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Study Hours",
                    f"{student['study_hours']:.1f}"
                )

            with col2:
                st.metric(
                    "Online Hours",
                    f"{student['online_hours']:.1f}"
                )

            with col3:
                st.metric(
                    "Library Visits",
                    f"{student['library_visits']:.0f}"
                )

            with col4:
                st.metric(
                    "Practice Tests",
                    f"{student['practice_tests']:.0f}"
                )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Sleep Hours",
                    f"{student['sleep_hours']:.1f}"
                )

            with col2:
                st.metric(
                    "Study Level",
                    str(student["study_level"])
                )

            with col3:
                st.metric(
                    "Attendance Category",
                    str(student["attendance_category"])
                )

            # =================================================
            # TEST INFORMATION
            # =================================================

            st.markdown(
                '<div class="section-title">📝 Test & Activity Information</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                test_score = student["test_score"]

                if pd.isna(test_score):
                    st.metric("Test Score", "Not Available")
                else:
                    st.metric(
                        "Test Score",
                        f"{test_score:.1f}"
                    )

            with col2:
                st.metric(
                    "Study Mode",
                    student["study_mode"]
                )

            with col3:
                st.metric(
                    "Remarks",
                    student["remarks"]
                )

            # =================================================
            # SCORE BREAKDOWN
            # =================================================

            st.markdown(
                '<div class="section-title">📊 Academic Score Breakdown</div>',
                unsafe_allow_html=True
            )

            score_data = pd.DataFrame({
                "Category": [
                    "Assignment",
                    "Internal",
                    "External"
                ],
                "Score": [
                    student["assignment_score"],
                    student["internal_marks"],
                    student["external_marks"]
                ]
            })

            st.bar_chart(
                score_data.set_index("Category")
            )

            # =================================================
            # INDIVIDUAL ANALYSIS
            # =================================================

            st.markdown(
                '<div class="section-title">🧠 Student Analysis</div>',
                unsafe_allow_html=True
            )

            average = student["average_score"]
            attendance = student["attendance"]
            study_hours = student["study_hours"]
            practice_tests = student["practice_tests"]

            st.subheader("💪 Strengths")

            strengths = []

            if average >= 85:
                strengths.append(
                    "Excellent overall academic performance"
                )

            elif average >= 70:
                strengths.append(
                    "Good academic performance"
                )

            if attendance >= 75:
                strengths.append(
                    "Good attendance"
                )

            if study_hours >= 5:
                strengths.append(
                    "Strong study habit"
                )

            if practice_tests >= 5:
                strengths.append(
                    "Good practice test participation"
                )

            if len(strengths) == 0:
                strengths.append(
                    "Student has opportunities to develop stronger academic habits"
                )

            for strength in strengths:
                st.write("✅", strength)

            st.subheader("⚠️ Areas Needing Improvement")

            weaknesses = []

            if average < 60:
                weaknesses.append(
                    "Overall academic performance needs improvement"
                )

            if attendance < 60:
                weaknesses.append(
                    "Attendance is below the recommended level"
                )

            if study_hours < 3:
                weaknesses.append(
                    "Study hours are relatively low"
                )

            if practice_tests < 3:
                weaknesses.append(
                    "More practice tests are recommended"
                )

            if len(weaknesses) == 0:
                weaknesses.append(
                    "No major weakness detected from the analyzed metrics"
                )

            for weakness in weaknesses:
                st.write("⚠️", weakness)

            st.subheader("💡 Personalized Recommendations")

            recommendations = []

            if attendance < 75:
                recommendations.append(
                    "Improve class attendance and maintain at least 75% attendance."
                )

            if study_hours < 5:
                recommendations.append(
                    "Increase daily study time gradually."
                )

            if practice_tests < 5:
                recommendations.append(
                    "Attempt more practice tests to improve exam readiness."
                )

            if average < 60:
                recommendations.append(
                    "Focus on weak subjects and revise fundamentals regularly."
                )

            if average >= 85 and attendance >= 75:
                recommendations.append(
                    "Maintain the current study strategy and continue consistent practice."
                )

            for recommendation in recommendations:
                st.write("💡", recommendation)


# =========================================================
# EXPERIMENT 1
# =========================================================

elif page == "📂 Experiment 1 - Read CSV":

    st.title("📂 Experiment 1 - Read and Display CSV")

    st.subheader("📋 First 5 Records")

    st.dataframe(
        students.head(),
        use_container_width=True
    )

    st.subheader("📋 Last 5 Records")

    st.dataframe(
        students.tail(),
        use_container_width=True
    )

    st.success(
        "CSV data was successfully read and displayed using Pandas."
    )


# =========================================================
# EXPERIMENT 2
# =========================================================

elif page == "🔍 Experiment 2 - Data Exploration":

    st.title("🔍 Experiment 2 - Dataset Exploration")

    st.subheader("📐 Dataset Shape")

    st.write(students.shape)

    st.subheader("📊 Statistical Description")

    st.dataframe(
        students.describe(include="all"),
        use_container_width=True
    )

    st.subheader("🔤 Data Types")

    st.dataframe(
        pd.DataFrame(
            students.dtypes,
            columns=["Data Type"]
        ),
        use_container_width=True
    )

    st.success(
        "Dataset structure, statistics and datatypes were explored."
    )


# =========================================================
# EXPERIMENT 3
# =========================================================

elif page == "🩹 Experiment 3 - Missing Values":

    st.title("🩹 Experiment 3 - Missing Value Handling")

    st.subheader("Missing Values")

    st.dataframe(
        students.isnull().sum().to_frame("Missing Values"),
        use_container_width=True
    )

    cleaned = students.copy()

    cleaned["gender"] = cleaned["gender"].fillna("Unknown")
    cleaned["city"] = cleaned["city"].fillna("Unknown")

    st.subheader("After Handling Missing Values")

    st.dataframe(
        cleaned.isnull().sum().to_frame("Missing Values"),
        use_container_width=True
    )

    st.success("Missing values were successfully handled.")


# =========================================================
# EXPERIMENT 4
# =========================================================

elif page == "🧹 Experiment 4 - Duplicates":

    st.title("🧹 Experiment 4 - Duplicate & Inconsistent Records")

    duplicate_count = students.duplicated().sum()

    st.metric(
        "🔁 Duplicate Records",
        duplicate_count
    )

    st.subheader("Duplicate Records")

    st.dataframe(
        students[students.duplicated()],
        use_container_width=True
    )

    cleaned = students.drop_duplicates()

    st.metric(
        "📊 Records After Cleaning",
        len(cleaned)
    )

    st.success(
        "Duplicates and inconsistent text formatting were cleaned."
    )


# =========================================================
# EXPERIMENT 5
# =========================================================

elif page == "🔄 Experiment 5 - Datatype Conversion":

    st.title("🔄 Experiment 5 - Datatype Conversion & Formatting")

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
        .str.strip()
        .str.title()
    )

    converted["remarks"] = (
        converted["remarks"]
        .str.strip()
        .str.title()
    )

    st.subheader("Converted Dataset")

    st.dataframe(
        converted.head(10),
        use_container_width=True
    )

    st.subheader("New Data Types")

    st.dataframe(
        converted.dtypes.to_frame("Data Type"),
        use_container_width=True
    )

    st.success(
        "Datatype conversion and text formatting completed."
    )


# =========================================================
# EXPERIMENT 6
# =========================================================

elif page == "🔗 Experiment 6 - Merge & Concatenate":

    st.title("🔗 Experiment 6 - Merge, Join & Concatenate")

    students_clean = students.drop_duplicates()
    academic_clean = academic.drop_duplicates()
    learning_clean = learning.drop_duplicates()

    merged = pd.merge(
        students_clean,
        academic_clean,
        on="student_id",
        how="inner"
    )

    merged = pd.merge(
        merged,
        learning_clean,
        on="student_id",
        how="inner"
    )

    concatenated = pd.concat(
        [students_clean, academic_clean],
        axis=0,
        ignore_index=True
    )

    st.subheader("🔗 Merged Dataset")

    st.write("Shape:", merged.shape)

    st.dataframe(
        merged.head(),
        use_container_width=True
    )

    st.subheader("📎 Concatenated Dataset")

    st.write("Shape:", concatenated.shape)

    st.dataframe(
        concatenated.head(),
        use_container_width=True
    )

    st.success(
        "Datasets were successfully merged and concatenated."
    )


# =========================================================
# EXPERIMENT 7
# =========================================================

elif page == "📏 Experiment 7 - Scaling":

    st.title("📏 Experiment 7 - Normalization & Standardization")

    features = [
        "attendance",
        "assignment_score",
        "internal_marks",
        "external_marks",
        "study_hours"
    ]

    scaling_data = final_data[features].copy()

    for column in features:

        scaling_data[column] = pd.to_numeric(
            scaling_data[column],
            errors="coerce"
        )

        scaling_data[column] = scaling_data[column].fillna(
            scaling_data[column].median()
        )

    from sklearn.preprocessing import MinMaxScaler, StandardScaler

    minmax = MinMaxScaler()

    normalized = pd.DataFrame(
        minmax.fit_transform(scaling_data),
        columns=features
    )

    standard = StandardScaler()

    standardized = pd.DataFrame(
        standard.fit_transform(scaling_data),
        columns=features
    )

    st.subheader("📊 Min-Max Normalized Data")

    st.dataframe(
        normalized.head(),
        use_container_width=True
    )

    st.subheader("📊 Standardized Data")

    st.dataframe(
        standardized.head(),
        use_container_width=True
    )

    st.success(
        "Numerical features were normalized and standardized."
    )


# =========================================================
# EXPERIMENT 8
# =========================================================

elif page == "🔤 Experiment 8 - Encoding":

    st.title("🔤 Experiment 8 - Label Encoding & One-Hot Encoding")

    from sklearn.preprocessing import LabelEncoder

    encoding_data = final_data.copy()

    encoder = LabelEncoder()

    encoding_data["gender_encoded"] = encoder.fit_transform(
        encoding_data["gender"].fillna("Unknown")
    )

    st.subheader("🏷️ Label Encoding")

    st.dataframe(
        encoding_data[
            ["gender", "gender_encoded"]
        ].head(10),
        use_container_width=True
    )

    one_hot = pd.get_dummies(
        encoding_data,
        columns=[
            "branch",
            "preferred_resource",
            "study_mode"
        ],
        dtype=int
    )

    st.subheader("🔤 One-Hot Encoded Data")

    st.dataframe(
        one_hot.head(),
        use_container_width=True
    )

    st.metric(
        "Encoded Dataset Columns",
        one_hot.shape[1]
    )

    st.success(
        "Categorical variables were successfully encoded."
    )


# =========================================================
# EXPERIMENT 9
# =========================================================

elif page == "📦 Experiment 9 - Binning":

    st.title(
        "📦 Experiment 9 - Binning, Transformation & Discretization"
    )

    bin_data = final_data.copy()

    bin_data["attendance_category"] = pd.cut(
        bin_data["attendance"],
        bins=[0, 60, 75, 90, 100],
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
        bins=[-1, 2, 5, 8, 20],
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

    st.subheader("📊 Binned Data")

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
        ].head(10),
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Attendance Categories")

        st.bar_chart(
            bin_data["attendance_category"].value_counts()
        )

    with col2:

        st.subheader("Study Level")

        st.bar_chart(
            bin_data["study_level"].value_counts()
        )

    st.success(
        "Binning, transformation and discretization completed."
    )


# =========================================================
# EXPERIMENT 10 - WEB SCRAPING
# =========================================================

elif page == "🌐 Experiment 10 - Web Scraping":

    st.title("🌐 Experiment 10 - Web Scraping")

    st.write("""
    This experiment demonstrates web scraping using
    Requests and BeautifulSoup.

    The program extracts a table from the W3Schools HTML Tables
    webpage and displays the scraped data.
    """)

    st.subheader("🌐 Scraped Website")

    url = "https://www.w3schools.com/html/html_tables.asp"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        st.write(
            "Status Code:",
            response.status_code
        )

        if response.status_code == 200:

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            table = soup.find("table")

            if table is None:

                st.error("No table found on the webpage.")

            else:

                headers_list = []

                for th in table.find_all("th"):
                    headers_list.append(
                        th.text.strip()
                    )

                rows = []

                for tr in table.find_all("tr")[1:]:

                    cells = tr.find_all("td")

                    row = [
                        cell.text.strip()
                        for cell in cells
                    ]

                    if row:
                        rows.append(row)

                scraped_data = pd.DataFrame(
                    rows,
                    columns=headers_list
                )

                st.subheader("📋 Extracted Table")

                st.dataframe(
                    scraped_data,
                    use_container_width=True
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Rows Extracted",
                        scraped_data.shape[0]
                    )

                with col2:
                    st.metric(
                        "Columns Extracted",
                        scraped_data.shape[1]
                    )

                csv_data = scraped_data.to_csv(
                    index=False
                )

                st.download_button(
                    label="⬇️ Download Scraped Data",
                    data=csv_data,
                    file_name="web_scraped_data.csv",
                    mime="text/csv",
                    use_container_width=True
                )

                st.success(
                    "Web scraping completed successfully."
                )

        else:

            st.error(
                f"Failed to access webpage. Status code: {response.status_code}"
            )

    except requests.exceptions.RequestException as e:

        st.error(
            f"Error while accessing webpage: {e}"
        )


# =========================================================
# OVERALL ANALYTICS
# =========================================================

elif page == "📊 Overall Analytics":

    st.title("📊 Overall Student Analytics")

    st.info(
        "This section analyzes the complete dataset of all students."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👨‍🎓 Total Students",
            len(final_data)
        )

    with col2:
        st.metric(
            "📈 Average Score",
            f"{final_data['average_score'].mean():.2f}"
        )

    with col3:
        st.metric(
            "🕒 Average Attendance",
            f"{final_data['attendance'].mean():.2f}%"
        )

    with col4:
        st.metric(
            "📖 Average Study Hours",
            f"{final_data['study_hours'].mean():.2f}"
        )

    st.subheader("🏫 Branch-wise Average Performance")

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

    st.bar_chart(branch_performance)

    st.subheader("📖 Study Hours vs Average Score")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(
        final_data["study_hours"],
        final_data["average_score"]
    )

    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Average Score")
    ax.set_title(
        "Study Hours vs Average Score"
    )

    st.pyplot(fig)

    st.subheader("🕒 Attendance vs Average Score")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(
        final_data["attendance"],
        final_data["average_score"]
    )

    ax.set_xlabel("Attendance (%)")
    ax.set_ylabel("Average Score")
    ax.set_title(
        "Attendance vs Average Score"
    )

    st.pyplot(fig)


# =========================================================
# STUDENT INSIGHTS
# =========================================================

elif page == "🏆 Student Insights":

    st.title("🏆 Student Insights")

    st.subheader("🥇 Top 10 Students")

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
        use_container_width=True
    )

    st.subheader("⚠️ Students Needing Improvement")

    at_risk_students = final_data[
        (final_data["average_score"] < 60) |
        (final_data["attendance"] < 60)
    ]

    st.metric(
        "Students Needing Improvement",
        len(at_risk_students)
    )

    st.dataframe(
        at_risk_students[
            [
                "student_id",
                "name",
                "branch",
                "attendance",
                "average_score",
                "performance_category"
            ]
        ],
        use_container_width=True
    )

    st.subheader("📊 Performance Category Distribution")

    st.bar_chart(
        final_data[
            "performance_category"
        ].value_counts()
    )

    st.subheader("🏫 Branch Performance")

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
        branch_performance.to_frame(
            "Average Score"
        ),
        use_container_width=True
    )

    st.success(
        "Overall student insights generated successfully."
    )