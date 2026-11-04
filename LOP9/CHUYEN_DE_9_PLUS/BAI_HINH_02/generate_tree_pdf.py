import os
import subprocess

def create_tree_tex(tex_path):
    tex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{geometry}
\geometry{a4paper, top=0.9cm, bottom=0.9cm, left=0.9cm, right=0.9cm}
\usepackage{tikz}
\usetikzlibrary{calc, positioning, shapes.geometric, arrows.meta, shadows}

\pagestyle{empty}

\begin{document}

\begin{center}
    {\LARGE\bfseries\color{blue!85!black} SƠ ĐỒ TƯ DUY NGƯỢC HÌNH CÂY THÔNG (PINE-TREE MINDMAP)}\\[2mm]
    {\large\bfseries\color{red!80!black} BẺ KHÓA Ý PHÂN HÓA 9+: TÌM VỊ TRÍ $A$ ĐỂ $DH \cdot DA$ LỚN NHẤT}\\[1.5mm]
    {\small\color{gray!80!black}\textit{(Dữ liệu thuần công thức logic toán học $\bullet$ Trích xuất từ Đề 02 / Tuyển tập 55 Đề Vào Lớp 10)}}
\end{center}

\vspace{3mm}

\begin{center}
\begin{tikzpicture}[
    x=1cm, y=1cm,
    font=\small,
    >=Stealth,
    arr_main/.style={-{Stealth[length=4.5mm, width=3mm]}, line width=1.8pt, red!85!black},
    arr_sub/.style={-{Stealth[length=4mm, width=2.6mm]}, line width=1.5pt, blue!75!black},
    arr_root/.style={-{Stealth[length=4.2mm, width=2.8mm]}, line width=1.6pt, teal!85!black},
    % Styles for nodes
    target_node/.style={
        rectangle, draw=red!85!black, fill=red!15, line width=1.5pt, rounded corners=3mm,
        inner sep=7pt, align=center, text width=11.2cm, drop shadow={opacity=0.2}
    },
    step_node/.style={
        rectangle, draw=blue!80!black, fill=blue!8, line width=1.1pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=13.0cm, drop shadow={opacity=0.15}
    },
    aux_node/.style={
        rectangle, draw=orange!90!black, fill=orange!12, line width=1.4pt, rounded corners=2.5mm,
        inner sep=7pt, align=center, text width=15.0cm, drop shadow={opacity=0.16}
    },
    core_node/.style={
        rectangle, draw=blue!85!black, fill=blue!10, line width=1.2pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=16.0cm, drop shadow={opacity=0.15}
    },
    branch_node/.style={
        rectangle, draw=purple!80!black, fill=purple!8, line width=1.2pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=8.2cm, drop shadow={opacity=0.14}
    },
    sim_node/.style={
        rectangle, draw=blue!85!black, fill=blue!8, line width=1.2pt, rounded corners=2.5mm,
        inner sep=7pt, align=center, text width=16.8cm, drop shadow={opacity=0.16}
    },
    base_node/.style={
        rectangle, draw=teal!95!black, fill=teal!22, line width=1.6pt, rounded corners=3.5mm,
        inner sep=8pt, align=center, text width=18.0cm, drop shadow={opacity=0.22}
    }
]

% ================= LEVEL 1: ĐỈNH CÂY THÔNG (ĐÍCH ĐẾN CỰC TRỊ) =================
\node[target_node] (N1) at (0, 0) {
    \textbf{\Large\color{red!85!black} [ĐÍCH ĐẾN]:\ $\max(DH \cdot DA) = \dfrac{BC^2}{4}$}\\[1mm]
    $\boldsymbol{\iff A \text{ LÀ ĐIỂM CHÍNH GIỮA CỦA CUNG LỚN } BC}$
};

% ================= LEVEL 2: ĐIỀU KIỆN DẤU BẰNG =================
\node[step_node] (N2) at (0, -2.3) {
    $\boldsymbol{\Uparrow} \quad \text{Dấu “=” xảy ra} \iff \boldsymbol{DB = DC} \iff D \equiv I \iff \boldsymbol{\triangle ABC \text{ cân tại } A}$
};

% ================= LEVEL 3: BẤT ĐẲNG THỨC CAUCHY =================
\node[aux_node] (N3) at (0, -4.6) {
    $\boldsymbol{\Uparrow} \quad \text{\textbf{BẤT ĐẲNG THỨC CAUCHY:}}\quad \boldsymbol{DB \cdot DC \le \left(\dfrac{DB+DC}{2}\right)^2 = \left(\dfrac{BC}{2}\right)^2 = \dfrac{BC^2}{4}}$\\[1mm]
    \textit{(Dây cung $BC$ cố định $\implies \dfrac{BC^2}{4}$ là hằng số không đổi)}
};

