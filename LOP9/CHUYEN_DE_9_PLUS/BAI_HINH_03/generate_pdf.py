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
\lhead{\small\textbf{TOÁN 9+ | BẺ KHÓA HÌNH HỌC VÀO LỚP 10}}
\rhead{\small\textbf{BÀI 03: TRỰC TÂM \& TIẾP TUYẾN EULER}}
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
    {\large\bfseries BÀI HÌNH 03: ĐƯỜNG TRÒN ĐƯỜNG KÍNH CẠNH ĐÁY \& TIẾP TUYẾN TRUNG ĐIỂM}\\[1mm]
    \textit{(Trích xuất và phát triển từ Đề 03 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10)}
\end{center}

\vspace{1mm}

\begin{modelbox}{I. ĐỀ BÀI TOÁN GỐC (TRÍCH ĐỀ 03)}
Cho tam giác $ABC$ có ba góc nhọn ($AB < AC$). Vẽ đường tròn $(O)$ đường kính $BC$. Đường tròn $(O)$ cắt các cạnh $AB, AC$ lần lượt tại $D$ và $E$ ($D \ne B, E \ne C$). Gọi $H$ là giao điểm của $BE$ và $CD$.
\begin{enumerate}[label=\textbf{\alph*)}]
    \item Chứng minh bốn điểm $A, D, H, E$ cùng nằm trên một đường tròn. Xác định vị trí tâm $I$ của đường tròn đó.
    \item Chứng minh $AE \cdot AC = AB \cdot AD$ và $\triangle ADE \backsim \triangle ACB$.
    \item \textbf{(Phân hóa 9+):} Gọi $I$ là trung điểm của $AH$. Chứng minh $IE$ là tiếp tuyến của đường tròn $(O)$ đường kính $BC$.
\end{enumerate}
\end{modelbox}

\vspace{1mm}

\begin{center}
\begin{tikzpicture}[line join = round, line cap=round, >=stealth, font=\footnotesize, scale=1.15]
    % Tham số
    \def\r{3.0}
    
    % Tọa độ các điểm
    \coordinate (O) at (0,0);
    \coordinate (B) at (-\r,0);
    \coordinate (C) at (\r,0);
    \coordinate (A) at (-0.9, 4.4); % Tam giác nhọn, AB < AC
    
    % Chân các đường cao
    \coordinate (D) at ($(A)!(C)!(B)$); % Chân đường cao CD
    \coordinate (E) at ($(A)!(B)!(C)$); % Chân đường cao BE
    \coordinate (H) at (intersection of B--E and C--D);
    \coordinate (I) at ($(A)!0.5!(H)$); % I là trung điểm AH
    \coordinate (K) at ($(B)!(A)!(C)$); % K là hình chiếu của A lên BC
    
    % Vẽ đường tròn (O) và (I)
    \draw[thick, teal] (O) circle (\r);
    \draw[dashed, blue!60] let \p1 = ($(I)-(A)$), \n1 = {veclen(\x1,\y1)} in (I) circle (\n1);
    
    % Vẽ các cạnh tam giác
    \draw[thick] (A) -- (B) -- (C) -- cycle;
    \draw[thick, blue!80!black] (B) -- (E);
    \draw[thick, blue!80!black] (C) -- (D);
    \draw[dashed, red!80!black] (A) -- (K);
    \draw[thick, red] (I) -- (E);
    \draw[thick, orange!90!black] (O) -- (E);
    \draw[dashed, purple] (D) -- (E);
    
    % Ký hiệu góc vuông
    \pic[draw, angle radius=2.5mm]{right angle = C--D--A};
    \pic[draw, angle radius=2.5mm]{right angle = B--E--A};
    \pic[draw, angle radius=2.5mm]{right angle = A--K--C};
    \pic[draw, red, angle radius=2.8mm]{right angle = I--E--O};
    
    % Điểm
    \fill (O) circle (1.5pt) node[below] {$O$};
    \fill (B) circle (1.5pt) node[below left] {$B$};
    \fill (C) circle (1.5pt) node[below right] {$C$};
    \fill (A) circle (1.5pt) node[above] {$A$};
    \fill (D) circle (1.5pt) node[above left] {$D$};
    \fill (E) circle (1.5pt) node[above right] {$E$};
    \fill (H) circle (1.5pt) node[below right=1pt] {$H$};
    \fill[red] (I) circle (1.5pt) node[left] {$I$};
    \fill (K) circle (1.5pt) node[below] {$K$};
