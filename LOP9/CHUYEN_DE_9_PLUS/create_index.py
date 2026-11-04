import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = 'd:/GitHub/SOANBAI-main'
TARGET_ROOT = os.path.join(ROOT_DIR, 'LOP9/CHUYEN_DE_9_PLUS')

rows = []
for i in range(1, 56):
    folder_name = f'BAI_HINH_{i:02d}'
    folder_path = os.path.join(TARGET_ROOT, folder_name)
    prompt_file = os.path.join(folder_path, 'prompt.md')
    de_bai_file = os.path.join(folder_path, 'de_bai.tex')
    
    first_line = ''
    if os.path.exists(de_bai_file):
        with open(de_bai_file, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines() if l.strip() and not l.strip().startswith('%') and not '\\begin{ex}' in l]
            if lines:
                first_line = lines[0][:80]
    
    status = '✅ Hoàn chỉnh PDF & JSON' if i in [1, 12] else '📝 Sẵn sàng Prompt & Script'
    rows.append((i, folder_name, first_line, status))

index_md = os.path.join(TARGET_ROOT, 'MUC_LUC_55_BAI_HINH.md')
with open(index_md, 'w', encoding='utf-8') as f:
    f.write('# 📚 MỤC LỤC 55 BÀI TOÁN HÌNH HỌC 9+ (CHUYÊN ĐỀ TƯ DUY NGƯỢC)\n\n')
    f.write('> **Tuyển tập 55 bài toán hình học phân hóa** được trích xuất từ bộ 55 Đề Thi Tuyển Sinh Vào Lớp 10.\n\n')
    f.write('Mỗi thư mục `BAI_HINH_01` -> `BAI_HINH_55` đều được tạo sẵn đầy đủ 3 tệp tin tiêu chuẩn:\n')
    f.write('1. `de_bai.tex`: Đề bài gốc và lời giải trích từ kho đề thi.\n')
    f.write('2. `prompt.md`: Bản prompt chuyên gia bồi dưỡng 9+ để gọi AI suy luận ngược & sinh sơ đồ cây thông.\n')
    f.write('3. `run_api.py`: Script tự động gọi API (Claude 3.5 Sonnet qua `apivn.vn`) để xuất kết quả JSON.\n\n')
    f.write('| STT | Thư Mục Bài Hình | Trích Yếu Đề Bài Toán | Trạng Thái |\n')
    f.write('| :---: | :--- | :--- | :---: |\n')
    for stt, name, excerpt, st in rows:
        target_link = f"file:///{TARGET_ROOT.replace(chr(92), '/')}/{name}"
        f.write(f"| {stt:02d} | [{name}]({target_link}) | {excerpt}... | {st} |\n")

print("SUCCESS: Created MUC_LUC_55_BAI_HINH.md")
print(f"Total rows: {len(rows)}")

