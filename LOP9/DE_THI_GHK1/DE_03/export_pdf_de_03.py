import os
import sys
import json
import subprocess
import pymupdf
import shutil

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\DE_03'
json_path = os.path.join(work_dir, 'de_03.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# =============================================================================
# 1. HÀM TẠO FILE TEX CHO ĐỀ THI (De_03_DeThi.tex)
# =============================================================================
def generate_dethi_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,arrows.meta,patterns}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage[top=0.9cm, bottom=0.9cm, left=1.2cm, right=1.2cm]{geometry}
\usepackage[dethi]{ex_test}
\SAOPTN{widthSA=3.2,heightSA=0.62}

\setlength{\headheight}{15pt}
\setlength{\parskip}{0pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Môn Toán 9 -- Đề số 03}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

% --- KHUNG TIÊU ĐỀ ĐỀ THI ---
\noindent
\begin{tabularx}{\linewidth}{X r}
\textbf{TRƯỜNG THCS: \dotfill} & \textbf{ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I} \\
\textbf{Họ và tên: \dotfill} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{Lớp: \dotfill \quad SBD: \dotfill} & \textbf{Môn: TOÁN 9} \\
\hline
\end{tabularx}
\vspace{2mm}

\begin{center}
  \textbf{\large ĐỀ ÔN TẬP GIỮA HỌC KỲ I -- ĐỀ SỐ 03}\\
  \textit{Thời gian làm bài: 90 phút (Không kể thời gian phát đề)}
\end{center}
\vspace{1mm}

% --- PHẦN I ---
\noindent\textbf{\large PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN (3,0 điểm)}

\textit{Thí sinh trả lời từ câu 1 đến câu 12. Mỗi câu hỏi thí sinh chỉ chọn một phương án duy nhất.}

\vspace{1mm}
'''
    body = ""
    for q in d['phan_I']:
        noi_dung = q['de']
        da = q['da'].strip().upper()
        hinh = q.get('hinh_ve')

        def clean_opt(val):
            val = val.strip()
            if not val.endswith('$') and val.endswith('.'):
                val = val[:-1].strip()
            return val

        a_txt = ("\\True " if da == 'A' else "") + clean_opt(q['a'])
        b_txt = ("\\True " if da == 'B' else "") + clean_opt(q['b'])
        c_txt = ("\\True " if da == 'C' else "") + clean_opt(q['c'])
        d_txt = ("\\True " if da == 'D' else "") + clean_opt(q['d'])

        choice_code = f"\\choice\n{{{a_txt}}}\n{{{b_txt}}}\n{{{c_txt}}}\n{{{d_txt}}}"

        if hinh:
            body += f"\\begin{{ex}}\n{noi_dung}\n{hinh}\n{choice_code}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_code}\n\\end{{ex}}\n\n"

    # Bảng đáp án trắc nghiệm Phần I
    body += r'''
\vspace{1mm}
\noindent\textbf{BẢNG TRẢ LỜI TRẮC NGHIỆM PHẦN I:}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{Chọn} & \rule{0pt}{0.65cm} & & & & & & & & & & & \\
\hline
\end{tabular}
\end{center}
\vspace{2mm}
'''

    # PHẦN II (Đúng / Sai)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI (2,0 điểm)}

\textit{Thí sinh trả lời câu 1 và câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}

\vspace{1mm}
'''
    for q in d['phan_II']:
        noi_dung = q['de']
        tf_items = []
        for y_key in ['y_a', 'y_b', 'y_c', 'y_d']:
            y_item = q[y_key]
            is_true = (y_item['da'].strip().upper() == 'D')
            prefix = "\\True " if is_true else ""
            txt = y_item['noi_dung'].strip()
            if not txt.endswith('$') and txt.endswith('.'):
                txt = txt[:-1].strip()
            tf_items.append(f"{{{prefix}{txt}}}")
        
        choice_tf_code = "\\choiceTF\n" + "\n".join(tf_items)
        body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf_code}\n\\end{{ex}}\n\n"

    # Bảng điền đáp án Phần II
    body += r'''
\noindent\textbf{BẢNG TRẢ LỜI PHẦN II:}
\begin{center}
\begin{tabular}{|c|c|c|c|c||c|c|c|c|c|}
\hline
\textbf{Câu 1} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} & \textbf{Câu 2} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\
\hline
\textbf{Đ/S} & \rule{0pt}{0.6cm} & & & & \textbf{Đ/S} & & & & \\
\hline
\end{tabular}
\end{center}
\vspace{2mm}
'''

    # PHẦN III (Trả lời ngắn)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN III. CÂU HỎI TRẢ LỜI NGẮN (2,0 điểm)}

