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
\rhead{\small\textbf{BÀI 04: TAM GIÁC TRỰC TÂM $IKL$}}
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
    {\large\bfseries BÀI HÌNH 04: BỔ ĐỀ TAM GIÁC TRỰC TÂM \& TÂM ĐƯỜNG TRÒN NỘI TIẾP}\\[1mm]
    \textit{(Trích xuất và phát triển từ Đề 04 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10)}
\end{center}

\vspace{1mm}

\begin{modelbox}{I. ĐỀ BÀI TOÁN GỐC (TRÍCH ĐỀ 04)}
Cho tam giác $ABC$ có ba góc nhọn ($AB < AC$). Ba đường cao $AI, BK, CL$ cắt nhau tại trực tâm $H$.
\begin{enumerate}[label=\textbf{\alph*)}]
    \item Chứng minh các tứ giác $BIHL$ và $CIHK$ nội tiếp đường tròn.
    \item Chứng minh $\widehat{AKL} = \widehat{IKC}$ và suy ra $KB$ là tia phân giác của $\widehat{LKI}$.
    \item \textbf{(Phân hóa 9+):} Chứng minh trực tâm $H$ là tâm của đường tròn nội tiếp tam giác trực tâm $IKL$.
\end{enumerate}
\end{modelbox}

\vspace{1mm}

\begin{center}
\begin{tikzpicture}[line join = round, line cap=round, >=stealth, font=\footnotesize, scale=1.15]
    % Tham số
    \def\r{3.2}
    
    % Tọa độ các đỉnh
    \coordinate (O) at (0,0);
    \coordinate (A) at (105:\r);
    \coordinate (B) at (-155:\r);
    \coordinate (C) at (-25:\r);
    
    % Chân các đường cao
    \coordinate (I) at ($(B)!(A)!(C)$); % A chiếu lên BC
    \coordinate (K) at ($(A)!(B)!(C)$); % B chiếu lên AC
    \coordinate (L) at ($(A)!(C)!(B)$); % C chiếu lên AB
    
    % Trực tâm H
    \coordinate (H) at (intersection of A--I and C--L);
    
    % Vẽ tam giác lớn và các đường cao
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    \draw[thick, blue!85!black] (A) -- (I);
    \draw[thick, blue!85!black] (B) -- (K);
    \draw[thick, blue!85!black] (C) -- (L);
    
    % Vẽ tam giác trực tâm IKL (màu cam đỏ nổi bật)
    \draw[thick, red!85!black] (I) -- (K) -- (L) -- cycle;
    
    % Ký hiệu góc vuông
    \pic[draw, angle radius=2.5mm]{right angle = A--I--C};
    \pic[draw, angle radius=2.5mm]{right angle = B--K--A};
    \pic[draw, angle radius=2.5mm]{right angle = C--L--B};
    
    % Điểm
    \fill (A) circle (1.5pt) node[above] {$A$};
    \fill (B) circle (1.5pt) node[below left] {$B$};
    \fill (C) circle (1.5pt) node[below right] {$C$};
    \fill[red] (I) circle (1.5pt) node[below] {$I$};
    \fill[red] (K) circle (1.5pt) node[above right] {$K$};
    \fill[red] (L) circle (1.5pt) node[above left] {$L$};
    \fill[blue!90!black] (H) circle (1.6pt) node[below left=1pt] {$H$};
\end{tikzpicture}
\end{center}

\vspace{1mm}

