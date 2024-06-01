from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup


def scrape_and_save(query, api_key):
    output = []
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    
    for result in results.get('organic_results', []):
        snippet = result.get('snippet', 'No snippet found')
        link = result.get('link', 'No link found')

        if link != 'No link found':
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraphs = soup.find_all('p')
                full_text = "\n".join([para.get_text() for para in paragraphs])
                output.append(full_text)
            else:
                print(f"Failed to retrieve the page: {link}")
    return output


def edit_answers(output, client):
    advanced_answers = {}
    for k in output:
        for i, text in enumerate(k):
            response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": f"Remove dates, addresses, and line breaks, then correct and rephrase the following text while retaining all specific words and names intact: {text}"},
                {"role": "user", "content": ""},
            ],
            stream=False)
            enhanced_answer = response.choices[0].message.content
            advanced_answers[f"Answers_{i+1}"] = enhanced_answer
    return advanced_answers




