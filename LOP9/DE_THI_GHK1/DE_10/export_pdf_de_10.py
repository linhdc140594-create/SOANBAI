import os
import sys
import json
import subprocess
import pymupdf
import shutil

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\DE_10'
json_path = os.path.join(work_dir, 'de_10.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

hinh_cau_7 = r'''\begin{center}
\begin{tikzpicture}[scale=0.85]
  \coordinate (B) at (0,0);
  \coordinate (H) at (1.8,0);
  \coordinate (C) at (4.5,0);
  \coordinate (A) at (1.8,2.2);
  \draw[thick] (B) node[below left]{$B$} -- (C) node[below right]{$C$} -- (A) node[above]{$A$} -- cycle;
  \draw[thick] (A) -- (H) node[below]{$H$};
  \draw (A) ++(-0.2,-0.24) -- ++(0.24,-0.2) -- ++(0.2,0.24);
  \draw (H) ++(0,0.25) -- ++(-0.25,0) -- ++(0,-0.25);
\end{tikzpicture}
\end{center}'''

hinh_cau_9 = r'''\begin{center}
\begin{tikzpicture}[scale=0.85]
  \coordinate (O) at (0,0);
  \draw[thick] (O) circle (1.3);
  \coordinate (A) at (0:1.3);
  \coordinate (B) at (65:1.3);
  \draw[thick] (O) -- (A) node[right]{$A$};
  \draw[thick] (O) -- (B) node[above right]{$B$};
  \fill (O) circle (1.5pt) node[below left]{$O$};
  \draw (0.35,0) arc (0:65:0.35);
\end{tikzpicture}
\end{center}'''

hinh_cau_11 = r'''\begin{center}
\begin{tikzpicture}[scale=0.85]
  \draw[thick, blue!80!black] (-0.8,0) -- (4,0);
  \draw[thick, blue!80!black] (-0.8,2) -- (4,2);
  \coordinate (A) at (0,0);
  \coordinate (H) at (0,2);
  \coordinate (B) at (2.4,2);
  \draw[dashed] (A) -- (H) node[above left]{$H$};
  \draw[thick, red!70!black] (A) node[below]{$A$} -- (B) node[above]{$B$};
  \draw (A) ++(0,0.25) -- ++(0.25,0) -- ++(0,-0.25);
  \draw (A) ++(0,0.55) arc (90:39.8:0.55);
  \node at (0.22,0.8) {\footnotesize $\alpha$};
  \node[left] at (0,1) {\footnotesize $250\text{ m}$};
  \node[above right] at (1.1,1) {\footnotesize $320\text{ m}$};
\end{tikzpicture}
\end{center}'''

d['phan_I'][6]['hinh_ve'] = hinh_cau_7
d['phan_I'][8]['hinh_ve'] = hinh_cau_9
d['phan_I'][10]['hinh_ve'] = hinh_cau_11


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
\rhead{\textit{Môn Toán 9 -- Đề số 10}}
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
  \textbf{\large ĐỀ ÔN TẬP GIỮA HỌC KỲ I -- ĐỀ SỐ 10}\\
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

% --- PHẦN II ---
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI (2,0 điểm)}

\textit{Thí sinh trả lời từ câu 1 đến câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn đúng hoặc sai.}

\vspace{1mm}
'''
    for q in d['phan_II']:
        noi_dung = q['de']
        ya = ("\\True " if q['y_a']['dung'] else "") + q['y_a']['noi_dung']
        yb = ("\\True " if q['y_b']['dung'] else "") + q['y_b']['noi_dung']
        yc = ("\\True " if q['y_c']['dung'] else "") + q['y_c']['noi_dung']
        yd = ("\\True " if q['y_d']['dung'] else "") + q['y_d']['noi_dung']

        choice_tf = f"\\choiceTF\n{{{ya}}}\n{{{yb}}}\n{{{yc}}}\n{{{yd}}}"
        body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf}\n\\end{{ex}}\n\n"

    body += r'''