\begin{pedagogybox}{II. MỤC TIÊU TRỌNG TÂM \& BẢN ĐỒ TƯ DUY 9+}
\begin{itemize}[leftmargin=*, nosep]
    \item \textbf{Cốt lõi hình học:} Tam giác $IKL$ tạo bởi ba chân đường cao được gọi là \textbf{Tam giác trực tâm (Orthic Triangle)}. Một tính chất kinh điển là ba đường cao của $\triangle ABC$ chính là ba đường phân giác trong của $\triangle IKL$.
    \item \textbf{Đòn bẩy tư duy ngược:} Để chứng minh $H$ là tâm nội tiếp, ta chứng minh $KH$ và $IH$ là phân giác. Để chứng minh $KH$ là phân giác góc $\widehat{LKI}$, ta chuyển việc so sánh hai góc $\widehat{LKB}$ và $\widehat{IKB}$ về hai góc phụ nhau với $90^\circ$ qua $BK \perp AC$, đó là $\widehat{AKL} = \widehat{IKC}$. Hai góc này liên kết trực tiếp với cặp góc đối đỉnh $\widehat{AHL} = \widehat{IHC}$ qua hai tứ giác nội tiếp $AKHL$ và $CIHK$!
\end{itemize}
\end{pedagogybox}

\newpage

% ==============================================================
% TRANG 2: SƠ ĐỒ TƯ DUY NGƯỢC HÌNH CÂY THÔNG
% ==============================================================
\begin{center}
    {\Large\bfseries\color{blue!80!black} SƠ ĐỒ TƯ DUY NGƯỢC HÌNH CÂY THÔNG (PINE-TREE FORMULA TREE)}\\[1.5mm]
    {\large\bfseries BẺ KHÓA: CHỨNG MINH $H$ LÀ TÂM ĐƯỜNG TRÒN NỘI TIẾP $\triangle IKL$}\\[1mm]
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
        inner sep=6pt, align=center, text width=11.5cm
    },
    step_node/.style={
        rectangle, draw=blue!80!black, fill=blue!8, line width=1.1pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=13.5cm
    },
    aux_node/.style={
        rectangle, draw=orange!90!black, fill=orange!12, line width=1.2pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=14.8cm
    },
    branch_node/.style={
        rectangle, draw=purple!80!black, fill=purple!8, line width=1.1pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=7.2cm
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
    \textbf{\large\color{red!85!black} [ĐÍCH ĐẾN]:\ $H$ LÀ TÂM NỘI TIẾP TAM GIÁC $IKL$}\\[1mm]
    $\boldsymbol{\iff KH, IH, LH \text{ LÀ CÁC ĐƯỜNG PHÂN GIÁC TRONG CỦA } \triangle IKL}$
};

% Tầng 2
\node[step_node] (T2) at (0, -1.9) {
    $\boldsymbol{\Uparrow} \quad \text{Phân giác trong đỉnh } K:\quad \boldsymbol{\widehat{LKB} = \widehat{IKB} \iff 90^\circ - \widehat{AKL} = 90^\circ - \widehat{IKC} \quad (BK \perp AC)}$
};

% Tầng 3
\node[aux_node] (T3) at (0, -3.8) {
    $\boldsymbol{\Uparrow} \quad \text{Quy về so sánh góc:}\quad \boldsymbol{\widehat{AKL} = \widehat{IKC} \iff \widehat{AHL} = \widehat{IHC}}$\\[1mm]
    \textit{(Hai góc phụ nhau với $90^\circ$ qua góc vuông $\widehat{AKB} = \widehat{BKC} = 90^\circ$)}
};

% Tầng 4: Hai nhánh
\node[branch_node] (T4_left) at (-4.2, -6.1) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- TỨ GIÁC $AKHL$]:}\\[1mm]
    $\widehat{AKH} = \widehat{ALH} = 90^\circ$\\[0.8mm]
    $\implies AKHL \text{ nội tiếp đường kính } AH$\\[0.8mm]
    $\boldsymbol{\implies \widehat{AKL} = \widehat{AHL}} \quad (\text{cùng chắn } \stackrel{\frown}{AL})$
};

\node[branch_node] (T4_right) at (4.2, -6.1) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- TỨ GIÁC $CIHK$]:}\\[1mm]
    $\widehat{HIC} = \widehat{HKC} = 90^\circ$\\[0.8mm]
    $\implies CIHK \text{ nội tiếp đường kính } CH$\\[0.8mm]
    $\boldsymbol{\implies \widehat{IKC} = \widehat{IHC}} \quad (\text{cùng chắn } \stackrel{\frown}{IC})$
};

