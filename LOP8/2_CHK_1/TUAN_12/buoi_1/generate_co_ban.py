import json
import os
import shutil
import subprocess
import pypdf
import pymupdf
import numpy as np
from PIL import Image

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
BRAIN_DIR = r"C:\Users\Admin\.gemini\antigravity\brain\0c8f089e-0c5d-4300-ba60-02f73af7a436"

def load_data():
    json_path = os.path.join(CUR_DIR, 'data_de_co_ban.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_tex(data, ob1=5, ob2=6, vspace_p1="2.6mm", vspace_p2="1.4mm", vspace_item1="1.6mm", vspace_item2="0.6mm"):
    t_p1 = data["title_p1"]
    t_p2 = data["title_p2"]
    codes = data["codes"]
    
    preamble = f'''\\documentclass[12pt,a4paper]{{article}}
\\usepackage[utf8]{{vietnam}}
\\usepackage{{amsmath,amssymb}}
\\usepackage{{tabularx}}
\\usepackage{{tikz}}
\\usepackage{{xcolor}}
\\usepackage[top=0.6cm, bottom=0.6cm, left=0.6cm, right=0.6cm]{{geometry}}
\\usepackage[dethi]{{ex_test}}

\\setlength{{\\parskip}}{{0pt}}

% Dong ke cham mo chuan viet tay
\\newcommand{{\\dongke}}[1]{{%
  \\begingroup%
  \\setlength{{\\parskip}}{{0pt}}%
  \\baselineskip=18.5pt%
  \\vspace{{1.0mm}}%
  \\foreach \\i in {{1,...,#1}}{{%
    \\noindent{{\\color{{gray!60}}\\dotfill}}\\par%
  }}%
  \\vspace{{0.6mm}}%
  \\endgroup%
}}

% Dinh nghia o bai tap tu luan trong bang cho Trang 1 va Trang 2
\\newcommand{{\\oBaiTapMot}}[3][5]{{%
  \\vspace{{{vspace_item1}}}%
  \\noindent\\textbf{{#2}} #3\\par%
  \\dongke{{#1}}%
}}
\\newcommand{{\\oBaiTapHai}}[3][6]{{%
  \\vspace{{{vspace_item2}}}%
  \\noindent\\textbf{{#2}} #3\\par%
  \\dongke{{#1}}%
}}

\\begin{{document}}
\\pagestyle{{empty}}
'''

    content = [preamble]
    code_list = list(codes.keys())
    
    for idx, c in enumerate(code_list):
        cd = codes[c]
        q1 = cd["q1"]
        q2 = cd["q2"]
        
        # --- TRANG 1 ---
        p1 = f'''% =============================================================================
% ========================= MA DE {c} - TRANG 1/2 =============================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p1}}} & \\textbf{{Mã đề: {c} - Trang 1/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{{vspace_p1}}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|p{{3.2cm}}|X|}}
\\hline
\\centering\\textbf{{ĐIỂM SỐ}} & \\centering\\textbf{{LỜI NHẬN XÉT CỦA THẦY CÔ}} \\tabularnewline
\\hline
\\rule{{0pt}}{{1.8cm}} & \\tabularnewline
\\hline
\\end{{tabularx}}

\\vspace{{{vspace_p1}}}
\\noindent\\textbf{{Bài 1 (5,0 điểm). Rút gọn các phân thức đại số sau:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTapMot[{ob1}]{{a) (0,5 điểm)}}{{{q1["a"]}}} & 
\\oBaiTapMot[{ob1}]{{b) (0,5 điểm)}}{{{q1["b"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{c) (0,5 điểm)}}{{{q1["c"]}}} & 
\\oBaiTapMot[{ob1}]{{d) (0,5 điểm)}}{{{q1["d"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{e) (0,5 điểm)}}{{{q1["e"]}}} & 
\\oBaiTapMot[{ob1}]{{f) (0,5 điểm)}}{{{q1["f"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{g) (0,5 điểm)}}{{{q1["g"]}}} & 
\\oBaiTapMot[{ob1}]{{h) (0,5 điểm)}}{{{q1["h"]}}} \\\\
\\hline
\\oBaiTapMot[{ob1}]{{i) (0,5 điểm)}}{{{q1["i"]}}} & 
\\oBaiTapMot[{ob1}]{{j) (0,5 điểm)}}{{{q1["j"]}}} \\\\
\\hline
\\end{{tabularx}}

\\newpage
'''
        # --- TRANG 2 ---
        p2 = f'''% =============================================================================
% ========================= MA DE {c} - TRANG 2/2 =============================
% =============================================================================
\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|c|}}
\\hline
\\textbf{{{t_p2}}} & \\textbf{{Mã đề: {c} - Trang 2/2}} \\\\
\\hline
\\end{{tabularx}}

\\vspace{{{vspace_p2}}}
\\noindent\\textbf{{Bài 2 (5,0 điểm). Rút gọn các phân thức đại số sau:}}
\\vspace{{0.8mm}}

\\noindent
\\begin{{tabularx}}{{\\linewidth}}{{|X|X|}}
\\hline
\\oBaiTapHai[{ob2}]{{a) (0,5 điểm)}}{{{q2["a"]}}} & 
\\oBaiTapHai[{ob2}]{{b) (0,5 điểm)}}{{{q2["b"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{c) (0,5 điểm)}}{{{q2["c"]}}} & 
\\oBaiTapHai[{ob2}]{{d) (0,5 điểm)}}{{{q2["d"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{e) (0,5 điểm)}}{{{q2["e"]}}} & 
\\oBaiTapHai[{ob2}]{{f) (0,5 điểm)}}{{{q2["f"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{g) (0,5 điểm)}}{{{q2["g"]}}} & 
\\oBaiTapHai[{ob2}]{{h) (0,5 điểm)}}{{{q2["h"]}}} \\\\
\\hline
\\oBaiTapHai[{ob2}]{{i) (0,5 điểm)}}{{{q2["i"]}}} & 
\\oBaiTapHai[{ob2}]{{j) (0,5 điểm)}}{{{q2["j"]}}} \\\\
\\hline
\\end{{tabularx}}
'''
        if idx < len(code_list) - 1:
            p2 += "\n\\newpage\n"
        
        content.append(p1)
        content.append(p2)
        
    content.append("\\end{document}\n")
    return "".join(content)

def check_margins(pdf_path):
    doc = pymupdf.open(pdf_path)
    
    margins = []
    for page_idx in range(min(2, len(doc))):
        pix = doc[page_idx].get_pixmap(dpi=150)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples).convert("L")
        arr = np.array(img)
        h, w = arr.shape
        non_white = np.where(arr < 250)[0]
        if len(non_white) > 0:
            last_row = non_white[-1]
            margin_bottom_px = h - last_row
            margin_bottom_mm = (margin_bottom_px / 150) * 25.4
            margins.append(margin_bottom_mm)
            
    # Render preview images
    p1_path = os.path.join(CUR_DIR, "page_co_ban_1.png")
    p2_path = os.path.join(CUR_DIR, "page_co_ban_2.png")
    doc[0].get_pixmap(dpi=150).save(p1_path)
    doc[1].get_pixmap(dpi=150).save(p2_path)
    
    if os.path.exists(BRAIN_DIR):
        shutil.copy(p1_path, os.path.join(BRAIN_DIR, "page_co_ban_1.png"))
        shutil.copy(p2_path, os.path.join(BRAIN_DIR, "page_co_ban_2.png"))
        
    return margins

