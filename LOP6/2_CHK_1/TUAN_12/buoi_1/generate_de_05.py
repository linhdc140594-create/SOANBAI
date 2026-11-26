import json
import os
import shutil
import subprocess
import pypdf
import pymupdf
import numpy as np

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
BRAIN_DIR = r"C:\Users\Admin\.gemini\antigravity\brain\0c8f089e-0c5d-4300-ba60-02f73af7a436"

data_05 = {
    "base_filename": "Phieu_Kiem_Tra_Tuan_12_Buoi_01_Ma05",
    "title_p1": "PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 6 - TUẦN 12 - BUỔI 1",
    "title_p2": "TOÁN 6 - TUẦN 12 - BUỔI 1",
    "code": "05",
    "short": [
        ["Bỏ dấu ngoặc của biểu thức $-(x - 15)$, ta được kết quả là:", "-x + 15"],
        ["Bỏ dấu ngoặc của biểu thức $+(-28 + x)$, ta được kết quả là:", "-28 + x"],
        ["Giá trị của biểu thức $(-58) + 32 + 58$ là:", "32"],
        ["Bỏ dấu ngoặc của biểu thức $-(u - v + 6)$, ta được kết quả là:", "-u + v - 6"],
        ["Điền vào chỗ trống: $50 - u - v = 50 - (\\dots)$ là:", "u + v"],
        ["Điền dấu thích hợp ($<, >, =$) vào chỗ trống: $-(-32) + (-40) \\; \\dots \\; 0$", "<"],
        ["Hình thoi có số trục đối xứng là:", "2"],
        ["Trong các chữ cái X, V, T, Y, chữ cái có tâm đối xứng là:", "X"],
        ["Hình chữ nhật có chiều dài $14\\text{ cm}$, chiều rộng $5\\text{ cm}$. Diện tích là:", "70\\text{ cm}^2"],
        ["Nhiệt độ trưa $26^\\circ\\text{C}$, đêm giảm xuống $17^\\circ\\text{C}$. Độ chênh lệch nhiệt độ là:", "9^\\circ\\text{C}"]
    ],
    "q11": {
        "a": "165 - (65 - 165)",
        "b": "(-95) - (25 - 190)",
        "c": "(482 - 76) - (482 - 176)",
        "d": "190 - [75 - (20 - 55)]",
        "e": "60 - 4 \\cdot (-2)^3",
        "f": "(27 - 38 + 65) - (27 - 38 - 35)"
    },
    "q12": {
        "a": "x - 16 = -35",
        "b": "36 - (x + 14) = 58",
        "c": "28 - (18 - x) = -16",
        "d": "Liệt kê và tính tổng các số nguyên $x$ thỏa mãn: $-4 < x \\le 4$"
    },
    "q13": {
        "de": "Một công ty may mặc xuất khẩu theo dõi kết quả kinh doanh trong năm và ghi nhận lợi nhuận qua từng quý (số tiền lãi ghi số dương, số tiền lỗ ghi số âm) như sau:\\par\\vspace{0.4mm}\\centerline{\\begin{tabular}{|l|c|c|c|c|}\\hline \\textbf{Quý trong năm} & Quý 1 & Quý 2 & Quý 3 & Quý 4 \\\\\\hline \\textbf{Lợi nhuận} & $-50\\text{ triệu đồng}$ & $+140\\text{ triệu đồng}$ & $-70\\text{ triệu đồng}$ & $+170\\text{ triệu đồng}$ \\\\\\hline\\end{tabular}}\\vspace{0.4mm}",
        "a": "Tính tổng lợi nhuận của công ty trong nửa đầu năm (Quý 1 và Quý 2).",
        "b": "Tính tổng lợi nhuận của cả năm và cho biết cả năm công ty lãi hay lỗ bao nhiêu tiền."
    },
    "q14": {
        "de": "Tìm tất cả các số nguyên $x$ để phân số sau nhận giá trị là một số nguyên: $A = \\dfrac{6}{x - 3}$."
    }
}

def format_math(expr):
    expr = expr.strip()
    if expr.startswith('$') and expr.endswith('$'):
        return expr
    return f"${expr}$"

def build_tex(data, ob11=7, vsa="0.25mm", ob12_ab=5, ob12_cd=6, dk13=9, dk14=8):
    t_p1 = data["title_p1"]
    t_p2 = data["title_p2"]
    c = data["code"]
    
    preamble = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\SAOPTN{widthSA=2.8,heightSA=0.62}
\setlength{\parskip}{0pt}

% Dòng kẻ chấm mờ chuẩn viết tay
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18.5pt%
  \vspace{1.0mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!60}\dotfill}\par%
  }%
  \vspace{0.6mm}%
  \endgroup%
}

% Định nghĩa ô bài tập tự luận trong bảng
\newcommand{\oBaiTap}[3][6]{%
  \vspace{1.0mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

\begin{document}
\pagestyle{empty}
'''
    content = [preamble]
    
    # --- TRANG 1 ---
    p1 = f'''% =============================================================================
% ========================= MA DE {c} - MAT TRUOC (TRANG 1/2) =============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p1}}} & \\textbf{{Mã đề: {c} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.0mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{Điểm số}} & \\centering\\textbf{{Lời nhận xét của thầy cô}} \\tabularnewline
\\rule{{0pt}}{{1.8cm}} & \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.0mm}}
'''
    for i, q in enumerate(data["short"], 1):
        p1 += f"\\noindent\\textbf{{Câu {i} (0,25 điểm).}} {q[0]} \\shortans{{{q[1]}}}\\par\\vspace{{{vsa}}}\n"
    
    p1 += f'''
