# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 22: SO SÁNH SỐ CÓ HAI CHỮ SỐ (CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100 - TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 22 ---

% 1. Bó 10 que tính
\providecommand{\VeBoQueTinh}[2][red]{% #1=màu nơ, #2=(x,y)
  \begin{scope}[shift={(#2)}, scale=0.7]
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
  \begin{scope}[shift={(#2,#3)}, rotate=#1, scale=0.7]
    \draw[fill=#4, draw=brown!80!black, line width=0.4pt, rounded corners=0.5pt] 
      (-0.03,-0.65) rectangle (0.03,0.65);
  \end{scope}
}

% 3. Cân thăng bằng / Cân đĩa so sánh số
\providecommand{\VeCanDia}[6]{% #1=(x,y), #2=độ nghiêng góc, #3=số bên trái, #4=số bên phải, #5=màu trái, #6=màu phải
  \begin{scope}[shift={(#1)}, scale=0.8]
    % Trụ cân
    \draw[fill=gray!40, draw=black!80, line width=0.8pt] (-0.2,0) rectangle (0.2,1.2);
    \draw[fill=gray!60, draw=black!80, line width=0.8pt] (-0.8,0) -- (0.8,0) -- (0.5,0.2) -- (-0.5,0.2) -- cycle;
    \fill[blue!70!black] (0,1.2) circle (0.15cm);
    % Đòn cân nghiêng góc #2
    \begin{scope}[shift={(0,1.2)}, rotate=#2]
      \draw[line width=2pt, brown!80!black] (-1.8,0) -- (1.8,0);
      % Dây treo và đĩa trái
      \draw[black!70, line width=0.6pt] (-1.7,0) -- (-2.1,-0.7) -- (-1.3,-0.7) -- cycle;
      \draw[fill=#5!30, draw=black!80, line width=0.8pt] (-2.2,-0.75) arc (180:360:0.5cm and 0.2cm) -- cycle;
      \node[draw=#5!80!black, fill=#5!15, rounded corners=2pt, font=\bfseries\normalsize, inner sep=2pt] at (-1.7,-0.45) {#3};
      % Dây treo và đĩa phải
      \draw[black!70, line width=0.6pt] (1.7,0) -- (1.3,-0.7) -- (2.1,-0.7) -- cycle;
      \draw[fill=#6!30, draw=black!80, line width=0.8pt] (1.2,-0.75) arc (180:360:0.5cm and 0.2cm) -- cycle;
      \node[draw=#6!80!black, fill=#6!15, rounded corners=2pt, font=\bfseries\normalsize, inner sep=2pt] at (1.7,-0.45) {#4};
    \end{scope}
  \end{scope}
}

% 4. Miệng cá sấu há to (dấu so sánh trực quan)
\providecommand{\VeCaSauBeHon}[1]{% #1=(x,y), há sang phải biểu thị dấu <
  \begin{scope}[shift={(#1)}, scale=0.65]
    \draw[fill=green!60!teal, draw=green!80!black, line width=0.8pt] 
      (-0.6,0) -- (0.6,0.6) -- (0.1,0.1) -- (0.6,-0.6) -- cycle;
    \fill[white] (-0.3,0.3) circle (0.12cm);
    \fill[black] (-0.28,0.3) circle (0.06cm);
    \draw[white, line width=0.8pt] (0.5,0.45) -- (0.4,0.3) -- (0.3,0.38);
    \draw[white, line width=0.8pt] (0.5,-0.45) -- (0.4,-0.3) -- (0.3,-0.38);
  \end{scope}
}

\providecommand{\VeCaSauLonHon}[1]{% #1=(x,y), há sang trái biểu thị dấu >
  \begin{scope}[shift={(#1)}, scale=0.65]
    \draw[fill=green!60!teal, draw=green!80!black, line width=0.8pt] 
      (0.6,0) -- (-0.6,0.6) -- (-0.1,0.1) -- (-0.6,-0.6) -- cycle;
    \fill[white] (0.3,0.3) circle (0.12cm);
    \fill[black] (0.28,0.3) circle (0.06cm);
    \draw[white, line width=0.8pt] (-0.5,0.45) -- (-0.4,0.3) -- (-0.3,0.38);
    \draw[white, line width=0.8pt] (-0.5,-0.45) -- (-0.4,-0.3) -- (-0.3,-0.38);
  \end{scope}
}

% 5. Bạn nhỏ cầm bóng bay có số
\providecommand{\VeBanCamBong}[4]{% #1=(x,y), #2=tên, #3=màu bóng, #4=số trên bóng
  \begin{scope}[shift={(#1)}, scale=0.7]
    % Dây bóng
    \draw[gray!70, line width=0.6pt] (0,0.6) -- (0,1.3);
    % Quả bóng bay
    \draw[fill=#3, draw=black!70, line width=0.6pt] (0,1.8) ellipse (0.45cm and 0.55cm);
    \fill[white!60!#3] (-0.15,2.05) circle (0.08cm);
    \node[font=\bfseries\normalsize, color=black] at (0,1.8) {#4};
    % Bạn nhỏ
    \fill[orange!25!yellow] (0,0.7) circle (0.25cm);
    \fill[brown!70!black] (0,0.85) arc (40:220:0.27cm) -- cycle;
    \fill[black] (-0.07,0.7) circle (0.02cm);
    \fill[black] (0.07,0.7) circle (0.02cm);
    \draw[fill=cyan!60, draw=black!70, line width=0.4pt] (-0.2,0.1) rectangle (0.2,0.48);
    \draw[blue!70!black, line width=1.6pt] (-0.1,0.1) -- (-0.1,-0.2);
    \draw[blue!70!black, line width=1.6pt] (0.1,0.1) -- (0.1,-0.2);
    \node[below, font=\scriptsize\bfseries] at (0,-0.25) {#2};
  \end{scope}
}

% 6. Ô tô chở thẻ số
\providecommand{\VeOToSo}[3]{% #1=(x,y), #2=màu xe, #3=số
  \begin{scope}[shift={(#1)}, scale=0.65]
    \draw[fill=#2!60!white, draw=black!80, line width=0.7pt, rounded corners=4pt] (-0.9,0) rectangle (0.9,0.7);
    \draw[fill=cyan!30, draw=black!80, line width=0.5pt, rounded corners=2pt] (-0.5,0.3) rectangle (0.5,0.65);
    \draw[fill=white, draw=orange!90!black, line width=0.8pt, rounded corners=2pt] (-0.45,-0.05) rectangle (0.45,0.45);
    \node[font=\bfseries\normalsize, color=red!85!black] at (0,0.2) {#3};
    \fill[black!80] (-0.6,-0.1) circle (0.18cm);
    \fill[gray!40] (-0.6,-0.1) circle (0.08cm);
    \fill[black!80] (0.6,-0.1) circle (0.18cm);
    \fill[gray!40] (0.6,-0.1) circle (0.08cm);
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: So sánh 35 và 53 bằng hình ảnh bó que tính
\begin{ex} %[1D6N22]
Quan sát hai nhóm que tính dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.62]
  % Nhóm bên trái: 3 bó và 5 que rời -> 35
  \begin{scope}[shift={(0,0)}]
    \VeBoQueTinh[blue]{-0.8,0}
    \VeBoQueTinh[blue]{0,0}
    \VeBoQueTinh[blue]{0.8,0}
    \begin{scope}[shift={(1.5,0)}]
      \VeQueRoi[-10]{-0.24}{0}{yellow!40!brown}
      \VeQueRoi[0]{-0.12}{0}{yellow!40!brown}
      \VeQueRoi[5]{0}{0}{yellow!40!brown}
      \VeQueRoi[-5]{0.12}{0}{yellow!40!brown}
      \VeQueRoi[8]{0.24}{0}{yellow!40!brown}
    \end{scope}
    \node[below, font=\bfseries\scriptsize, color=blue!85!black] at (0.35,-0.6) {Số $35$ ($3$ chục $5$ đv)};
  \end{scope}

  \node[font=\bfseries\normalsize, draw=black!70, fill=yellow!20, rounded corners=2pt, inner sep=2pt] at (3.1,0) {~?~};

  % Nhóm bên phải: 5 bó và 3 que rời -> 53
  \begin{scope}[shift={(4.8,0)}]
    \VeBoQueTinh[red]{-1.1,0}
    \VeBoQueTinh[red]{-0.55,0}
    \VeBoQueTinh[red]{0,0}
    \VeBoQueTinh[red]{0.55,0}
    \VeBoQueTinh[red]{1.1,0}
    \begin{scope}[shift={(1.8,0)}]
      \VeQueRoi[-10]{-0.15}{0}{yellow!40!brown}
      \VeQueRoi[0]{0}{0}{yellow!40!brown}
      \VeQueRoi[8]{0.15}{0}{yellow!40!brown}
    \end{scope}
    \node[below, font=\bfseries\scriptsize, color=red!85!black] at (0.35,-0.6) {Số $53$ ($5$ chục $3$ đv)};
  \end{scope}
\end{tikzpicture}
\end{center}
Dấu thích hợp để điền vào ô trống so sánh $35 \dots 53$ là:
\begin{multicols}{4}
\choice
{$>$}
{\True $<$}
{$=$}
{$+$}
\end{multicols}
\loigiai{
So sánh chữ số hàng chục: $3 < 5$ nên $35 < 53$. Dấu cần điền là $<$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 2: So sánh khi hàng chục bằng nhau (68 và 62)
\begin{ex} %[1D6N22]
So sánh hai số dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \node[draw=blue!80!black, fill=cyan!15, rounded corners=4pt, inner sep=4pt, font=\bfseries\large] (b1) at (0,0) {68};
  \node[below=1pt of b1, font=\tiny\bfseries, color=blue!80!black] {6 chục 8 đơn vị};

  \node[draw=orange!90!black, fill=yellow!25, rounded corners=2pt, inner sep=2.5pt, font=\bfseries\small] at (1.8,0) {~?~};

  \node[draw=purple!80!black, fill=pink!20, rounded corners=4pt, inner sep=4pt, font=\bfseries\large] (b2) at (3.6,0) {62};
  \node[below=1pt of b2, font=\tiny\bfseries, color=purple!80!black] {6 chục 2 đơn vị};
\end{tikzpicture}
\end{center}
Vì hàng chục bằng nhau ($6 = 6$), ta so sánh hàng đơn vị ($8 > 2$). Dấu cần điền là:
\begin{multicols}{4}
\choice
{$<$}
{\True $>$}
{$=$}
{$-$}
\end{multicols}
\loigiai{
Hàng chục bằng nhau đều là 6, so sánh hàng đơn vị có $8 > 2$. Vậy $68 > 62$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 3: Tìm số lớn nhất trong các số trên chùm bóng bay
\begin{ex} %[1D6H22]
Bốn bạn nhỏ cùng cầm bốn quả bóng bay ghi các số dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.75]
  \VeBanCamBong{-3.3,0}{An}{yellow!60}{$45$}
  \VeBanCamBong{-1.1,0}{Bình}{green!50}{$62$}
  \VeBanCamBong{1.1,0}{Cúc}{pink!60}{$38$}
  \VeBanCamBong{3.3,0}{Dũng}{cyan!50}{$59$}
\end{tikzpicture}
\end{center}
Trong các số $45, 62, 38, 59$ trên quả bóng của các bạn, số lớn nhất là số nào?
\begin{multicols}{4}
\choice
{$59$}
{\True $62$}
{$45$}
{$38$}
\end{multicols}
\loigiai{
So sánh chữ số hàng chục: $3 < 4 < 5 < 6$. Chữ số hàng chục lớn nhất là 6, vậy số lớn nhất là $62$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 4: Tìm số bé nhất qua đoàn xe ô tô
\begin{ex} %[1D6H22]
Bốn chiếc ô tô đồ chơi mang các số lần lượt:
\begin{center}
\begin{tikzpicture}[scale=0.75]
  \VeOToSo{-3.3,0}{red}{$72$}
  \VeOToSo{-1.1,0}{blue}{$85$}
  \VeOToSo{1.1,0}{green}{$49$}
  \VeOToSo{3.3,0}{orange}{$63$}
\end{tikzpicture}
\end{center}
Trong bốn số $72, 85, 49, 63$, số bé nhất là:
\begin{multicols}{4}
\choice
{$63$}
{\True $49$}
{$72$}
{$85$}
\end{multicols}
\loigiai{
So sánh hàng chục: các số có hàng chục lần lượt là 7, 8, 4, 6. Chữ số hàng chục bé nhất là 4, vậy số bé nhất là $49$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Sắp xếp theo thứ tự từ bé đến lớn
\begin{ex} %[1D6H22]
Bốn chú thỏ mang bốn củ cà rốt có ghi các số:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \foreach \x/\num in {-3.6/24, -1.2/65, 1.2/38, 3.6/51} {
    % Củ cà rốt
    \draw[fill=orange, draw=orange!80!black, line width=0.7pt] 
      (\x,0.4) .. controls (\x-0.4,0.4) and (\x-0.2,-0.5) .. (\x,-0.8)
      .. controls (\x+0.2,-0.5) and (\x+0.4,0.4) .. cycle;
    \draw[fill=green!70!black] (\x-0.1,0.4) -- (\x-0.2,0.8) -- (\x,0.5) -- (\x+0.2,0.8) -- (\x+0.1,0.4);
    \node[font=\bfseries\normalsize, color=white] at (\x,-0.1) {\num};
  }
\end{tikzpicture}
\end{center}
Sắp xếp các số $24, 65, 38, 51$ theo thứ tự từ bé đến lớn là:
\begin{multicols}{2}
\choice
{$65, 51, 38, 24$}
{\True $24, 38, 51, 65$}
{$24, 51, 38, 65$}
{$38, 24, 51, 65$}
\end{multicols}
\loigiai{
So sánh các hàng chục: $2 < 3 < 5 < 6$. Thứ tự từ bé đến lớn: $24, 38, 51, 65$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 6: Điền số thích hợp vào giữa 48 và 50
\begin{ex} %[1D6H22]
Quan sát trục số có các ngôi sao liên tiếp:
\begin{center}
\begin{tikzpicture}[scale=0.85]
  \draw[->, >=stealth, line width=1.2pt, blue!80!black] (-0.5,0) -- (6.5,0);
  \foreach \x/\num in {1/48, 3/?, 5/50} {
    \draw[line width=1.2pt] (\x,-0.15) -- (\x,0.15);
    \if\num?
      \node[draw=red!80!black, fill=yellow!30, rounded corners=2pt, font=\bfseries\Large, text=red!80!black] at (\x,0.6) {?};
    \else
      \node[draw=blue!70!black, fill=cyan!15, rounded corners=2pt, font=\bfseries\normalsize] at (\x,0.6) {\num};
    \fi
  }
  \node[right, font=\small, color=blue!80!black] at (6.5,0) {Tia số};
\end{tikzpicture}
\end{center}
Số thích hợp điền vào dấu ``$?$'' để $48 < \text{\textbf{?}} < 50$ là:
\begin{multicols}{4}
\choice
{$48$}
{\True $49$}
{$50$}
{$51$}
\end{multicols}
\loigiai{
Số tự nhiên lớn hơn 48 và bé hơn 50 là $49$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 7: Sắp xếp theo thứ tự từ lớn đến bé
\begin{ex} %[1D6V22]
Bốn chiếc thuyền buồm ra khơi mang các số:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \foreach \x/\num/\c in {-3.6/82/cyan!40, -1.2/45/pink!50, 1.2/90/yellow!50, 3.6/67/green!40} {
    % Thân thuyền
    \draw[fill=brown!60, draw=black!80, line width=0.7pt] (\x-0.8,-0.4) -- (\x+0.8,-0.4) -- (\x+0.5,-0.75) -- (\x-0.5,-0.75) -- cycle;
    % Cánh buồm
    \draw[fill=\c, draw=black!80, line width=0.7pt] (\x,-0.35) -- (\x+0.7,-0.35) -- (\x,0.65) -- cycle;
    \draw[line width=1pt] (\x,-0.4) -- (\x,0.7);
    \node[font=\bfseries\normalsize, color=red!85!black] at (\x+0.25,0.05) {\num};
  }
\end{tikzpicture}
\end{center}
Sắp xếp các số $82, 45, 90, 67$ theo thứ tự từ lớn đến bé là:
\begin{multicols}{2}
\choice
{$45, 67, 82, 90$}
{\True $90, 82, 67, 45$}
{$90, 67, 82, 45$}
{$82, 90, 67, 45$}
\end{multicols}
\loigiai{
So sánh chữ số hàng chục từ lớn đến bé: $9 > 8 > 6 > 4$. Thứ tự: $90, 82, 67, 45$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 8: Điền chữ số thích hợp
\begin{ex} %[1D6V22]
Chú ong mật bay đến bông hoa có ghi phép so sánh:
\begin{center}
\begin{tikzpicture}
  \node[draw=orange!90!black, fill=yellow!20, rounded corners=6pt, inner sep=6pt, align=center, font=\normalsize] {
    Phép so sánh: \quad \textbf{\Large $5* < 52$}\\[1mm]
    \footnotesize Tìm chữ số thích hợp thay cho dấu $*$ để được so sánh đúng
  };
\end{tikzpicture}
\end{center}
Chữ số nào dưới đây có thể điền vào dấu $*$?
\begin{multicols}{4}
\choice
{$3$}
{\True $1$}
{$4$}
{$5$}
\end{multicols}
\loigiai{
Hàng chục đều là 5, để $5* < 52$ thì chữ số hàng đơn vị $*$ phải bé hơn 2 ($* < 2$). Trong các lựa chọn, chỉ có chữ số 1 thỏa mãn ($51 < 52$).\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Cân đĩa so sánh số
\begin{ex} %[1D6N22]
Quan sát chiếc cân đĩa dưới đây đang nghiêng về bên phải:
\begin{center}
\begin{tikzpicture}
  \VeCanDia{0,0}{-12}{74}{81}{cyan}{orange}
\end{tikzpicture}
\end{center}
Bên phải đĩa cân nặng hơn, điều này tương ứng với phép so sánh đúng nào?
\begin{multicols}{4}
\choice
{$74 > 81$}
{\True $74 < 81$}
{$74 = 81$}
{$81 < 74$}
\end{multicols}
\loigiai{
Đĩa cân mang số 81 chìm xuống thấp hơn tức là 81 lớn hơn 74, hay $74 < 81$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 10: Cá sấu ăn số lớn hơn
\begin{ex} %[1D6H22]
Chú cá sấu há to miệng về phía số lớn hơn:
\begin{center}
\begin{tikzpicture}
  \node[draw=blue!80!black, fill=blue!10, rounded corners=3pt, font=\bfseries\LARGE] at (-1.8,0) {39};
  \VeCaSauBeHon{0,0}
  \node[draw=red!80!black, fill=red!10, rounded corners=3pt, font=\bfseries\LARGE] at (1.8,0) {41};
\end{tikzpicture}
\end{center}
Hình ảnh chú cá sấu há miệng về phía số $41$ thể hiện phép so sánh nào?
\begin{multicols}{4}
\choice
{$39 > 41$}
{\True $39 < 41$}
{$39 = 41$}
{$41 < 39$}
\end{multicols}
\loigiai{
Vì hàng chục $3 < 4$ nên $39 < 41$. Chú cá sấu há miệng về phía số lớn hơn là 41, biểu diễn dấu $<$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 11: Số lớn hơn 65 nhưng bé hơn 70
\begin{ex} %[1D6H22]
Một hộp quà bí mật chứa số tròn chục:
\begin{center}
\begin{tikzpicture}
  \node[draw=purple!80!black, fill=purple!10, rounded corners=6pt, inner sep=6pt, align=center] {
    ``Tôi là số \textbf{lớn hơn 65} và \textbf{bé hơn 70}.\\
    Chữ số hàng đơn vị của tôi là \textbf{8}. Hỏi tôi là số nào?''
  };
\end{tikzpicture}
\end{center}
Số trong hộp quà là:
\begin{multicols}{4}
\choice
{$58$}
{\True $68$}
{$78$}
{$88$}
\end{multicols}
\loigiai{
Số từ 65 đến 70 có hàng chục là 6. Chữ số hàng đơn vị là 8, vậy số đó là $68$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

% CÂU 12: So sánh số tròn chục
\begin{ex} %[1D6V22]
Hai chú gấu trúc ăn các cây trúc có ghi số tròn chục:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \node[draw=green!70!black, fill=green!15, rounded corners=3pt, font=\bfseries\Large] at (-2.0,0) {70};
  \node[font=\bfseries\normalsize, draw=orange!80!black, fill=yellow!20, rounded corners=2pt, inner sep=3pt] at (0,0) {~?~};
  \node[draw=green!70!black, fill=green!15, rounded corners=3pt, font=\bfseries\Large] at (2.0,0) {90};
\end{tikzpicture}
\end{center}
Dấu so sánh thích hợp điền vào giữa hai số $70$ và $90$ là:
\begin{multicols}{4}
\choice
{$>$}
{\True $<$}
{$=$}
{Không so sánh được}
\end{multicols}
\loigiai{
7 chục bé hơn 9 chục, vậy $70 < 90$.\\
\textbf{Đáp án đúng là B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 VÀ CÂU 14 (ĐÚNG / SAI) ---

\textbf{Phần 2. Câu trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Đánh giá tính đúng sai của các phép so sánh
\begin{ex} %[1D6H22]
Quan sát bảng so sánh giữa các cặp số do bạn Nam thực hiện:
\begin{center}
\begin{tikzpicture}
  \node[draw=blue!80!black, fill=blue!5, rounded corners=4pt, inner sep=6pt, align=center] {
    \textbf{\textcolor{blue!90!black}{BẢNG SO SÁNH CÁC CẶP SỐ}}\\[1.5mm]
    \begin{tabular}{cc}
      \textbf{a)} $27 < 72$ \quad & \quad \textbf{b)} $84 > 81$ \\[1mm]
      \textbf{c)} $56 = 65$ \quad & \quad \textbf{d)} $99 > 98$
    \end{tabular}
  };
\end{tikzpicture}
\end{center}
Xét tính Đúng hay Sai của mỗi phép so sánh trên:
\choiceTF
{\True Phép so sánh $27 < 72$ là đúng}
{\True Phép so sánh $84 > 81$ là đúng}
{Phép so sánh $56 = 65$ là đúng}
{\True Phép so sánh $99 > 98$ là đúng}
\loigiai{
\begin{itemize}
  \item Ý a) Đúng: Hàng chục $2 < 7$ nên $27 < 72$.
  \item Ý b) Đúng: Hàng chục bằng 8, hàng đơn vị $4 > 1$ nên $84 > 81$.
  \item Ý c) Sai: $56$ có 5 chục, $65$ có 6 chục nên $56 < 65$ (không thể bằng nhau).
  \item Ý d) Đúng: $99$ lớn hơn $98$ một đơn vị ($99 > 98$).
\end{itemize}
}
\end{ex}

% CÂU 14: Nhận định về tuổi của các thành viên trong gia đình
\begin{ex} %[1D6V22]
Hình ảnh số tuổi của các thành viên trong gia đình bạn Mai:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \node[draw=blue!80!black, fill=blue!10, rounded corners=3pt, inner sep=4pt, align=center] at (-4.5,0) {
    \textbf{Ông nội}\\
    \textcolor{red!80!black}{\textbf{\normalsize 68 tuổi}}
  };
  \node[draw=purple!80!black, fill=purple!10, rounded corners=3pt, inner sep=4pt, align=center] at (-1.5,0) {
    \textbf{Bà nội}\\
    \textcolor{red!80!black}{\textbf{\normalsize 65 tuổi}}
  };
  \node[draw=teal!80!black, fill=teal!10, rounded corners=3pt, inner sep=4pt, align=center] at (1.5,0) {
    \textbf{Bố}\\
    \textcolor{red!80!black}{\textbf{\normalsize 38 tuổi}}
  };
  \node[draw=pink!80!black, fill=pink!20, rounded corners=3pt, inner sep=4pt, align=center] at (4.5,0) {
    \textbf{Mẹ}\\
    \textcolor{red!80!black}{\textbf{\normalsize 35 tuổi}}
  };
\end{tikzpicture}
\end{center}
Xét tính Đúng hay Sai của mỗi khẳng định sau:
\choiceTF
{\True Ông nội ($68$ tuổi) nhiều tuổi hơn bà nội ($65$ tuổi)}
{Bố ($38$ tuổi) ít tuổi hơn mẹ ($35$ tuổi)}
{\True Trong bốn người, ông nội là người nhiều tuổi nhất}
{\True Trong bốn người, mẹ là người ít tuổi nhất}
\loigiai{
\begin{itemize}
  \item Ý a) Đúng: $68 > 65$ nên ông nhiều tuổi hơn bà.
  \item Ý b) Sai: $38 > 35$ nên bố nhiều tuổi hơn mẹ.
  \item Ý c) Đúng: $68$ là số lớn nhất trong bốn số $68, 65, 38, 35$.
  \item Ý d) Đúng: $35$ là số bé nhất trong bốn số $68, 65, 38, 35$.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: CÂU 15 ĐẾN CÂU 20 (ĐIỀN SỐ) ---

\textbf{Phần 3. Câu trắc nghiệm trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 15: Tìm số lớn nhất
\begin{ex} %[1D6N22]
Trong các số được viết trên những quả táo đỏ dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.85]
  \foreach \x/\num in {-3.6/42, -1.2/89, 1.2/76, 3.6/58} {
    \begin{scope}[shift={(\x,0)}, scale=0.75]
      \shadedraw[left color=red!85!black, right color=orange!80!yellow, draw=red!90!black, line width=0.8pt]
        (-0.55,0.1) .. controls (-0.75,0.9) and (-0.15,1.1) .. (0,0.8)
        .. controls (0.15,1.1) and (0.75,0.9) .. (0.55,0.1)
        .. controls (0.45,-0.7) and (-0.45,-0.7) .. (-0.55,0.1);
      \draw[brown!70!black, line width=1.5pt] (0,0.8) .. controls (0.05,1.05) .. (0.15,1.25);
      \fill[green!70!black] (0.08,1.0) .. controls (0.35,1.15) and (0.4,0.9) .. (0.1,0.9) -- cycle;
      \node[font=\bfseries\normalsize, color=white] at (0,0.1) {\num};
    \end{scope}
  }
\end{tikzpicture}
\end{center}
Số lớn nhất trong các số trên là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$89$}}
\loigiai{
Hàng chục lớn nhất là 8 trong số $89$. Vậy số lớn nhất là $89$.\\
\textbf{Đáp số: $89$.}
}
\end{ex}

% CÂU 16: Tìm số bé nhất
\begin{ex} %[1D6N22]
Trong các số ghi trên những bông hoa dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \foreach \x/\num/\c in {-3/54/yellow!60, -1/31/pink!60, 1/67/cyan!50, 3/82/orange!60} {
    \foreach \a in {0,60,120,180,240,300} {
      \fill[\c, draw=black!60, line width=0.3pt] (\x,0) +(\a:0.35cm) circle (0.18cm);
    }
    \fill[white, draw=black!70, line width=0.5pt] (\x,0) circle (0.28cm);
    \node[font=\bfseries\small, color=red!80!black] at (\x,0) {\num};
  }
\end{tikzpicture}
\end{center}
Số bé nhất trong các số trên là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$31$}}
\loigiai{
Hàng chục bé nhất là 3 trong số $31$. Vậy số bé nhất là $31$.\\
\textbf{Đáp số: $31$.}
}
\end{ex}

% CÂU 17: Điền số thích hợp vào ô trống
\begin{ex} %[1D6H22]
Cho dãy số tăng dần liên tiếp trên đoàn tàu:
\begin{center}
\begin{tikzpicture}[scale=0.75]
  \draw[fill=purple!60, draw=black!80, line width=0.7pt, rounded corners=2pt] (-2.0,0) rectangle (-1.0,0.9);
  \node[font=\bfseries\small, color=white] at (-1.5,0.45) {TÀU};
  \draw[fill=black!80] (-1.7,-0.12) circle (0.12cm);
  \draw[fill=black!80] (-1.3,-0.12) circle (0.12cm);
  \draw[line width=1.2pt] (-1.0,0.3) -- (-0.6,0.3);

  \foreach \x/\num in {-0.6/68, 0.8/69, 2.2/?, 3.6/71} {
    \draw[fill=yellow!40, draw=black!80, line width=0.7pt, rounded corners=2pt] (\x,0) rectangle (\x+1.1,0.8);
    \if\num?
      \node[font=\bfseries\Large, color=red!85!black] at (\x+0.55,0.4) {?};
    \else
      \node[font=\bfseries\normalsize, color=black] at (\x+0.55,0.4) {\num};
    \fi
    \draw[fill=black!80] (\x+0.25,-0.12) circle (0.12cm);
    \draw[fill=black!80] (\x+0.85,-0.12) circle (0.12cm);
    \ifdim\x pt < 3.6 pt
      \draw[line width=1.2pt] (\x+1.1,0.3) -- (\x+1.4,0.3);
    \fi
  }
\end{tikzpicture}
\end{center}
Số thích hợp điền vào toa tàu có dấu ``$?$'' là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$70$}}
\loigiai{
Số liền sau của 69 và liền trước của 71 là số $70$.\\
\textbf{Đáp số: $70$.}
}
\end{ex}

% CÂU 18: Đếm số lượng số lớn hơn 50
\begin{ex} %[1D6H22]
Bạn Việt có một giỏ các viên bi ghi các số:
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \foreach \x/\num in {-3/45, -1.8/52, -0.6/38, 0.6/64, 1.8/49, 3/71} {
    \draw[fill=cyan!30, draw=blue!80!black, line width=0.6pt] (\x,0) circle (0.38cm);
    \fill[white] (\x-0.1,\x*0+0.12) circle (0.07cm);
    \node[font=\bfseries\small, color=black] at (\x,0) {\num};
  }
\end{tikzpicture}
\end{center}
Trong các viên bi trên, có bao nhiêu viên bi ghi số \textbf{lớn hơn 50}?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$3$}}
\loigiai{
Các số lớn hơn 50 là: $52, 64, 71$. Có tất cả $3$ số.\\
\textbf{Đáp số: $3$.}
}
\end{ex}

% CÂU 19: Tìm số tròn chục lớn nhất bé hơn 65
\begin{ex} %[1D6V22]
Một chú sóc muốn tìm hạt dẻ ghi số tròn chục:
\begin{center}
\begin{tikzpicture}
  \node[draw=brown!80!black, fill=orange!15, rounded corners=6pt, inner sep=6pt, align=center, font=\normalsize] {
    ``Tìm số \textbf{tròn chục lớn nhất} nhưng phải \textbf{bé hơn 65}''
  };
\end{tikzpicture}
\end{center}
Số tròn chục cần tìm là số nào?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$60$}}
\loigiai{
Các số tròn chục bé hơn 65 là: 10, 20, 30, 40, 50, 60. Trong đó số lớn nhất là $60$.\\
\textbf{Đáp số: $60$.}
}
\end{ex}

% CÂU 20: Tìm hiệu số lớn nhất và số bé nhất
\begin{ex} %[1D6V22]
Cho ba tấm thẻ số dưới đây:
\begin{center}
\begin{tikzpicture}
  \node[draw=orange!90!black, fill=yellow!25, rounded corners=3pt, font=\bfseries\LARGE, inner sep=6pt] at (-2,0) {30};
  \node[draw=blue!90!black, fill=cyan!25, rounded corners=3pt, font=\bfseries\LARGE, inner sep=6pt] at (0,0) {80};
  \node[draw=green!90!black, fill=lime!25, rounded corners=3pt, font=\bfseries\LARGE, inner sep=6pt] at (2,0) {50};
\end{tikzpicture}
\end{center}
Lấy số lớn nhất trừ đi số bé nhất trong ba tấm thẻ trên, ta được kết quả là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$50$}}
\loigiai{
Số lớn nhất là 80, số bé nhất là 30. Kết quả là: $80 - 30 = 50$.\\
\textbf{Đáp số: $50$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 6 Bai 22
tex_path = os.path.abspath('CHỦ ĐỀ 6 - CÁC SỐ ĐẾN 100/Chuong6_Bai22_SoSanhSoCoHaiChuSo.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_22_preview.tex độc lập 5 trang
preview_content = r'''\documentclass[14pt,a4paper]{extbook}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,calc,positioning,backgrounds,patterns,decorations.pathreplacing}
\usepackage{tcolorbox}
\tcbuselibrary{skins,theorems}
\usepackage{geometry}
\geometry{a4paper,left=18mm,right=18mm,top=16mm,bottom=16mm}
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
  \par\vspace{0.3ex}%
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 22: SO SÁNH SỐ CÓ HAI CHỮ SỐ},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 6: Các số đến 100}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-22}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_22_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_22_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_22_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_22_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_22_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    # Sao chép vào PDF_DeThi_TungBai
    out_dir = os.path.abspath('PDF_DeThi_TungBai')
    os.makedirs(out_dir, exist_ok=True)
    out_pdf = os.path.join(out_dir, 'Bai_22_So_sanh_so_co_hai_chu_so.pdf')
    import shutil
    shutil.copy2('Bai_22_preview.pdf', out_pdf)
    print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
