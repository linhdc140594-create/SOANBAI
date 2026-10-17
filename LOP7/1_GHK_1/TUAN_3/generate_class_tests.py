import os, sys, json, urllib.request, subprocess, shutil

sys.stdout.reconfigure(encoding='utf-8')

SUPABASE_URL = "https://ulzcqypxfvexjpnxuxgo.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVsemNxeXB4ZnZleGpwbnh1eGdvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3ODU4ODU5OSwiZXhwIjoyMDk0MTY0NTk5fQ.qPPEHTYlwRp-2NuynRXbSbrmNvMTJoHQN5KI1LfYerc"
ANON_KEY = "sb_publishable_9co-50aMwmxNnE1Bd5Ou3Q_IuTdSZtD"

HEADERS = {
    'apikey': ANON_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}'
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEST_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "SAP_XEP_THEO_TUAN", "TUAN_3"))

CLASS_CONFIG = [
    {
        'id': '37634997-7636-4736-b1e6-ac7fa72b85e6',
        'raw_name': '2014 - TOÁN 7 - TÂY SƠN',
        'display_name': 'TOÁN 7 - TÂY SƠN',
        'short_class': 'TOÁN 7 TÂY SƠN',
        'folder_name': 'LOP_TOAN_7_TAY_SON',
        'file_suffix': 'TOAN_7_TAY_SON'
    },
    {
        'id': 'bc0972c2-70b1-44e0-81cd-69693f5b3d79',
        'raw_name': '2014 TOÁN 7 - KT',
        'display_name': 'TOÁN 7 - KIẾN THIẾT',
        'short_class': 'TOÁN 7 KIẾN THIẾT',
        'folder_name': 'LOP_TOAN_7_KT',
        'file_suffix': 'TOAN_7_KT'
    },
    {
        'id': 'a45caec4-ed52-4f59-a48e-4e649ee0a4d3',
        'raw_name': '2014 KÈM',
        'display_name': 'TOÁN 7 - KÈM RIÊNG',
        'short_class': 'TOÁN 7 KÈM RIÊNG',
        'folder_name': 'LOP_TOAN_7_KEM_RIENG',
        'file_suffix': 'TOAN_7_KEM_RIENG'
    }
]

FRONT_TARGET = r"\rule[-2.5mm]{0pt}{8mm}\textbf{Họ và tên học sinh:} \dotfill \quad \textbf{Mã HS:} \makebox[3.5cm]{\dotfill} \\"
BACK_TARGET = r"\rule[-2mm]{0pt}{7mm}\textbf{Họ và tên học sinh:} \dotfill \quad \textbf{Mã HS:} \makebox[3.5cm]{\dotfill} \\"

def vietnamese_sort_key(full_name):
    char_order = "aàảãáạăằẳẵắặâầẩẫấậbcdđeèẻẽéẹêềểễếệghiìỉĩíịklmnoòỏõóọôồổỗốộơờởỡớợpqrstuùủũúụưừửữứựvxyỳỷỹýỵ"
    order_dict = {c: i for i, c in enumerate(char_order)}
    parts = full_name.strip().split()
    first_name = parts[-1] if parts else ""
    key = []
    for char in (first_name + " " + full_name).lower():
        key.append(order_dict.get(char, ord(char)))
    return key

def fetch_students():
    url = f"{SUPABASE_URL}/rest/v1/enrollments?select=class_id,status,students(id,student_code,full_name,status)"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        enrollments = json.loads(resp.read().decode('utf-8'))

    result = {}
    for cfg in CLASS_CONFIG:
        cid = cfg['id']
        st_list = []
        for e in enrollments:
            if e.get('class_id') == cid and e.get('status') == 'active':
                st = e.get('students')
                if st and st.get('status') == 'active':
                    st_list.append({
                        'code': st.get('student_code', '').strip(),
                        'name': st.get('full_name', '').strip()
                    })
        st_list.sort(key=lambda s: vietnamese_sort_key(s['name']))
        result[cid] = st_list
    return result

def load_template_parts(buoi_num):
    tex_path = os.path.join(BASE_DIR, f"Phieu_Kiem_Tra_Tuan_03_Buoi_{buoi_num:02d}.tex")
    with open(tex_path, 'r', encoding='utf-8') as f:
        text = f.read()
    parts = text.split(r'\newpage')
    preamble, de101_p1 = parts[0].split(r'\pagestyle{empty}')
    preamble = preamble + r'\pagestyle{empty}'
    de101_p2 = parts[1]
    de102_p1 = parts[2]
    de102_p2 = parts[3]
    de103_p1 = parts[4]
    de103_p2 = parts[5]
    de104_p1 = parts[6]
    de104_p2 = parts[7].replace(r'\end{document}', '')
    
    de_dict = {
        101: (de101_p1, de101_p2),
        102: (de102_p1, de102_p2),
        103: (de103_p1, de103_p2),
        104: (de104_p1, de104_p2),
    }
    return preamble, de_dict

def personalize_page_front(page_text, name, code, short_class):
    new_line = (
        r"\rule[-2mm]{0pt}{7.5mm}\textbf{Họ và tên:} \textbf{\large " + name + r"} \hfill "
        r"\textbf{Mã HS:} \texttt{" + code + r"} \quad \\"
    )
    return page_text.replace(FRONT_TARGET, new_line)

