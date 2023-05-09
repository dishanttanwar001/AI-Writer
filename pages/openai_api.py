import requests
import openai

def generate_answer(prompt, api_key):
    openai.api_key="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"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        "prompt": prompt,
        "model": "text-davinci-002",
        "max_tokens":100,
        "stop":"."
    }

    resp = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate answer "+resp.text)

    return resp.json()['choices'][0]['text']



