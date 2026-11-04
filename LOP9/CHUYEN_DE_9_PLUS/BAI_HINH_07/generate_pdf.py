import os
import subprocess

def create_tex_file(output_tex_path):
    tex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{geometry}
\geometry{a4paper, top=1.2cm, bottom=1.2cm, left=1.4cm, right=1.4cm}
\usepackage{tikz}
\usetikzlibrary{calc, intersections, angles, arrows.meta, shapes.geometric, positioning}
\usepackage{tcolorbox}
\tcbuselibrary{skins, breakable}
\usepackage{tabularx}
\usepackage{enumitem}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\setlength{\headheight}{15pt}
\lhead{\small\textbf{CHUYÊN ĐỀ 9+ | HÌNH HỌC VÀO 10}}
\rhead{\small\textbf{BÀI 07: ĐỒNG DẠNG XOAY \& BỔ ĐỀ TRUNG ĐIỂM}}
\cfoot{\thepage}

% Custom tcolorbox styles
\tcbset{
    boxrule=0.8pt,
    arc=2.5mm,
    fonttitle=\bfseries\sffamily,
    coltitle=white
}

\newtcolorbox{modelbox}[1]{
    colback=blue!4!white,
    colframe=blue!75!black,
    title=#1
}

\newtcolorbox{formulabox}[1]{
    colback=orange!3!white,
    colframe=orange!85!black,
    title=#1
}

\newtcolorbox{pedagogybox}[1]{
    colback=teal!4!white,
    colframe=teal!80!black,
    title=#1
}

\newtcolorbox{solutionbox}[1]{
    colback=green!4!white,
    colframe=green!60!black,
    title=#1
}

\newtcolorbox{exercisebox}[1]{
    colback=purple!4!white,
    colframe=purple!75!black,
    title=#1
}

\begin{document}

% ==============================================================
% TRANG 1: ĐỀ BÀI VÀ HÌNH VẼ TIKZ TRỰC QUAN
% ==============================================================
\begin{center}
    {\Large\bfseries\color{blue!80!black} TUYỆT PHẨM HÌNH HỌC 9+ VÀO LỚP 10 CHUYÊN \& CÔNG LẬP TOP ĐẦU}\\[2mm]
    {\large\bfseries BÀI HÌNH 07: BỔ ĐỀ ĐỒNG DẠNG XOAY \& KỸ THUẬT TAM GIÁC CÂN KÉP}\\[1mm]
    \textit{(Trích xuất và phát triển từ Đề 07 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10)}
\end{center}

\vspace{1mm}

\begin{modelbox}{I. ĐỀ BÀI TOÁN GỐC (TRÍCH ĐỀ 07)}
Cho tam giác nhọn $ABC$ nội tiếp trong đường tròn $(O)$ có $AB < AC$. Trên cung nhỏ $AC$ lấy điểm $M$ khác $A$ thỏa mãn $MA < MC$. Vẽ đường kính $MN$ của đường tròn $(O)$. Gọi $H$ và $K$ lần lượt là hình chiếu vuông góc của điểm $A$ trên các đường thẳng $MB$ và $MN$.
\begin{enumerate}[label=\textbf{\alph*)}]
    \item Chứng minh bốn điểm $A, H, K, M$ cùng thuộc một đường tròn đường kính $AM$.
    \item Chứng minh $\triangle AHK \backsim \triangle ABN$ và $AH \cdot AN = AK \cdot AB$.
    \item \textbf{(Phân hóa 9+):} Chứng minh đường thẳng $HK$ cắt đoạn thẳng $AB$ tại đúng trung điểm của $AB$.
\end{enumerate}
\end{modelbox}

\vspace{1mm}

