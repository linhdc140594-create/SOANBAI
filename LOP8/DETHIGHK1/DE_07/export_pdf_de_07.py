import os
import sys
import json
import subprocess
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP8\DETHIGHK1\DE_07'
json_path = os.path.join(work_dir, 'de_07.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# =============================================================================
# 1. HÀM TẠO FILE TEX CHO ĐỀ THI (De_07_DeThi.tex)
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
\usepackage[top=1.0cm, bottom=1.0cm, left=1.2cm, right=1.2cm]{geometry}
\usepackage[dethi]{ex_test}
\SAOPTN{widthSA=3.2,heightSA=0.62}

\setlength{\headheight}{15pt}
\setlength{\parskip}{0pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Môn Toán 8 -- Đề số 07}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

% --- KHUNG TIÊU ĐỀ ĐỀ THI ---
\noindent
\begin{tabularx}{\linewidth}{X r}
\textbf{TRƯỜNG THCS: \dotfill} & \textbf{ĐỀ KIỂM TRA ĐỊNH KỲ GIỮA HỌC KỲ I} \\
\textbf{Họ và tên: \dotfill} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{Lớp: \dotfill \quad SBD: \dotfill} & \textbf{Môn: TOÁN 8} \\
\hline
\end{tabularx}
\vspace{2mm}

\begin{center}
  \textbf{\large ĐỀ ÔN TẬP GIỮA HỌC KỲ I -- ĐỀ SỐ 07}\\
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
\begin{center}
\rule{4cm}{0.4pt}\\
\textit{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer


# =============================================================================
# 2. HÀM TẠO FILE TEX CHO ĐÁP ÁN (De_07_DapAn.tex)
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
\rhead{\textit{Môn Toán 8 -- Hướng dẫn giải Đề số 07}}
\lhead{\textit{Bộ đề ôn tập Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

\begin{center}
  \textbf{\Large HƯỚNG DẪN GIẢI CHI TIẾT VÀ BẢNG ĐÁP ÁN}\\
  \textbf{\large ĐỀ ÔN TẬP GIỮA HỌC KỲ I -- ĐỀ SỐ 07}\\
  \textit{Môn: Toán 8 -- Năm học 2026 -- 2027}
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
\textbf{Đ/A} & \textbf{C} & \textbf{B} & \textbf{A} & \textbf{B} & \textbf{C} & \textbf{A} & \textbf{A} & \textbf{A} & \textbf{B} & \textbf{C} & \textbf{C} & \textbf{A} \\
\hline
\end{tabular}
\end{center}
\vspace{0.5mm}

\noindent\textbf{2. Phần II (Đúng 1 ý: 0,1đ; 2 ý: 0,25đ; 3 ý: 0,5đ; 4 ý: 1,0đ):}
\begin{center}
\begin{tabular}{|c|c|c|c|c||c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} & \textbf{Câu} & \textbf{a)} & \textbf{b)} & \textbf{c)} & \textbf{d)} \\
\hline
\textbf{Câu 1} & \textbf{Đ} & \textbf{Đ} & \textbf{Đ} & \textbf{S} & \textbf{Câu 2} & \textbf{Đ} & \textbf{Đ} & \textbf{Đ} & \textbf{S} \\
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
\textbf{Đáp án} & $\mathbf{100}$ & $\mathbf{x = 0; x = 2; x = -2}$ \\
\hline
\end{tabular}
\end{center}
\vspace{1.5mm}