\textit{Thí sinh trả lời câu 1 và câu 2. Điền kết quả vào ô trống tương ứng.}

\vspace{1mm}
'''
    for q in d['phan_III']:
        noi_dung = q['de']
        da = q['da'].strip()
        body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da}}}\n\\end{{ex}}\n\n"

    # PHẦN IV (Tự luận)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN (3,0 điểm)}

\textit{Thí sinh trình bày chi tiết lời giải vào giấy làm bài.}

\vspace{1mm}
'''
    for q in d['phan_IV']:
        diem_str = f" ({q['diem']})" if 'diem' in q else ""
        noi_dung = q['de']

        body += f"\\begin{{ex}}{diem_str}\n"
        if noi_dung:
            body += f"{noi_dung}\n"

        if 'hinh_ve' in q:
            body += f"{q['hinh_ve']}\n"

        if 'cac_y' in q and q['cac_y']:
            body += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=2pt]\n"
            for y_item in q['cac_y']:
                diem_y = f" ({y_item['diem_y']} điểm)" if 'diem_y' in y_item else ""
                body += f"\\item{diem_y} {y_item['noi_dung']}\n"
            body += "\\end{enumerate}\n"

        body += f"\\end{{ex}}\n\\vspace{{0.5mm}}\n\n"

    footer = r'''
\enlargethispage{1.5cm}
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer


# =============================================================================
# 2. HÀM TẠO FILE TEX CHO ĐÁP ÁN (De_03_DapAn.tex)
# =============================================================================
def generate_dapan_tex(d):
    header = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usetikzlibrary{calc,angles,quotes,arrows.meta,patterns}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage[top=0.9cm, bottom=0.9cm, left=1.2cm, right=1.2cm]{geometry}
\usepackage[loigiai]{ex_test}
\SAOPTN{widthSA=3.2,heightSA=0.62}

\setlength{\headheight}{15pt}
\setlength{\parskip}{0pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Môn Toán 9 -- Hướng dẫn giải Đề số 03}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

\begin{center}
  \textbf{\Large HƯỚNG DẪN GIẢI CHI TIẾT VÀ BẢNG ĐÁP ÁN}\\
  \textbf{\large ĐỀ ÔN TẬP GIỮA HỌC KỲ I -- ĐỀ SỐ 03}\\
  \textit{Môn: Toán 9 -- Năm học 2026 -- 2027}
\end{center}
\vspace{2mm}

% --- BẢNG ĐÁP ÁN TRẮC NGHIỆM TÓM TẮT ---
\noindent\textbf{\large A. BẢNG ĐÁP ÁN TRẮC NGHIỆM TỔNG HỢP}
\vspace{1mm}

\noindent\textbf{1. Phần I (Mỗi câu trả lời đúng được 0,25 điểm):}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{Đ/A} & \textbf{B} & \textbf{A} & \textbf{B} & \textbf{C} & \textbf{D} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{D} & \textbf{C} & \textbf{A} & \textbf{B} \\
\hline
\end{tabular}
\end{center}
\vspace{0.5mm}

\noindent\textbf{2. Phần II (Đúng 1 ý: 0,1đ; Đúng 2 ý: 0,25đ; Đúng 3 ý: 0,5đ; Đúng 4 ý: 1,0đ):}
\begin{center}
\begin{tabular}{|c|c|c|c|c||c|c|c|c|c|}
\hline
\textbf{Câu 1} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} & \textbf{Câu 2} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\
\hline
\textbf{Đáp án} & Đ & S & S & Đ & \textbf{Đáp án} & Đ & Đ & S & Đ \\
\hline
\end{tabular}
\end{center}
\vspace{0.5mm}

\noindent\textbf{3. Phần III (Mỗi câu trả lời đúng được 1,0 điểm):}
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
\textbf{Câu} & \textbf{Câu 1} & \textbf{Câu 2} \\
\hline
\textbf{Đáp án} & Nam: 22, Nữ: 18 & $62^\circ$ \\
\hline
\end{tabular}
\end{center}
\vspace{2mm}

% --- LỜI GIẢI CHI TIẾT ---
\noindent\textbf{\large B. HƯỚNG DẪN GIẢI CHI TIẾT TỪNG CÂU}
\vspace{1mm}

\noindent\textbf{\large PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN}
\vspace{1mm}
'''
    body = ""
    for q in d['phan_I']:
        noi_dung = q['de']
        da = q['da'].strip().upper()
        hinh = q.get('hinh_ve')
        loi_giai = q.get('loi_giai', '')

        def clean_opt(val):
            val = val.strip()
            if not val.endswith('$') and val.endswith('.'):
                val = val[:-1].strip()
            return val

        a_txt = ("\\True " if da == 'A' else "") + clean_opt(q['a'])
        b_txt = ("\\True " if da == 'B' else "") + clean_opt(q['b'])
        c_txt = ("\\True " if da == 'C' else "") + clean_opt(q['c'])
        d_txt = ("\\True " if da == 'D' else "") + clean_opt(q['d'])

        choice_code = f"\\choice\n{{{a_txt}}}\n{{{b_txt}}}\n{{{c_txt}}}\n{{{d_txt}}}"

        lg_block = f"\\loigiai{{\n{loi_giai}\n\\par\\textbf{{Chọn đáp án {da}.}}\n}}"
        if hinh:
            body += f"\\begin{{ex}}\n{noi_dung}\n{hinh}\n{choice_code}\n{lg_block}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_code}\n{lg_block}\n\\end{{ex}}\n\n"

    # PHẦN II (Đúng / Sai)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI}