\\vspace{{0.3mm}}
\\noindent\\textbf{{Câu 11 (3,0 điểm). Thực hiện phép tính (hợp lý nếu có thể):}}
\\vspace{{0.4mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob11}]{{a) (0,5 điểm)}}{{{format_math(data["q11"]["a"])}}} & \\oBaiTap[{ob11}]{{b) (0,5 điểm)}}{{{format_math(data["q11"]["b"])}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{c) (0,5 điểm)}}{{{format_math(data["q11"]["c"])}}} & \\oBaiTap[{ob11}]{{d) (0,5 điểm)}}{{{format_math(data["q11"]["d"])}}} \\\\
\\hline
\\oBaiTap[{ob11}]{{e) (0,5 điểm)}}{{{format_math(data["q11"]["e"])}}} & \\oBaiTap[{ob11}]{{f) (0,5 điểm)}}{{{format_math(data["q11"]["f"])}}} \\\\
\\hline
\\end{{tabularx}}
\\newpage
'''
    # --- TRANG 2 ---
    p2 = f'''% =============================================================================
% ========================= MA DE {c} - MAT SAU (TRANG 2/2) ==============
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\centering\\textbf{{{t_p2} | Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent\\textbf{{Câu 12 (2,0 điểm). Tìm số nguyên $x$, biết:}}
\\vspace{{0.5mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{ob12_ab}]{{a) (0,5 điểm)}}{{{format_math(data["q12"]["a"])}}} & \\oBaiTap[{ob12_ab}]{{b) (0,5 điểm)}}{{{format_math(data["q12"]["b"])}}} \\\\
\\hline
\\oBaiTap[{ob12_cd}]{{c) (0,5 điểm)}}{{{format_math(data["q12"]["c"])}}} & \\oBaiTap[{ob12_cd}]{{d) (0,5 điểm)}}{{{data["q12"]["d"]}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.4mm}}
\\textbf{{Câu 13 (2,0 điểm).}} {data["q13"]["de"]}\\par\\vspace{{0.3mm}}
\\textbf{{a) (1,0 điểm)}} {data["q13"]["a"]}\\par\\vspace{{0.3mm}}
\\textbf{{b) (1,0 điểm)}} {data["q13"]["b"]}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk13}}}
\\\\ \\hline
\\end{{tabularx}}

\\vspace{{1.2mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.4mm}}
\\textbf{{Câu 14 (0,5 điểm).}} {data["q14"]["de"]}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{dk14}}}
\\\\ \\hline
\\end{{tabularx}}
'''
    content.append(p1)
    content.append(p2)
    content.append("\\end{document}\n")
    return "".join(content)

def check_pdf_margins(pdf_path):
    doc = pymupdf.open(pdf_path)
    margins = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
        gray = np.mean(img, axis=2) if pix.n >= 3 else img[:,:,0]
        non_white = np.where(gray < 250)
        if len(non_white[0]) > 0:
            last_y = np.max(non_white[0])
            m = ((pix.h - last_y) / 150.0) * 25.4
            margins.append(m)
        else:
            margins.append(0.0)
    doc.close()
    return margins

def main():
    base_name = data_05["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    # Cấu hình kiểm tra
    cfg = {"ob11": 7, "vsa": "0.10mm", "ob12_ab": 5, "ob12_cd": 6, "dk13": 9, "dk14": 8}
    
    print(f"Generating TeX for Ma 05 with config: {cfg}...")
    tex_content = build_tex(data_05, **cfg)
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
        
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"]
    print("Compiling pdflatex (run 1)...")
    subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Compiling pdflatex (run 2)...")
    subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    if not os.path.exists(pdf_path):
        print("Compilation error! Check log.")
        return
        
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    margins = check_pdf_margins(pdf_path)
    print(f"Total pages: {num_pages}")
    for idx, m in enumerate(margins):
        print(f"Page {idx+1:02d} (Mã 05 - Trang {idx+1}/2): bottom margin = {m:.2f} mm")
    
    # Render preview pngs
    doc = pymupdf.open(pdf_path)
    p1_path = os.path.join(CUR_DIR, "page_1_ma05.png")
    p2_path = os.path.join(CUR_DIR, "page_2_ma05.png")
    doc[0].get_pixmap(dpi=150).save(p1_path)
    doc[1].get_pixmap(dpi=150).save(p2_path)
    doc.close()
    print("Rendered page_1_ma05.png and page_2_ma05.png")
    
    # Copy to brain
    if os.path.exists(BRAIN_DIR):
        shutil.copy(p1_path, os.path.join(BRAIN_DIR, "page_1_ma05.png"))
        shutil.copy(p2_path, os.path.join(BRAIN_DIR, "page_2_ma05.png"))
        print("Copied preview images to brain artifact directory.")
        
    if num_pages == 2 and all(10.0 <= m <= 15.5 for m in margins):
        print(">>> SUCCESS: Exactly 2 pages and all margins within 10-15 mm! <<<")
    else:
        print("Review margin details above.")

if __name__ == "__main__":
    main()
