import os
import sys
import json
import re
import subprocess

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_ai_data():
    raw_path = os.path.join(BASE_DIR, "ai_raw_response.json")
    with open(raw_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    match = re.search(r"```(?:json)?(.*?)```", text, re.DOTALL)
    if match:
        text = match.group(1).strip()
    data = json.loads(text)
    
    # Cập nhật Câu 1 ý b về hệ phương trình bậc nhất hai ẩn thông thường (giải bằng phương pháp cộng đại số)
    data["codes"]["101"]["c1"]["b"] = r"\begin{cases} 3x + 2y = 7 \\ 2x + 3y = 8 \end{cases}"
    data["codes"]["102"]["c1"]["b"] = r"\begin{cases} 2x + 3y = 7 \\ 3x + 2y = 8 \end{cases}"
    data["codes"]["103"]["c1"]["b"] = r"\begin{cases} 3x + 4y = 10 \\ 2x + 3y = 7 \end{cases}"
    data["codes"]["104"]["c1"]["b"] = r"\begin{cases} 4x + 3y = 11 \\ 3x + 2y = 8 \end{cases}"
    
    return data

def get_solutions_markdown():
    return """## ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM CHI TIẾT

### PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (2,5 điểm)
*Mỗi câu trắc nghiệm đúng được 0,5 điểm.*

| Câu | Mã 101 | Mã 102 | Mã 103 | Mã 104 |
| :---: | :---: | :---: | :---: | :---: |
| **1** | A | B | C | D |
| **2** | B | C | D | A |
| **3** | C | D | A | B |
| **4** | D | A | B | C |
| **5** | A | B | C | D |

---

### PHẦN II. TỰ LUẬN (7,5 điểm)

#### **Câu 1 (2,5 điểm). Giải các hệ phương trình sau:**

**a) (1,25 điểm) Giải hệ phương trình cơ bản:**
* **Mã 101:** $\\begin{cases} 2x + y = 5 \\\\ x - y = 1 \\end{cases} \\Leftrightarrow \\begin{cases} 3x = 6 \\\\ y = x - 1 \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ y = 1 \\end{cases}$. Vậy nghiệm của hệ là $(x; y) = (2; 1)$.
* **Mã 102:** $\\begin{cases} 3x - y = 4 \\\\ x + y = 4 \\end{cases} \\Leftrightarrow \\begin{cases} 4x = 8 \\\\ y = 4 - x \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ y = 2 \\end{cases}$. Vậy nghiệm của hệ là $(x; y) = (2; 2)$.
* **Mã 103:** $\\begin{cases} x + 2y = 7 \\\\ 2x - y = 4 \\end{cases} \\Leftrightarrow \\begin{cases} x + 2y = 7 \\\\ 4x - 2y = 8 \\end{cases} \\Leftrightarrow \\begin{cases} 5x = 15 \\\\ y = 2x - 4 \\end{cases} \\Leftrightarrow \\begin{cases} x = 3 \\\\ y = 2 \\end{cases}$. Vậy nghiệm của hệ là $(x; y) = (3; 2)$.
* **Mã 104:** $\\begin{cases} 2x - 3y = 1 \\\\ x + 3y = 14 \\end{cases} \\Leftrightarrow \\begin{cases} 3x = 15 \\\\ 3y = 14 - x \\end{cases} \\Leftrightarrow \\begin{cases} x = 5 \\\\ y = 3 \\end{cases}$. Vậy nghiệm của hệ là $(x; y) = (5; 3)$.

*Biểu điểm câu 1a:*
- Biến đổi nhân hệ số/cộng đại số triệt tiêu 1 ẩn: 0,5đ
- Tìm được ẩn thứ nhất: 0,5đ
- Tìm được ẩn thứ hai và kết luận nghiệm: 0,25đ

**b) (1,25 điểm) Giải hệ phương trình bằng phương pháp cộng đại số:**
* **Mã 101:** $\\begin{cases} 3x + 2y = 7 \\\\ 2x + 3y = 8 \\end{cases} \\Leftrightarrow \\begin{cases} 6x + 4y = 14 \\\\ 6x + 9y = 24 \\end{cases} \\Leftrightarrow \\begin{cases} 5y = 10 \\\\ 3x + 2y = 7 \\end{cases} \\Leftrightarrow \\begin{cases} y = 2 \\\\ x = 1 \\end{cases}$.  
  Vậy nghiệm duy nhất của hệ là $(x; y) = (1; 2)$.
* **Mã 102:** $\\begin{cases} 2x + 3y = 7 \\\\ 3x + 2y = 8 \\end{cases} \\Leftrightarrow \\begin{cases} 6x + 9y = 21 \\\\ 6x + 4y = 16 \\end{cases} \\Leftrightarrow \\begin{cases} 5y = 5 \\\\ 2x + 3y = 7 \\end{cases} \\Leftrightarrow \\begin{cases} y = 1 \\\\ x = 2 \\end{cases}$.  
  Vậy nghiệm duy nhất của hệ là $(x; y) = (2; 1)$.
* **Mã 103:** $\\begin{cases} 3x + 4y = 10 \\\\ 2x + 3y = 7 \\end{cases} \\Leftrightarrow \\begin{cases} 6x + 8y = 20 \\\\ 6x + 9y = 21 \\end{cases} \\Leftrightarrow \\begin{cases} y = 1 \\\\ 2x + 3y = 7 \\end{cases} \\Leftrightarrow \\begin{cases} y = 1 \\\\ x = 2 \\end{cases}$.  
  Vậy nghiệm duy nhất của hệ là $(x; y) = (2; 1)$.
* **Mã 104:** $\\begin{cases} 4x + 3y = 11 \\\\ 3x + 2y = 8 \\end{cases} \\Leftrightarrow \\begin{cases} 8x + 6y = 22 \\\\ 9x + 6y = 24 \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ 3x + 2y = 8 \\end{cases} \\Leftrightarrow \\begin{cases} x = 2 \\\\ y = 1 \\end{cases}$.  
  Vậy nghiệm duy nhất của hệ là $(x; y) = (2; 1)$.

*Biểu điểm câu 1b:*
- Nhân hai vế các phương trình với hệ số thích hợp để đồng nhất hệ số: 0,25đ
- Trừ/cộng từng vế để tìm ẩn thứ nhất: 0,5đ
- Thay vào tìm ẩn thứ hai: 0,25đ
- Kết luận nghiệm: 0,25đ

---

#### **Câu 2 (2,5 điểm). Rút gọn các biểu thức phân thức chứa căn bậc hai:**

**a) (1,25 điểm) Rút gọn biểu thức A:**
* **Mã 101:** $A = \\dfrac{2\\sqrt{x}+6}{x-9} + \\dfrac{2}{\\sqrt{x}-3} = \\dfrac{2(\\sqrt{x}+3)}{(\\sqrt{x}-3)(\\sqrt{x}+3)} + \\dfrac{2}{\\sqrt{x}-3} = \\dfrac{2}{\\sqrt{x}-3} + \\dfrac{2}{\\sqrt{x}-3} = \\dfrac{4}{\\sqrt{x}-3}$.
* **Mã 102:** $A = \\dfrac{3\\sqrt{x}+12}{x-16} + \\dfrac{2}{\\sqrt{x}-4} = \\dfrac{3(\\sqrt{x}+4)}{(\\sqrt{x}-4)(\\sqrt{x}+4)} + \\dfrac{2}{\\sqrt{x}-4} = \\dfrac{3}{\\sqrt{x}-4} + \\dfrac{2}{\\sqrt{x}-4} = \\dfrac{5}{\\sqrt{x}-4}$.
* **Mã 103:** $A = \\dfrac{4\\sqrt{x}+20}{x-25} + \\dfrac{3}{\\sqrt{x}-5} = \\dfrac{4(\\sqrt{x}+5)}{(\\sqrt{x}-5)(\\sqrt{x}+5)} + \\dfrac{3}{\\sqrt{x}-5} = \\dfrac{4}{\\sqrt{x}-5} + \\dfrac{3}{\\sqrt{x}-5} = \\dfrac{7}{\\sqrt{x}-5}$.
* **Mã 104:** $A = \\dfrac{5\\sqrt{x}+10}{x-4} + \\dfrac{4}{\\sqrt{x}-2} = \\dfrac{5(\\sqrt{x}+2)}{(\\sqrt{x}-2)(\\sqrt{x}+2)} + \\dfrac{4}{\\sqrt{x}-2} = \\dfrac{5}{\\sqrt{x}-2} + \\dfrac{4}{\\sqrt{x}-2} = \\dfrac{9}{\\sqrt{x}-2}$.

*Biểu điểm câu 2a:*
- Đổi dấu phân thức thứ hai và nhận dạng mẫu thức: 0,5đ
- Rút gọn phân thức thứ nhất hoặc quy đồng mẫu thức chung: 0,5đ
- Kết quả thu gọn cuối cùng: 0,25đ

**b) (1,25 điểm) Rút gọn biểu thức B:**
* **Mã 101:** $B = \\dfrac{\\sqrt{x}-2 + \\sqrt{x}+2 + \\sqrt{x}-6}{(\\sqrt{x}-2)(\\sqrt{x}+2)} = \\dfrac{3\\sqrt{x}-6}{(\\sqrt{x}-2)(\\sqrt{x}+2)} = \\dfrac{3(\\sqrt{x}-2)}{(\\sqrt{x}-2)(\\sqrt{x}+2)} = \\dfrac{3}{\\sqrt{x}+2}$.
* **Mã 102:** $B = \\dfrac{2(\\sqrt{x}-3) + 2(\\sqrt{x}+3) + \\sqrt{x}-15}{(\\sqrt{x}-3)(\\sqrt{x}+3)} = \\dfrac{5\\sqrt{x}-15}{(\\sqrt{x}-3)(\\sqrt{x}+3)} = \\dfrac{5(\\sqrt{x}-3)}{(\\sqrt{x}-3)(\\sqrt{x}+3)} = \\dfrac{5}{\\sqrt{x}+3}$.
* **Mã 103:** $B = \\dfrac{3(\\sqrt{x}-1) + 3(\\sqrt{x}+1) + \\sqrt{x}-7}{(\\sqrt{x}-1)(\\sqrt{x}+1)} = \\dfrac{7\\sqrt{x}-7}{(\\sqrt{x}-1)(\\sqrt{x}+1)} = \\dfrac{7(\\sqrt{x}-1)}{(\\sqrt{x}-1)(\\sqrt{x}+1)} = \\dfrac{7}{\\sqrt{x}+1}$.
* **Mã 104:** $B = \\dfrac{4(\\sqrt{x}-4) + 4(\\sqrt{x}+4) + \\sqrt{x}-36}{(\\sqrt{x}-4)(\\sqrt{x}+4)} = \\dfrac{9\\sqrt{x}-36}{(\\sqrt{x}-4)(\\sqrt{x}+4)} = \\dfrac{9(\\sqrt{x}-4)}{(\\sqrt{x}-4)(\\sqrt{x}+4)} = \\dfrac{9}{\\sqrt{x}+4}$.

*Biểu điểm câu 2b:*
- Quy đồng mẫu thức chung đúng: 0,5đ
- Phá ngoặc và rút gọn trên tử thức: 0,5đ
- Phân tích tử thành nhân tử và rút gọn ra kết quả tối giản: 0,25đ

---

#### **Câu 3 (2,5 điểm). Bài toán thực tế hình học khu vườn:**
*Gọi chiều rộng ban đầu của khu vườn là $x$ (m), ĐK: $x > 0$. Chiều dài của khu vườn là $x + d$ (m).*  
*Diện tích khu vườn là $S$ m$^2$ nên ta có phương trình: $x(x + d) = S \\Leftrightarrow x^2 + dx - S = 0$.*

**a) (1,5 điểm) Tìm chiều dài và chiều rộng ban đầu:**
* **Mã 101:** $x(x+5) = 150 \\Leftrightarrow x^2 + 5x - 150 = 0 \\Rightarrow x = 10$ (TM), $x = -15$ (Loại).  
  Vậy chiều rộng là $10$ m, chiều dài là $15$ m.
* **Mã 102:** $x(x+4) = 96 \\Leftrightarrow x^2 + 4x - 96 = 0 \\Rightarrow x = 8$ (TM), $x = -12$ (Loại).  
  Vậy chiều rộng là $8$ m, chiều dài là $12$ m.
* **Mã 103:** $x(x+6) = 112 \\Leftrightarrow x^2 + 6x - 112 = 0 \\Rightarrow x = 8$ (TM), $x = -14$ (Loại).  
  Vậy chiều rộng là $8$ m, chiều dài là $14$ m.
* **Mã 104:** $x(x+7) = 144 \\Leftrightarrow x^2 + 7x - 144 = 0 \\Rightarrow x = 9$ (TM), $x = -16$ (Loại).  
  Vậy chiều rộng là $9$ m, chiều dài là $16$ m.

*Biểu điểm câu 3a:*
- Chọn ẩn, đặt điều kiện và đơn vị: 0,25đ
- Biểu diễn chiều dài và lập phương trình: 0,5đ
- Giải phương trình và chọn nghiệm thích hợp: 0,5đ
- Kết luận kích thước ban đầu: 0,25đ

**b) (1,0 điểm) Chiều dài bờ tường cần xây:**
*Công thức: Chiều dài bờ tường = Chu vi khu vườn - Độ rộng cổng = $2 \\times (\\text{Dài} + \\text{Rộng}) - w$.*
* **Mã 101:** Chu vi = $2 \\times (10 + 15) = 50$ (m). Chiều dài bờ tường = $50 - 2 = 48$ (m).
* **Mã 102:** Chu vi = $2 \\times (8 + 12) = 40$ (m). Chiều dài bờ tường = $40 - 3 = 37$ (m).
* **Mã 103:** Chu vi = $2 \\times (8 + 14) = 44$ (m). Chiều dài bờ tường = $44 - 4 = 40$ (m).
* **Mã 104:** Chu vi = $2 \\times (9 + 16) = 50$ (m). Chiều dài bờ tường = $50 - 5 = 45$ (m).

*Biểu điểm câu 3b:*
- Tính đúng chu vi: 0,5đ
- Trừ cổng và kết luận chiều dài tường: 0,5đ
"""

def generate_tex(data, c1_lines=16, c2_lines=14, c3_lines=14):
    tex = []
    tex.append(r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{tikz}
\usepackage{xcolor}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{geometry}
\usepackage[dethi]{ex_test}

\setlength{\parskip}{0pt}
\setlength{\parindent}{0pt}

% Dòng kẻ chấm mờ đều đặn chuẩn viết tay (khoảng cách 20.5pt)
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=20.5pt%
  \vspace{1.5mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!60}\dotfill}\par%
  }%
  \vspace{1mm}%
  \endgroup%
}