% Tầng 5: Hai góc đối đỉnh
\node[sim_node] (T5) at (0, -8.5) {
    $\boldsymbol{\Uparrow} \quad \text{Hai góc đối đỉnh:}\quad \boldsymbol{\widehat{AHL} = \widehat{IHC}} \quad \left(A, H, I \text{ thẳng hàng và } C, H, L \text{ thẳng hàng}\right)$
};

% Bệ đỡ khởi phát
\node[base_node] (T6) at (0, -10.6) {
    \textbf{\color{teal!95!black} [GỐC RỄ KHỞI PHÁT]:}\\[1mm]
    $AI, BK, CL \text{ là ba đường cao của } \triangle ABC \text{ cắt nhau tại trực tâm } H\\[0.8mm]
    $\boldsymbol{\implies AI \perp BC, \ BK \perp AC, \ CL \perp AB \implies A, H, I \text{ THẲNG HÀNG VÀ } C, H, L \text{ THẲNG HÀNG}}$
};

% Mũi tên liên kết
\draw[arr_main] (T2.north) -- (T1.south);
\draw[arr_main] (T3.north) -- (T2.south);
\draw[arr_sub] (T4_left.north) to[out=90, in=210] (T3.south);
\draw[arr_sub] (T4_right.north) to[out=90, in=330] (T3.south);
\draw[arr_sub] (T5.north) to[out=150, in=270] (T4_left.south);
\draw[arr_sub] (T5.north) to[out=30, in=270] (T4_right.south);
\draw[arr_root] (T6.north) -- (T5.south);

\end{tikzpicture}
\end{center}

\vspace{1mm}

