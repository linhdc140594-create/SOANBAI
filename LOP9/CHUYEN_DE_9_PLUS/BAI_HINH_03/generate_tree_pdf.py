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
    {\large\bfseries\color{red!80!black} BẺ KHÓA Ý PHÂN HÓA 9+: CHỨNG MINH $IE$ LÀ TIẾP TUYẾN CỦA $(O)$ ĐƯỜNG KÍNH $BC$}\\[1.5mm]
    {\small\color{gray!80!black}\textit{(Dữ liệu thuần công thức logic toán học $\bullet$ Trích xuất từ Đề 03 / Tuyển tập 55 Đề Vào Lớp 10)}}
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
        inner sep=7pt, align=center, text width=11.5cm, drop shadow={opacity=0.2}
    },
    step_node/.style={
        rectangle, draw=blue!80!black, fill=blue!8, line width=1.1pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=13.5cm, drop shadow={opacity=0.15}
    },
    aux_node/.style={
        rectangle, draw=orange!90!black, fill=orange!12, line width=1.4pt, rounded corners=2.5mm,
        inner sep=7pt, align=center, text width=15.0cm, drop shadow={opacity=0.16}
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

% ================= LEVEL 1: ĐỈNH CÂY THÔNG (ĐÍCH ĐẾN TIẾP TUYẾN) =================
\node[target_node] (N1) at (0, 0) {
    \textbf{\Large\color{red!85!black} [ĐÍCH ĐẾN]:\ $IE$ LÀ TIẾP TUYẾN CỦA $(O)$ TẠI $E$}\\[1mm]
    $\boldsymbol{\iff IE \perp OE \iff \widehat{IEO} = 90^\circ \quad (E \in (O))}$
};

% ================= LEVEL 2: PHÂN RÃ GÓC =================
\node[step_node] (N2) at (0, -2.3) {
    $\boldsymbol{\Uparrow} \quad \text{Phân rã góc qua tia } EH:\quad \boldsymbol{\widehat{IEO} = \widehat{IEH} + \widehat{HEO} = 90^\circ}$
};

% ================= LEVEL 3: CHUYỂN GÓC VỀ TAM GIÁC VUÔNG BHK =================
\node[aux_node] (N3) at (0, -4.6) {
    $\boldsymbol{\Uparrow} \quad \text{Thay thế bằng các góc đáy của hai tam giác cân:}\quad \boldsymbol{\widehat{KHB} + \widehat{KBH} = 90^\circ}$\\[1mm]
    \textit{($H$ là trực tâm $\implies AH \perp BC$ tại $K \implies \triangle BHK$ vuông tại $K$)}
};

% ================= LEVEL 4: TÁCH 2 CÀNH THÔNG (HAI TAM GIÁC CÂN ĐỈNH I VÀ ĐỈNH O) =================
\node[branch_node] (N4_left) at (-4.7, -7.4) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- TAM GIÁC CÂN ĐỈNH $I$]:}\\[1mm]
    $\triangle AEH$ vuông tại $E$, $I$ là trung điểm $AH$\\[1mm]
    $\implies IE = IH = \dfrac{AH}{2} \implies \triangle IEH \text{ cân tại } I$\\[1mm]
    $\boldsymbol{\implies \widehat{IEH} = \widehat{IHE} = \widehat{KHB}} \quad \text{(đối đỉnh)}$
};

\node[branch_node] (N4_right) at (4.7, -7.4) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- TAM GIÁC CÂN ĐỈNH $O$]:}\\[1mm]
    $E, B \in (O) \implies OE = OB = R$\\[1mm]
    $\implies \triangle OBE \text{ cân tại } O$\\[1mm]
    $\boldsymbol{\implies \widehat{HEO} = \widehat{BEO} = \widehat{KBH}}$
};

% ================= LEVEL 5: TỔNG HAI GÓC NHỌN PHỤ NHAU =================
\node[sim_node] (N5) at (0, -10.3) {
    $\boldsymbol{\Uparrow} \quad \text{Tam giác } BHK \text{ vuông tại } K \implies \boldsymbol{\widehat{KHB} + \widehat{KBH} = 90^\circ} \quad \left(AH \perp BC \text{ tại } K\right)$
};

% ================= LEVEL 6: BỆ ĐỠ GỐC RỄ (GIẢ THIẾT GỐC NỬA ĐƯỜNG TRÒN) =================
\node[base_node] (N6) at (0, -12.9) {
    \textbf{\large\color{teal!95!black} [GỐC RỄ KHỞI PHÁT]:}\\[1mm]
    $D, E \in (O) \text{ đường kính } BC \implies \boldsymbol{\widehat{BDC} = \widehat{BEC} = 90^\circ}$ (Góc nội tiếp chắn nửa đường tròn)\\[1mm]
    $\boldsymbol{\implies CD \perp AB \quad \text{và} \quad BE \perp AC \implies H \text{ LÀ TRỰC TÂM TAM GIÁC } ABC \implies AH \perp BC \text{ TẠI } K}$
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
