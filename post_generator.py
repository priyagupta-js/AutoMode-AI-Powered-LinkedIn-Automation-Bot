import openai
import os 
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("Open_api_key")

# generate post
 
def generate_post(data):
    questions_format = ""
    for i,q in enumerate(data["questions"]):
        questions_format+=f"Problem{i+1}:{q}\n"

promt = f"""
You are helping a developer to write a LinkedIn post for Day{data['day']} of #100DaysOfDSAChallenge.
- Start with: Day {data ['day']} of 100 | #100DaysOfDSAChallenge.
- Topic : {data['topic']}
- Problem Solved : {question_foramt}
- Based on these learnings: {data['learning']}
Write 2 bullet points starting with ~ to summarize key learnings.

Add 8–10 relevant hashtags including #100DaysOfDSAChallenge, #DSA, #Java, #ProblemSolving, #CodingChallenge.
"""