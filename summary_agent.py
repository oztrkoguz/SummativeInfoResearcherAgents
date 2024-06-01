
def summary_blog(client,enhanced_questions):
    blog_text = ""
    for query_number, text in enhanced_questions.items():
        response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": f"Take the following answers one by one and turn them into a summary blog post: {text}"},
            {"role": "user", "content": ""},
        ],
        stream=False)
        blog_text += response.choices[0].message.content
    return blog_text
