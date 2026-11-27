import os
import subprocess
import fitz

BASE_DIR = r'd:/GitHub/SOANBAI-main/LOP9/DETHITHU/ROAD_TO_24_12/BO_10_DE_THI_THU'

def compile_pdf(tex_path, cwd):
    cmd = ['pdflatex', '-interaction=nonstopmode', os.path.basename(tex_path)]
    p = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return p.returncode == 0

print("Ready to generate exams!")
