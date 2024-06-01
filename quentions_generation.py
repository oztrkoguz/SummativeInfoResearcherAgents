import json 
import re


def extract_json(text):
    json_match = re.search(r'({.*})', text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            raise ValueError("Extracted text is not a valid JSON")
    else:
        raise ValueError("No JSON object found in the text")

def generate_enhanced_questions(api_key, question,client):  
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that outputs in JSON. For a given question, include the original question and provide 5 enhanced versions of that question. JSON fields should be {Question_i}: {that question}"},
            {"role": "user", "content": f"{question}"},
        ],
        stream=False
    )

    question_json = response.choices[0].message.content
    question_json = extract_json(question_json)
    return question_json