\begin{center}
\begin{tikzpicture}[line join = round, line cap=round, >=stealth, font=\footnotesize, scale=1.12]
    % Định nghĩa tham số
    \def\r{2.9}
    
    % Tọa độ các đỉnh trên đường tròn
    \coordinate (O) at (0,0);
    \coordinate (A) at (130:\r);
    \coordinate (B) at (-160:\r);
    \coordinate (C) at (-20:\r);
    \coordinate (M) at (65:\r);
    \coordinate (N) at ($(O)!-1!(M)$);
    
    % Hình chiếu vuông góc
    \coordinate (H) at ($(M)!(A)!(B)$);
    \coordinate (K) at ($(M)!(A)!(N)$);
    \coordinate (E) at ($(A)!0.5!(B)$);
    
    % Tâm đường tròn ngoại tiếp tứ giác AHKM
    \coordinate (I) at ($(A)!0.5!(M)$);
    
    % Vẽ các đường tròn
    \draw[thick, teal] (O) circle (\r);
    \draw[dashed, purple!80!black] let \p1 = ($(I)-(A)$), \n1 = {veclen(\x1,\y1)} in (I) circle (\n1);
    
    % Vẽ tam giác và các đường thẳng
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    \draw[thick, blue!80!black] (M) -- (N);
    \draw[thick, blue!80!black] (M) -- (B);
    \draw[thick, blue!80!black] (B) -- (N);
    \draw[thick, red!85!black] (A) -- (H);
    \draw[thick, red!85!black] (A) -- (K);
    \draw[dashed, blue!80!black] (A) -- (N);
    \draw[thick, orange!90!black] (H) -- (E);
    \draw[thick, orange!90!black] (K) -- (E);
    
    % Ký hiệu góc vuông
    \pic[draw, angle radius=2.5mm]{right angle = A--H--M};
    \pic[draw, angle radius=2.5mm]{right angle = A--K--N};
    \pic[draw, red, angle radius=2.5mm]{right angle = M--B--N};
    
    % Đánh dấu các điểm
    \fill (O) circle (1.5pt) node[below left] {$O$};
    \fill (A) circle (1.5pt) node[above left] {$A$};
    \fill (B) circle (1.5pt) node[below left] {$B$};
    \fill (C) circle (1.5pt) node[below right] {$C$};
    \fill (M) circle (1.5pt) node[above right] {$M$};
    \fill (N) circle (1.5pt) node[below left] {$N$};
    \fill[red] (H) circle (1.5pt) node[above right=1pt] {$H$};
    \fill[red] (K) circle (1.5pt) node[left] {$K$};
    \fill[blue!90!black] (E) circle (1.6pt) node[above left] {$E$};
\end{tikzpicture}
\end{center}

\vspace{1mm}

\begin{pedagogybox}{II. MỤC TIÊU TRỌNG TÂM \& BẢN ĐỒ TƯ DUY 9+}
\begin{itemize}[leftmargin=*, nosep]
    \item \textbf{Cốt lõi hình học:} Tam giác đồng dạng xoay $\triangle AHK \backsim \triangle ABN$ tạo mối liên kết góc chặt chẽ giữa tứ giác nội tiếp $AHKM$ và đường tròn lớn $(O)$: $\widehat{AHK} = \widehat{ABN}$.
    \item \textbf{Đòn bẩy tư duy ngược:} Để chứng minh $E = HK \cap AB$ là trung điểm $AB$, ta vận dụng \textbf{"Kỹ thuật Tam giác cân kép"} trong tam giác vuông $AHB$: Chỉ cần chứng minh $\triangle EAH$ cân tại $E \implies EA = EH$, tính chất góc phụ với $90^\circ$ sẽ tự động kéo theo $\triangle EHB$ cân tại $E \implies EB = EH$, từ đó $EA = EB = EH = \frac{AB}{2}$!
\end{itemize}
\end{pedagogybox}

\newpage

% ==============================================================
% TRANG 2: SƠ ĐỒ TƯ DUY NGƯỢC HÌNH CÂY THÔNG
% ==============================================================
\begin{center}
    {\Large\bfseries\color{blue!80!black} SƠ ĐỒ TƯ DUY NGƯỢC HÌNH CÂY THÔNG (PINE-TREE FORMULA TREE)}\\[1.5mm]
    {\large\bfseries BẺ KHÓA: ĐƯỜNG THẲNG $HK$ ĐI QUA TRUNG ĐIỂM $E$ CỦA $AB$}\\[1mm]
    \textit{(Quy tắc đọc ngược: Từ bệ đỡ khởi phát ở chân trang $\implies$ Hội tụ tại đỉnh ngọn)}
\end{center}

\vspace{1mm}