\end{tikzpicture}
\end{center}

\vspace{1mm}

\begin{pedagogybox}{II. MỤC TIÊU TRỌNG TÂM \& BẢN ĐỒ TƯ DUY 9+}
\begin{itemize}[leftmargin=*, nosep]
    \item \textbf{Cốt lõi hình học:} Điểm $E$ là giao điểm của hai đường tròn $(I)$ đường kính $AH$ và $(O)$ đường kính $BC$. Muốn chứng minh $IE$ là tiếp tuyến của $(O)$, ta cần chứng minh $IE \perp OE \iff \widehat{IEO} = 90^\circ$.
    \item \textbf{Đòn bẩy tư duy ngược:} Phân rã góc $\widehat{IEO} = \widehat{IEH} + \widehat{HEO}$, sau đó chuyển đổi hai góc này thành hai góc đáy của hai tam giác cân $\triangle IEH$ (đỉnh $I$) và $\triangle OBE$ (đỉnh $O$). Tổng của hai góc đáy này quy về hai góc nhọn phụ nhau của tam giác vuông $BHK$ tại chân đường cao $K$!
\end{itemize}
\end{pedagogybox}

\newpage

% ==============================================================
% TRANG 2: SƠ ĐỒ TƯ DUY NGƯỢC HÌNH CÂY THÔNG
% ==============================================================
\begin{center}
    {\Large\bfseries\color{blue!80!black} SƠ ĐỒ TƯ DUY NGƯỢC HÌNH CÂY THÔNG (PINE-TREE FORMULA TREE)}\\[1.5mm]
    {\large\bfseries BẺ KHÓA: CHỨNG MINH TIẾP TUYẾN $IE \perp OE$ TẠI $E \in (O)$}\\[1mm]
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
        inner sep=6pt, align=center, text width=11.0cm
    },
    step_node/.style={
        rectangle, draw=blue!80!black, fill=blue!8, line width=1.1pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=13.0cm
    },
    aux_node/.style={
        rectangle, draw=orange!90!black, fill=orange!12, line width=1.2pt, rounded corners=2mm,
        inner sep=5pt, align=center, text width=14.5cm
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
        inner sep=6pt, align=center, text width=16.5cm
    }
]

% Đỉnh cây thông
\node[target_node] (T1) at (0, 0) {
    \textbf{\large\color{red!85!black} [ĐÍCH ĐẾN]:\ $IE$ LÀ TIẾP TUYẾN CỦA $(O)$ TẠI $E$}\\[1mm]
    $\boldsymbol{\iff IE \perp OE \iff \widehat{IEO} = 90^\circ \quad (E \in (O))}$
};

% Tầng 2
\node[step_node] (T2) at (0, -1.9) {
    $\boldsymbol{\Uparrow} \quad \text{Phân rã góc qua tia } EH:\quad \boldsymbol{\widehat{IEO} = \widehat{IEH} + \widehat{HEO} = 90^\circ}$
};

% Tầng 3
\node[aux_node] (T3) at (0, -3.8) {
    $\boldsymbol{\Uparrow} \quad \text{Quy đổi về hai góc đáy tam giác cân:}\quad \boldsymbol{\widehat{KHB} + \widehat{KBH} = 90^\circ}$\\[1mm]
    \textit{($H$ là trực tâm $\implies AH \perp BC$ tại $K \implies \triangle BHK$ vuông tại $K$)}
};

