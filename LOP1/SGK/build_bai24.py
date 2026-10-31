# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 24: LUYỆN TẬP CHUNG (CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100 - TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 24 ---

% 1. Bó 10 que tính
\providecommand{\VeBoQueTinh}[2][red]{% #1=màu nơ, #2=(x,y)
  \begin{scope}[shift={(#2)}, scale=0.65]
    \foreach \i in {-0.24, -0.18, -0.12, -0.06, 0, 0.06, 0.12, 0.18, 0.24} {
      \draw[fill=yellow!35!brown, draw=brown!80!black, line width=0.4pt, rounded corners=0.5pt] 
        (\i-0.03, -0.65) rectangle (\i+0.03, 0.65);
    }
    \draw[fill=#1, draw=black!80, line width=0.6pt] (-0.3,-0.1) rectangle (0.3,0.1);
    \fill[#1!90!black] (-0.1,0) circle (0.07cm);
    \fill[#1!90!black] (0.1,0) circle (0.07cm);
    \fill[yellow!90!orange] (0,0) circle (0.05cm);
  \end{scope}
}

% 2. Que tính đơn lẻ
\providecommand{\VeQueRoi}[4][30]{% #1=góc nghiêng, #2=x, #3=y, #4=màu
  \begin{scope}[shift={(#2,#3)}, rotate=#1, scale=0.65]
    \draw[fill=#4, draw=brown!80!black, line width=0.4pt, rounded corners=0.5pt] 
      (-0.03,-0.65) rectangle (0.03,0.65);
  \end{scope}
}

% 3. Thuyền buồm chở số
\providecommand{\VeThuyenSo}[3]{% #1=(x,y), #2=màu cánh buồm, #3=số
  \begin{scope}[shift={(#1)}, scale=0.6]
    % Thân thuyền
    \draw[fill=brown!70!black, draw=black!80, line width=0.7pt] (-1.2,0) -- (1.2,0) -- (0.8,-0.5) -- (-0.8,-0.5) -- cycle;
    % Cột buồm
    \draw[black!85, line width=1.4pt] (0,0) -- (0,1.5);
    % Cánh buồm
    \draw[fill=#2!60, draw=black!80, line width=0.6pt] (0.1,0.2) -- (1.1,0.2) -- (0.1,1.4) -- cycle;
    \node[font=\bfseries\normalsize, color=red!90!black] at (0.45,0.6) {#3};
    % Sóng nước
    \draw[cyan!70, line width=0.8pt] (-1.4,-0.6) sin (-1.1,-0.5) cos (-0.8,-0.6) sin (-0.5,-0.7) cos (-0.2,-0.6) sin (0.1,-0.5) cos (0.4,-0.6) sin (0.7,-0.7) cos (1.0,-0.6) sin (1.3,-0.5);
  \end{scope}
}

% 4. Ô tô chở thẻ số
\providecommand{\VeOToSoMini}[3]{% #1=(x,y), #2=màu xe, #3=số
  \begin{scope}[shift={(#1)}, scale=0.55]
    \draw[fill=#2!50, draw=black!80, line width=0.7pt, rounded corners=3pt] (-1,0) rectangle (1,0.7);
    \draw[fill=cyan!25, draw=black!70, line width=0.5pt, rounded corners=2pt] (-0.6,0.3) rectangle (0.6,0.65);
    \draw[fill=white, draw=orange!90!black, line width=0.7pt, rounded corners=2pt] (-0.5,-0.05) rectangle (0.5,0.4);
    \node[font=\bfseries\normalsize, color=blue!90!black] at (0,0.18) {#3};
    \fill[black!85] (-0.65,-0.1) circle (0.18cm);
    \fill[gray!40] (-0.65,-0.1) circle (0.08cm);
    \fill[black!85] (0.65,-0.1) circle (0.18cm);
    \fill[gray!40] (0.65,-0.1) circle (0.08cm);
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Cấu tạo số gồm 8 chục và 4 đơn vị
\begin{ex} %[1D6N24]
Quan sát nhóm que tính dưới đây:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.7]
  % 8 bó que tính
  \foreach \k in {0,1,2,3,4,5,6,7} {
    \VeBoQueTinh[blue]{\k*0.65,0}
  }
  % 4 que tính rời
  \begin{scope}[shift={(5.6,0)}]
    \VeQueRoi[-10]{-0.3}{0}{yellow!40!brown}
    \VeQueRoi[0]{-0.1}{0}{yellow!40!brown}
    \VeQueRoi[5]{0.1}{0}{yellow!40!brown}
    \VeQueRoi[12]{0.3}{0}{yellow!40!brown}
  \end{scope}
  \node[below, font=\bfseries\tiny, color=blue!85!black] at (2.28,-0.55) {$8$ bó que tính ($8$ chục)};
  \node[below, font=\bfseries\tiny, color=orange!90!black] at (5.6,-0.55) {$4$ que rời};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số gồm $8$ chục và $4$ đơn vị là:
\begin{multicols}{4}
\choice
{$48$}
{\True $84$}
{$804$}
{$80$}
\end{multicols}
\loigiai{
Số gồm $8$ chục và $4$ đơn vị viết là $84$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Số liền sau của 69
\begin{ex} %[1D6N24]
Đoàn tàu hỏa chạy qua ga số $69$, đang tiến về toa tiếp theo:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=teal!40, draw=black!80, line width=0.7pt, rounded corners=2pt] (-2,0) rectangle (-0.2,0.8);
  \node[font=\bfseries\normalsize, color=black] at (-1.1,0.4) {$69$};
  \draw[line width=1.5pt, black!80] (-0.2,0.2) -- (0.4,0.2);
  \draw[fill=orange!40, draw=black!80, line width=0.7pt, rounded corners=2pt] (0.4,0) rectangle (2.2,0.8);
  \node[font=\bfseries\normalsize, color=red!90!black] at (1.3,0.4) {?};
  \node[above, font=\bfseries\tiny, color=blue!80!black] at (1.3,0.85) {Số liền sau $69$};
  \fill[black] (-1.6,-0.1) circle (0.15cm);
  \fill[black] (-0.6,-0.1) circle (0.15cm);
  \fill[black] (0.8,-0.1) circle (0.15cm);
  \fill[black] (1.8,-0.1) circle (0.15cm);
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số liền sau của số $69$ là số nào?
\begin{multicols}{4}
\choice
{$68$}
{\True $70$}
{$71$}
{$60$}
\end{multicols}
\loigiai{
Số liền sau của $69$ là: $69 + 1 = 70$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Số liền trước của 80
\begin{ex} %[1D6H24]
Ngôi nhà số $80$ có cửa bên trái ghi số liền trước:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=red!70, draw=black!80, line width=0.7pt] (-2,1.2) -- (0,2.2) -- (2,1.2) -- cycle;
  \draw[fill=yellow!25, draw=black!80, line width=0.7pt] (-1.8,-0.4) rectangle (1.8,1.2);
  \draw[fill=brown!60, draw=black!80, line width=0.6pt] (-0.4,-0.4) rectangle (0.4,0.6);
  \node[font=\bfseries\normalsize, color=white] at (0,0.1) {$80$};
  \draw[fill=cyan!30, draw=blue!80, line width=0.6pt] (-1.5,0.1) rectangle (-0.7,0.7);
  \node[font=\bfseries\normalsize, color=red!90!black] at (-1.1,0.4) {?};
  \node[below, font=\bfseries\tiny, color=blue!80!black] at (-1.1,0.05) {Liền trước};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số liền trước của số $80$ là:
\begin{multicols}{4}
\choice
{$81$}
{\True $79$}
{$78$}
{$70$}
\end{multicols}
\loigiai{
Số đứng liền trước của $80$ là: $80 - 1 = 79$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: So sánh 57 và 75
\begin{ex} %[1D6H24]
Hai bạn thỏ cầm hai củ cà rốt có ghi số:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\large, inner sep=3pt] (t1) at (-1.8,0) {57};
  \node[below=1pt of t1, font=\tiny\bfseries, color=blue!80!black] {5 chục 7 đơn vị};
  \node[draw=orange!90, fill=yellow!25, rounded corners=2pt, font=\bfseries\normalsize, inner sep=2pt] at (0,0) {~?~};
  \node[draw=red!80, fill=pink!20, rounded corners=3pt, font=\bfseries\large, inner sep=3pt] (t2) at (1.8,0) {75};
  \node[below=1pt of t2, font=\tiny\bfseries, color=red!80!black] {7 chục 5 đơn vị};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Dấu thích hợp để điền vào ô trống so sánh $57 \dots 75$ là:
\begin{multicols}{4}
\choice
{$>$}
{\True $<$}
{$=$}
{$+$}
\end{multicols}
\loigiai{
So sánh hàng chục: $5 < 7$ nên $57 < 75$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Tìm số lớn nhất trong 4 số
\begin{ex} %[1D6H24]
Bốn chú chim mang theo các tấm thẻ số:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \foreach \i/\num/\c in {-3.3/48/cyan, -1.1/84/pink, 1.1/76/yellow, 3.3/67/green} {
    \draw[fill=\c!40, draw=black!80, line width=0.7pt, rounded corners=3pt] (\i-0.7,0) rectangle (\i+0.7,0.9);
    \node[font=\bfseries\large, color=blue!90!black] at (\i,0.45) {\num};
    \fill[\c!80!black] (\i,1.15) circle (0.22cm);
    \draw[line width=0.8pt, orange] (\i+0.1,1.15) -- (\i+0.35,1.15);
  }
\end{tikzpicture}
\end{center}
Trong các số $48, 84, 76, 67$, số lớn nhất là số nào?
\begin{multicols}{4}
\choice
{$76$}
{\True $84$}
{$67$}
{$48$}
\end{multicols}
\loigiai{
So sánh hàng chục: $8 > 7 > 6 > 4$, vậy số lớn nhất là $84$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Tìm số bé nhất trong 4 số
\begin{ex} %[1D6H24]
Bốn chiếc thuyền buồm đang lướt sóng ra khơi:
\begin{center}
\begin{tikzpicture}
  \VeThuyenSo{-3.6,0}{cyan}{$92$}
  \VeThuyenSo{-1.2,0}{pink}{$35$}
  \VeThuyenSo{1.2,0}{yellow}{$71$}
  \VeThuyenSo{3.6,0}{green}{$29$}
\end{tikzpicture}
\end{center}
Trong các số $92, 35, 71, 29$ trên cánh buồm, số bé nhất là số nào?
\begin{multicols}{4}
\choice
{$35$}
{\True $29$}
{$71$}
{$92$}
\end{multicols}
\loigiai{
So sánh hàng chục: $2 < 3 < 7 < 9$, vậy số bé nhất là $29$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Sắp xếp từ bé đến lớn
\begin{ex} %[1D6V24]
Bốn toa xe lửa chở các số $42, 85, 58, 24$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \foreach \i/\num in {0/42, 2.2/85, 4.4/58, 6.6/24} {
    \draw[fill=orange!30, draw=black!80, line width=0.6pt, rounded corners=2pt] (\i,0) rectangle (\i+1.6,0.9);
    \node[font=\bfseries\large, color=blue!90!black] at (\i+0.8,0.45) {\num};
    \fill[black] (\i+0.4,-0.1) circle (0.14cm);
    \fill[black] (\i+1.2,-0.1) circle (0.14cm);
  }
\end{tikzpicture}
\end{center}
Sắp xếp các số trên theo thứ tự từ bé đến lớn là:
\begin{multicols}{2}
\choice
{$85, 58, 42, 24$}
{\True $24, 42, 58, 85$}
{$24, 58, 42, 85$}
{$42, 24, 58, 85$}
\end{multicols}
\loigiai{
So sánh: $24 < 42 < 58 < 85$. Thứ tự từ bé đến lớn là: $24, 42, 58, 85$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Số tròn chục ở giữa 50 và 70
\begin{ex} %[1D6V24]
Trên đoạn cầu số, ô tô đang tìm trạm dừng chân tròn chục:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \draw[line width=1.5pt, gray!70] (-3.5,0) -- (3.5,0);
  \node[draw=blue!80, fill=cyan!20, rounded corners=2pt, font=\bfseries\normalsize] at (-2.8,0.4) {$50$};
  \node[draw=orange!90, fill=yellow!30, rounded corners=2pt, font=\bfseries\normalsize] at (0,0.4) {?};
  \node[draw=blue!80, fill=cyan!20, rounded corners=2pt, font=\bfseries\normalsize] at (2.8,0.4) {$70$};
  \VeOToSoMini{0,1.2}{green}{~?~}
\end{tikzpicture}
\end{center}
Số tròn chục lớn hơn $50$ và bé hơn $70$ là số nào?
\begin{multicols}{4}
\choice
{$55$}
{\True $60$}
{$65$}
{$70$}
\end{multicols}
\loigiai{
Các số tròn chục liên tiếp là $50, 60, 70$. Vậy số tròn chục ở giữa $50$ và $70$ là $60$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Tìm số ở giữa 89 và 91
\begin{ex} %[1D6V24]
Điền số thích hợp vào chỗ trống $89 < \dots < 91$:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\Large, inner sep=4pt] at (-2.2,0) {89};
  \node[font=\bfseries\Large, color=blue!80] at (-1.1,0) {$<$};
  \node[draw=red!80, fill=yellow!30, rounded corners=3pt, font=\bfseries\Large, inner sep=4pt] at (0,0) {~?~};
  \node[font=\bfseries\Large, color=blue!80] at (1.1,0) {$<$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\Large, inner sep=4pt] at (2.2,0) {91};
\end{tikzpicture}
\end{center}
Số thích hợp để điền vào chỗ trống là:
\begin{multicols}{4}
\choice
{$89$}
{\True $90$}
{$91$}
{$92$}
\end{multicols}
\loigiai{
Số liền sau của $89$ và liền trước của $91$ là số $90$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Số lớn nhất có hai chữ số khác nhau
\begin{ex} %[1D6V24]
Chiếc huy chương vàng ghi danh số lớn nhất có hai chữ số khác nhau:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!75!orange, draw=orange!90!black, line width=1pt] (0,0) circle (0.85cm);
  \draw[fill=yellow!30, draw=orange!70, line width=0.6pt] (0,0) circle (0.65cm);
  \node[font=\bfseries\LARGE, color=red!90!black] at (0,0) {?};
  \draw[fill=blue!70, draw=black!80, line width=0.6pt] (-0.3,0.8) -- (-0.6,1.6) -- (-0.1,1.6) -- cycle;
  \draw[fill=red!70, draw=black!80, line width=0.6pt] (0.3,0.8) -- (0.6,1.6) -- (0.1,1.6) -- cycle;
\end{tikzpicture}
\end{center}
Số lớn nhất có hai chữ số khác nhau là số nào?
\begin{multicols}{4}
\choice
{$99$}
{\True $98$}
{$89$}
{$97$}
\end{multicols}
\loigiai{
Chữ số hàng chục lớn nhất là $9$. Để hai chữ số khác nhau, chữ số hàng đơn vị lớn nhất chỉ có thể là $8$. Vậy số đó là $98$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Số bé nhất có hai chữ số khác nhau
\begin{ex} %[1D6V24]
Bình hoa ghi số bé nhất có hai chữ số khác nhau:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=cyan!30, draw=blue!80, line width=0.8pt] (-0.6,0) to[out=70,in=-70] (-0.3,1.2) -- (0.3,1.2) to[out=-70,in=70] (0.6,0) -- cycle;
  \node[font=\bfseries\large, color=blue!90!black] at (0,0.45) {?};
  \draw[fill=pink!80, draw=red!70, line width=0.5pt] (0,1.5) circle (0.3cm);
  \fill[yellow] (0,1.5) circle (0.1cm);
\end{tikzpicture}
\end{center}
Số bé nhất có hai chữ số khác nhau là số nào?
\begin{multicols}{4}
\choice
{$11$}
{\True $10$}
{$12$}
{$01$}
\end{multicols}
\loigiai{
Chữ số hàng chục bé nhất khác 0 là $1$. Để số bé nhất và hai chữ số khác nhau, chữ số hàng đơn vị là $0$. Vậy số đó là $10$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Đố vui cấu tạo số
\begin{ex} %[1D6C24]
Bức thư mang mật mã tìm số có hai chữ số:
\begin{center}
\begin{tikzpicture}
  \draw[fill=yellow!15, draw=orange!80, line width=0.8pt, rounded corners=3pt] (-3.8,-0.6) rectangle (3.8,0.6);
  \node[font=\bfseries\scriptsize, color=blue!90!black, align=center] at (0,0) {
    ``Chữ số hàng chục là $7$,\\
    chữ số hàng đơn vị kém chữ số hàng chục $5$ đơn vị.''
  };
\end{tikzpicture}
\end{center}
Số tìm được là:
\begin{multicols}{4}
\choice
{$75$}
{\True $72$}
{$70$}
{$73$}
\end{multicols}
\loigiai{
Chữ số hàng chục là $7$. Chữ số hàng đơn vị là: $7 - 5 = 2$. Vậy số đó là $72$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Các khẳng định tổng hợp về số
\begin{ex} %[1D6H24]
Quan sát bảng phân loại số dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=gray!10, draw=black!80, line width=0.6pt] (-4,-0.6) rectangle (4,0.6);
  \node[font=\bfseries\scriptsize, color=blue!90!black] at (-2.5,0) {Số $60$};
  \node[font=\bfseries\scriptsize, color=red!90!black] at (0,0) {Số $99$};
  \node[font=\bfseries\scriptsize, color=green!80!black] at (2.5,0) {Số $100$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Số $100$ là số có ba chữ số.}
{\True Số $99$ là số lớn nhất có hai chữ số.}
{Số $60$ gồm $0$ chục và $6$ đơn vị.}
{\True Số $60$ gồm $6$ chục và $0$ đơn vị.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Số $100$ gồm $3$ chữ số ($1, 0, 0$).
  \item b) \textbf{Đúng}: Sau số $99$ là số $100$ (có 3 chữ số).
  \item c) \textbf{Sai}: Chữ số $6$ ở hàng chục, chữ số $0$ ở hàng đơn vị.
  \item d) \textbf{Đúng}: Số $60 = 6$ chục và $0$ đơn vị.
\end{itemize}
}
\end{ex}

% CÂU 14: So sánh và đếm số trong nhóm 4 số
\begin{ex} %[1D6V24]
Cho bốn số trên bốn tấm thẻ: $56, 65, 50, 60$:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \foreach \i/\num/\c in {-3/56/yellow, -1/65/pink, 1/50/cyan, 3/60/green} {
    \draw[fill=\c!35, draw=black!80, line width=0.6pt, rounded corners=2pt] (\i-0.7,-0.4) rectangle (\i+0.7,0.4);
    \node[font=\bfseries\large, color=blue!90!black] at (\i,0) {\num};
  }
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các nhận xét sau:
\choiceTF
{\True Số lớn nhất trong bốn số trên là $65$.}
{\True Số bé nhất trong bốn số trên là $50$.}
{Trong bốn số trên có ba số tròn chục.}
{\True Trong bốn số trên chỉ có hai số tròn chục là $50$ và $60$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $65 > 60 > 56 > 50$, lớn nhất là $65$.
  \item b) \textbf{Đúng}: Bé nhất là $50$.
  \item c) \textbf{Sai}: Chỉ có hai số tròn chục là $50$ và $60$.
  \item d) \textbf{Đúng}: $56$ và $65$ không phải số tròn chục.
\end{itemize}
}
\end{ex}

% CÂU 15: Cấu tạo và thứ tự dãy số
\begin{ex} %[1D6V24]
Dãy các số từ $30$ đến $35$ trên bậc thang:
\begin{center}
\begin{tikzpicture}[scale=0.55]
  \foreach \k/\num in {0/30, 1/31, 2/32, 3/33, 4/34, 5/35} {
    \draw[fill=blue!\num!white, draw=black!80, line width=0.6pt] (\k*1.3, \k*0.4) rectangle (\k*1.3+1.2, \k*0.4+0.6);
    \node[font=\bfseries\scriptsize, color=white] at (\k*1.3+0.6, \k*0.4+0.3) {\num};
  }
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Số liền trước của số $31$ là $30$.}
{\True Số liền sau của số $34$ là $35$.}
{Số $33$ gồm $3$ chục và $5$ đơn vị.}
{\True Số $33$ gồm hai chữ số giống nhau.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $31 - 1 = 30$.
  \item b) \textbf{Đúng}: $34 + 1 = 35$.
  \item c) \textbf{Sai}: Số $33$ gồm $3$ chục và $3$ đơn vị.
  \item d) \textbf{Đúng}: Cả hai chữ số đều là $3$.
\end{itemize}
}
\end{ex}

% CÂU 16: So sánh các cặp số
\begin{ex} %[1D6V24]
Các cặp số trên đĩa cân so sánh:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\scriptsize] at (-3,0) {$47 < 74$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\scriptsize] at (-1,0) {$80 > 79$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\scriptsize] at (1,0) {$93 = 39$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\scriptsize] at (3,0) {$100 > 99$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phép so sánh sau:
\choiceTF
{\True Phép so sánh $47 < 74$ là đúng.}
{\True Phép so sánh $80 > 79$ là đúng.}
{Phép so sánh $93 = 39$ là đúng.}
{\True Phép so sánh $100 > 99$ là đúng.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Hàng chục có $4 < 7$.
  \item b) \textbf{Đúng}: Hàng chục có $8 > 7$.
  \item c) \textbf{Sai}: $93 > 39$ (không bằng nhau).
  \item d) \textbf{Đúng}: Số có $3$ chữ số luôn lớn hơn số có $2$ chữ số.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN / ĐIỀN SỐ) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Tìm số liền trước của số 60
\begin{ex} %[1D6H24]
Bảng số chỉ đường hiển thị số liền trước của $60$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=blue!80!black, draw=black, line width=0.8pt, rounded corners=3pt] (-1.8,-0.5) rectangle (1.8,0.5);
  \node[font=\bfseries\normalsize, color=white] at (-0.6,0) {Liền trước $60$:};
  \node[draw=yellow, fill=yellow!25, rounded corners=2pt, font=\bfseries\large, color=red!90!black, inner sep=2pt] at (1.1,0) {?};
\end{tikzpicture}
\end{center}
Số liền trước của số $60$ là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$59$}}
\loigiai{
Số đứng liền trước số $60$ là: $60 - 1 = 59$.\\
\textbf{Đáp số: $59$.}
}
\end{ex}

% CÂU 18: Tìm số liền sau của số 89
\begin{ex} %[1D6H24]
Mũi tên chỉ hướng đến số liền sau của $89$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=teal!30, draw=black!80, line width=0.7pt, rounded corners=2pt] (-2,-0.45) rectangle (-0.6,0.45);
  \node[font=\bfseries\Large, color=blue!90!black] at (-1.3,0) {89};
  \draw[line width=1.5pt, red!85, ->] (-0.3,0) -- (0.6,0) node[midway, above, font=\tiny\bfseries] {Liền sau};
  \draw[fill=orange!30, draw=black!80, line width=0.7pt, rounded corners=2pt] (0.9,-0.45) rectangle (2.3,0.45);
  \node[font=\bfseries\Large, color=red!90!black] at (1.6,0) {?};
\end{tikzpicture}
\end{center}
Số liền sau của số $89$ là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$90$}}
\loigiai{
Số đứng liền sau số $89$ là: $89 + 1 = 90$.\\
\textbf{Đáp số: $90$.}
}
\end{ex}

% CÂU 19: Viết số từ cấu tạo chục và đơn vị
\begin{ex} %[1D6V24]
Bảng cấu tạo số gồm $9$ chục và $5$ đơn vị:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=yellow!25, draw=blue!80, line width=0.7pt] (-2,-0.5) rectangle (0,0.5);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (-1,0) {$9$ chục};
  \draw[fill=cyan!25, draw=blue!80, line width=0.7pt] (0,-0.5) rectangle (2,0.5);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (1,0) {$5$ đơn vị};
\end{tikzpicture}
\end{center}
Viết số gồm $9$ chục và $5$ đơn vị:
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$95$}}
\loigiai{
Số gồm $9$ chục và $5$ đơn vị viết là $95$.\\
\textbf{Đáp số: $95$.}
}
\end{ex}

% CÂU 20: Vận dụng cao - Tìm số lớn nhất có hai chữ số khác nhau
\begin{ex} %[1D6C24]
Cho bốn chữ số: $2, 5, 8, 9$.
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \foreach \i/\num/\c in {-2.4/2/cyan, -0.8/5/green, 0.8/8/yellow, 2.4/9/pink} {
    \draw[fill=\c!40, draw=black!80, line width=0.7pt, rounded corners=2pt] (\i-0.6,-0.4) rectangle (\i+0.6,0.4);
    \node[font=\bfseries\large, color=blue!90!black] at (\i,0) {\num};
  }
\end{tikzpicture}
\end{center}
Ghép hai chữ số khác nhau trong bốn chữ số trên để được số có hai chữ số lớn nhất. Số đó là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$98$}}
\loigiai{
Để được số lớn nhất, chữ số hàng chục phải lớn nhất, chọn chữ số $9$.\\
Chữ số hàng đơn vị phải lớn nhất trong các chữ số còn lại, chọn chữ số $8$.\\
Vậy số lớn nhất ghép được là $98$.\\
\textbf{Đáp số: $98$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 6 Bai 24
tex_path = os.path.abspath('CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100/Chuong6_Bai24_LuyenTapChung.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_24_preview.tex độc lập 5 trang
preview_content = r'''\documentclass[14pt,a4paper]{extbook}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,calc,positioning,backgrounds,patterns,decorations.pathreplacing}
\usepackage{tcolorbox}
\tcbuselibrary{skins,theorems}
\usepackage{geometry}
\geometry{a4paper,left=15mm,right=15mm,top=11mm,bottom=12mm}
\usepackage{multicol}
\usepackage{enumitem}
\usepackage{qrcode}
\usepackage{fontawesome5}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}

\newcounter{ex}
\newcommand{\setcounterpageref}[2]{}

\newenvironment{ex}[1][]{%
  \refstepcounter{ex}%
  \par\noindent\textbf{Câu \theex.}%
  \hspace{0.5em}%
}{%
  \par\vspace{0.2ex}%
}

\newcommand{\choice}[4]{%
  \begin{enumerate}[label=\Alph*.,leftmargin=2.2em,itemsep=0.1ex,parsep=0pt,topsep=0.2ex]
    \item #1
    \item #2
    \item #3
    \item #4
  \end{enumerate}
}

\newcommand{\choiceTF}[4]{%
  \begin{enumerate}[label=\alph*),leftmargin=2.2em,itemsep=0.15ex,parsep=0pt,topsep=0.25ex]
    \item #1
    \item #2
    \item #3
    \item #4
  \end{enumerate}
}

\newcommand{\True}{}
\newcommand{\loigiai}[1]{}

\begin{document}

% --- KHUNG TIÊU ĐỀ TRANG 1 KÈM QR CODE ---
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 24: LUYỆN TẬP CHUNG},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 6: Các số đến 100}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-24}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_24_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_24_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_24_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_24_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_24_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    # Sao chép vào PDF_DeThi_TungBai
    out_dir = os.path.abspath('PDF_DeThi_TungBai')
    os.makedirs(out_dir, exist_ok=True)
    out_pdf = os.path.join(out_dir, 'Bai_24_Luyen_tap_chung.pdf')
    import shutil
    shutil.copy2('Bai_24_preview.pdf', out_pdf)
    print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