\vspace{1mm}
'''
    for q in d['phan_II']:
        noi_dung = q['de']
        tf_items = []
        for y_key in ['y_a', 'y_b', 'y_c', 'y_d']:
            y_item = q[y_key]
            is_true = (y_item['da'].strip().upper() == 'D')
            prefix = "\\True " if is_true else ""
            txt = y_item['noi_dung'].strip()
            if not txt.endswith('$') and txt.endswith('.'):
                txt = txt[:-1].strip()
            tf_items.append(f"{{{prefix}{txt}}}")
        
        choice_tf_code = "\\choiceTF\n" + "\n".join(tf_items)

        # Lời giải từng ý
        lg_items = []
        labels = [('y_a', 'a)'), ('y_b', 'b)'), ('y_c', 'c)'), ('y_d', 'd)')]
        for key, lbl in labels:
            y_item = q[key]
            d_s = "Đúng" if y_item['da'].strip().upper() == 'D' else "Sai"
            lg_items.append(f"\\textbf{{{lbl}}} [{d_s}]: {y_item.get('loi_giai', '')}")

        lg_block = "\\loigiai{\n" + "\n\n".join(lg_items) + "\n}"
        body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf_code}\n{lg_block}\n\\end{{ex}}\n\n"

    # PHẦN III (Trả lời ngắn)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN III. CÂU HỎI TRẢ LỜI NGẮN}
\vspace{1mm}
'''
    for q in d['phan_III']:
        noi_dung = q['de']
        da = q['da'].strip()
        loi_giai = q.get('loi_giai', '')
        lg_block = f"\\loigiai{{\n{loi_giai}\n\\par\\textbf{{Đáp án:}} {da}\n}}"
        body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da}}}\n{lg_block}\n\\end{{ex}}\n\n"

    # PHẦN IV (Tự luận)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN}
