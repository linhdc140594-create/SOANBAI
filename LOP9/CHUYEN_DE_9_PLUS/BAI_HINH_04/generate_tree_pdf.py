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
    {\large\bfseries\color{red!80!black} BẺ KHÓA Ý PHÂN HÓA 9+: TRỰC TÂM $H$ LÀ TÂM NỘI TIẾP TAM GIÁC TRỰC TÂM $IKL$}\\[1.5mm]
    {\small\color{gray!80!black}\textit{(Dữ liệu thuần công thức logic toán học $\bullet$ Trích xuất từ Đề 04 / Tuyển tập 55 Đề Vào Lớp 10)}}
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
        inner sep=7pt, align=center, text width=12.0cm, drop shadow={opacity=0.2}
    },
    step_node/.style={
        rectangle, draw=blue!80!black, fill=blue!8, line width=1.1pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=14.0cm, drop shadow={opacity=0.15}
    },
    aux_node/.style={
        rectangle, draw=orange!90!black, fill=orange!12, line width=1.4pt, rounded corners=2.5mm,
        inner sep=7pt, align=center, text width=15.2cm, drop shadow={opacity=0.16}
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

% ================= LEVEL 1: ĐỈNH CÂY THÔNG (TÂM ĐƯỜNG TRÒN NỘI TIẾP) =================
\node[target_node] (N1) at (0, 0) {
    \textbf{\Large\color{red!85!black} [ĐÍCH ĐẾN]:\ $H$ LÀ TÂM NỘI TIẾP TAM GIÁC $IKL$}\\[1mm]
    $\boldsymbol{\iff KH, IH, LH \text{ LÀ CÁC PHÂN GIÁC TRONG CỦA } \triangle IKL}$
};

% ================= LEVEL 2: PHÂN GIÁC ĐỈNH K =================
\node[step_node] (N2) at (0, -2.3) {
    $\boldsymbol{\Uparrow} \quad \text{Phân giác trong đỉnh } K:\quad \boldsymbol{\widehat{LKB} = \widehat{IKB} \iff 90^\circ - \widehat{AKL} = 90^\circ - \widehat{IKC} \quad (BK \perp AC)}$
};

% ================= LEVEL 3: SO SÁNH HAI GÓC PHỤ NHAU =================
\node[aux_node] (N3) at (0, -4.6) {
    $\boldsymbol{\Uparrow} \quad \text{Quy về so sánh góc:}\quad \boldsymbol{\widehat{AKL} = \widehat{IKC} \iff \widehat{AHL} = \widehat{IHC}}$\\[1mm]
    \textit{(Hai góc phụ nhau với $90^\circ$ qua góc vuông $\widehat{AKB} = \widehat{BKC} = 90^\circ$)}
};

% ================= LEVEL 4: TÁCH 2 CÀNH THÔNG (HAI TỨ GIÁC NỘI TIẾP) =================
\node[branch_node] (N4_left) at (-4.7, -7.4) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- TỨ GIÁC $AKHL$]:}\\[1mm]
    $\widehat{AKH} = \widehat{ALH} = 90^\circ$\\[1mm]
    $\implies AKHL \text{ nội tiếp đường kính } AH$\\[1mm]
    $\boldsymbol{\implies \widehat{AKL} = \widehat{AHL}} \quad (\text{cùng chắn } \stackrel{\frown}{AL})$
};

\node[branch_node] (N4_right) at (4.7, -7.4) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- TỨ GIÁC $CIHK$]:}\\[1mm]
    $\widehat{HIC} = \widehat{HKC} = 90^\circ$\\[1mm]
    $\implies CIHK \text{ nội tiếp đường kính } CH$\\[1mm]
    $\boldsymbol{\implies \widehat{IKC} = \widehat{IHC}} \quad (\text{cùng chắn } \stackrel{\frown}{IC})$
};

% ================= LEVEL 5: HAI GÓC ĐỐI ĐỈNH TẠI TRỰC TÂM H =================
\node[sim_node] (N5) at (0, -10.3) {
    $\boldsymbol{\Uparrow} \quad \text{Hai góc đối đỉnh:}\quad \boldsymbol{\widehat{AHL} = \widehat{IHC}} \quad \left(A, H, I \text{ thẳng hàng và } C, H, L \text{ thẳng hàng}\right)$
};

% ================= LEVEL 6: BỆ ĐỠ GỐC RỄ (ĐỊNH NGHĨA TRỰC TÂM) =================
\node[base_node] (N6) at (0, -12.9) {
    \textbf{\large\color{teal!95!black} [GỐC RỄ KHỞI PHÁT]:}\\[1mm]
    $AI, BK, CL \text{ là ba đường cao của } \triangle ABC \text{ cắt nhau tại trực tâm } H\\[1mm]
    $\boldsymbol{\implies AI \perp BC, \ BK \perp AC, \ CL \perp AB \implies A, H, I \text{ THẲNG HÀNG VÀ } C, H, L \text{ THẲNG HÀNG}}$
};

% ================= VÉC TƠ LIÊN KẾT DÀI RÕ NÉT =================
\draw[arr_main] (N2.north) -- (N1.south);
\draw[arr_main] (N3.north) -- (N2.south);

% Tách 2 nhánh
\draw[arr_sub] (N4_left.north) to[out=90, in=210] (N3.south);
\draw[arr_sub] (N4_right.north) to[out=90, in=330] (N3.south);

% Gom từ Level 5 lên 2 nhánh
\draw[arr_sub] (N5.north) to[out=150, in=270] (N4_left.south);
\draw[arr_sub] (N5.north) to[out=30, in=270] (N4_right.south);

% Từ Gốc rễ lên Level 5
\draw[arr_root] (N6.north) -- (N5.south);

\end{tikzpicture}
\end{center}

\vfill
\begin{center}
    {\footnotesize\color{gray!70!black} \textbf{Quy tắc đọc ngược:} Bắt đầu từ \textbf{[GỐC RỄ KHỞI PHÁT]} ở chân trang $\longrightarrow$ Đi theo các véc-tơ suy luận $\longrightarrow$ Hội tụ tại \textbf{[ĐÍCH ĐẾN]} ở đỉnh cây thông.}
\end{center}

\end{document}
"""
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)

def compile_pdf(tex_path):
    folder = os.path.dirname(tex_path)
    base_name = os.path.splitext(os.path.basename(tex_path))[0]
    cmd = ['pdflatex', '-interaction=nonstopmode', base_name + '.tex']
    print(f"Compiling {base_name}.tex...")
    res = subprocess.run(cmd, cwd=folder, capture_output=True, text=True, encoding='utf-8', errors='ignore')
    if res.returncode == 0:
        print(f"SUCCESS: {base_name}.pdf created!")
    else:
        print(f"Error compiling: {res.stderr}")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tex_file = os.path.join(base_dir, 'SO_DO_TU_DUY_HINH_THONG.tex')
    create_tree_tex(tex_file)
    compile_pdf(tex_file)