\begin{formulabox}{III. CÔNG THỨC VÀ BỔ ĐỀ CHỐT HẠ}
\begin{itemize}[leftmargin=*, nosep]
    \item \textbf{Bổ đề góc phụ với đường cao:} Khi một đường thẳng vuông góc với một cạnh, hai góc kề bù sẽ chuyển hóa thành hai góc phụ: $\widehat{LKB} = 90^\circ - \widehat{AKL}$ và $\widehat{IKB} = 90^\circ - \widehat{IKC}$.
    \item \textbf{Định lý Tam giác trực tâm:} Trong mọi tam giác nhọn $ABC$, trực tâm $H$ của tam giác ban đầu đồng thời là tâm đường tròn nội tiếp của tam giác trực tâm $IKL$ (tạo bởi ba chân đường cao).
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
    \item \textbf{Chứng minh các tứ giác $BIHL$ và $CIHK$ nội tiếp đường tròn (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Vì $AI, CL$ là các đường cao của $\triangle ABC$ nên $AI \perp BC \implies \widehat{HIB} = 90^\circ$ và $CL \perp AB \implies \widehat{HLB} = 90^\circ$. \hfill \textbf{[0,25đ]}
        \item Xét tứ giác $BIHL$ có: $\widehat{HIB} + \widehat{HLB} = 90^\circ + 90^\circ = 180^\circ$.\\
        Do đó tứ giác $BIHL$ nội tiếp đường tròn đường kính $BH$. \hfill \textbf{[0,25đ]}
        \item Tương tự, xét tứ giác $CIHK$ có $AI \perp BC \implies \widehat{HIC} = 90^\circ$ và $BK \perp AC \implies \widehat{HKC} = 90^\circ$.
        Suy ra $\widehat{HIC} + \widehat{HKC} = 90^\circ + 90^\circ = 180^\circ$.\\
        Do đó tứ giác $CIHK$ nội tiếp đường tròn đường kính $CH$. \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Chứng minh $\widehat{AKL} = \widehat{IKC}$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Xét tứ giác $AKHL$ có $\widehat{AKH} = 90^\circ$ và $\widehat{ALH} = 90^\circ \implies \widehat{AKH} + \widehat{ALH} = 180^\circ$.\\
        Do đó tứ giác $AKHL$ nội tiếp đường tròn đường kính $AH$. \hfill \textbf{[0,25đ]}
        \item Suy ra $\widehat{AKL} = \widehat{AHL}$ (hai góc nội tiếp cùng chắn cung $AL$). \hfill \textbf{[0,25đ]}
        \item Trong tứ giác nội tiếp $CIHK$ (đường kính $CH$), ta có $\widehat{IKC} = \widehat{IHC}$ (hai góc nội tiếp cùng chắn cung $IC$).\\
        Mặt khác, hai đường cao $AI$ và $CL$ cắt nhau tại $H$ nên hai góc $\widehat{AHL}$ và $\widehat{IHC}$ là hai góc đối đỉnh $\implies \widehat{AHL} = \widehat{IHC}$.\\
        Từ đó suy ra $\widehat{AKL} = \widehat{IKC}$ (đpcm). \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Chứng minh $KB$ là tia phân giác trong của góc $\widehat{LKI}$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Do $BK \perp AC$ tại $K$ nên $\widehat{AKB} = 90^\circ$ và $\widehat{BKC} = 90^\circ$. \hfill \textbf{[0,25đ]}
        \item Ta có các cặp góc phụ nhau:
        \[
        \widehat{LKB} = \widehat{AKB} - \widehat{AKL} = 90^\circ - \widehat{AKL},
        \]
        \[
        \widehat{IKB} = \widehat{BKC} - \widehat{IKC} = 90^\circ - \widehat{IKC}.
        \] \hfill \textbf{[0,25đ]}
        \item Theo chứng minh câu b ta có $\widehat{AKL} = \widehat{IKC}$, do đó suy ra:
        \[
        \widehat{LKB} = \widehat{IKB}.
        \]
        Vậy $KB$ (hay đoạn thẳng $KH$) là tia phân giác trong của góc $\widehat{LKI}$ của $\triangle IKL$. \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Chứng minh trực tâm $H$ là tâm nội tiếp tam giác $IKL$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Chứng minh hoàn toàn tương tự đối với đỉnh $I$: Xét hai tứ giác nội tiếp $BIHL$ và $CIHK$, ta chứng minh được $\widehat{BI L} = \widehat{CIK} \implies \widehat{LIH} = \widehat{KIH}$.
        Suy ra $IH$ là tia phân giác trong của góc $\widehat{LI K}$ của $\triangle IKL$. \hfill \textbf{[0,25đ]}
        \item Tương tự đối với đỉnh $L$, ta cũng có $LH$ là tia phân giác trong của góc $\widehat{ILK}$ của $\triangle IKL$. \hfill \textbf{[0,25đ]}
        \item Trong tam giác trực tâm $IKL$, ba đường thẳng $KH, IH, LH$ là ba đường phân giác trong cùng đồng quy tại trực tâm $H$.\\
        Vậy trực tâm $H$ chính là tâm của đường tròn nội tiếp tam giác trực tâm $IKL$ (đpcm). \hfill \textbf{[0,25đ]}
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

\begin{pedagogybox}{I. NGHỆ THUẬT SƯ PHẠM: SỰ CHUYỂN HÓA KỲ DIỆU TỪ ĐƯỜNG CAO SANG PHÂN GIÁC}
\begin{itemize}[leftmargin=*]
    \item \textbf{Cội nguồn tư duy:} Trong hình học tam giác, tam giác trực tâm $IKL$ là cấu trúc có tính đối xứng góc cao nhất. Đường cao $BK$ vuông góc với tiếp tuyến của đường tròn ngoại tiếp tam giác trực tâm tại $K$.
    \item \textbf{Kỹ thuật chuyển góc qua phần bù:} Thay vì chứng minh trực tiếp hai góc nhọn bằng nhau, ta lật ngược bài toán bằng cách chứng minh hai góc phụ với chúng bằng nhau: $\widehat{LKB} = \widehat{IKB} \iff 90^\circ - \widehat{AKL} = 90^\circ - \widehat{IKC} \iff \widehat{AKL} = \widehat{IKC}$. Cặp góc mới này lập tức bám vào các dây cung của hai tứ giác nội tiếp!
    \item \textbf{4 câu hỏi dẫn dắt của Giáo viên trên lớp:}
    \begin{enumerate}[label=\arabic*., nosep]
        \item Muốn chứng minh $H$ là tâm đường tròn nội tiếp của $\triangle IKL$, ta cần chỉ ra những đoạn thẳng nào là phân giác?
        \item Đường cao $BK$ vuông góc với $AC$ tạo ra hai góc $90^\circ$ nào tại đỉnh $K$?
        \item Hai góc $\widehat{LKB}$ và $\widehat{IKB}$ lần lượt phụ với hai góc nào?
        \item Hai góc $\widehat{AKL}$ và $\widehat{IKC}$ lần lượt bằng hai góc nào tại đỉnh $H$? Hai góc đó có vị trí gì với nhau?
    \end{enumerate}
\end{itemize}
\end{pedagogybox}

\vspace{1mm}

\begin{pedagogybox}{II. CÁC BẪY TƯ DUY VÀ SAI LẦM HỌC SINH THƯỜNG GẶP}
\begin{itemize}[leftmargin=*, nosep]
    \item \textbf{Bẫy 1 -- Thiếu chứng minh tia phân giác thứ hai:} Rất nhiều học sinh sau khi chứng minh được $KH$ là phân giác của $\widehat{LKI}$ liền kết luận ngay $H$ là tâm nội tiếp. Điểm đồng quy của đường tròn nội tiếp bắt buộc phải là giao của ít nhất hai đường phân giác trong (cần thêm $IH$ hoặc $LH$).
    \item \textbf{Bẫy 2 -- Nhầm lẫn phân giác trong và phân giác ngoài:} Đoạn $AC$ vuông góc với $BK$ nên $AC$ chính là đường phân giác ngoài của góc $\widehat{LKI}$ tại đỉnh $K$. Cần ghi rõ $KB$ là phân giác trong.
\end{itemize}
\end{pedagogybox}

\vspace{1mm}

\begin{exercisebox}{III. BÀI TẬP PHÁT TRIỂN ĐỈNH CAO (LUYỆN TẬP 9+)}
\textbf{Bài toán phát triển 1 (Tam giác đồng dạng \& Tỉ số diện tích):}\\
Chứng minh rằng ba tam giác $\triangle AKL, \triangle B I L, \triangle CIK$ đều đồng dạng với $\triangle ABC$. Từ đó chứng minh hệ thức diện tích:
\[
S_{\triangle IKL} = \left(1 - \cos^2 A - \cos^2 B - \cos^2 C\right) S_{\triangle ABC}.
\]
\textit{(Gợi ý: Tứ giác $BCLK$ nội tiếp $\implies \triangle AKL \backsim \triangle ABC$ theo tỉ số $k_1 = \cos A$. Tương tự cho hai đỉnh còn lại, rồi lấy diện tích tam giác lớn trừ ba tam giác góc nhọn xung quanh).}\\[2mm]
\textbf{Bài toán phát triển 2 (Định lý Cực trị Fagnano):}\\
Trong tất cả các tam giác có ba đỉnh lần lượt nằm trên ba cạnh của tam giác nhọn $ABC$, chứng minh rằng tam giác trực tâm $IKL$ có chu vi nhỏ nhất.\\[1mm]
\textit{(Gợi ý: Dùng tính chất góc phản xạ ánh sáng $\widehat{AKL} = \widehat{IKC}$ và phép đối xứng trục qua ba cạnh của tam giác $ABC$).}
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
        print(f"Return code: {res.returncode}")
        with open(os.path.join(folder, base_name + '.log'), 'r', encoding='utf-8', errors='ignore') as f:
            print("Tail of log:\n" + "\n".join(f.readlines()[-35:]))

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tex_file = os.path.join(base_dir, 'SO_DO_TU_DUY_NGUOC_HINH9.tex')
    create_tex_file(tex_file)
    compile_pdf(tex_file)
