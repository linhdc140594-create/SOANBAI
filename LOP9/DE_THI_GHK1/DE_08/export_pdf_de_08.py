import os
import sys
import json
import subprocess
import pymupdf
import shutil

sys.stdout.reconfigure(encoding='utf-8')
work_dir = r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\DE_08'
json_path = os.path.join(work_dir, 'de_08.json')

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

hinh_cay_gay = r'''\begin{center}
\begin{tikzpicture}[scale=0.9]
  \coordinate (A) at (0,0);
  \coordinate (B) at (0,3.04);
  \coordinate (C) at (4.5,0);
  \draw[thick] (-0.8,0) -- (5.5,0);
  \draw[line width=2.5pt, brown!70!black] (0,0) -- (0,3.04);
  \draw[line width=2pt, brown!70!black] (0,3.04) -- (4.5,0);
  \fill[green!60!black] (4.5,0) circle (0.3);
  \draw (A) ++(0,0.25) -- ++(0.25,0) -- ++(0,-0.25);
  \draw (C) ++(-0.8,0) arc (180:146:0.8);
  \node at (3.4,0.25) {\footnotesize $34^\circ$};
  \node[below] at (2.25,0) {\footnotesize $4{,}5\text{ m}$};
  \node[left] at (0,1.5) {\footnotesize $h_1$};
  \node[above right] at (2.25,1.5) {\footnotesize $h_2$};
  \node[below left] at (A) {$A$};
  \node[above left] at (B) {$B$};
  \node[below right] at (C) {$C$};
\end{tikzpicture}
\end{center}'''

d['phan_IV'][2]['hinh_ve'] = hinh_cay_gay


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
\rhead{\textit{Môn Toán 9 -- Đề số 08}}
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
  \textbf{\large ĐỀ ÔN TẬP GIỮA HỌC KỲ I -- ĐỀ SỐ 08}\\
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
\rhead{\textit{Hướng dẫn giải chi tiết -- Đề số 08}}
\lhead{\textit{Môn Toán 9 -- Giữa học kì I}}
\cfoot{\thepage}

\begin{document}

\begin{center}
  \textbf{\Large HƯỚNG DẪN GIẢI CHI TIẾT -- ĐỀ SỐ 08}\\
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
\textbf{Chọn} & \textbf{C} & \textbf{A} & \textbf{B} & \textbf{D} & \textbf{B} & \textbf{B} & \textbf{B} & \textbf{C} & \textbf{B} & \textbf{A} & \textbf{A} & \textbf{A} \\
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
 & c) & \textbf{X} & & 0,5 & & c) & & \textbf{X} & 0,5 \\
\cline{2-5}\cline{7-10}
 & d) & & \textbf{X} & 1,0 & & d) & \textbf{X} & & 1,0 \\
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
\textbf{Đáp án} & $\mathbf{2}$ & $\mathbf{0{,}48}$ (hoặc $\mathbf{\frac{12}{25}}$) \\
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
print('--- ĐANG TẠO FILE TEX CHO ĐỀ 08 ---')
dethi_tex = generate_dethi_tex(d)
dapan_tex = generate_dapan_tex(d)

dethi_tex_path = os.path.join(work_dir, 'De_08_DeThi.tex')
dapan_tex_path = os.path.join(work_dir, 'De_08_DapAn.tex')

with open(dethi_tex_path, 'w', encoding='utf-8') as f:
    f.write(dethi_tex)

with open(dapan_tex_path, 'w', encoding='utf-8') as f:
    f.write(dapan_tex)

print('--- BIÊN DỊCH PDF ---')
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_08_DeThi.tex'], cwd=work_dir, stdout=subprocess.DEVNULL)
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_08_DeThi.tex'], cwd=work_dir, stdout=subprocess.DEVNULL)

subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_08_DapAn.tex'], cwd=work_dir, stdout=subprocess.DEVNULL)
subprocess.run(['pdflatex', '-interaction=nonstopmode', 'De_08_DapAn.tex'], cwd=work_dir, stdout=subprocess.DEVNULL)

dethi_pdf = os.path.join(work_dir, 'De_08_DeThi.pdf')
dapan_pdf = os.path.join(work_dir, 'De_08_DapAn.pdf')

doc_dt = pymupdf.open(dethi_pdf)
doc_da = pymupdf.open(dapan_pdf)

print(f'De_08_DeThi.pdf: {len(doc_dt)} trang')
print(f'De_08_DapAn.pdf: {len(doc_da)} trang')

# Sao chép vào PHAN_DE_THI và PHAN_LOI_GIAI
phan_dt_dir = r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\PHAN_DE_THI'
phan_lg_dir = r'd:\GitHub\SOANBAI-main\LOP9\DE_THI_GHK1\PHAN_LOI_GIAI'

shutil.copy2(dethi_pdf, os.path.join(phan_dt_dir, 'De_08_DeThi.pdf'))
shutil.copy2(dapan_pdf, os.path.join(phan_lg_dir, 'De_08_DapAn.pdf'))
print('Đã copy vào PHAN_DE_THI và PHAN_LOI_GIAI thành công!')