\vspace{1mm}
'''
    for q in d['phan_IV']:
        diem_str = f" ({q['diem']})" if 'diem' in q else ""
        noi_dung = q['de']
        hinh = q.get('hinh_ve', '')

        body += f"\\begin{{ex}}{diem_str}\n"
        if noi_dung:
            body += f"{noi_dung}\n"

        if hinh:
            body += f"{hinh}\n"

        if 'cac_y' in q and q['cac_y']:
            body += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=2pt]\n"
            for y_item in q['cac_y']:
                diem_y = f" ({y_item['diem_y']} điểm)" if 'diem_y' in y_item else ""
                body += f"\\item{diem_y} {y_item['noi_dung']}\n"
            body += "\\end{enumerate}\n"

        # Lời giải chi tiết
        lg_body = ""
        if 'cac_y' in q and q['cac_y']:
            for y_item in q['cac_y']:
                diem_y = f" ({y_item['diem_y']} điểm)" if 'diem_y' in y_item else ""
                lg_body += f"\\textbf{{\\alph*)}} {diem_y}\n{y_item.get('loi_giai', '')}\n\n"
        else:
            lg_body = q.get('loi_giai', '')

        body += f"\\loigiai{{\n{lg_body}\n}}\n"
        body += f"\\end{{ex}}\n\\vspace{{1mm}}\n\n"

    footer = r'''
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer


# =============================================================================
# 3. THỰC THI BIÊN DỊCH VÀ XUẤT PDF
# =============================================================================
print("--- [ĐỀ 03] BẮT ĐẦU TẠO MÃ TEX VÀ BIÊN DỊCH PDF ---")

# A. ĐỀ THI
dethi_tex_content = generate_dethi_tex(d)
dethi_tex_path = os.path.join(work_dir, 'De_03_DeThi.tex')
with open(dethi_tex_path, 'w', encoding='utf-8') as f:
    f.write(dethi_tex_content)

print("Biên dịch De_03_DeThi.tex...")
cmd_dethi = f'pdflatex -interaction=nonstopmode De_03_DeThi.tex'
subprocess.run(cmd_dethi, cwd=work_dir, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(cmd_dethi, cwd=work_dir, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

dethi_pdf = os.path.join(work_dir, 'De_03_DeThi.pdf')
if os.path.exists(dethi_pdf):
    doc_dt = pymupdf.open(dethi_pdf)
    print(f"==> ĐỀ THI ĐÃ TẠO THÀNH CÔNG: {len(doc_dt)} trang")
    dest_dt = os.path.join(r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\PHAN_DE_THI', 'De_03_DeThi.pdf')
    shutil.copy2(dethi_pdf, dest_dt)
else:
    print("LỖI: Chưa tạo được De_03_DeThi.pdf")

# B. LỜI GIẢI
dapan_tex_content = generate_dapan_tex(d)
dapan_tex_path = os.path.join(work_dir, 'De_03_DapAn.tex')
with open(dapan_tex_path, 'w', encoding='utf-8') as f:
    f.write(dapan_tex_content)

print("Biên dịch De_03_DapAn.tex...")
cmd_dapan = f'pdflatex -interaction=nonstopmode De_03_DapAn.tex'
subprocess.run(cmd_dapan, cwd=work_dir, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(cmd_dapan, cwd=work_dir, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

dapan_pdf = os.path.join(work_dir, 'De_03_DapAn.pdf')
if os.path.exists(dapan_pdf):
    doc_da = pymupdf.open(dapan_pdf)
    print(f"==> LỜI GIẢI ĐÃ TẠO THÀNH CÔNG: {len(doc_da)} trang")
    dest_da = os.path.join(r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\PHAN_LOI_GIAI', 'De_03_DapAn.pdf')
    shutil.copy2(dapan_pdf, dest_da)
else:
    print("LỖI: Chưa tạo được De_03_DapAn.pdf")

print("--- [ĐỀ 03] HOÀN TẤT XUẤT SẮC ---")