% Tầng 4: Hai nhánh
\node[branch_node] (T4_left) at (-4.2, -6.1) {
    \textbf{\color{purple!90!black} [NHÁNH 1 -- TAM GIÁC CÂN ĐỈNH $I$]:}\\[1mm]
    $\triangle AEH$ vuông tại $E$, $I$ là trung điểm $AH$\\[0.8mm]
    $\implies IE = IH = \dfrac{AH}{2} \implies \triangle IEH \text{ cân tại } I$\\[0.8mm]
    $\boldsymbol{\implies \widehat{IEH} = \widehat{IHE} = \widehat{KHB}} \quad \text{(đối đỉnh)}$
};

\node[branch_node] (T4_right) at (4.2, -6.1) {
    \textbf{\color{purple!90!black} [NHÁNH 2 -- TAM GIÁC CÂN ĐỈNH $O$]:}\\[1mm]
    $E, B \in (O) \implies OE = OB = R$\\[0.8mm]
    $\implies \triangle OBE \text{ cân tại } O$\\[0.8mm]
    $\boldsymbol{\implies \widehat{HEO} = \widehat{BEO} = \widehat{KBH}}$
};

% Tầng 5: Tam giác vuông BHK
\node[sim_node] (T5) at (0, -8.5) {
    $\boldsymbol{\Uparrow} \quad \text{Tam giác } BHK \text{ vuông tại } K \implies \boldsymbol{\widehat{KHB} + \widehat{KBH} = 90^\circ} \quad \left(AH \perp BC \text{ tại } K\right)$
};