def run_pdflatex(base_name):
    cmd = ["pdflatex", "-interaction=nonstopmode", f"{base_name}.tex"]
    subprocess.run(cmd, cwd=CUR_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    data = load_data()
    base_name = data["base_filename"]
    tex_path = os.path.join(CUR_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(CUR_DIR, f"{base_name}.pdf")
    
    candidates = [
        # (ob1, ob2, vp1, vp2, vi1, vi2)
        (5, 6, "2.6mm", "1.4mm", "1.6mm", "0.6mm"),
        (5, 6, "2.4mm", "1.2mm", "1.5mm", "0.6mm"),
        (5, 6, "2.2mm", "1.0mm", "1.6mm", "0.5mm"),
        (5, 6, "2.8mm", "1.5mm", "1.7mm", "0.7mm"),
        (5, 6, "2.5mm", "1.3mm", "1.6mm", "0.6mm"),
    ]
    
    best_config = None
    best_margins = None
    best_score = float('inf')
    
    for cfg in candidates:
        ob1, ob2, vp1, vp2, vi1, vi2 = cfg
        print(f"\n--- Testing config: ob1={ob1}, ob2={ob2}, vp1={vp1}, vp2={vp2}, vi1={vi1}, vi2={vi2} ---")
        tex_content = build_tex(data, ob1=ob1, ob2=ob2, vspace_p1=vp1, vspace_p2=vp2, vspace_item1=vi1, vspace_item2=vi2)
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(tex_content)
            
        run_pdflatex(base_name)
        
        if os.path.exists(pdf_path):
            try:
                reader = pypdf.PdfReader(pdf_path)
                num_pages = len(reader.pages)
                print(f"-> Result: {num_pages} pages")
                if num_pages == 8:
                    margins = check_margins(pdf_path)
                    if len(margins) == 2:
                        score = sum(abs(m - 12.5) for m in margins)
                        print(f"-> Margins: Page 1 = {margins[0]:.2f} mm, Page 2 = {margins[1]:.2f} mm (score={score:.2f})")
                        if all(10.0 <= m <= 15.0 for m in margins):
                            print(f">>> PERFECT! Margins {margins} within [10.0, 15.0] mm!")
                            return
                        if score < best_score:
                            best_score = score
                            best_config = cfg
                            best_margins = margins
            except Exception as e:
                print(f"Error checking pdf: {e}")
                
    if best_config:
        print(f"\n>>> Applying best found config: {best_config} with margins {best_margins}")
        ob1, ob2, vp1, vp2, vi1, vi2 = best_config
        tex_content = build_tex(data, ob1=ob1, ob2=ob2, vspace_p1=vp1, vspace_p2=vp2, vspace_item1=vi1, vspace_item2=vi2)
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(tex_content)
        run_pdflatex(base_name)
        check_margins(pdf_path)

if __name__ == "__main__":
    main()
