# GapSense_Project
# 📊 GapSense

**GapSense** is an AI-powered Learning Gap Analyzer built using **Python** and **Streamlit**. It evaluates a student’s quiz performance, identifies topic-wise learning gaps, and provides clear, explainable, and personalized study recommendations.

This project is designed to be **simple, transparent, and beginner-friendly**, making it ideal for academic projects, mini-projects, and AI/ML demonstrations.

---

## 🚀 Features

* 📝 Interactive quiz-based assessment
* 📊 Topic-wise performance analysis
* 🎯 Automatic classification:

  * Weak
  * Average
  * Strong
* 📈 Visual performance dashboard (bar chart)
* 💡 Personalized learning recommendations
* 🔍 Explainable AI logic (rule-based, transparent)

---

## 🧠 Topics Covered in Quiz

* Algebra
* Trigonometry
* Geometry
* Probability

Each topic contains multiple questions to accurately evaluate understanding.

---

## 🛠️ Tech Stack

* **Frontend & UI**: Streamlit
* **Backend Logic**: Python
* **Data Handling**: Pandas
* **Visualization**: Streamlit / Plotly (optional for colored charts)

---

## 📂 Project Structure

```
GapSense/
│
├── app.py          # Main Streamlit application
├── README.md       # Project documentation
└── requirements.txt (optional)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites

Make sure you have:

* Python 3.8 or above
* pip installed

### 2️⃣ Install Required Libraries

```bash
pip install streamlit pandas plotly
```

---

## ▶️ How to Run the Project

1. Open terminal / command prompt
2. Navigate to the project folder
3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the browser link shown in the terminal (usually `http://localhost:8501`)

---

## 📈 How GapSense Works (AI Logic)

1. Student answers quiz questions
2. System calculates **topic-wise accuracy**
3. Performance levels are assigned:

   * **< 40%** → Weak
   * **40% – 70%** → Average
   * **> 70%** → Strong
4. Personalized recommendations are generated for each topic

> 🔍 This is a form of **Explainable AI**, as decisions are made using clear and understandable rules.

---

## 🎯 Sample Output

* Topic-wise score table
* Performance bar chart
* Text-based personalized recommendations

---

## 📌 Use Cases

* Student self-assessment
* Academic mini-project / final-year project
* AI & data analytics demonstrations
* Learning analytics systems

---

## 🔮 Future Enhancements

* Difficulty-level analysis (Easy / Medium / Hard)
* Overall performance score
* User login & result history
* PDF report generation
* Integration with ML models
* Deployment on Streamlit Cloud

---

## 👨‍🎓 Target Audience

* Students
* Beginners in AI & Python
* Educators
* Academic evaluators

---

## 📄 License

This project is for **educational purposes**. You are free to modify and extend it for learning and academic use.

---

## 🙌 Acknowledgment

Built as part of an academic AI-based learning analytics project to demonstrate how technology can support personalized education.

---

✨ *Happy Learning with GapSense!*
