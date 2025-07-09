import streamlit as st
import os
import json
import textstat
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("LLM_API_KEY")
API_URL = os.getenv("LLM_API_URL")


# Role-specific interview questions
role_questions = {
    "Software Engineer": [
        "Tell me about a project you're proud of.",
        "What's your favorite programming language and why?",
        "How do you handle debugging in your code?",
        "Describe a time you had to learn a new technology quickly.",
    ],
    "Data Scientist": [
        "Can you explain the difference between supervised and unsupervised learning?",
        "What's your favorite machine learning algorithm and why?",
        "How do you handle data cleaning and preprocessing?",
        "Describe a project where you used data visualization to communicate insights.",
    ],
    "Product Manager": [
        "How do you prioritize features in a product roadmap?",
        "What's your favorite product management tool and why?",
        "How do you handle stakeholder feedback and prioritization?",
        "Describe a time you had to make a tough decision in a product roadmap.",
    ],
    "UX Designer": [
        "How do you conduct user research and usability testing?",
        "What's your favorite UX design tool and why?",
        "How do you balance aesthetics and usability in your designs?",
        "Describe a time you had to make a design decision that balanced aesthetics and usability.",
    ]
}

#Streamlit app layout
st.set_page_config(page_title="AI Interview Coach", page_icon="🎤")
st.title("🎤 AI-Powered Interview Coach")
st.markdown("Simulate job interviews and receive feedback powered by your preferred AI API.")

#Role + question selection
selected_role = st.selectbox("💼 Choose a Job Role", list(role_questions.keys()))
question = st.selectbox("🧠 Select an Interview Question", role_questions[selected_role])
user_answer = st.text_area("✍️ Enter Your Answer Below", height=200)


# Evaluate function (abstracted for any model)
def evaluate_answer_generic(prompt_text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4",  # Change model as per your vendor
        "messages": [{"role": "user", "content": prompt_text}],
        "temperature": 0.5
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Prompt template
def generate_prompt(question, answer):
    return f"""
You are an expert interview coach. Analyze the following answer to an interview question.

Question: "{question}"
Answer: "{answer}"

Rate the answer on:
1. Relevance to the question (0-10)
2. Confidence and clarity (0-10)
3. Grammar and language quality (0-10)

Then, give a short constructive feedback summary.
Respond in JSON format:
{{
  "relevance": <score>,
  "confidence": <score>,
  "grammar": <score>,
  "feedback": "<summary>"
}}
"""

# Button logic
if st.button("🚀 Evaluate Answer"):
    if not user_answer.strip():
        st.warning("Please provide your answer.")
    else:
        with st.spinner("Evaluating your response..."):
            try:
                prompt = generate_prompt(question, user_answer)
                result = evaluate_answer_generic(prompt)
                data = json.loads(result)

                st.success("✅ Feedback Summary")
                st.markdown(f"""
- **Relevance:** {data['relevance']} / 10  
- **Confidence:** {data['confidence']} / 10  
- **Grammar:** {data['grammar']} / 10  
- **📝 Feedback:** _{data['feedback']}_  
""")

                readability = textstat.flesch_reading_ease(user_answer)
                st.info(f"📚 Readability Score: {round(readability, 2)} / 100")

            except Exception as e:
                st.error("An error occurred during evaluation.")
                st.exception(e)