% Bệ đỡ khởi phát
\node[base_node] (T6) at (0, -10.6) {
    \textbf{\color{teal!95!black} [GỐC RỄ KHỞI PHÁT]:}\\[1mm]
    $D, E \in (O) \text{ đường kính } BC \implies \boldsymbol{\widehat{BDC} = \widehat{BEC} = 90^\circ}$ (Góc nội tiếp chắn nửa đường tròn)\\[1mm]
    $\boldsymbol{\implies CD \perp AB \quad \text{và} \quad BE \perp AC \implies H \text{ LÀ TRỰC TÂM } \triangle ABC \implies AH \perp BC \text{ TẠI } K}$
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
    \item \textbf{Bổ đề đường trung tuyến tam giác vuông:} $\triangle AEH$ vuông tại $E \implies IE = IA = IH = \dfrac{AH}{2}$.
    \item \textbf{Phương pháp phân rã góc chứng minh tiếp tuyến:} Để chứng minh $IE \perp OE$, ta chẻ góc bẹt qua cát tuyến $BE$, tận dụng hai tam giác cân có đỉnh là hai tâm đường tròn: $\widehat{IEO} = \widehat{IEH} + \widehat{HEO} = \widehat{KHB} + \widehat{KBH} = 90^\circ$.
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
    \item \textbf{Chứng minh bốn điểm $A, D, H, E$ cùng thuộc đường tròn $(I)$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Vì $D, E$ thuộc đường tròn $(O)$ đường kính $BC$ nên $\widehat{BDC} = 90^\circ$ và $\widehat{BEC} = 90^\circ$ (góc nội tiếp chắn nửa đường tròn). \hfill \textbf{[0,25đ]}
        \item Suy ra $CD \perp AB \implies \widehat{ADH} = 90^\circ$ và $BE \perp AC \implies \widehat{AEH} = 90^\circ$.
        \item Xét tứ giác $ADHE$ có tổng hai góc đối diện:
        \[
        \widehat{ADH} + \widehat{AEH} = 90^\circ + 90^\circ = 180^\circ.
        \]
        Do đó tứ giác $ADHE$ nội tiếp đường tròn đường kính $AH$. \hfill \textbf{[0,25đ]}
        \item Tâm $I$ của đường tròn này là trung điểm của đoạn thẳng $AH$. \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Chứng minh $AE \cdot AC = AB \cdot AD$ và $\triangle ADE \backsim \triangle ACB$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Xét hai tam giác vuông $\triangle AEB$ và $\triangle ADC$ có:
        \[
        \widehat{AEB} = \widehat{ADC} = 90^\circ \quad \text{và} \quad \widehat{BAC} \text{ là góc chung.}
        \]
        Suy ra $\triangle AEB \backsim \triangle ADC$ (g-g). \hfill \textbf{[0,25đ]}
        \item Do đó ta có tỉ số đồng dạng: $\dfrac{AE}{AD} = \dfrac{AB}{AC} \implies AE \cdot AC = AB \cdot AD$. \hfill \textbf{[0,25đ]}
        \item Từ $AE \cdot AC = AB \cdot AD \implies \dfrac{AE}{AB} = \dfrac{AD}{AC}$. Kết hợp với góc $\widehat{BAC}$ chung, suy ra $\triangle ADE \backsim \triangle ACB$ (c-g-c). \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Thiết lập hai tam giác cân từ tâm $I$ và tâm $O$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Trong tam giác $ABC$, hai đường cao $BE$ và $CD$ cắt nhau tại $H \implies H$ là trực tâm của $\triangle ABC$. Suy ra $AH \perp BC$ tại điểm $K$. \hfill \textbf{[0,25đ]}
        \item Xét $\triangle AEH$ vuông tại $E$ có $I$ là trung điểm cạnh huyền $AH$, theo tính chất đường trung tuyến ứng với cạnh huyền ta có $IE = IH = \dfrac{AH}{2}$.
        Suy ra $\triangle IEH$ cân tại $I \implies \widehat{IEH} = \widehat{IHE}$.
        Mặt khác tia $HI$ đối tia $HK$, tia $HE$ đối tia $HB$ nên $\widehat{IHE} = \widehat{KHB}$ (hai góc đối đỉnh). Do đó $\widehat{IEH} = \widehat{KHB}$. \hfill \textbf{[0,25đ]}
        \item Do $E, B \in (O)$ nên $OE = OB = R \implies \triangle OBE$ cân tại $O \implies \widehat{BEO} = \widehat{OBE}$.
        Vì $H \in BE$ và $K \in BC$ nên $\widehat{HEO} = \widehat{KBH}$. \hfill \textbf{[0,25đ]}
    \end{itemize}

    \vspace{1mm}
    \item \textbf{Chứng minh $IE$ là tiếp tuyến của $(O)$ tại điểm $E$ (0,75 điểm)}
    \begin{itemize}[leftmargin=*, nosep]
        \item Do điểm $I$ thuộc đoạn $AH$ và điểm $O$ thuộc đoạn $BC$ nằm về hai phía khác nhau so với đường thẳng $BE$, nên tia $EH$ nằm giữa hai tia $EI$ và $EO$. Ta có:
        \[
        \widehat{IEO} = \widehat{IEH} + \widehat{HEO} = \widehat{KHB} + \widehat{KBH}.
        \] \hfill \textbf{[0,25đ]}
        \item Xét tam giác $BHK$ vuông tại $K$ ($AH \perp BC$), ta có hai góc nhọn phụ nhau:
        \[
        \widehat{KHB} + \widehat{KBH} = 90^\circ.
        \]
        Suy ra $\widehat{IEO} = 90^\circ \implies IE \perp OE$ tại điểm $E$. \hfill \textbf{[0,25đ]}
        \item Mà điểm $E$ thuộc đường tròn $(O)$. Vậy $IE$ là tiếp tuyến của đường tròn $(O)$ đường kính $BC$ (đpcm). \hfill \textbf{[0,25đ]}
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

\begin{pedagogybox}{I. NGHỆ THUẬT SƯ PHẠM: TẠI SAO LẠI NGHĨ RA CÁCH CHẺ ĐÔI GÓC?}
\begin{itemize}[leftmargin=*]
    \item \textbf{Cội nguồn tư duy:} Đoạn thẳng $IE$ không thuộc tam giác vuông nào trực tiếp chứa cạnh $OE$. Nhưng điểm $E$ lại là điểm đồng quy của hai đường tròn có hai tâm đã biết là $I$ và $O$.
    \item \textbf{Đường nối phân rã:} Cát tuyến $BE$ nối hai đường tròn này. Khi hạ tia $EH$, góc lớn $\widehat{IEO}$ lập tức tách thành hai góc con: một góc gắn liền với tâm $I$ ($\triangle IEH$ cân), một góc gắn liền với tâm $O$ ($\triangle OBE$ cân). Kỹ thuật này gọi là \textbf{"Phân rã góc bẹt qua cát tuyến chung"}.
    \item \textbf{4 câu hỏi dẫn dắt của Giáo viên trên lớp:}
    \begin{enumerate}[label=\arabic*., nosep]
        \item Muốn chứng minh $IE$ là tiếp tuyến của $(O)$ tại điểm $E$, ta cần chứng minh góc nào bằng $90^\circ$?
        \item Tia $EH$ chia góc $\widehat{IEO}$ thành tổng của hai góc nào?
        \item Trong hai góc con đó, góc $\widehat{IEH}$ chuyển thành góc nào nhờ tam giác cân đỉnh $I$? Góc $\widehat{HEO}$ chuyển thành góc nào nhờ tam giác cân đỉnh $O$?
        \item Hai góc đáy vừa tìm được có quan hệ gì với tam giác vuông $BHK$ tại chân đường cao $K$?
    \end{enumerate}
\end{itemize}
\end{pedagogybox}

\vspace{1mm}

\begin{pedagogybox}{II. CÁC BẪY TƯ DUY VÀ SAI LẦM HỌC SINH THƯỜNG GẶP}
\begin{itemize}[leftmargin=*, nosep]
    \item \textbf{Bẫy 1 -- Quên chỉ ra điểm $E \in (O)$:} Nhiều học sinh chỉ chứng minh $IE \perp OE$ rồi kết luận ngay là tiếp tuyến. Theo chuẩn đáp án tuyển sinh, nếu thiếu câu khẳng định $E \in (O)$ sẽ bị trừ $0{,}25$đ.
    \item \textbf{Bẫy 2 -- Xác định sai góc đối đỉnh:} Học sinh hay ngộ nhận $\widehat{IHE}$ đối đỉnh với $\widehat{BHD}$. Thực tế, tia $HI$ và tia $HK$ mới là hai tia đối nhau (vì $A, I, H, K$ thẳng hàng), do đó góc đối đỉnh chính xác với $\widehat{IHE}$ phải là góc $\widehat{KHB}$.
\end{itemize}
\end{pedagogybox}

\vspace{1mm}

\begin{exercisebox}{III. BÀI TẬP PHÁT TRIỂN ĐỈNH CAO (LUYỆN TẬP 9+)}
\textbf{Bài toán phát triển 1 (Hệ thống tiếp tuyến Euler):}\\
Chứng minh rằng đoạn thẳng $ID$ cũng là tiếp tuyến của đường tròn $(O)$ đường kính $BC$. Từ đó suy ra bốn điểm $I, D, O, E$ cùng nằm trên một đường tròn và $IO \perp DE$.\\[1mm]
\textit{(Gợi ý: Chứng minh hoàn toàn tương tự cho $\triangle ADH$ vuông tại $D$, ta có $ID = IH \implies \triangle IDH$ cân tại $I$. Khi đó $\widehat{IDO} = 90^\circ$, suy ra $ID$ và $IE$ là hai tiếp tuyến cắt nhau tại $I$ của $(O)$ nên $IO$ là trung trực của $DE$).}\\[2mm]
\textbf{Bài toán phát triển 2 (Hệ thức diện tích và Lượng giác):}\\
Chứng minh rằng tỉ số diện tích giữa $\triangle ADE$ và $\triangle ABC$ thỏa mãn hệ thức:
\[
\dfrac{S_{\triangle ADE}}{S_{\triangle ABC}} = \cos^2 A.
\]
\textit{(Gợi ý: Do $\triangle ADE \backsim \triangle ACB$ theo tỉ số $k = \dfrac{AE}{AB} = \cos A$, do đó tỉ số diện tích bằng bình phương tỉ số đồng dạng $k^2 = \cos^2 A$).}
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