\vspace{1mm}
\noindent\textbf{BẢNG TRẢ LỜI ĐÚNG SAI PHẦN II:}
\begin{center}
\begin{tabular}{|c|c|c|c|c||c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Lệnh hỏi} & \textbf{Đúng} & \textbf{Sai} & \textbf{Điểm} & \textbf{Câu} & \textbf{Lệnh hỏi} & \textbf{Đúng} & \textbf{Sai} & \textbf{Điểm} \\
\hline
 & a) & & & & & a) & & & \\
\cline{2-4}\cline{7-9}
\textbf{1} & b) & & & & \textbf{2} & b) & & & \\
\cline{2-4}\cline{7-9}
 & c) & & & & & c) & & & \\
\cline{2-4}\cline{7-9}
 & d) & & & & & d) & & & \\
\hline
\end{tabular}
\end{center}
\vspace{2mm}

% --- PHẦN III ---
\noindent\textbf{\large PHẦN III. CÂU TRẮC NGHIỆM TRẢ LỜI NGẮN (1,0 điểm)}

\textit{Thí sinh trả lời từ câu 1 đến câu 2. Viết câu trả lời vào ô quy định.}

\vspace{1mm}
'''
    for q in d['phan_III']:
        noi_dung = q['de']
        da = q['da']
        body += f"\\begin{{ex}}\n{noi_dung}\n\\shortans{{{da}}}\n\\end{{ex}}\n\n"

    body += r'''
\vspace{2mm}
% --- PHẦN IV ---
\noindent\textbf{\large PHẦN IV. TỰ LUẬN (4,0 điểm)}

\textit{Thí sinh trình bày chi tiết lời giải vào giấy làm bài.}

\vspace{1mm}
'''
    for q in d['phan_IV']:
        c_num = q['cau']
        diem = q['diem']
        noi_dung = q['de']
        hinh = q.get('hinh_ve')
        if hinh:
            body += f"\\noindent\\textbf{{Câu {c_num} ({diem}).}}\n\n{noi_dung}\n{hinh}\n\n\\vspace{{2mm}}\n"
        else:
            body += f"\\noindent\\textbf{{Câu {c_num} ({diem}).}}\n\n{noi_dung}\n\n\\vspace{{2mm}}\n"

    footer = r'''
\vfill
\begin{center}
  \textbf{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer


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
\usepackage[sol]{ex_test}
\SAOPTN{widthSA=3.2,heightSA=0.62}

\setlength{\headheight}{15pt}
\setlength{\parskip}{0pt}

\pagestyle{fancy}
\fancyhf{}
\rhead{\textit{Hướng dẫn giải chi tiết -- Đề số 10}}
\lhead{\textit{Môn Toán 9 -- Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

\begin{center}
  \textbf{\Large HƯỚNG DẪN GIẢI CHI TIẾT -- ĐỀ SỐ 10}\\
  \textbf{\large MÔN TOÁN 9 -- GIỮA HỌC KỲ I}
\end{center}
\vspace{2mm}

% --- BẢNG ĐÁP ÁN TỔNG HỢP ---
\noindent\textbf{\large I. BẢNG ĐÁP ÁN TỔNG HỢP}

\vspace{1mm}
\noindent\textbf{1. Phần I - Trắc nghiệm nhiều phương án lựa chọn (3,0 điểm):}
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} \\
\hline
\textbf{Chọn} & \textbf{C} & \textbf{C} & \textbf{D} & \textbf{C} & \textbf{C} & \textbf{A} & \textbf{A} & \textbf{C} & \textbf{D} & \textbf{C} & \textbf{B} & \textbf{A} \\
\hline
\end{tabular}
\end{center}
\vspace{1mm}

\noindent\textbf{2. Phần II - Trắc nghiệm Đúng/Sai (2,0 điểm):}
\begin{center}
\begin{tabular}{|c|c|c|c|c||c|c|c|c|c|}
\hline
\textbf{Câu} & \textbf{Lệnh hỏi} & \textbf{Đúng} & \textbf{Sai} & \textbf{Điểm} & \textbf{Câu} & \textbf{Lệnh hỏi} & \textbf{Đúng} & \textbf{Sai} & \textbf{Điểm} \\
\hline
 & a) & \textbf{X} & & 0,1 & & a) & \textbf{X} & & 0,1 \\
