import streamlit as st
import pandas as pd

# -----------------------------
# Project Title
# -----------------------------
st.set_page_config(page_title="GapSense", layout="centered")

st.title("📊 GapSense")
st.subheader("AI-powered Learning Gap Analyzer for Students")

st.write(
    "This system analyzes your quiz performance to identify learning gaps "
    "and provides personalized study recommendations."
)

# -----------------------------
# Question Bank
# -----------------------------
questions = [
    # Algebra
    {"q": "What is the value of x if 2x + 4 = 10?", "options": ["2", "3", "4", "5"], "answer": "3", "topic": "Algebra"},
    {"q": "Simplify: 5x - 2x", "options": ["7x", "3x", "2x", "x"], "answer": "3x", "topic": "Algebra"},
    {"q": "What is x² when x = 4?", "options": ["8", "12", "16", "20"], "answer": "16", "topic": "Algebra"},

    # Trigonometry
    {"q": "sin 90° =", "options": ["0", "1", "-1", "0.5"], "answer": "1", "topic": "Trigonometry"},
    {"q": "cos 0° =", "options": ["0", "1", "-1", "0.5"], "answer": "1", "topic": "Trigonometry"},
    {"q": "tan 45° =", "options": ["0", "1", "-1", "√3"], "answer": "1", "topic": "Trigonometry"},

    # Geometry
    {"q": "Sum of angles of a triangle?", "options": ["90°", "180°", "270°", "360°"], "answer": "180°", "topic": "Geometry"},
    {"q": "A square has how many sides?", "options": ["3", "4", "5", "6"], "answer": "4", "topic": "Geometry"},
    {"q": "Area of square = ?", "options": ["a²", "2a", "4a", "a³"], "answer": "a²", "topic": "Geometry"},

    # Probability
    {"q": "Probability value lies between?", "options": ["0 and 1", "1 and 2", "-1 and 1", "0 and 100"], "answer": "0 and 1", "topic": "Probability"},
    {"q": "Probability of a sure event?", "options": ["0", "0.5", "1", "-1"], "answer": "1", "topic": "Probability"},
    {"q": "Probability of impossible event?", "options": ["0", "1", "0.5", "-1"], "answer": "0", "topic": "Probability"},
]

# -----------------------------
# Quiz Section
# -----------------------------
st.header("📝 Student Assessment")

user_answers = {}
for i, q in enumerate(questions):
    user_answers[i] = st.radio(q["q"], q["options"], index=None, key=f"q_{i}")

  

# -----------------------------
# Submit Button
# -----------------------------
if st.button("🔍 Analyze My Learning Gaps"):
    topic_scores = {}

    for i, q in enumerate(questions):
        topic = q["topic"]
        if topic not in topic_scores:
            topic_scores[topic] = {"correct": 0, "total": 0}

        topic_scores[topic]["total"] += 1
        if user_answers[i] == q["answer"]:
            topic_scores[topic]["correct"] += 1

    # -----------------------------
    # AI Logic: Gap Analysis
    # -----------------------------
    results = []
    recommendations = []

    for topic, data in topic_scores.items():
        score = (data["correct"] / data["total"]) * 100

        if score < 40:
            level = "Weak"
            rec = "Revise basics and practice daily."
        elif score <= 70:
            level = "Average"
            rec = "Practice more problems to strengthen understanding."
        else:
            level = "Strong"
            rec = "You can move to advanced concepts."

        results.append([topic, f"{score:.0f}%", level])
        recommendations.append(f"📌 **{topic}**: {rec}")

    # -----------------------------
    # Results Dashboard
    # -----------------------------
    st.header("📈 Learning Gap Analysis Result")

    df = pd.DataFrame(results, columns=["Topic", "Score", "Performance Level"])
    st.table(df)

    st.subheader("📊 Topic-wise Performance")
    st.bar_chart(
        {row[0]: int(row[1].replace("%", "")) for row in results}
    )

    st.subheader("🎯 Personalized Recommendations")
    for r in recommendations:
        st.write(r)

    st.info(
        "🔍 **Explainable AI Note:** This system uses topic-wise performance analysis "
        "and transparent rules to identify learning gaps."
    )