\begin{center}
\begin{tikzpicture}[
    x=1cm, y=1cm,
    font=\footnotesize,
    >=Stealth,
    arr_main/.style={-{Stealth[length=3.8mm, width=2.4mm]}, line width=1.6pt, red!85!black},
    arr_sub/.style={-{Stealth[length=3.4mm, width=2.2mm]}, line width=1.3pt, blue!75!black},
    arr_root/.style={-{Stealth[length=3.6mm, width=2.4mm]}, line width=1.4pt, teal!85!black},
    target_node/.style={
        rectangle, draw=red!85!black, fill=red!15, line width=1.4pt, rounded corners=2.5mm,
        inner sep=6pt, align=center, text width=12.5cm
    },
    step_node/.style={
        rectangle, draw=blue!80!black, fill=blue!8, line width=1.1pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=14.0cm
    },
    aux_node/.style={
        rectangle, draw=orange!90!black, fill=orange!12, line width=1.2pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=15.0cm
    },
    branch_node/.style={
        rectangle, draw=purple!80!black, fill=purple!8, line width=1.1pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=7.4cm
    },
    sim_node/.style={
        rectangle, draw=blue!85!black, fill=blue!8, line width=1.1pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=15.5cm
    },
    base_node/.style={
        rectangle, draw=teal!95!black, fill=teal!20, line width=1.4pt, rounded corners=3mm,
        inner sep=6pt, align=center, text width=16.8cm
    }
]

% Đỉnh cây thông
\node[target_node] (T1) at (0, 0) {
    \textbf{\large\color{red!85!black} [ĐÍCH ĐẾN]:\ $E = HK \cap AB$ LÀ TRUNG ĐIỂM $AB$}\\[1mm]
    $\boldsymbol{\iff EA = EB = \dfrac{AB}{2}}$
};

% Tầng 2
\node[step_node] (T2) at (0, -1.9) {
    $\boldsymbol{\Uparrow} \quad \text{Bắc cầu qua đoạn thẳng trung gian:}\quad \boldsymbol{EA = EH \quad \text{và} \quad EB = EH}$
};

% Tầng 3
\node[aux_node] (T3) at (0, -3.8) {
    $\boldsymbol{\Uparrow} \quad \text{Hai tam giác cân:}\quad \boldsymbol{\triangle EAH \text{ cân tại } E \ (EA=EH) \quad \& \quad \triangle EHB \text{ cân tại } E \ (EB=EH)}$\\[0.8mm]
    \textit{(Trong tam giác vuông $AHB$ vuông tại $H$, trung tuyến ứng với cạnh huyền $EH = \frac{AB}{2}$)}
};

% Tầng 4
\node[sim_node] (T4) at (0, -6.1) {
    $\boldsymbol{\Uparrow} \quad \text{Chuyển hóa góc phụ trong } \triangle AHB:\quad \boldsymbol{\widehat{EHA} = \widehat{EAH} \iff \widehat{EHB} = 90^\circ - \widehat{EHA} = 90^\circ - \widehat{EAH} = \widehat{EBH}}$
};

% Tầng 5: Tách 2 nhánh
\node[branch_node] (T5_left) at (-4.2, -8.6) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- TỨ GIÁC NỘI TIẾP]:}\\[1mm]
    Tứ giác $AHKM$ nội tiếp\\[0.8mm]
    $\boldsymbol{\implies \widehat{EHA} = \widehat{AHK} = \widehat{AMN} = \widehat{ABN}}$\\[0.8mm]
    $\left(\text{hai góc nội tiếp chắn } \stackrel{\frown}{AN} \text{ trong } (O)\right)$
};

\node[branch_node] (T5_right) at (4.2, -8.6) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- CẶP GÓC SO LE TRONG]:}\\[1mm]
    $AH \parallel BN$ (cùng $\perp MB$)\\[0.8mm]
    $\boldsymbol{\implies \widehat{EAH} = \widehat{HAB} = \widehat{ABN}}$\\[0.8mm]
    $\left(\text{hai góc so le trong tạo bởi cát tuyến } AB\right)$
};

% Bệ đỡ khởi phát
\node[base_node] (T6) at (0, -11.0) {
    \textbf{\color{teal!95!black} [GỐC RỄ KHỞI PHÁT]:}\\[1mm]
    $MN \text{ là đường kính của } (O) \implies \boldsymbol{\widehat{MBN} = 90^\circ \implies BN \perp MB} \quad (\text{Góc nội tiếp chắn nửa đường tròn})\\[0.8mm]
    $AH \perp MB \text{ tại } H \implies \boldsymbol{AH \parallel BN \quad \text{và} \quad \widehat{AHM} = \widehat{AKM} = 90^\circ \implies AHKM \text{ NỘI TIẾP ĐƯỜNG KÍNH } AM}$
};

