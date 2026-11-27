import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

def make_header(de_num):
    return r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage[top=1.8cm, bottom=2.0cm, left=1.8cm, right=1.8cm]{geometry}

\setlength{\parskip}{3pt}
\setlength{\parindent}{0pt}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\lhead{\footnotesize \textbf{CHÙA HƯƠNG SƠN -- ÔN THI VÀO 10}}
\rhead{\footnotesize \textbf{ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ ''' + f'{de_num:02d}' + r''')}}
\cfoot{\thepage}

\begin{document}

\noindent
\begin{tabular*}{\linewidth}{@{\extracolsep{\fill}}cc@{}}
\textbf{SỞ GIÁO DỤC VÀ ĐÀO TẠO} & \textbf{ĐỀ KIỂM TRA CUỐI HỌC KỲ I} \\
\textbf{CHÙA HƯƠNG SƠN} & \textbf{NĂM HỌC 2026 -- 2027} \\
\textbf{ĐỀ THI THỬ SỐ ''' + f'{de_num:02d}' + r'''} & \textbf{MÔN: TOÁN -- LỚP 9} \\
\textit{(Đề thi gồm 03 trang)} & \textit{Thời gian làm bài: 90 phút (không kể thời gian phát đề)} \\
\end{tabular*}

\vspace{2mm}
\noindent
\rule{\linewidth}{0.8pt}

\vspace{1mm}
\noindent
Họ và tên thí sinh: \dotfill Số báo danh: \dotfill

\vspace{2mm}
\noindent
\textbf{\large I. TRẮC NGHIỆM KHÁCH QUAN (7,0 điểm)}

\vspace{1mm}
\noindent
\textbf{Phần 1. Trắc nghiệm nhiều lựa chọn (3,0 điểm).} \textit{Từ câu 1 đến câu 12, thí sinh chọn đáp án đúng nhất trong 4 đáp án A, B, C, D rồi ghi vào bài làm.}
'''

def make_sol_header(de_num):
    return r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage[top=1.8cm, bottom=2.0cm, left=1.8cm, right=1.8cm]{geometry}

\setlength{\parskip}{3pt}
\setlength{\parindent}{0pt}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\lhead{\footnotesize \textbf{CHÙA HƯƠNG SƠN -- HƯỚNG DẪN CHẤM THI}}
\rhead{\footnotesize \textbf{ĐÁP ÁN CHI TIẾT ĐỀ THI THỬ SỐ ''' + f'{de_num:02d}' + r''')}}
\cfoot{\thepage}

\begin{document}

\begin{center}
{\large\bfseries ĐÁP ÁN \& HƯỚNG DẪN CHẤM ĐỀ THI THỬ CUỐI HỌC KỲ I (ĐỀ SỐ ''' + f'{de_num:02d}' + r''')}\\[1.5mm]
{\bfseries ĐƠN VỊ: CHÙA HƯƠNG SƠN \quad|\quad MÔN: TOÁN -- LỚP 9 \quad|\quad NĂM HỌC 2026 -- 2027}\\[1mm]
\textit{(Chuẩn cấu trúc định dạng mới của Sở Giáo dục và Đào tạo)}
\end{center}

\vspace{1mm}
\hrule
\vspace{3mm}

\noindent
\textbf{\large PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (7,0 ĐIỂM)}
'''

def compile_doc(folder, tex_name):
    cmd = ['pdflatex', '-interaction=nonstopmode', tex_name]
    p = subprocess.run(cmd, cwd=folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    pdf_name = tex_name.replace('.tex', '.pdf')
    pdf_path = os.path.join(folder, pdf_name)
    if os.path.exists(pdf_path):
        doc = fitz.open(pdf_path)
        pages = len(doc)
        doc.close()
        return True, pages
    return False, 0

print("Helper loaded.")