% --- B. LỜI GIẢI CHI TIẾT ---
\noindent\textbf{\large B. LỜI GIẢI CHI TIẾT CÁC CÂU HỎI}
\vspace{1mm}
'''
    body = ""
    for q in d['phan_I']:
        noi_dung = q['de']
        da = q['da'].strip().upper()
        hinh = q.get('hinh_ve')
        loigiai = q.get('loigiai', '')

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
            body += f"\\begin{{ex}}\n{noi_dung}\n{hinh}\n{choice_code}\n\\loigiai{{\n{loigiai}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_code}\n\\loigiai{{\n{loigiai}\n}}\n\\end{{ex}}\n\n"

    # PHẦN II (Đúng / Sai)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI}
\vspace{1mm}
'''
    for q in d['phan_II']:
        noi_dung = q['de']
        tf_items = []
        loigiai_tf = []
        for y_key in ['y_a', 'y_b', 'y_c', 'y_d']:
            y_item = q[y_key]
            is_true = (y_item['da'].strip().upper() == 'D')
            prefix = "\\True " if is_true else ""
            txt = y_item['noi_dung'].strip()
            if not txt.endswith('$') and txt.endswith('.'):
                txt = txt[:-1].strip()
            tf_items.append(f"{{{prefix}{txt}}}")
            
            y_lbl = y_key.split('_')[1]
            loigiai_tf.append(f"\\textbf{{{y_lbl})}} {y_item.get('giai', '')}")

        choice_tf_code = "\\choiceTF\n" + "\n".join(tf_items)
        lg_str = "\n\n".join(loigiai_tf)
        body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf_code}\n\\loigiai{{\n{lg_str}\n}}\n\\end{{ex}}\n\n"

    # PHẦN III (Trả lời ngắn)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN III. CÂU HỎI TRẢ LỜI NGẮN}
\vspace{1mm}
'''
    for q in d['phan_III']:
        noi_dung = q['de']
        da = q['da'].strip()
        loigiai = q.get('loigiai', '')
        body += f"\\begin{{ex}}\n{noi_dung} \\shortans{{{da}}}\n\\loigiai{{\n{loigiai}\n}}\n\\end{{ex}}\n\n"

    # PHẦN IV (Tự luận)
    body += r'''
\setcounter{ex}{0}
\noindent\textbf{\large PHẦN IV. TỰ LUẬN (HƯỚNG DẪN GIẢI VÀ THANG ĐIỂM)}
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

        loigiai_tu_luan = ""
        if 'cac_y' in q and q['cac_y']:
            body += "\\begin{enumerate}[label=\\textbf{\\alph*)}, leftmargin=0.8cm, itemsep=0pt, topsep=1pt]\n"
            for y_item in q['cac_y']:
                diem_y = f" ({y_item['diem_y']} điểm)" if 'diem_y' in y_item else ""
                body += f"\\item{diem_y} {y_item['noi_dung']}\n"

                y_lbl = y_item['y']
                loigiai_tu_luan += f"\\textbf{{{y_lbl})}} \\textit{diem_y}: {y_item.get('loigiai', '')}\n\n"
            body += "\\end{enumerate}\n"

        body += f"\\loigiai{{\n{loigiai_tu_luan}\n}}\n\\end{{ex}}\n\\vspace{{0.5mm}}\n\n"

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
# 3. GHI FILE TEX VÀ BIÊN DỊCH PDF
# =============================================================================
dethi_tex_path = os.path.join(work_dir, 'De_07_DeThi.tex')
dapan_tex_path = os.path.join(work_dir, 'De_07_DapAn.tex')

with open(dethi_tex_path, 'w', encoding='utf-8') as f:
    f.write(generate_dethi_tex(d))

with open(dapan_tex_path, 'w', encoding='utf-8') as f:
    f.write(generate_dapan_tex(d))

print("Ghi file TeX thanh cong! Bat dau bien dich pdflatex...")

def compile_tex(tex_file):
    for pass_num in [1, 2]:
        cmd = ["pdflatex", "-interaction=nonstopmode", tex_file]
        res = subprocess.run(cmd, cwd=work_dir, capture_output=True)
        if res.returncode != 0 and pass_num == 2:
            print(f"LỖI BIÊN DỊCH: {tex_file}")
            stdout_str = res.stdout.decode('latin-1', errors='ignore')
            print(stdout_str[-1200:])
            return False
    print(f"Biên dịch THÀNH CÔNG: {os.path.basename(tex_file)}")
    return True

compile_tex(dethi_tex_path)
compile_tex(dapan_tex_path)

# Kiểm tra số trang
dethi_pdf = os.path.join(work_dir, 'De_07_DeThi.pdf')
dapan_pdf = os.path.join(work_dir, 'De_07_DapAn.pdf')

if os.path.exists(dethi_pdf):
    doc1 = pymupdf.open(dethi_pdf)
    print(f"De_07_DeThi.pdf có: {len(doc1)} trang")

if os.path.exists(dapan_pdf):
    doc2 = pymupdf.open(dapan_pdf)
    print(f"De_07_DapAn.pdf có: {len(doc2)} trang")

