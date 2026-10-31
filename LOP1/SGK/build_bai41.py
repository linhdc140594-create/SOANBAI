# -*- coding: utf-8 -*-
"""
Script tạo đề kiểm tra chuẩn 5 trang cho Bài 41: Ôn tập chung cuối năm
Đảm bảo 100% các câu hỏi đều có hình minh họa TikZ 2D trực quan.
Cấu trúc:
- Phần 1: 12 câu trắc nghiệm chia đều cho 3 trang (Trang 1, 2, 3: 4 câu/trang).
- Phần 2: 4 câu trắc nghiệm đúng sai (Trang 4).
- Phần 3: 4 câu trả lời ngắn (Trang 5).
"""

content = r'''% =========================================================================
% BÀI 41: ÔN TẬP CHUNG CUỐI NĂM
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 41 ---

% 1. Vẽ đồng hồ kim tròn
\providecommand{\VeBamiMotDongHo}[3]{% #1=(x,y), #2=giờ, #3=phút
  \begin{scope}[shift={(#1)}, scale=0.48]
    \draw[fill=blue!5, draw=blue!85, line width=1.3pt] (0,0) circle (1.25cm);
    \draw[fill=blue!85] (0,0) circle (0.07cm);
    \foreach \h in {1,...,12} {
      \pgfmathsetmacro{\ang}{90 - \h * 30}
      \draw[line width=0.6pt, blue!70] (\ang:1.1cm) -- (\ang:1.23cm);
      \ifcase\h\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {1};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {2};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {3};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {4};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {5};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {6};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {7};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {8};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {9};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {10};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {11};\or
        \node[font=\tiny\bfseries] at (\ang:0.92cm) {12};\fi
    }
    % Kim giờ (ngắn)
    \pgfmathsetmacro{\hAng}{90 - (#2 + #3/60)*30}
    \draw[->, >=stealth, line width=1.5pt, red!85!black] (0,0) -- (\hAng:0.65cm);
    % Kim phút (dài)
    \pgfmathsetmacro{\mAng}{90 - #3*6}
    \draw[->, >=stealth, line width=1.1pt, blue!90!black] (0,0) -- (\mAng:0.95cm);
  \end{scope}
}

% 2. Vẽ khối lập phương 3D
\providecommand{\VeBamiMotKhoiLapPhuong}[2]{% #1=(x,y), #2=scale
  \begin{scope}[shift={(#1)}, scale=#2]
    \draw[fill=blue!15, draw=blue!85, line width=0.8pt] (0,0) rectangle (1.2,1.2);
    \draw[fill=blue!25, draw=blue!85, line width=0.8pt] (0,1.2) -- (0.5,1.6) -- (1.7,1.6) -- (1.2,1.2) -- cycle;
    \draw[fill=blue!10, draw=blue!85, line width=0.8pt] (1.2,0) -- (1.7,0.4) -- (1.7,1.6) -- (1.2,1.2) -- cycle;
  \end{scope}
}

% 3. Vẽ bó que tính chục
\providecommand{\VeBamiMotBoQue}[2]{% #1=(x,y), #2=scale
  \begin{scope}[shift={(#1)}, scale=#2]
    \draw[fill=orange!25, draw=orange!80, line width=0.6pt, rounded corners=1pt] (-0.3,-0.6) rectangle (0.3,0.6);
    \draw[line width=1.2pt, red!85] (-0.35,-0.05) -- (0.35,-0.05);
    \draw[line width=1.2pt, red!85] (-0.35,0.05) -- (0.35,0.05);
    \node[font=\tiny\bfseries, color=orange!90!black] at (0,-0.8) {10};
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Cấu tạo số gồm 7 chục và 5 đơn vị
\begin{ex} %[1D10N41]
Quan sát hình ảnh các bó que tính chục và que tính rời:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.7]
  % 7 bó que tính chục
  \foreach \i in {1,...,7} {
    \pgfmathsetmacro{\x}{-5.5 + (\i-1)*0.8}
    \VeBamiMotBoQue{\x,0}{0.65}
  }
  \node[below=2pt, font=\bfseries\tiny, color=orange!90!black] at (-3.1,-0.65) {7 chục que tính};
  % Dấu cộng
  \node[font=\bfseries\normalsize, color=black!60] at (0.2,0) {$+$};
  % 5 que rời
  \foreach \j in {1,...,5} {
    \pgfmathsetmacro{\xj}{0.8 + (\j-1)*0.4}
    \draw[line width=1.8pt, teal!85] (\xj,-0.4) -- (\xj,0.4);
  }
  \node[below=2pt, font=\bfseries\tiny, color=teal!90!black] at (1.6,-0.65) {5 que rời};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Số gồm $7$ chục và $5$ đơn vị được viết là
\begin{multicols}{4}
\choice
{$57$}
{\True $75$}
{$70$}
{$12$}
\end{multicols}
\loigiai{
Số gồm 7 chục và 5 đơn vị có chữ số hàng chục là $7$, chữ số hàng đơn vị là $5$, viết là $75$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Số liền trước của số 100
\begin{ex} %[1D10N41]
Quan sát thứ tự các số trên đoàn tàu hỏa dưới đây:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  % Toa 1: 98
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (T1) at (-3.2,0) {\bfseries\small\color{blue!90!black} 98};
  % Toa 2: ?
  \node[draw=red!80, fill=yellow!25, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (T2) at (0,0) {\bfseries\small\color{red!90!black} ?};
  % Toa 3: 100
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (T3) at (3.2,0) {\bfseries\small\color{teal!90!black} 100};
  % Mũi tên liên kết
  \draw[->, >=stealth, line width=1.1pt, blue!70] (T1) -- (T2) node[midway, above=1pt, font=\tiny] {$+1$};
  \draw[->, >=stealth, line width=1.1pt, red!85] (T2) -- (T3) node[midway, above=1pt, font=\tiny] {$+1$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Số liền trước của số $100$ là số nào?
\begin{multicols}{4}
\choice
{$101$}
{\True $99$}
{$98$}
{$90$}
\end{multicols}
\loigiai{
Số liền trước của $100$ là số đứng ngay trước số $100$ khi đếm xuôi: $100 - 1 = 99$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Phép cộng hai số tròn chục: 50 + 40
\begin{ex} %[1D10N41]
Gộp hai túi bóng tròn chục lại với nhau:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=4pt, inner xsep=10pt, inner ysep=5pt] (T1) at (-2.5,0) {\bfseries\small\color{blue!90!black} 50 quả};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=orange!80, fill=orange!15, line width=1pt, rounded corners=4pt, inner xsep=10pt, inner ysep=5pt] (T2) at (2.5,0) {\bfseries\small\color{orange!90!black} 40 quả};
  \draw[->, >=stealth, line width=1.2pt, purple!80] (0,-0.4) -- (0,-1.0) node[below=2pt, font=\bfseries\small, color=purple!90!black] {Tổng cộng: ? quả};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $50 + 40$ là
\begin{multicols}{4}
\choice
{$80$}
{\True $90$}
{$100$}
{$70$}
\end{multicols}
\loigiai{
Cộng các số tròn chục: $5\text{ chục} + 4\text{ chục} = 9\text{ chục} = 90$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Phép cộng hai chữ số không nhớ: 65 + 23
\begin{ex} %[1D10H41]
Sơ đồ gộp hai phần số để tính tổng:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (A) at (-2.2,0.4) {\bfseries\small\color{teal!90!black} $65$};
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (B) at (-2.2,-0.4) {\bfseries\small\color{teal!90!black} $23$};
  \node[draw=red!80, fill=yellow!25, line width=1.2pt, rounded corners=4pt, inner xsep=10pt, inner ysep=5pt] (C) at (2.2,0) {\bfseries\small\color{red!90!black} Tổng: ?};
  \draw[->, >=stealth, line width=1.1pt, teal!80] (A.east) -- (C.west);
  \draw[->, >=stealth, line width=1.1pt, teal!80] (B.east) -- (C.west);
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $65 + 23$ là
\begin{multicols}{4}
\choice
{$87$}
{\True $88$}
{$89$}
{$90$}
\end{multicols}
\loigiai{
Thực hiện cộng từ hàng đơn vị sang hàng chục: $5 + 3 = 8$; $6 + 2 = 8$. Vậy $65 + 23 = 88$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Phép trừ hai chữ số không nhớ: 79 - 35
\begin{ex} %[1D10H41]
Băng giấy dài có số đo $79$, bị cắt bớt một phần có số đo $35$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  % Toàn bộ
  \draw[fill=blue!10, draw=blue!80, line width=1pt] (-3.5,0) rectangle (3.5,0.7);
  \node[font=\bfseries\tiny, color=blue!90!black] at (0,0.35) {Cả băng giấy: $79$};
  % Phần cắt bớt
  \draw[fill=red!20, draw=red!85, line width=1pt] (-3.5,-0.9) rectangle (-0.5,-0.3);
  \node[font=\bfseries\tiny, color=red!90!black] at (-2.0,-0.6) {Cắt bớt: $35$};
  % Phần còn lại
  \draw[fill=teal!20, draw=teal!85, line width=1pt] (-0.5,-0.9) rectangle (3.5,-0.3);
  \node[font=\bfseries\tiny, color=teal!90!black] at (1.5,-0.6) {Còn lại: ?};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $79 - 35$ là
\begin{multicols}{4}
\choice
{$43$}
{\True $44$}
{$45$}
{$46$}
\end{multicols}
\loigiai{
Trừ hàng đơn vị: $9 - 5 = 4$; Trừ hàng chục: $7 - 3 = 4$. Vậy $79 - 35 = 44$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: So sánh hai vế biểu thức: 43 + 32 ... 98 - 23
\begin{ex} %[1D10H41]
Cân đĩa thăng bằng đặt hai biểu thức ở hai bên:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  % Trục cân
  \draw[line width=2pt, gray!70] (0,-0.6) -- (0,0.5);
  \draw[line width=2pt, gray!70] (-1.0,-0.6) -- (1.0,-0.6);
  \draw[line width=2.5pt, blue!80] (-3.0,0.5) -- (3.0,0.5);
  \draw[fill=red!85] (0,0.5) circle (0.1cm);
  % Đĩa trái: 43 + 32
  \draw[line width=1pt, gray!70] (-3.0,0.5) -- (-3.0,-0.2);
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (-3.0,-0.4) {\bfseries\scriptsize $43 + 32$};
  % Đĩa phải: 98 - 23
  \draw[line width=1pt, gray!70] (3.0,0.5) -- (3.0,-0.2);
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (3.0,-0.4) {\bfseries\scriptsize $98 - 23$};
  % Dấu ở giữa
  \node[draw=red!80, fill=yellow!25, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=2pt] at (0,0.9) {\bfseries\small\color{red!90!black} ?};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Điền dấu thích hợp vào chỗ chấm: $43 + 32 \dots 98 - 23$.
\begin{multicols}{4}
\choice
{$>$}
{\True $=$}
{$<$}
{Không so sánh được}
\end{multicols}
\loigiai{
Tính giá trị hai vế: $43 + 32 = 75$ và $98 - 23 = 75$. Vì $75 = 75$ nên điền dấu $=$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Nhận biết hình tròn: không có cạnh và không có đỉnh
\begin{ex} %[1H10H41]
Quan sát bốn hình phẳng dưới đây:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  % Hình vuông
  \draw[fill=teal!15, draw=teal!80, line width=1pt] (-5.2,-0.5) rectangle (-4.0,0.7);
  \node[below=2pt, font=\bfseries\tiny, color=teal!90!black] at (-4.6,-0.5) {Hình vuông};
  % Hình tròn
  \draw[fill=purple!15, draw=purple!80, line width=1pt] (-1.6,0.1) circle (0.6cm);
  \node[below=2pt, font=\bfseries\tiny, color=purple!90!black] at (-1.6,-0.5) {Hình tròn};
  % Hình tam giác
  \draw[fill=orange!15, draw=orange!80, line width=1pt] (0.8,-0.5) -- (2.0,-0.5) -- (1.4,0.7) -- cycle;
  \node[below=2pt, font=\bfseries\tiny, color=orange!90!black] at (1.4,-0.5) {Hình tam giác};
  % Hình chữ nhật
  \draw[fill=blue!15, draw=blue!80, line width=1pt] (3.8,-0.5) rectangle (5.4,0.7);
  \node[below=2pt, font=\bfseries\tiny, color=blue!90!black] at (4.6,-0.5) {Hình chữ nhật};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Hình nào sau đây là đường cong khép kín, không có cạnh và không có đỉnh?
\begin{multicols}{4}
\choice
{Hình vuông}
{\True Hình tròn}
{Hình tam giác}
{Hình chữ nhật}
\end{multicols}
\loigiai{
Hình tròn được bao quanh bởi một đường cong tròn khép kín, không có cạnh thẳng và không có đỉnh.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Tính giá trị biểu thức: 42 + 25 - 14
\begin{ex} %[1D10V41]
Sơ đồ chuỗi phép tính hai bước liên tiếp:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (A) at (-3.6,0) {\bfseries\small 42};
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (B) at (0,0) {\bfseries\small 67};
  \node[draw=red!80, fill=yellow!25, line width=1.2pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (C) at (3.6,0) {\bfseries\small\color{red!90!black} ?};
  \draw[->, >=stealth, line width=1.2pt, blue!75] (A) -- (B) node[midway, above=1pt, font=\bfseries\tiny, color=blue!90!black] {$+25$};
  \draw[->, >=stealth, line width=1.2pt, red!85] (B) -- (C) node[midway, above=1pt, font=\bfseries\tiny, color=red!90!black] {$-14$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Giá trị thích hợp điền vào dấu hỏi chấm là
\begin{multicols}{4}
\choice
{$52$}
{\True $53$}
{$54$}
{$55$}
\end{multicols}
\loigiai{
Thực hiện từ trái sang phải: Bước 1: $42 + 25 = 67$; Bước 2: $67 - 14 = 53$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Học sinh hai lớp 1A và 1B
\begin{ex} %[1D10V41]
Số học sinh của hai lớp 1A và 1B được biểu thị bằng sơ đồ khối:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (L1) at (-2.4,0.35) {\bfseries\small Lớp 1A: $35$ bạn};
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (L2) at (-2.4,-0.35) {\bfseries\small Lớp 1B: $34$ bạn};
  \node[draw=red!80, fill=yellow!25, line width=1.2pt, rounded corners=4pt, inner xsep=10pt, inner ysep=5pt] (Tong) at (2.4,0) {\bfseries\small\color{red!90!black} Cả hai lớp: ?};
  \draw[->, >=stealth, line width=1.1pt, blue!75] (L1.east) -- (Tong.west);
  \draw[->, >=stealth, line width=1.1pt, teal!75] (L2.east) -- (Tong.west);
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Cả hai lớp có tất cả số học sinh là
\begin{multicols}{4}
\choice
{$68$ bạn}
{\True $69$ bạn}
{$70$ bạn}
{$71$ bạn}
\end{multicols}
\loigiai{
Cả hai lớp có tất cả số học sinh là: $35 + 34 = 69$ bạn.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Đoạn dây 95 cm cắt bớt 40 cm
\begin{ex} %[1H10V41]
Đoạn dây dài $95\text{ cm}$, cắt bớt đi một đoạn $40\text{ cm}$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  \draw[fill=blue!12, draw=blue!85, line width=1pt, rounded corners=3pt] (-3.8,-0.3) rectangle (3.8,0.3);
  \node[font=\bfseries\tiny, color=blue!90!black] at (0,0) {Đoạn dây ban đầu dài: $95\text{ cm}$};
  \draw[fill=red!20, draw=red!85, line width=1pt] (-3.8,-0.9) rectangle (-0.6,-0.4);
  \node[font=\bfseries\tiny, color=red!90!black] at (-2.2,-0.65) {Cắt: $40\text{ cm}$};
  \draw[fill=teal!20, draw=teal!85, line width=1pt] (-0.6,-0.9) rectangle (3.8,-0.4);
  \node[font=\bfseries\tiny, color=teal!90!black] at (1.6,-0.65) {Còn lại: ? cm};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Đoạn dây còn lại dài bao nhiêu xăng-ti-mét?
\begin{multicols}{4}
\choice
{$54\text{ cm}$}
{\True $55\text{ cm}$}
{$56\text{ cm}$}
{$57\text{ cm}$}
\end{multicols}
\loigiai{
Thực hiện phép trừ: $95\text{ cm} - 40\text{ cm} = 55\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Đồng hồ chỉ 8 giờ sáng, sau 3 giờ nữa
\begin{ex} %[1H10V41]
Mặt đồng hồ lúc 8 giờ sáng và tiến trình sau 3 giờ nữa:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.85]
  \VeBamiMotDongHo{-2.4,0}{8}{0}
  \node[below=2pt, font=\bfseries\tiny, color=blue!90!black] at (-2.4,-0.65) {8 giờ sáng};
  \draw[->, >=stealth, line width=1.3pt, red!85] (-1.0,0) -- (1.0,0) node[midway, above=1pt, font=\bfseries\tiny, color=red!90!black] {Sau 3 giờ};
  \VeBamiMotDongHo{2.4,0}{11}{0}
  \node[below=2pt, font=\bfseries\tiny, color=teal!90!black] at (2.4,-0.65) {? giờ};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Đồng hồ chỉ $8$ giờ sáng, sau $3$ giờ nữa sẽ là mấy giờ?
\begin{multicols}{4}
\choice
{$10$ giờ sáng}
{\True $11$ giờ trưa}
{$12$ giờ trưa}
{$9$ giờ sáng}
\end{multicols}
\loigiai{
Cộng thêm số giờ: $8 + 3 = 11$ giờ trưa.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Thứ Tư tuần này ngày 10, Thứ Tư tuần sau
\begin{ex} %[1H10V41]
Hai tờ lịch của Thứ Tư tuần này và Thứ Tư tuần sau:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  % Tờ 1
  \node[draw=blue!80, fill=blue!10, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (L1) at (-2.8,0) {
    \begin{tabular}{c}\bfseries\tiny THỨ TƯ\\\bfseries\normalsize 10\end{tabular}
  };
  \node[below=2pt, font=\bfseries\tiny, color=blue!90!black] at (-2.8,-0.6) {Tuần này};
  % Mũi tên
  \draw[->, >=stealth, line width=1.2pt, red!85] (-1.2,0) -- (1.2,0) node[midway, above=1pt, font=\bfseries\tiny, color=red!90!black] {$+7$ ngày};
  % Tờ 2
  \node[draw=teal!80, fill=yellow!25, line width=1.2pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (L2) at (2.8,0) {
    \begin{tabular}{c}\bfseries\tiny THỨ TƯ\\\bfseries\normalsize ?\end{tabular}
  };
  \node[below=2pt, font=\bfseries\tiny, color=teal!90!black] at (2.8,-0.6) {Tuần sau};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Thứ Tư tuần này là ngày 10. Thứ Tư tuần sau là ngày bao nhiêu?
\begin{multicols}{4}
\choice
{Ngày 16}
{\True Ngày 17}
{Ngày 18}
{Ngày 19}
\end{multicols}
\loigiai{
Một tuần lễ có 7 ngày. Thứ Tư tuần sau là ngày: $10 + 7 = 17$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Kiến thức tổng quát lớp 1
\begin{ex} %[1D10H41]
Quan sát các hình ảnh tóm tắt kiến thức Toán lớp 1:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.75]
  % Thẻ 100
  \node[draw=blue!80, fill=blue!12, line width=0.8pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (-4.8,0) {\bfseries\scriptsize Số 100};
  % Khối lập phương
  \VeBamiMotKhoiLapPhuong{-2.1,-0.4}{0.55}
  \node[below=2pt, font=\tiny\bfseries, color=blue!90!black] at (-1.6,-0.4) {Khối lập phương};
  % Tờ lịch tuần 7 ngày
  \node[draw=orange!80, fill=orange!12, line width=0.8pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (1.6,0) {\bfseries\scriptsize Tuần lễ: 7 ngày};
  % Thước 1m
  \node[draw=teal!80, fill=teal!12, line width=0.8pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] at (4.8,0) {\bfseries\scriptsize $1\text{ m} = 100\text{ cm}$};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Số 100 là số tròn trăm có 3 chữ số.}
{\True Khối lập phương có tất cả 6 mặt đều là hình vuông bằng nhau.}
{Một tuần lễ chỉ gồm có 6 ngày.}
{\True Độ dài $1\text{ m}$ bằng $100\text{ cm}$.}
\loigiai{\textbf{a)} Đúng ($100$ gồm 3 chữ số: 1, 0, 0). \textbf{b)} Đúng (Khối lập phương có 6 mặt hình vuông bằng nhau). \textbf{c)} Sai (Một tuần lễ gồm $7$ ngày). \textbf{d)} Đúng ($1\text{ m} = 100\text{ cm}$).}
\end{ex}

% CÂU 14: Bài toán viên bi của Bình và An
\begin{ex} %[1D10V41]
Số bi của hai bạn Bình và An được biểu diễn dưới dạng hai hộp bi:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.75]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (-2.8,0) {\bfseries\scriptsize Bình: $45$ viên};
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] at (2.8,0) {\bfseries\scriptsize An: $34$ viên};
  \draw[<->, >=stealth, line width=1.1pt, purple!85] (-1.4,0) -- (1.4,0) node[midway, above=1pt, font=\tiny\bfseries] {Chênh lệch: ?};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các nhận định sau:
\choiceTF
{\True Cả hai bạn có tất cả $79$ viên bi ($45 + 34 = 79$).}
{\True Bình có nhiều hơn An $11$ viên bi ($45 - 34 = 11$).}
{Cả hai bạn có tất cả $80$ viên bi.}
{\True An có ít hơn Bình $11$ viên bi.}
\loigiai{\textbf{a)} Đúng ($45 + 34 = 79$). \textbf{b)} Đúng ($45 - 34 = 11$). \textbf{c)} Sai (Tổng số bi là $79$ chứ không phải $80$). \textbf{d)} Đúng (Bình hơn An 11 viên thì An ít hơn Bình 11 viên).}
\end{ex}

% CÂU 15: Xem đồng hồ và các thời điểm trong ngày
\begin{ex} %[1H10H41]
Hai mốc thời gian sáng và trưa trên mặt đồng hồ:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.75]
  \VeBamiMotDongHo{-2.5,0}{7}{0}
  \node[below=2pt, font=\bfseries\tiny, color=blue!90!black] at (-2.5,-0.65) {7 giờ sáng};
  \VeBamiMotDongHo{2.5,0}{12}{0}
  \node[below=2pt, font=\bfseries\tiny, color=red!90!black] at (2.5,-0.65) {12 giờ trưa};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Lúc 7 giờ sáng, kim ngắn chỉ số 7 và kim dài chỉ số 12.}
{\True Lúc 12 giờ trưa, kim ngắn và kim dài trùng nhau cùng chỉ số 12.}
{Một ngày chỉ có 12 giờ.}
{\True Từ 7 giờ sáng đến 12 giờ trưa cùng ngày có khoảng cách là 5 giờ ($12 - 7 = 5$).}
\loigiai{\textbf{a)} Đúng (Giờ đúng kim phút luôn chỉ số 12). \textbf{b)} Đúng (12 giờ đúng cả 2 kim đều chỉ số 12). \textbf{c)} Sai (Một ngày có 24 giờ). \textbf{d)} Đúng ($12 - 7 = 5$ giờ).}
\end{ex}

% CÂU 16: So sánh độ dài hai đoạn dây
\begin{ex} %[1H10V41]
Hai đoạn dây đặt song song so sánh độ dài:
\begin{center}\vspace{-3mm}
\begin{tikzpicture}[scale=0.75]
  \draw[line width=3pt, blue!80] (-3.0,0.25) -- (1.5,0.25) node[midway, above=1pt, font=\bfseries\tiny, color=blue!85] {Dây 1: $45\text{ cm}$};
  \draw[line width=3pt, orange!85] (-3.0,-0.25) -- (2.5,-0.25) node[midway, below=1pt, font=\bfseries\tiny, color=orange!85] {Dây 2: $55\text{ cm}$};
\end{tikzpicture}
\vspace{-3mm}\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Cả hai đoạn dây có tổng độ dài là $100\text{ cm}$ ($1\text{ m}$).}
{\True Đoạn dây 2 dài hơn đoạn dây 1 là $10\text{ cm}$ ($55 - 45 = 10$).}
{Tổng độ dài hai đoạn dây ngắn hơn $90\text{ cm}$.}
{\True Cắt bớt đoạn dây 2 đi $15\text{ cm}$ thì đoạn 2 còn lại $40\text{ cm}$.}
\loigiai{\textbf{a)} Đúng ($45 + 55 = 100\text{ cm} = 1\text{ m}$). \textbf{b)} Đúng ($55 - 45 = 10\text{ cm}$). \textbf{c)} Sai (Tổng độ dài là $100\text{ cm} > 90\text{ cm}$). \textbf{d)} Đúng ($55 - 15 = 40\text{ cm}$).}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Tính 62 + 27
\begin{ex} %[1D10H41]
Sơ đồ tính tổng hai số có hai chữ số:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (A) at (-2.2,0) {\bfseries\small 62};
  \node[font=\bfseries\large, color=black!60] at (0,0) {$+$};
  \node[draw=teal!80, fill=teal!12, line width=1pt, rounded corners=3pt, inner xsep=8pt, inner ysep=4pt] (B) at (2.2,0) {\bfseries\small 27};
  \draw[->, >=stealth, line width=1.2pt, red!85] (0,-0.4) -- (0,-0.95) node[below=2pt, font=\bfseries\small, color=red!90!black] {Kết quả: ?};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tính kết quả của phép tính: $62 + 27$.
\shortans{89}
\loigiai{
Thực hiện cộng: $2 + 7 = 9$; $6 + 2 = 8$. Kết quả: $62 + 27 = 89$.\\
\textbf{Đáp số:} $89$.
}
\end{ex}

% CÂU 18: Tìm x biết x + 35 = 89
\begin{ex} %[1D10V41]
Sơ đồ thanh ngang tìm thành phần chưa biết:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  % Toàn phần
  \draw[fill=blue!10, draw=blue!80, line width=1pt] (-3.2,0) rectangle (3.2,0.6);
  \node[font=\bfseries\tiny, color=blue!90!black] at (0,0.3) {Tổng: $89$};
  % Phần đã biết: 35
  \draw[fill=teal!20, draw=teal!85, line width=1pt] (-3.2,-0.8) rectangle (-0.7,-0.2);
  \node[font=\bfseries\tiny, color=teal!90!black] at (-1.95,-0.5) {Đã biết: $35$};
  % Phần chưa biết: x
  \draw[fill=yellow!25, draw=red!85, line width=1pt] (-0.7,-0.8) rectangle (3.2,-0.2);
  \node[font=\bfseries\tiny, color=red!90!black] at (1.25,-0.5) {Chưa biết: $x = ?$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tìm số thích hợp điền vào chỗ chấm: $x + 35 = 89$.
\shortans{54}
\loigiai{
Để tìm số hạng chưa biết, ta lấy tổng trừ đi số hạng đã biết: $x = 89 - 35 = 54$.\\
\textbf{Đáp số:} $54$.
}
\end{ex}

% CÂU 19: Tính độ dài 45 cm + 34 cm
\begin{ex} %[1H10V41]
Hai thanh gỗ đặt nối tiếp nhau đo bằng đơn vị xăng-ti-mét:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.75]
  \draw[fill=orange!20, draw=orange!80, line width=1pt] (-3.5,-0.25) rectangle (0,0.25);
  \node[font=\bfseries\tiny, color=orange!90!black] at (-1.75,0) {$45\text{ cm}$};
  \draw[fill=teal!20, draw=teal!80, line width=1pt] (0,-0.25) rectangle (3.0,0.25);
  \node[font=\bfseries\tiny, color=teal!90!black] at (1.5,0) {$34\text{ cm}$};
  \draw[<->, >=stealth, line width=1.1pt, purple!85] (-3.5,-0.65) -- (3.0,-0.65) node[midway, below=1pt, font=\bfseries\tiny, color=purple!90!black] {Tổng cả hai thanh: ? cm};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tính tổng độ dài của hai thanh gỗ: $45\text{ cm} + 34\text{ cm}$.
\shortans{79}
\loigiai{
Cộng số đo kèm theo đơn vị: $45 + 34 = 79\text{ cm}$.\\
\textbf{Đáp số:} $79$.
}
\end{ex}

% CÂU 20: Tính nhanh 27 + 16 + 33 + 24
\begin{ex} %[1D10C41]
Sơ đồ ghép cặp các số có tổng tròn chục:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.8]
  % 4 số
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] (N1) at (-3.6,0.6) {\bfseries\small 27};
  \node[draw=orange!80, fill=orange!15, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] (N2) at (-1.2,0.6) {\bfseries\small 16};
  \node[draw=blue!80, fill=blue!12, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] (N3) at (1.2,0.6) {\bfseries\small 33};
  \node[draw=orange!80, fill=orange!15, line width=1pt, rounded corners=3pt, inner xsep=6pt, inner ysep=3pt] (N4) at (3.6,0.6) {\bfseries\small 24};
  % Cặp 27 + 33 = 60
  \draw[->, >=stealth, line width=1.1pt, blue!85] (N1.south) to[out=-40, in=-140] node[midway, below=1pt, font=\tiny\bfseries, color=blue!90!black] {$27 + 33 = 60$} (N3.south);
  % Cặp 16 + 24 = 40
  \draw[->, >=stealth, line width=1.1pt, orange!85] (N2.north) to[out=40, in=140] node[midway, above=1pt, font=\tiny\bfseries, color=orange!90!black] {$16 + 24 = 40$} (N4.north);
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Tính nhanh giá trị của biểu thức: $27 + 16 + 33 + 24$.
\shortans{100}
\loigiai{
Ghép các cặp số có tận cùng cộng lại tròn chục: $(27 + 33) + (16 + 24) = 60 + 40 = 100$.\\
\textbf{Đáp số:} $100$.
}
\end{ex}
'''

