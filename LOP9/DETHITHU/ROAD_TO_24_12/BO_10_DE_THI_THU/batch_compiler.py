import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

def compile_and_check(folder, tex_exam_name, tex_sol_name):
    cmd_e = ['pdflatex', '-interaction=nonstopmode', tex_exam_name]
    subprocess.run(cmd_e, cwd=folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    cmd_s = ['pdflatex', '-interaction=nonstopmode', tex_sol_name]
    subprocess.run(cmd_s, cwd=folder, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    pdf_e = os.path.join(folder, tex_exam_name.replace('.tex', '.pdf'))
    pdf_s = os.path.join(folder, tex_sol_name.replace('.tex', '.pdf'))
    
    p_e = len(fitz.open(pdf_e)) if os.path.exists(pdf_e) else 0
    p_s = len(fitz.open(pdf_s)) if os.path.exists(pdf_s) else 0
    return p_e, p_s

print("Batch compiler loaded.")