% Mũi tên liên kết
\draw[arr_main] (T2.north) -- (T1.south);
\draw[arr_main] (T3.north) -- (T2.south);
\draw[arr_main] (T4.north) -- (T3.south);
\draw[arr_sub] (T5_left.north) to[out=90, in=210] (T4.south);
\draw[arr_sub] (T5_right.north) to[out=90, in=330] (T4.south);
\draw[arr_root] (T6.north) to[out=150, in=270] (T5_left.south);
\draw[arr_root] (T6.north) to[out=30, in=270] (T5_right.south);

\end{tikzpicture}
\end{center}

\vspace{1mm}

\begin{formulabox}{III. CÔNG THỨC VÀ BỔ ĐỀ CHỐT HẠ}
\begin{itemize}[leftmargin=*, nosep]
    \item \textbf{Định lý Tam giác cân kép:} Một điểm $E$ nằm trên cạnh huyền $AB$ của tam giác vuông $AHB$ là trung điểm khi và chỉ khi $EA = EH = EB$.
    \item \textbf{Cặp góc đồng vị và so le trong:} $AH \parallel BN \implies \widehat{HAB} = \widehat{ABN}$. Kết hợp với góc nội tiếp $\widehat{AHK} = \widehat{ABN}$ tạo ra tam giác cân $EAH$.
\end{itemize}
\end{formulabox}

\newpage

% ==============================================================
% TRANG 3: LỜI GIẢI XUÔI CHUẨN MỰC & BAREM ĐIỂM
% ==============================================================
\begin{center}
    {\Large\bfseries\color{blue!80!black} LỜI GIẢI XUÔI CHUẨN MỰC \& BAREM ĐIỂM CHI TIẾT}\\[1.5mm]
    {\large\bfseries BÀI TOÁN HÌNH HỌC 9+ (3,0 ĐIỂM - CHUẨN THI TUYỂN SINH VÀO LỚP 10)}
\end{center}

\vspace{1mm}