# Template wrapper để biên dịch độc lập xem trước
preview_tex = r'''\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb}
\usepackage{geometry}
\geometry{a4paper, top=14mm, bottom=14mm, left=14mm, right=14mm}
\usepackage{tikz}
\usetikzlibrary{arrows.meta, calc, shapes.geometric}
\usepackage{multicol}
\usepackage{tcolorbox}
\usepackage{fontawesome5}
\usepackage{qrcode}
\usepackage{enumitem}

% Setup ex/choice counters & commands
\newcounter{ex}
\newcounter{choice}[ex]
\newenvironment{ex}{\refstepcounter{ex}\noindent\textbf{Câu \theex.} }{\par\vspace{2.5mm}}
\newcommand{\choice}[4]{%
  \begin{enumerate}[label=\textbf{\Alph*.}, leftmargin=1.8em, itemsep=1pt, topsep=1pt]
    \item #1 \item #2 \item #3 \item #4
  \end{enumerate}
}
\newcommand{\True}{}
\newcommand{\choiceTF}[4]{%
  \begin{enumerate}[label=\textbf{\alph*)}, leftmargin=1.6em, itemsep=0.8pt, topsep=0.8pt]
    \item #1 \item #2 \item #3 \item #4
  \end{enumerate}
}
\newcommand{\loigiai}[1]{\par\noindent\textit{\footnotesize Lời giải: #1}}
\newcommand{\shortans}[1]{\hfill\textbf{[Đáp số: #1]}}
\newcommand{\setcounterpageref}[2]{}

\begin{document}
% HEADER BÀI KIỂM TRA
\begin{tcolorbox}[colback=white, colframe=blue!85!black, boxrule=1.0pt, arc=2mm, left=2mm, right=2mm, top=1.5mm, bottom=1.5mm]
  \begin{minipage}[c]{0.26\textwidth}
    \begin{tcolorbox}[colback=blue!8, colframe=blue!80!black, boxrule=0.6pt, arc=1.5mm, halign=center, top=1.2mm, bottom=1.2mm, left=1mm, right=1mm]
      {\bfseries\color{blue!95!black}\small LỚP TOÁN THẦY LĨNH}\\[1.5pt]
      {\scriptsize\color{blue!70!black}\faGlobe~loptoanthaylinh.vn}\\[1.5pt]
      {\scriptsize\bfseries\color{blue!85!black}\faPhone~Hotline: 0866976878}
    \end{tcolorbox}
  \end{minipage}%
  \hfill
  \begin{minipage}[c]{0.56\textwidth}
    \centering
    {\footnotesize\bfseries\color{blue!80!black}CHỦ ĐỀ 10 -- ÔN TẬP CUỐI NĂM}\\[2pt]
    {\large\bfseries\color{red!85!black}BÀI 41: ÔN TẬP CHUNG CUỐI NĂM}\\[2pt]
    {\scriptsize\itshape Thời gian làm bài: 35 phút -- Đề gồm 20 câu chuẩn 5 trang}
  \end{minipage}%
  \hfill
  \begin{minipage}[c]{0.14\textwidth}
    \centering
    \qrcode[height=1.35cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-41}\\[2pt]
    {\tiny\bfseries\color{blue!90!black}\faQrcode~Quét QR thi}
  \end{minipage}
\end{tcolorbox}
\vspace{1mm}

''' + content + r'''
\end{document}
'''

with open("Bai_41_preview.tex", "w", encoding="utf-8") as f:
    f.write(preview_tex)

# Lưu nội dung vào file chương chính
target_chapter = r"CHỦ ĐỀ 10 - ÔN TẬP CUỐI NĂM\Chuong10_Bai41_OnTapChung.tex"
with open(target_chapter, "w", encoding="utf-8") as f:
    f.write(content)

print("Đã tạo Bai_41_preview.tex và cập nhật " + target_chapter)