\cline{2-5}\cline{7-10}
\textbf{1} & b) & & \textbf{X} & 0,25 & \textbf{2} & b) & & \textbf{X} & 0,25 \\
\cline{2-5}\cline{7-10}
 & c) & \textbf{X} & & 0,5 & & c) & \textbf{X} & & 0,5 \\
\cline{2-5}\cline{7-10}
 & d) & \textbf{X} & & 1,0 & & d) & & \textbf{X} & 1,0 \\
\hline
\end{tabular}
\end{center}
\vspace{1mm}

\noindent\textbf{3. Phần III - Trả lời ngắn (1,0 điểm):}
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
\textbf{Câu} & \textbf{1} & \textbf{2} \\
\hline
\textbf{Đáp án} & $\mathbf{x = 5}$ & $\mathbf{8\text{ cm}}$ \\
\hline
\end{tabular}
\end{center}
\vspace{3mm}

% --- LỜI GIẢI CHI TIẾT ---
\noindent\textbf{\large II. HƯỚNG DẪN GIẢI CHI TIẾT}

\vspace{2mm}
\noindent\textbf{\large PHẦN I. CÂU TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN LỰA CHỌN}
\vspace{1mm}
'''
    body = ""
    count_p1 = 0
    for q in d['phan_I']:
        count_p1 += 1
        if count_p1 == 7:
            body += "\\newpage\n"
        noi_dung = q['de']
        da = q['da'].strip().upper()
        hinh = q.get('hinh_ve')
        loi_giai = q['loi_giai']

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
            body += f"\\begin{{ex}}\n{noi_dung}\n{hinh}\n{choice_code}\n\\loigiai{{\n{loi_giai}\n}}\n\\end{{ex}}\n\n"
        else:
            body += f"\\begin{{ex}}\n{noi_dung}\n{choice_code}\n\\loigiai{{\n{loi_giai}\n}}\n\\end{{ex}}\n\n"

    body += r'''
\newpage
\noindent\textbf{\large PHẦN II. CÂU TRẮC NGHIỆM ĐÚNG SAI}
\vspace{1mm}
'''
    for q in d['phan_II']:
        noi_dung = q['de']
        ya = ("\\True " if q['y_a']['dung'] else "") + q['y_a']['noi_dung']
        yb = ("\\True " if q['y_b']['dung'] else "") + q['y_b']['noi_dung']
        yc = ("\\True " if q['y_c']['dung'] else "") + q['y_c']['noi_dung']
        yd = ("\\True " if q['y_d']['dung'] else "") + q['y_d']['noi_dung']

        choice_tf = f"\\choiceTF\n{{{ya}}}\n{{{yb}}}\n{{{yc}}}\n{{{yd}}}"
        loi_giai = f"\\begin{{itemize}}[leftmargin=*]\n  \\item a) {'Đúng' if q['y_a']['dung'] else 'Sai'}. {q['y_a']['loi_giai']}\n  \\item b) {'Đúng' if q['y_b']['dung'] else 'Sai'}. {q['y_b']['loi_giai']}\n  \\item c) {'Đúng' if q['y_c']['dung'] else 'Sai'}. {q['y_c']['loi_giai']}\n  \\item d) {'Đúng' if q['y_d']['dung'] else 'Sai'}. {q['y_d']['loi_giai']}\n\\end{{itemize}}"

        body += f"\\begin{{ex}}\n{noi_dung}\n{choice_tf}\n\\loigiai{{\n{loi_giai}\n}}\n\\end{{ex}}\n\n"

    body += r'''
