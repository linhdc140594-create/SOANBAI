import os
import sys
import json
import urllib.request
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('APIVN_API_KEY')
base_url = os.getenv('APIVN_BASE_URL', 'https://apivn.vn/v1').rstrip('/')
model = 'claude-sonnet-5-5'

def call_api(prompt, system_prompt='You are an expert Math teacher and LaTeX exam author.'):
    url = f'{base_url}/chat/completions'
    payload = {
        'model': model,
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        'temperature': 0.2
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    })
    with urllib.request.urlopen(req, timeout=120) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        return res['choices'][0]['message']['content']

print('API test callable!')