% ================= LEVEL 4: PHƯƠNG TÍCH & ĐỐI XỨNG =================
\node[core_node] (N4) at (0, -7.0) {
    $\boldsymbol{\Uparrow} \quad \text{Quy đổi tích biến thiên về tích cố định:}\quad \boldsymbol{DH \cdot DA = DK \cdot DA = DB \cdot DC}$
};

% ================= LEVEL 5: TÁCH 2 CÀNH THÔNG (PHƯƠNG TÍCH & TRUNG TRỰC) =================
\node[branch_node] (N5_left) at (-4.7, -9.8) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- PHƯƠNG TÍCH]:}\\[1mm]
    $\boldsymbol{\triangle DBK \sim \triangle DAC \text{ (g-g)}}$\\[1mm]
    $\left(\widehat{BDK}=\widehat{ADC}=90^\circ,\ \widehat{BKD}=\widehat{ACD}\right)$\\[1mm]
    $\boldsymbol{\implies DK \cdot DA = DB \cdot DC}$
};

\node[branch_node] (N5_right) at (4.7, -9.8) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- TÍNH CHẤT ĐỐI XỨNG]:}\\[1mm]
    $\boldsymbol{\triangle HBK \text{ cân tại } B}$\\[1mm]
    $\left(BD \text{ vừa là đường cao, vừa là phân giác}\right)$\\[1mm]
    $\boldsymbol{\implies BD \text{ là trung trực } HK \implies DH = DK}$
};

% ================= LEVEL 6: SO SÁNH GÓC GỐC =================
\node[sim_node] (N6) at (0, -13.0) {
    $\boldsymbol{\Uparrow} \quad \text{Phân giác góc:}\quad \boldsymbol{\widehat{HBD} = \widehat{KBD} = \widehat{KAC} = 90^\circ - \widehat{C}}$\\[1.5mm]
    $\left(\text{Do } \widehat{HBD} = 90^\circ - \widehat{C} \text{ và } \widehat{KBD} = \widehat{KAC} \text{ cùng chắn cung } \stackrel{\frown}{KC} \text{ của } (O)\right)$
};

% ================= LEVEL 7: BỆ ĐỠ ĐIỂM KHỞI PHÁT (ĐẤT MẸ GỐC RỄ) =================
\node[base_node] (N7) at (0, -15.8) {
    $\boldsymbol{\Uparrow} \qquad \text{\textbf{KÉO DÀI ĐƯỜNG CAO }} \boldsymbol{AD} \text{\textbf{ CẮT }} \boldsymbol{(O)} \text{\textbf{ TẠI ĐIỂM THỨ HAI }} \boldsymbol{K} \qquad \boldsymbol{\Uparrow}$\\[1.5mm]
    \textbf{\large\color{teal!95!black} [ĐIỂM KHỞI PHÁT TỰ NHIÊN -- BẮT ĐẦU TRÌNH BÀY BÀI TOÁN XUÔI]}
};

% ================= CÁC VÉC-TƠ CHỈ DÀI & ĐẬM TỪ DƯỚI LÊN TRÊN =================
\draw[arr_root] (N7.north) -- (N6.south);

\draw[arr_sub] (N6.north -| N5_left.south) -- (N5_left.south);
\draw[arr_sub] (N6.north -| N5_right.south) -- (N5_right.south);

\draw[arr_sub] (N5_left.north) -- (N4.south -| N5_left.north) -- (N4.south west);
\draw[arr_sub] (N5_right.north) -- (N4.south -| N5_right.north) -- (N4.south east);

\draw[arr_main] (N4.north) -- (N3.south);
\draw[arr_main] (N3.north) -- (N2.south);
\draw[arr_main] (N2.north) -- (N1.south);

\end{tikzpicture}
\end{center}

\vspace{5mm}

\begin{center}
    \small\color{gray!85!black}
    \textbf{Cơ chế tư duy:}\ \textit{Dò ngược từ Đất mẹ ($\uparrow$) lên Đỉnh ngọn để tìm đường phụ $\bullet$ Trình bày xuôi từ Đất mẹ ($\downarrow$) theo chiều các hệ thức.}
\end{center}

\end{document}
"""
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print(f"Created: {tex_path}")

if __name__ == "__main__":
    tex_file = 'LOP9/CHUYEN_DE_9_PLUS/BAI_HINH_02/SO_DO_TU_DUY_HINH_THONG.tex'
    pdf_file = 'LOP9/CHUYEN_DE_9_PLUS/BAI_HINH_02/SO_DO_TU_DUY_HINH_THONG.pdf'
    
    create_tree_tex(tex_file)
    
    work_dir = os.path.dirname(os.path.abspath(tex_file))
    cmd = ['pdflatex', '-interaction=nonstopmode', os.path.basename(tex_file)]
    res = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True)
    
    if os.path.exists(pdf_file):
        print(f"SUCCESS: PDF created at {pdf_file}")
        print(f"Size: {os.path.getsize(pdf_file)} bytes")
    else:
        print("Failed to compile. Output snippet:")
        print(res.stdout[-800:])