\begin{solutionbox}{LỜI GIẢI CHI TIẾT TỪNG BƯỚC}
\begin{enumerate}[label=\textbf{\arabic*.}, leftmargin=*]
    \item \textbf{Chứng minh bốn điểm $A, H, K, M$ cùng thuộc đường tròn đường kính $AM$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Theo giả thiết: $AH \perp MB$ tại $H \implies \widehat{AHM} = 90^\circ$. \hfill \textbf{[0,25đ]}
        \item $AK \perp MN$ tại $K \implies \widehat{AKM} = 90^\circ$. \hfill \textbf{[0,25đ]}
        \item Xét tứ giác $AHKM$ có hai đỉnh kề $H$ và $K$ cùng nhìn đoạn thẳng $AM$ dưới một góc vuông $90^\circ$.\\
        Do đó tứ giác $AHKM$ nội tiếp đường tròn đường kính $AM$. Bốn điểm $A, H, K, M$ cùng thuộc đường tròn này. \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Chứng minh $\triangle AHK \backsim \triangle ABN$ và $AH \cdot AN = AK \cdot AB$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Trong đường tròn ngoại tiếp tứ giác $AHKM$, ta có: $\widehat{AHK} = \widehat{AMK} = \widehat{AMN}$ (hai góc nội tiếp cùng chắn cung $AK$).\\
        Trong đường tròn $(O)$, ta có: $\widehat{AMN} = \widehat{ABN}$ (hai góc nội tiếp cùng chắn cung $AN$).\\
        Suy ra $\widehat{AHK} = \widehat{ABN}$. \hfill \textbf{[0,25đ]}
        \item Tương tự, trong đường tròn ngoại tiếp tứ giác $AHKM$: $\widehat{AKH} = \widehat{AMH} = \widehat{AMB}$ (cùng chắn cung $AH$).\\
        Trong đường tròn $(O)$, ta có: $\widehat{AMB} = \widehat{ANB}$ (hai góc nội tiếp cùng chắn cung $AB$).\\
        Suy ra $\widehat{AKH} = \widehat{ANB}$. \hfill \textbf{[0,25đ]}
        \item Xét hai tam giác $\triangle AHK$ và $\triangle ABN$ có: $\widehat{AHK} = \widehat{ABN}$ và $\widehat{AKH} = \widehat{ANB}$.\\
        Suy ra $\triangle AHK \backsim \triangle ABN$ (g-g) $\implies \dfrac{AH}{AB} = \dfrac{AK}{AN} \implies AH \cdot AN = AK \cdot AB$ (đpcm). \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Chứng minh tam giác $EAH$ cân tại $E$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Gọi $E$ là giao điểm của đường thẳng $HK$ với đoạn thẳng $AB$.
        \item Vì $MN$ là đường kính của $(O)$ nên $\widehat{MBN} = 90^\circ$ (góc nội tiếp chắn nửa đường tròn) $\implies BN \perp MB$. \hfill \textbf{[0,25đ]}
        \item Mà theo giả thiết $AH \perp MB$, suy ra $AH \parallel BN$ (hai đường thẳng cùng vuông góc với $MB$).\\
        Do đó hai góc so le trong bằng nhau: $\widehat{EAH} = \widehat{HAB} = \widehat{ABN}$. \hfill \textbf{[0,25đ]}
        \item Theo chứng minh câu b, ta có $\widehat{EHA} = \widehat{AHK} = \widehat{ABN}$.\\
        Suy ra $\widehat{EHA} = \widehat{EAH}$. Do đó tam giác $EAH$ cân tại $E \implies EA = EH$. \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Chứng minh tam giác $EHB$ cân tại $E$ và kết luận trung điểm (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Xét tam giác $AHB$ vuông tại $H$ ($AH \perp MB$), ta có hai góc nhọn phụ nhau:
        \[
        \widehat{EAH} + \widehat{EBH} = 90^\circ \implies \widehat{EBH} = 90^\circ - \widehat{EAH}.
        \] \hfill \textbf{[0,25đ]}
        \item Lại có: $\widehat{EHA} + \widehat{EHB} = \widehat{AHB} = 90^\circ \implies \widehat{EHB} = 90^\circ - \widehat{EHA}$.\\
        Vì $\widehat{EHA} = \widehat{EAH}$ nên suy ra: $\widehat{EHB} = \widehat{EBH}$.\\
        Do đó tam giác $EHB$ cân tại $E \implies EB = EH$. \hfill \textbf{[0,25đ]}
        \item Từ $EA = EH$ và $EB = EH$, suy ra $EA = EB = EH = \dfrac{AB}{2}$.\\
        Vậy đường thẳng $HK$ cắt đoạn thẳng $AB$ tại đúng trung điểm $E$ của $AB$ (đpcm). \hfill \textbf{[0,25đ]}
    \end{itemize}
\end{enumerate}
\end{solutionbox}

\newpage

% ==============================================================
% TRANG 4: BÌNH LUẬN SƯ PHẠM & BÀI TẬP PHÁT TRIỂN
% ==============================================================
\begin{center}
    {\Large\bfseries\color{blue!80!black} BÌNH LUẬN SƯ PHẠM, BẪY TƯ DUY \& BÀI TẬP PHÁT TRIỂN}\\[1.5mm]
    {\large\bfseries GIẢI MÃ NGHỆ THUẬT DẪN DẮT \& MỞ RỘNG TẦM NHÌN HÌNH HỌC 9+}
\end{center}

\vspace{1mm}

\begin{pedagogybox}{I. NGHỆ THUẬT SƯ PHẠM: TẠI SAO LẠI BẮC CẦU QUA ĐOẠN EH?}
\begin{itemize}[leftmargin=*]
    \item \textbf{Cội nguồn tư duy:} Đoạn thẳng $AB$ là cạnh huyền của tam giác vuông $AHB$. Định lý đảo về đường trung tuyến chỉ ra rằng: một điểm $E$ nằm trên cạnh huyền của tam giác vuông là trung điểm khi và chỉ khi khoảng cách từ $E$ tới đỉnh góc vuông bằng khoảng cách tới hai đỉnh còn lại ($EA = EB = EH$).
    \item \textbf{Đòn bẩy hình học:} Bằng việc tách thành hai bài toán con: chứng minh $\triangle EAH$ cân và $\triangle EHB$ cân, ta lập tức nhận ra điểm $H$ đóng vai trò "công tắc chuyển mạch": một nửa góc vuông gắn với tứ giác nội tiếp $AHKM$, nửa góc vuông còn lại tự động khép góc với tam giác vuông $AHB$!
    \item \textbf{4 câu hỏi dẫn dắt của Giáo viên trên lớp:}
    \begin{enumerate}[label=\arabic*., nosep]
        \item Đường kính $MN$ tạo ra góc vuông nào tại đỉnh $B$? Nhận xét quan hệ giữa hai đoạn thẳng $AH$ và $BN$?
        \item Khi $AH$ song song với $BN$, góc $\widehat{HAB}$ bằng góc nào theo tính chất so le trong?
        \item Từ hai tam giác đồng dạng $\triangle AHK \backsim \triangle ABN$, góc $\widehat{AHK}$ bằng góc nào?
        \item Tam giác $EAH$ có hai góc đáy $\widehat{EHA}$ và $\widehat{EAH}$ bằng nhau cho ta điều gì? Trong tam giác vuông $AHB$, điểm $E$ thỏa mãn $EA = EH$ thì có vị trí như thế nào trên cạnh huyền $AB$?
    \end{enumerate}
\end{itemize}
\end{pedagogybox}

\vspace{1mm}

\begin{pedagogybox}{II. CÁC BẪY TƯ DUY VÀ SAI LẦM HỌC SINH THƯỜNG GẶP}
\begin{itemize}[leftmargin=*, nosep]
    \item \textbf{Bẫy 1 -- Cố gắng dùng Menelaus hoặc Ta-lét phức tạp:} Nhiều học sinh kéo dài các đường thẳng để tìm giao điểm và tính tỉ số đoạn thẳng. Điều này vừa tốn thời gian vừa dễ nhầm lẫn dấu. Kỹ thuật tam giác cân kép trong tam giác vuông $AHB$ giải quyết bài toán chỉ trong 4 dòng gọn gàng.
    \item \textbf{Bẫy 2 -- Quên chứng minh $\triangle EHB$ cân mà suy diễn vội:} Một số học sinh sau khi chứng minh được $EA = EH$ liền ngộ nhận ngay $E$ là trung điểm. Cần nhớ rằng nếu chỉ có $EA = EH$ thì $E$ chỉ nằm trên đường trung trực của $AH$, bắt buộc phải chỉ ra thêm $EB = EH$ (hoặc dùng tính chất góc phụ) mới đủ điều kiện kết luận $E$ là trung điểm của $AB$.
\end{itemize}
\end{pedagogybox}

\vspace{1mm}

\begin{exercisebox}{III. BÀI TẬP PHÁT TRIỂN ĐỈNH CAO (LUYỆN TẬP 9+)}
\textbf{Bài toán phát triển 1 (Bán kính đường tròn ngoại tiếp Euler):}\\
Chứng minh rằng bán kính đường tròn ngoại tiếp của tam giác $AHK$ thỏa mãn hệ thức:
\[
R_{\triangle AHK} = R_{(O)} \cdot \sin \widehat{AMB}.
\]
\textit{(Gợi ý: Do $\triangle AHK \backsim \triangle ABN$ với tỉ số đồng dạng $k = \dfrac{AH}{AB} = \sin \widehat{ABH}$, và bán kính đường tròn ngoại tiếp $\triangle ABN$ bằng $R_{(O)}$ vì $MN$ là đường kính).}\\[2mm]
\textbf{Bài toán phát triển 2 (Đẳng thức diện tích và Cực trị):}\\
Xác định vị trí của điểm $M$ trên cung nhỏ $AC$ để tích $AH \cdot AK$ đạt giá trị lớn nhất.\\[1mm]
\textit{(Gợi ý: Chuyển tích $AH \cdot AK$ thành $\dfrac{AB \cdot AK^2}{AN}$ hoặc dùng bất đẳng thức Cauchy kết hợp với dây cung $AB$ cố định).}
\end{exercisebox}

\end{document}
"""
    with open(output_tex_path, 'w', encoding='utf-8') as f:
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
    tex_file = os.path.join(base_dir, 'SO_DO_TU_DUY_NGUOC_HINH9.tex')
    create_tex_file(tex_file)
    compile_pdf(tex_file)

