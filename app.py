import streamlit as st
import openai
import os
import json
import textstat
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


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