def personalize_page_back(page_text, name, code, short_class):
    new_line = (
        r"\rule[-2mm]{0pt}{7mm}\textbf{Họ và tên:} \textbf{\large " + name + r"} \hfill "
        r"\textbf{Mã HS:} \texttt{" + code + r"} \quad \\"
    )
    return page_text.replace(BACK_TARGET, new_line)

def generate_for_class(cfg, students, b1_parts, b2_parts):
    folder_path = os.path.join(BASE_DIR, cfg['folder_name'])
    os.makedirs(folder_path, exist_ok=True)
    
    # Copy ex_test.sty
    shutil.copy2(os.path.join(BASE_DIR, 'ex_test.sty'), os.path.join(folder_path, 'ex_test.sty'))
    
    # Generate Roster Markdown
    test_codes = [101, 102, 103, 104]
    roster_md = f"# DANH SÁCH PHÁT PHIẾU KIỂM TRA - TUẦN 03\n\n"
    roster_md += f"**Lớp:** {cfg['display_name']} | **Sĩ số:** {len(students)} học sinh\n\n"
    roster_md += "| STT | Mã học sinh | Họ và tên học sinh | Mã đề kiểm tra | Ký nhận bài | Ghi chú |\n"
    roster_md += "| :---: | :---: | :--- | :---: | :---: | :---: |\n"
    for i, s in enumerate(students):
        made = test_codes[i % 4]
        roster_md += f"| {i+1:02d} | `{s['code']}` | **{s['name']}** | **Mã đề {made}** | | |\n"
    
    with open(os.path.join(folder_path, "DANH_SACH_PHAT_DE.md"), 'w', encoding='utf-8') as f:
        f.write(roster_md)
        
    for buoi_num, (preamble, de_dict) in [(1, b1_parts), (2, b2_parts)]:
        tex_filename = f"Phieu_Kiem_Tra_Tuan_03_Buoi_{buoi_num:02d}_{cfg['file_suffix']}.tex"
        pdf_filename = f"Phieu_Kiem_Tra_Tuan_03_Buoi_{buoi_num:02d}_{cfg['file_suffix']}.pdf"
        tex_path = os.path.join(folder_path, tex_filename)
        pdf_path = os.path.join(folder_path, pdf_filename)
        
        body_parts = [preamble]
        for i, s in enumerate(students):
            made = test_codes[i % 4]
            raw_p1, raw_p2 = de_dict[made]
            p1 = personalize_page_front(raw_p1, s['name'], s['code'], cfg['short_class'])
            p2 = personalize_page_back(raw_p2, s['name'], s['code'], cfg['short_class'])
                
            body_parts.append(p1)
            body_parts.append(r"\newpage")
            body_parts.append(p2)
            if i < len(students) - 1:
                body_parts.append(r"\newpage")
                
        body_parts.append(r"\end{document}" + "\n")
        
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(body_parts))
            
        print(f" -> Biên dịch {tex_filename} ({len(students)} học sinh = {len(students)*2} trang)...")
        p = subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename],
                           cwd=folder_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
        
        if os.path.exists(pdf_path):
            import pypdf
            reader = pypdf.PdfReader(pdf_path)
            total_pages = len(reader.pages)
            expected = len(students) * 2
            status = "[OK]" if total_pages == expected else f"[CẢNH BÁO: {total_pages} trang != {expected} trang]"
            print(f"    {status} Đã tạo thành công {pdf_filename}: {total_pages} trang (kỳ vọng: {expected} trang)")
            
            # Sync to SAP_XEP_THEO_TUAN/TUAN_3/<folder_name>/
            dest_folder = os.path.join(DEST_DIR, cfg['folder_name'])
            os.makedirs(dest_folder, exist_ok=True)
            shutil.copy2(pdf_path, os.path.join(dest_folder, pdf_filename))
            shutil.copy2(tex_path, os.path.join(dest_folder, tex_filename))
            shutil.copy2(os.path.join(folder_path, "DANH_SACH_PHAT_DE.md"), os.path.join(dest_folder, "DANH_SACH_PHAT_DE.md"))
        else:
            print(f"    [FAIL] Lỗi biên dịch {tex_filename}")
            print(p.stdout[-1500:])

if __name__ == '__main__':
    print("1. Đang kết nối Supabase lấy danh sách 3 lớp 7...")
    student_data = fetch_students()
    
    print("2. Đang đọc template Buổi 1 và Buổi 2...")
    b1_parts = load_template_parts(1)
    b2_parts = load_template_parts(2)
    
    print("3. Đang tạo phiếu kiểm tra cá nhân hóa theo từng lớp...")
    for cfg in CLASS_CONFIG:
        st_list = student_data[cfg['id']]
        print(f"\n=======================================================")
        print(f"LỚP: {cfg['display_name']} - SĨ SỐ: {len(st_list)} HỌC SINH")
        print(f"=======================================================")
        generate_for_class(cfg, st_list, b1_parts, b2_parts)
        
    print("\n=======================================================")
    print("ĐÃ HOÀN THÀNH TOÀN BỘ PHIẾU KIỂM TRA CHO CẢ 3 LỚP 7!")
    print("=======================================================")
