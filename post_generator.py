from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load progress.json
with open("progress.json", "r", encoding="utf-8") as file:
    progress_data = json.load(file)

# Find first unposted entry
unposted_entry = None
for entry in progress_data:
    if not entry.get("posted", False):
        unposted_entry = entry
        break

if unposted_entry is None:
    print("All posts are already marked as posted.")
    exit()

# Format questions
questions_formatted = ""
for i, question in enumerate(unposted_entry["questions"]):
    questions_formatted += f"✅ Problem {i+1}: {question}\n"

# Create prompt
prompt = f"""
You are helping a developer write a LinkedIn post for Day {unposted_entry['day']} of #100DaysOfDSAChallenge.

- Start with: Day {unposted_entry['day']} of 100 | #100DaysOfDSAChallenge
- Topic: {unposted_entry['topic']}
- Problems Solved:
{questions_formatted}
- Based on these learnings: {unposted_entry['learnings']}

Write 2 bullet points starting with ~ to summarize key learnings.

Add 8–10 relevant hashtags including #100DaysOfDSAChallenge, #DSA, #Java, #ProblemSolving, #CodingChallenge.
"""

# Call GPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=400
)

# Extract post content
post_content = response['choices'][0]['message']['content']

# Print to console
print("\n📢 Generated LinkedIn Post:\n")
print(post_content)

# Save to desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, f"day-{unposted_entry['day']}-post.txt")

with open(output_file, "w", encoding="utf-8") as file:
    file.write(post_content)

print(f"\n✅ Post saved to: {output_file}")
