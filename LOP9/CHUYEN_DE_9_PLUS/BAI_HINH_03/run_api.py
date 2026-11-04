import os
import sys
import json
import requests
from dotenv import load_dotenv

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Load .env từ thư mục gốc
root_env = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
if os.path.exists(root_env):
    load_dotenv(root_env)
else:
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
        {'role': 'system', 'content': 'Bạn là chuyên gia giải toán THCS và luyện thi 9+ vào 10 hàng đầu. Luôn trả về DUY NHẤT một chuỗi JSON hợp lệ 100%, không kèm bất kỳ lời giải thích ngoài nào.'},
        {'role': 'user', 'content': prompt_content}
    ],
    'max_tokens': 4000,
    'temperature': 0.1
}

print(f"Calling API for BAI_HINH_03 using model {model}...")
response = requests.post(url, headers=headers, json=payload, timeout=120)

if response.status_code != 200:
    print(f"Error {response.status_code}: {response.text}")
    sys.exit(1)

res_json = response.json()
raw = res_json['choices'][0]['message']['content'].strip()

if raw.startswith('```json'): raw = raw[7:]
if raw.startswith('```'): raw = raw[3:]
if raw.endswith('```'): raw = raw[:-3]
raw = raw.strip()

out_json = os.path.join(os.path.dirname(__file__), 'so_do_tu_duy_nguoc.json')
with open(out_json, 'w', encoding='utf-8') as f:
    f.write(raw)

print(f"Saved: {out_json}")

# Kiểm tra cú pháp JSON
try:
    with open(out_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("JSON validation SUCCESSFUL!")
    print(f"- Ma bai: {data.get('bai_toan', {}).get('ma_bai')}")
    print(f"- Mo hinh: {data.get('bai_toan', {}).get('mo_hinh')}")
    print(f"- So tang tu duy nguoc: {len(data.get('so_do_tu_duy_nguoc', []))}")
except Exception as e:
    print(f"JSON Parse Warning/Error: {e}")
