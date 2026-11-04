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
    {\large\bfseries\color{red!80!black} BẺ KHÓA Ý PHÂN HÓA 9+: TRỰC TÂM $M$ LÀ TÂM NỘI TIẾP TAM GIÁC TRỰC TÂM $HKN$}\\[1.5mm]
    {\small\color{gray!80!black}\textit{(Dữ liệu thuần công thức logic toán học $\bullet$ Trích xuất từ Đề 05 / Tuyển tập 55 Đề Vào Lớp 10)}}
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
    \textbf{\Large\color{red!85!black} [ĐÍCH ĐẾN]:\ $M$ LÀ TÂM NỘI TIẾP TAM GIÁC $HKN$}\\[1mm]
    $\boldsymbol{\iff KM, NM, HM \text{ LÀ CÁC PHÂN GIÁC TRONG CỦA } \triangle HKN}$
};

% ================= LEVEL 2: PHÂN GIÁC ĐỈNH K =================
\node[step_node] (N2) at (0, -2.3) {
    $\boldsymbol{\Uparrow} \quad \text{Phân giác trong đỉnh } K:\quad \boldsymbol{\widehat{MKH} = \widehat{MKN} \iff 90^\circ - \widehat{IKH} = 90^\circ - \widehat{CKN} \quad (DK \perp CI)}$
};

% ================= LEVEL 3: SO SÁNH HAI GÓC PHỤ NHAU =================
\node[aux_node] (N3) at (0, -4.6) {
    $\boldsymbol{\Uparrow} \quad \text{Quy về so sánh góc:}\quad \boldsymbol{\widehat{IKH} = \widehat{CKN} \iff \widehat{IMH} = \widehat{CDN}}$\\[1mm]
    \textit{(Hai góc phụ nhau với $90^\circ$ qua góc vuông $\widehat{DKI} = \widehat{DKC} = 90^\circ$)}
};

% ================= LEVEL 4: TÁCH 2 CÀNH THÔNG (HAI TỨ GIÁC NỘI TIẾP) =================
\node[branch_node] (N4_left) at (-4.7, -7.4) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- TỨ GIÁC $HKMI$]:}\\[1mm]
    $\widehat{MHI} = \widehat{MKI} = 90^\circ$\\[1mm]
    $\implies HKMI \text{ nội tiếp đường kính } MI$\\[1mm]
    $\boldsymbol{\implies \widehat{IKH} = \widehat{IMH}} \quad (\text{cùng chắn } \stackrel{\frown}{IH})$
};

\node[branch_node] (N4_right) at (4.7, -7.4) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- TỨ GIÁC $DKNC$]:}\\[1mm]
    $\widehat{DKC} = \widehat{DNC} = 90^\circ$\\[1mm]
    $\implies DKNC \text{ nội tiếp đường kính } CD$\\[1mm]
    $\boldsymbol{\implies \widehat{CKN} = \widehat{CDN}} \quad (\text{cùng chắn } \stackrel{\frown}{CN})$
};

% ================= LEVEL 5: HAI TAM GIÁC ĐỒNG DẠNG QUA ĐỐI ĐỈNH =================
\node[sim_node] (N5) at (0, -10.3) {
    $\boldsymbol{\Uparrow} \quad \text{So sánh qua đối đỉnh:}\quad \boldsymbol{\widehat{IMH} = \widehat{DMN} = 90^\circ - \widehat{MDN} = \widehat{CDN}} \quad \left(\triangle IMH \backsim \triangle CDN\right)$
};

% ================= LEVEL 6: BỆ ĐỠ GỐC RỄ (M LÀ TRỰC TÂM TAM GIÁC CDI) =================
\node[base_node] (N6) at (0, -12.9) {
    \textbf{\large\color{teal!95!black} [GỐC RỄ KHỞI PHÁT -- TRỰC TÂM ẨN $M$]:}\\[1mm]
    $H \text{ là trung điểm } AB \implies CD \perp AB \text{ tại } H \implies \boldsymbol{IH \perp CD \text{ tại } H} \quad (\text{Đường cao 1})\\[1mm]
    $N \in (O) \text{ đường kính } CD \implies \boldsymbol{CN \perp DI \text{ tại } N} \quad (\text{Đường cao 2})\\[1mm]
    $\boldsymbol{\implies M = IH \cap CN \text{ LÀ TRỰC TÂM } \triangle CDI \implies DK \perp CI \text{ TẠI } K} \quad (\text{Đường cao 3})$
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
        print(f"Compilation finished (check output)")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tex_file = os.path.join(base_dir, 'SO_DO_TU_DUY_HINH_THONG.tex')
    create_tree_tex(tex_file)
    compile_pdf(tex_file)

