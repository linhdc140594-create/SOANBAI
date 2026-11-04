import os
import sys
import json
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
url = os.getenv('APIVN_BASE_URL', 'https://apivn.vn/v1').rstrip('/') + '/chat/completions'
key = os.getenv('APIVN_API_KEY')
model = os.getenv('APIVN_MODEL', 'claude-sonnet-5-5')

headers = {'Authorization': 'Bearer ' + str(key), 'Content-Type': 'application/json'}

def process_problem(idx):
    folder_name = f"BAI_HINH_{idx:02d}"
    folder_path = os.path.join(BASE_DIR, folder_name)
    prompt_file = os.path.join(folder_path, "prompt.md")
    out_json = os.path.join(folder_path, "so_do_tu_duy_nguoc.json")

    if not os.path.exists(prompt_file):
        print(f"[{folder_name}] Prompt not found, skipping.")
        return False

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

    print(f"[{folder_name}] Calling API...")
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=90)
        raw = response.json()['choices'][0]['message']['content'].strip()

        if raw.startswith('```json'): raw = raw[7:]
        if raw.startswith('```'): raw = raw[3:]
        if raw.endswith('```'): raw = raw[:-3]
        raw = raw.strip()

        # verify json
        json.loads(raw)

        with open(out_json, 'w', encoding='utf-8') as f:
            f.write(raw)

        print(f"[{folder_name}] SUCCESS -> Saved to {out_json}")
        return True
    except Exception as e:
        print(f"[{folder_name}] ERROR: {e}")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Batch run API for geometry problems")
    parser.add_argument('--start', type=int, default=1, help="Start problem index (1-55)")
    parser.add_argument('--end', type=int, default=55, help="End problem index (1-55)")
    args = parser.parse_args()

    print(f"Batch running from BAI_HINH_{args.start:02d} to BAI_HINH_{args.end:02d}...")
    success_count = 0
    for i in range(args.start, args.end + 1):
        if process_problem(i):
            success_count += 1

    print(f"\nDone! Completed {success_count}/{args.end - args.start + 1} problems.")