\vspace{2mm}
\noindent\textbf{\large PHẦN III. CÂU TRẢ LỜI NGẮN}
\vspace{1mm}
'''
    for q in d['phan_III']:
        noi_dung = q['de']
        da = q['da']
        loi_giai = q['loi_giai']
        body += f"\\begin{{ex}}\n{noi_dung}\n\\shortans{{{da}}}\n\\loigiai{{\n{loi_giai}\n}}\n\\end{{ex}}\n\n"

    body += r'''
\newpage
\noindent\textbf{\large PHẦN IV. TỰ LUẬN}
\vspace{1mm}
'''
    for q in d['phan_IV']:
        c_num = q['cau']
        diem = q['diem']
        noi_dung = q['de']
        hinh = q.get('hinh_ve')
        loi_giai = q['loi_giai']

        if c_num == 3:
            body += "\\newpage\n"

        if hinh:
            body += f"\\noindent\\textbf{{Câu {c_num} ({diem}).}}\n\n{noi_dung}\n{hinh}\n\n\\noindent\\textbf{{Lời giải:}}\n\n{loi_giai}\n\n\\vspace{{3mm}}\n"
        else:
            body += f"\\noindent\\textbf{{Câu {c_num} ({diem}).}}\n\n{noi_dung}\n\n\\noindent\\textbf{{Lời giải:}}\n\n{loi_giai}\n\n\\vspace{{3mm}}\n"

    footer = r'''
\vfill
\begin{center}
  \textbf{--- HẾT ---}
\end{center}
\end{document}
'''
    return header + body + footer


# =============================================================================
# THỰC THI BIÊN DỊCH VÀ KIỂM TRA SỐ TRANG
# =============================================================================
print('--- ĐANG TẠO FILE TEX CHO ĐỀ 10 ---')
dethi_tex = generate_dethi_tex(d)
dapan_tex = generate_dapan_tex(d)

dethi_tex_path = os.path.join(work_dir, 'De_10_DeThi.tex')
dapan_tex_path = os.path.join(work_dir, 'De_10_DapAn.tex')

with open(dethi_tex_path, 'w', encoding='utf-8') as f:
    f.write(dethi_tex)

with open(dapan_tex_path, 'w', encoding='utf-8') as f:
    f.write(dapan_tex)

print('--- BIÊN DỊCH PDF ---')
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_10_DeThi.tex'], cwd=work_dir, stdout=subprocess.DEVNULL)
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_10_DeThi.tex'], cwd=work_dir, stdout=subprocess.DEVNULL)

subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_10_DapAn.tex'], cwd=work_dir, stdout=subprocess.DEVNULL)
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_10_DapAn.tex'], cwd=work_dir, stdout=subprocess.DEVNULL)

dethi_pdf = os.path.join(work_dir, 'De_10_DeThi.pdf')
dapan_pdf = os.path.join(work_dir, 'De_10_DapAn.pdf')

doc_dt = pymupdf.open(dethi_pdf)
doc_da = pymupdf.open(dapan_pdf)

print(f'De_10_DeThi.pdf: {len(doc_dt)} trang')
print(f'De_10_DapAn.pdf: {len(doc_da)} trang')

# Sao chép vào PHAN_DE_THI và PHAN_LOI_GIAI
phan_dt_dir = r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\PHAN_DE_THI'
phan_lg_dir = r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\PHAN_LOI_GIAI'

shutil.copy2(dethi_pdf, os.path.join(phan_dt_dir, 'De_10_DeThi.pdf'))
shutil.copy2(dapan_pdf, os.path.join(phan_lg_dir, 'De_10_DapAn.pdf'))
print('Đã copy vào PHAN_DE_THI và PHAN_LOI_GIAI thành công!')

