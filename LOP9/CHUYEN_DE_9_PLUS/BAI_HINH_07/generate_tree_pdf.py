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
    {\large\bfseries\color{red!80!black} BẺ KHÓA Ý PHÂN HÓA 9+: ĐƯỜNG THẲNG $HK$ ĐI QUA TRUNG ĐIỂM $E$ CỦA $AB$}\\[1.5mm]
    {\small\color{gray!80!black}\textit{(Dữ liệu thuần công thức logic toán học $\bullet$ Trích xuất từ Đề 07 / Tuyển tập 55 Đề Vào Lớp 10)}}
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
        inner sep=7pt, align=center, text width=12.5cm, drop shadow={opacity=0.2}
    },
    step_node/.style={
        rectangle, draw=blue!80!black, fill=blue!8, line width=1.1pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=14.5cm, drop shadow={opacity=0.15}
    },
    aux_node/.style={
        rectangle, draw=orange!90!black, fill=orange!12, line width=1.4pt, rounded corners=2.5mm,
        inner sep=7pt, align=center, text width=15.5cm, drop shadow={opacity=0.16}
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

% ================= LEVEL 1: ĐỈNH CÂY THÔNG (TRUNG ĐIỂM CỦA AB) =================
\node[target_node] (N1) at (0, 0) {
    \textbf{\Large\color{red!85!black} [ĐÍCH ĐẾN]:\ $E = HK \cap AB$ LÀ TRUNG ĐIỂM $AB$}\\[1mm]
    $\boldsymbol{\iff EA = EB = \dfrac{AB}{2}}$
};

% ================= LEVEL 2: BẮC CẦU QUA ĐOẠN EH =================
\node[step_node] (N2) at (0, -2.3) {
    $\boldsymbol{\Uparrow} \quad \text{Bắc cầu qua đoạn thẳng trung gian:}\quad \boldsymbol{EA = EH \quad \text{và} \quad EB = EH}$
};

% ================= LEVEL 3: TAM GIÁC CÂN KÉP =================
\node[aux_node] (N3) at (0, -4.6) {
    $\boldsymbol{\Uparrow} \quad \text{Hai tam giác cân:}\quad \boldsymbol{\triangle EAH \text{ cân tại } E \ (EA=EH) \quad \& \quad \triangle EHB \text{ cân tại } E \ (EB=EH)}$\\[1mm]
    \textit{(Trong tam giác vuông $AHB$ vuông tại $H$, trung tuyến ứng với cạnh huyền $EH = \frac{AB}{2}$)}
};

% ================= LEVEL 4: QUY VỀ GÓC PHỤ NHAU =================
\node[sim_node] (N4) at (0, -7.0) {
    $\boldsymbol{\Uparrow} \quad \text{Chuyển hóa góc phụ trong } \triangle AHB:\quad \boldsymbol{\widehat{EHA} = \widehat{EAH} \iff \widehat{EHB} = 90^\circ - \widehat{EHA} = 90^\circ - \widehat{EAH} = \widehat{EBH}}$
};

% ================= LEVEL 5: TÁCH 2 CÀNH THÔNG (TỨ GIÁC NỘI TIẾP & SO LE TRONG) =================
\node[branch_node] (N5_left) at (-4.7, -9.8) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- TỨ GIÁC NỘI TIẾP]:}\\[1mm]
    Tứ giác $AHKM$ nội tiếp\\[1mm]
    $\boldsymbol{\implies \widehat{EHA} = \widehat{AHK} = \widehat{AMN} = \widehat{ABN}}$\\[1mm]
    $\left(\text{hai góc nội tiếp cùng chắn } \stackrel{\frown}{AN} \text{ trong } (O)\right)$
};

\node[branch_node] (N5_right) at (4.7, -9.8) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- CẶP GÓC SO LE TRONG]:}\\[1mm]
    $AH \parallel BN$ (cùng $\perp MB$)\\[1mm]
    $\boldsymbol{\implies \widehat{EAH} = \widehat{HAB} = \widehat{ABN}}$\\[1mm]
    $\left(\text{hai góc so le trong tạo bởi cát tuyến } AB\right)$
};

% ================= LEVEL 6: BỆ ĐỠ GỐC RỄ (ĐƯỜNG KÍNH MN VÀ HAI GÓC VUÔNG) =================
\node[base_node] (N6) at (0, -12.9) {
    \textbf{\large\color{teal!95!black} [GỐC RỄ KHỞI PHÁT]:}\\[1mm]
    $MN \text{ là đường kính của } (O) \implies \boldsymbol{\widehat{MBN} = 90^\circ \implies BN \perp MB} \quad (\text{Góc nội tiếp chắn nửa đường tròn})\\[1mm]
    $AH \perp MB \text{ tại } H \implies \boldsymbol{AH \parallel BN \quad \text{và} \quad \widehat{AHM} = \widehat{AKM} = 90^\circ \implies AHKM \text{ NỘI TIẾP ĐƯỜNG KÍNH } AM}$
};

% ================= VÉC TƠ LIÊN KẾT DÀI RÕ NÉT =================
\draw[arr_main] (N2.north) -- (N1.south);
\draw[arr_main] (N3.north) -- (N2.south);
\draw[arr_main] (N4.north) -- (N3.south);

% Tách 2 nhánh từ Level 4
\draw[arr_sub] (N5_left.north) to[out=90, in=210] (N4.south);
\draw[arr_sub] (N5_right.north) to[out=90, in=330] (N4.south);

% Từ Gốc rễ lên 2 nhánh
\draw[arr_root] (N6.north) to[out=150, in=270] (N5_left.south);
\draw[arr_root] (N6.north) to[out=30, in=270] (N5_right.south);

\end{tikzpicture}
\end{center}

\vfill
\begin{center}
    {\footnotesize\color{gray!70!black} \textbf{Quy tắc đọc ngược:} Bắt đầu từ \textbf{[GỐC RỄ KHỞI PHÁT]} ở chân trang $\longrightarrow$ Phân nhánh theo các véc-tơ suy luận $\longrightarrow$ Hội tụ tại \textbf{[ĐÍCH ĐẾN]} ở đỉnh cây thông.}
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
        print(f"Compilation finished (check output)")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tex_file = os.path.join(base_dir, 'SO_DO_TU_DUY_HINH_THONG.tex')
    create_tree_tex(tex_file)
    compile_pdf(tex_file)

