from openai import OpenAI
import json 
from quentions_generation import generate_enhanced_questions, extract_json
from research_agent import scrape_and_save, edit_answers
from summary_agent import summary_blog


api_key = "DeepSeek_API_KEY"
research_api_key = "serpapi_API_KEY"
question = "How does regular exercise impact mental health"
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

#step1
questions = generate_enhanced_questions(api_key, question,client)
print("generated questions")
print(questions)

#step2
output = []
for _, enhanced_question in questions.items():
    result = scrape_and_save(enhanced_question, research_api_key)
    output.append(result)
print("research results")
print(output)

enhanced_answers = edit_answers(output, client)
print("cleared research results)
print(enhanced_answers)

# step3
summary = summary_blog(client,enhanced_answers)
print("Summary Blog Post:")
print(summary)

with open("output\final_report.md", 'w', encoding='utf-8') as file:
        file.write(summary)