% Định nghĩa ô bài tập tự luận trong bảng
\newcommand{\oBaiTap}[3][6]{%
  \vspace{1.5mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

% Câu trắc nghiệm 1 cột: 4 đáp án dàn hàng ngang trên 1 dòng
\newcommand{\cauTN}[6]{% \cauTN{số câu}{đề}{A}{B}{C}{D}
  \noindent\textbf{Câu #1.} #2\par\vspace{0.4mm}%
  \noindent%
  \makebox[0.25\linewidth][l]{\textbf{A.} #3}%
  \makebox[0.25\linewidth][l]{\textbf{B.} #4}%
  \makebox[0.25\linewidth][l]{\textbf{C.} #5}%
  \makebox[0.25\linewidth][l]{\textbf{D.} #6}\par\vspace{0.8mm}%
}

% Câu trắc nghiệm 2 dòng: mỗi dòng 2 đáp án (dành cho câu có đáp án dài)
\newcommand{\cauTNB}[6]{% \cauTNB{số câu}{đề}{A}{B}{C}{D}
  \noindent\textbf{Câu #1.} #2\par\vspace{0.4mm}%
  \noindent%
  \makebox[0.5\linewidth][l]{\textbf{A.} #3}%
  \makebox[0.5\linewidth][l]{\textbf{B.} #4}\par\vspace{0.4mm}%
  \noindent%
  \makebox[0.5\linewidth][l]{\textbf{C.} #5}%
  \makebox[0.5\linewidth][l]{\textbf{D.} #6}\par\vspace{0.8mm}%
}

\begin{document}
\pagestyle{empty}
""")

    codes = ["101", "102", "103", "104"]
    for idx, code in enumerate(codes):
        cdata = data["codes"][code]
        
        # --- TRANG 1/2 (MẶT TRƯỚC) ---
        tex.append(f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 05 - BUỔI 01: MÃ ĐỀ {code} =============
% ========================= MẶT TRƯỚC (TRANG 1/2) ==============================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 05 - BUỔI 01}} & \\textbf{{Mã đề: {code} - Trang 1/2}} \\\\
\\textit{{Chủ đề: Hệ phương trình \\& Rút gọn phân thức chứa căn bậc hai}} & \\textit{{Thời gian: 45 phút}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\rule[-3.5mm]{{0pt}}{{10mm}}\\textbf{{Họ và tên học sinh:}} \\hfill \\textbf{{Mã HS:}} \\makebox[3.5cm]{{\\dotfill}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{1mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.8cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{2mm}}

\\noindent\\textbf{{\\large PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (2,5 điểm)}} \\hfill \\textit{{(Khoanh tròn đáp án đúng)}}\\par
\\vspace{{1mm}}
""")
        # 5 câu trắc nghiệm
        for q_idx, q in enumerate(cdata["mcq"], 1):
            q_text = q["q"]
            opt_a = q["A"]
            opt_b = q["B"]
            opt_c = q["C"]
            opt_d = q["D"]
            if len(opt_a) > 25 or "so sánh" in q_text.lower():
                tex.append(f"\\cauTNB{{{q_idx}}}{{{q_text}}}{{{opt_a}}}{{{opt_b}}}{{{opt_c}}}{{{opt_d}}}\n")
            else:
                tex.append(f"\\cauTN{{{q_idx}}}{{{q_text}}}{{{opt_a}}}{{{opt_b}}}{{{opt_c}}}{{{opt_d}}}\n")

        tex.append(f"""\\vspace{{1.5mm}}

\\noindent\\textbf{{\\large PHẦN II. TỰ LUẬN (7,5 điểm)}}

\\noindent\\textbf{{Câu 1 (2,5 điểm). Giải các hệ phương trình sau:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{c1_lines}]{{a)}}{{${cdata["c1"]["a"]}$}} & 
\\oBaiTap[{c1_lines}]{{b)}}{{${cdata["c1"]["b"]}$}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
""")

        # --- TRANG 2/2 (MẶT SAU) ---
        c3_text = cdata["c3"]["text"]
        c3_sa = cdata["c3"]["sub_a"]
        c3_sb = cdata["c3"]["sub_b"]

        def fmt_c2(raw):
            for delimiter in [r"\quad \text{với }", r"\text{với }"]:
                if delimiter in raw:
                    p1, p2 = raw.split(delimiter, 1)
                    return f"${p1.strip()}$\\par\\vspace{{0.5mm}}\\textit{{(với ${p2.strip()}$)}}"
            return f"${raw}$"

        c2_a_str = fmt_c2(cdata["c2"]["a"])
        c2_b_str = fmt_c2(cdata["c2"]["b"])

        tex.append(f"""% =============================================================================
% ========================= TOÁN 9 - TUẦN 05 - BUỔI 01: MÃ ĐỀ {code} =============
% ========================= MẶT SAU (TRANG 2/2) ================================
% =============================================================================

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{PHẦN II. TỰ LUẬN (Tiếp theo) - TOÁN 9 TUẦN 05 BUỔI 01}} & \\textbf{{Mã đề: {code} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{2.5mm}}

\\noindent\\textbf{{\\large Câu 2 (2,5 điểm). Rút gọn các biểu thức phân thức chứa căn sau:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTap[{c2_lines}]{{a)}}{{{c2_a_str}}} & 
\\oBaiTap[{c2_lines}]{{b)}}{{{c2_b_str}}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{2.5mm}}

\\noindent\\textbf{{\\large Câu 3 (2,5 điểm). Bài toán thực tế hình học khu vườn (Trích Đề 25):}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|}}
\\hline
\\vspace{{0.5mm}}
{c3_text}\\par
\\vspace{{0.5mm}}
$a)$ {c3_sa}\\par
$b)$ {c3_sb}\\par
\\vspace{{0.4mm}}
\\noindent\\textit{{Bài giải:}}\\dongke{{{c3_lines}}}
\\\\ \\hline
\\end{{tabularx}}
""")
        if idx < len(codes) - 1:
            tex.append("\n\\newpage\n")

    tex.append("\n\\end{document}\n")
    return "".join(tex)

def get_page_count(log_file):
    if not os.path.exists(log_file):
        return None
    with open(log_file, "r", encoding="latin-1") as f:
        content = f.read()
    match = re.search(r"Output written on .*?\((\d+)\s+pages?", content)
    if match:
        return int(match.group(1))
    return None

def compile_tex(tex_path):
    cmd = ["pdflatex", "-interaction=nonstopmode", os.path.basename(tex_path)]
    res = subprocess.run(cmd, cwd=os.path.dirname(tex_path), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    log_path = tex_path.replace(".tex", ".log")
    return get_page_count(log_path)

def main():
    data = load_ai_data()
    
    # Save solution markdown
    md_path = os.path.join(BASE_DIR, "DAP_AN_VA_THANG_DIEM.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# BAREM ĐÁP ÁN & THANG ĐIỂM CHI TIẾT (MÃ ĐỀ: 101, 102, 103, 104)\n")
        f.write("## MÔN TOÁN 9 - TUẦN 05 - BUỔI 01\n")
        f.write("### CHỦ ĐỀ: HỆ PHƯƠNG TRÌNH & RÚT GỌN PHÂN THỨC CHỨA CĂN BẬC HAI\n\n---\n\n")
        f.write(get_solutions_markdown())
    print(f"Đã cập nhật Barem vào {md_path}")

    tex_path = os.path.join(BASE_DIR, "Phieu_Kiem_Tra_Tuan_05_Buoi_01.tex")
    
    # Tìm thông số dòng kẻ tối ưu sao cho:
    # 1. Số dòng ở Câu 2 và Câu 3 được tối đa hóa
    # 2. Không bị tràn trang (chính xác 8 trang)
    best_c1 = 15
    best_c2 = 14
    best_c3 = 14
    
    configs = [
        (16, 14, 15),
        (16, 14, 14),
        (15, 14, 14),
        (15, 13, 14),
        (15, 13, 13),
        (14, 13, 13),
        (14, 12, 12),
        (13, 11, 11),
    ]
    
    for c1, c2, c3 in configs:
        print(f"Thử nghiệm biên dịch với (c1={c1}, c2={c2}, c3={c3})...")
        tex_content = generate_tex(data, c1_lines=c1, c2_lines=c2, c3_lines=c3)
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex_content)
        pages = compile_tex(tex_path)
        print(f"-> Số trang: {pages}")
        if pages == 8:
            print(f"===> ĐẠT CHUẨN XÁC 8 TRANG với cấu hình tối ưu: c1={c1}, c2={c2}, c3={c3}!")
            best_c1, best_c2, best_c3 = c1, c2, c3
            break

if __name__ == "__main__":
    main()
