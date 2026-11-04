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
    {\large\bfseries\color{red!80!black} BẺ KHÓA Ý PHÂN HÓA 9+: NĂM ĐIỂM $O, D, E, K, F$ CÙNG THUỘC ĐƯỜNG TRÒN ĐƯỜNG KÍNH $OK$}\\[1.5mm]
    {\small\color{gray!80!black}\textit{(Dữ liệu thuần công thức logic toán học $\bullet$ Trích xuất từ Đề 06 / Tuyển tập 55 Đề Vào Lớp 10)}}
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
        inner sep=7pt, align=center, text width=13.0cm, drop shadow={opacity=0.2}
    },
    step_node/.style={
        rectangle, draw=blue!80!black, fill=blue!8, line width=1.1pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=15.0cm, drop shadow={opacity=0.15}
    },
    branch_node/.style={
        rectangle, draw=purple!80!black, fill=purple!8, line width=1.2pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=5.6cm, drop shadow={opacity=0.14}
    },
    detail_node/.style={
        rectangle, draw=orange!90!black, fill=orange!12, line width=1.2pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=8.5cm, drop shadow={opacity=0.15}
    },
    base_node/.style={
        rectangle, draw=teal!95!black, fill=teal!22, line width=1.6pt, rounded corners=3.5mm,
        inner sep=8pt, align=center, text width=18.0cm, drop shadow={opacity=0.22}
    }
]

% ================= LEVEL 1: ĐỈNH CÂY THÔNG (NGŨ GIÁC NỘI TIẾP ĐƯỜNG KÍNH OK) =================
\node[target_node] (N1) at (0, 0) {
    \textbf{\Large\color{red!85!black} [ĐÍCH ĐẾN]:\ $5$ ĐIỂM $O, D, E, K, F$ CÙNG THUỘC $(M, \frac{OK}{2})$}\\[1mm]
    $\boldsymbol{\iff \widehat{KEO} = \widehat{KDO} = \widehat{KFO} = 90^\circ \quad \text{VÀ} \quad OK \perp EF}$
};

% ================= LEVEL 2: CẠNH HUYỀN CHUNG OK =================
\node[step_node] (N2) at (0, -2.3) {
    $\boldsymbol{\Uparrow} \quad \text{Ba đỉnh } E, D, F \text{ cùng nhìn đoạn thẳng } OK \text{ dưới một góc vuông } \boldsymbol{90^\circ}$
};

% ================= LEVEL 3: TÁCH 3 NHÁNH CÂN XỨNG =================
\node[branch_node] (N3_left) at (-6.0, -5.2) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- TIẾP TUYẾN $KE$]:}\\[1mm]
    $KE \perp OE \text{ tại } E \in (O)$\\[1mm]
    $\boldsymbol{\implies \widehat{KEO} = 90^\circ}$
};

\node[branch_node] (N3_mid) at (0, -5.2) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- ĐƯỜNG CAO $AD$]:}\\[1mm]
    $AD \perp BC \text{ tại } D$\\[1mm]
    $\boldsymbol{\implies \widehat{KDO} = 90^\circ}$
};

\node[branch_node] (N3_right) at (6.0, -5.2) {
    \textbf{\color{purple!90!black} [NHÁNH 3 -- TIẾP TUYẾN $KF$]:}\\[1mm]
    $KF \perp OF \text{ tại } F \in (O)$\\[1mm]
    $\boldsymbol{\implies \widehat{KFO} = 90^\circ}$
};

% ================= LEVEL 4: KỸ THUẬT PHÂN RÃ GÓC BẸT =================
\node[detail_node] (N4_left) at (-4.7, -8.6) {
    \textbf{\color{orange!90!black} Phân rã góc bẹt tại $E$:}\\[1mm]
    $\widehat{KEO} = 180^\circ - (\widehat{KEA} + \widehat{OEB})$\\[1mm]
    $= 180^\circ - (\widehat{KAE} + \widehat{OBE})$\\[1mm]
    $\boldsymbol{= 180^\circ - 90^\circ = 90^\circ} \quad (\triangle ABD \text{ vuông tại } D)$
};

\node[detail_node] (N4_right) at (4.7, -8.6) {
    \textbf{\color{orange!90!black} Phân rã góc bẹt tại $F$:}\\[1mm]
    $\widehat{KFO} = 180^\circ - (\widehat{KAF} + \widehat{OCF})$\\[1mm]
    $= 180^\circ - (\widehat{KAF} + \widehat{OCF})$\\[1mm]
    $\boldsymbol{= 180^\circ - 90^\circ = 90^\circ} \quad (\triangle ACD \text{ vuông tại } D)$
};

% ================= LEVEL 5: BỆ ĐỠ GỐC RỄ (TRỰC TÂM H VÀ ĐƯỜNG KÍNH BC) =================
\node[base_node] (N5) at (0, -12.3) {
    \textbf{\large\color{teal!95!black} [GỐC RỄ KHỞI PHÁT]:}\\[1mm]
    $E, F \in (O) \text{ đường kính } BC \implies \boldsymbol{\widehat{BEC} = \widehat{BFC} = 90^\circ} \implies \boldsymbol{CE \perp AB \quad \text{và} \quad BF \perp AC}\\[1mm]
    $\boldsymbol{\implies H = CE \cap BF \text{ LÀ TRỰC TÂM } \triangle ABC \implies AD \perp BC \text{ TẠI } D \quad \& \quad K \text{ LÀ TRUNG ĐIỂM } AH}$
};

% ================= VÉC TƠ LIÊN KẾT =================
\draw[arr_main] (N2.north) -- (N1.south);

% Gom 3 nhánh lên Level 2
\draw[arr_sub] (N3_left.north) to[out=90, in=200] (N2.south);
\draw[arr_sub] (N3_mid.north) -- (N2.south);
\draw[arr_sub] (N3_right.north) to[out=90, in=340] (N2.south);

% Từ Level 4 lên Level 3
\draw[arr_sub] (N4_left.north) -- (N3_left.south);
\draw[arr_sub] (N4_right.north) -- (N3_right.south);

% Từ Gốc rễ lên Level 4 và Nhánh giữa
\draw[arr_root] (N5.north) to[out=140, in=270] (N4_left.south);
\draw[arr_root] (N5.north) -- (N3_mid.south);
\draw[arr_root] (N5.north) to[out=40, in=270] (N4_right.south);

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

