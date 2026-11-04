import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('APIVN_BASE_URL', 'https://apivn.vn/v1').rstrip('/') + '/chat/completions'
key = os.getenv('APIVN_API_KEY')
model = os.getenv('APIVN_MODEL', 'claude-sonnet-5-5')

headers = {'Authorization': 'Bearer ' + str(key), 'Content-Type': 'application/json'}

prompt_file = os.path.join(os.path.dirname(__file__), 'prompt.md')
with open(prompt_file, 'r', encoding='utf-8') as f:
    prompt_content = f.read()

payload = {
    'model': model,
    'messages': [
        {'role': 'system', 'content': 'Bạn là chuyên gia giải toán THCS hàng đầu, luôn trả về JSON hợp lệ chính xác 100%.'},
        {'role': 'user', 'content': prompt_content}
    ],
    'max_tokens': 3500,
    'temperature': 0.1
}

print(f"Calling API using model {model}...")
response = requests.post(url, headers=headers, json=payload, timeout=90)
raw = response.json()['choices'][0]['message']['content'].strip()

if raw.startswith('```json'): raw = raw[7:]
if raw.startswith('```'): raw = raw[3:]
if raw.endswith('```'): raw = raw[:-3]
raw = raw.strip()

out_json = os.path.join(os.path.dirname(__file__), 'so_do_tu_duy_nguoc.json')
with open(out_json, 'w', encoding='utf-8') as f:
    f.write(raw)

print(f"Saved: {out_json}")
