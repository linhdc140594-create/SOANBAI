# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 33: LUYỆN TẬP CHUNG (PHÉP CỘNG, PHÉP TRỪ PV 100)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 33 ---

% 1. Đặt tính cộng cột dọc
\providecommand{\VeDatTinhCongDoc}[4]{% #1=(x,y), #2=số trên, #3=số dưới, #4=tổng
  \begin{scope}[shift={(#1)}, scale=0.65]
    \draw[fill=blue!5, draw=blue!70, line width=0.8pt, rounded corners=3pt] (-1.1,-1.15) rectangle (1.1,1.15);
    \node[font=\bfseries\Large, color=black] at (0.3,0.55) {#2};
    \node[font=\bfseries\Large, color=red!85] at (-0.6,0.0) {$+$};
    \node[font=\bfseries\Large, color=black] at (0.3,0.0) {#3};
    \draw[line width=1.1pt, black!80] (-0.8,-0.28) -- (0.8,-0.28);
    \node[font=\bfseries\Large, color=blue!90!black] at (0.3,-0.7) {#4};
  \end{scope}
}

% 2. Đặt tính trừ cột dọc
\providecommand{\VeDatTinhTruDocLT}[4]{% #1=(x,y), #2=số bị trừ, #3=số trừ, #4=hiệu
  \begin{scope}[shift={(#1)}, scale=0.65]
    \draw[fill=orange!5, draw=orange!75, line width=0.8pt, rounded corners=3pt] (-1.1,-1.15) rectangle (1.1,1.15);
    \node[font=\bfseries\Large, color=black] at (0.3,0.55) {#2};
    \node[font=\bfseries\Large, color=red!85] at (-0.6,0.0) {$-$};
    \node[font=\bfseries\Large, color=black] at (0.3,0.0) {#3};
    \draw[line width=1.1pt, black!80] (-0.8,-0.28) -- (0.8,-0.28);
    \node[font=\bfseries\Large, color=orange!90!black] at (0.3,-0.7) {#4};
  \end{scope}
}

% 3. Khối lập phương trừ hai số
\providecommand{\VeKhoiTruHaiSoLT}[5]{% #1=(x,y), #2=tổng chục, #3=chục gạch, #4=tổng đv, #5=đv gạch
  \begin{scope}[shift={(#1)}, scale=0.4]
    \foreach \c in {1,...,#2} {
      \draw[fill=orange!50, draw=black!80, line width=0.4pt] (\c*0.7-0.7,0) rectangle (\c*0.7-0.2,2.6);
      \foreach \y in {0.26,0.52,...,2.4} {
        \draw[black!50, line width=0.2pt] (\c*0.7-0.7,\y) -- (\c*0.7-0.2,\y);
      }
      \ifnum\c>#2-#3
        \draw[line width=1.1pt, red!85] (\c*0.7-0.7,0) -- (\c*0.7-0.2,2.6);
        \draw[line width=1.1pt, red!85] (\c*0.7-0.7,2.6) -- (\c*0.7-0.2,0);
      \fi
    }
    \pgfmathsetmacro{\xstart}{#2*0.7 + 0.3}
    \foreach \u in {1,...,#4} {
      \draw[fill=cyan!50, draw=black!80, line width=0.4pt] (\xstart,\u*0.42-0.42) rectangle (\xstart+0.38,\u*0.42-0.05);
      \ifnum\u>#4-#5
        \draw[line width=1.0pt, red!85] (\xstart,\u*0.42-0.42) -- (\xstart+0.38,\u*0.42-0.05);
        \draw[line width=1.0pt, red!85] (\xstart,\u*0.42-0.05) -- (\xstart+0.38,\u*0.42-0.42);
      \fi
    }
  \end{scope}
}

% 4. Xe tải chở phép tính
\providecommand{\VeXePhepTinhLT}[4]{% #1=(x,y), #2=màu xe, #3=phép tính, #4=kết quả
  \begin{scope}[shift={(#1)}, scale=0.55]
    \draw[fill=#2!35, draw=black!80, line width=0.7pt, rounded corners=3pt] (-1.6,0) rectangle (1.6,0.85);
    \draw[fill=white, draw=black!70, line width=0.5pt, rounded corners=2pt] (-1.4,0.12) rectangle (1.4,0.72);
    \node[font=\bfseries\small, color=blue!90!black] at (0,0.42) {#3 = #4};
    \fill[black!85] (-1.0,-0.12) circle (0.18cm);
    \fill[gray!40] (-1.0,-0.12) circle (0.08cm);
    \fill[black!85] (1.0,-0.12) circle (0.18cm);
    \fill[gray!40] (1.0,-0.12) circle (0.08cm);
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Đặt tính 45 + 32
\begin{ex} %[1D8N33]
Quan sát phép tính đặt theo cột dọc:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDatTinhCongDoc{0,0}{45}{32}{77}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $45 + 32$ là:
\begin{multicols}{4}
\choice
{$76$}
{\True $77$}
{$78$}
{$79$}
\end{multicols}
\loigiai{
Hàng đơn vị: $5 + 2 = 7$. Hàng chục: $4 + 3 = 7$. Vậy $45 + 32 = 77$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Mô hình trừ 78 - 35
\begin{ex} %[1D8N33]
Mô hình $7$ thanh chục và $8$ khối đơn vị, bớt đi $3$ thanh chục và $5$ khối đơn vị:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeKhoiTruHaiSoLT{0,0}{7}{3}{8}{5}
  \node[below, font=\bfseries\tiny, color=blue!90!black] at (2.4,-0.15) {Ban đầu: $78$};
  \node[below, font=\bfseries\tiny, color=red!85] at (5.8,-0.15) {Bớt: $35$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $78 - 35$ là:
\begin{multicols}{4}
\choice
{$42$}
{\True $43$}
{$44$}
{$45$}
\end{multicols}
\loigiai{
Hàng đơn vị: $8 - 5 = 3$. Hàng chục: $7 - 3 = 4$. Vậy $78 - 35 = 43$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Cộng 2 chữ số với 1 chữ số 62 + 7
\begin{ex} %[1D8H33]
Chiếc xe buýt mang phép tính cộng:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeXePhepTinhLT{0,0}{green}{$62 + 7$}{$69$}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $62 + 7$ là:
\begin{multicols}{4}
\choice
{$68$}
{\True $69$}
{$70$}
{$71$}
\end{multicols}
\loigiai{
Hàng đơn vị: $2 + 7 = 9$, giữ nguyên hàng chục là $6$. Vậy $62 + 7 = 69$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Trừ 2 chữ số cho 1 chữ số 89 - 5
\begin{ex} %[1D8H33]
Bảng con ghi phép tính trừ cột dọc:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDatTinhTruDocLT{0,0}{89}{5}{84}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $89 - 5$ là:
\begin{multicols}{4}
\choice
{$83$}
{\True $84$}
{$85$}
{$86$}
\end{multicols}
\loigiai{
Hàng đơn vị: $9 - 5 = 4$, giữ nguyên hàng chục là $8$. Vậy $89 - 5 = 84$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: So sánh hai phép tính 53 + 24 và 98 - 21
\begin{ex} %[1D8H33]
Hai chú gấu cầm bảng số trên bập bênh:
\begin{center}\vspace{-1mm}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=blue!15, draw=blue!80, line width=0.8pt, rounded corners=3pt] (-3.2,-0.4) rectangle (-0.8,0.6);
  \node[font=\bfseries\small, color=blue!90!black] at (-2.0,0.1) {$53 + 24$};
  \draw[fill=yellow!30, draw=orange!80, line width=1pt] (0,0.1) circle (0.42cm);
  \node[font=\bfseries\normalsize, color=red!85] at (0,0.1) {$?$};
  \draw[fill=purple!15, draw=purple!80, line width=0.8pt, rounded corners=3pt] (0.8,-0.4) rectangle (3.2,0.6);
  \node[font=\bfseries\small, color=purple!90!black] at (2.0,0.1) {$98 - 21$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Dấu thích hợp để điền vào ô trống là:
\begin{multicols}{4}
\choice
{$>$}
{\True $=$}
{$<$}
{$+$}
\end{multicols}
\loigiai{
Vế trái: $53 + 24 = 77$. Vế phải: $98 - 21 = 77$. Vì $77 = 77$ nên điền dấu $=$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Biểu thức liên tiếp 34 + 25 - 18
\begin{ex} %[1D8H33]
Đoàn tàu hỏa mang các phép tính theo thứ tự:
\begin{center}\vspace{-1mm}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!30, draw=orange!80, line width=0.8pt, rounded corners=3pt] (-3.6,-0.4) rectangle (-1.8,0.5);
  \node[font=\bfseries\small, color=black] at (-2.7,0.05) {$34$};
  \draw[->, line width=1pt, blue!80] (-1.7,0.05) -- (-0.3,0.05) node[midway, above, font=\bfseries\tiny, color=blue!85] {$+25$};
  \draw[fill=green!20, draw=green!70!black, line width=0.8pt, rounded corners=3pt] (-0.2,-0.4) rectangle (1.6,0.5);
  \node[font=\bfseries\small, color=black] at (0.7,0.05) {$59$};
  \draw[->, line width=1pt, red!80] (1.7,0.05) -- (3.1,0.05) node[midway, above, font=\bfseries\tiny, color=red!85] {$-18$};
  \draw[fill=cyan!30, draw=blue!80, line width=0.8pt, rounded corners=3pt] (3.2,-0.4) rectangle (5.0,0.5);
  \node[font=\bfseries\small, color=blue!90!black] at (4.1,0.05) {$?$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Giá trị của biểu thức $34 + 25 - 18$ là:
\begin{multicols}{4}
\choice
{$40$}
{\True $41$}
{$42$}
{$43$}
\end{multicols}
\loigiai{
Tính từ trái sang phải: $34 + 25 = 59$; tiếp tục lấy $59 - 18 = 41$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Trang trại gà và vịt
\begin{ex} %[1D8V33]
Một trang trại nuôi $54$ con gà và $32$ con vịt:
\begin{center}\vspace{-1mm}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=orange!20, draw=orange!80, line width=0.8pt] (0,0) rectangle (4.5,0.6) node[midway, font=\bfseries\footnotesize] {Gà: $54$ con};
  \draw[fill=teal!20, draw=teal!80, line width=0.8pt] (4.5,0) rectangle (7.5,0.6) node[midway, font=\bfseries\footnotesize] {Vịt: $32$ con};
  \draw[<->, line width=0.7pt, black] (0,-0.3) -- (7.5,-0.3) node[midway, below, font=\bfseries\footnotesize] {Tất cả: $?$ con};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Trang trại có tất cả số con gia cầm là:
\begin{multicols}{4}
\choice
{$85$ con}
{\True $86$ con}
{$87$ con}
{$88$ con}
\end{multicols}
\loigiai{
Tổng số con gia cầm là: $54 + 32 = 86$ (con).\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Cuộn cáp cắt bớt
\begin{ex} %[1D8V33]
Một cuộn cáp dài $96\text{ m}$, người ta đã cắt dùng $45\text{ m}$:
\begin{center}\vspace{-1mm}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=purple!20, draw=purple!80, line width=0.8pt] (0,0) rectangle (4.5,0.6) node[midway, font=\bfseries\footnotesize] {Đã cắt $45\text{ m}$};
  \draw[fill=gray!15, draw=gray!70, dashed, line width=0.8pt] (4.5,0) rectangle (9.0,0.6) node[midway, font=\bfseries\footnotesize] {Còn lại $?\text{ m}$};
  \draw[<->, line width=0.7pt, blue!85] (0,-0.3) -- (9.0,-0.3) node[midway, below, font=\bfseries\footnotesize] {Cả cuộn cáp dài: $96\text{ m}$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Cuộn cáp còn lại dài là:
\begin{multicols}{4}
\choice
{$50\text{ m}$}
{\True $51\text{ m}$}
{$52\text{ m}$}
{$53\text{ m}$}
\end{multicols}
\loigiai{
Độ dài cuộn cáp còn lại là: $96 - 45 = 51\text{ m}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Tìm x: x - 32 = 45
\begin{ex} %[1D8V33]
Chiếc cân thăng bằng có hộp quà $x$ bị lấy đi $32$ quả cầu thì còn bằng $45$:
\begin{center}\vspace{-1mm}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=gray!80] (-0.15,0) rectangle (0.15,1.5);
  \draw[fill=gray!90] (-0.8,0) rectangle (0.8,0.25);
  \fill[orange!80] (0,1.5) circle (0.12cm);
  \draw[line width=1.8pt, blue!80!black] (-2.8,1.5) -- (2.8,1.5);
  \draw[line width=0.7pt] (-2.8,1.5) -- (-3.4,0.6) -- (-2.2,0.6) -- cycle;
  \draw[fill=yellow!30, rounded corners=2pt] (-3.5,0.6) rectangle (-2.1,1.1) node[midway, font=\bfseries\footnotesize] {$x - 32$};
  \draw[line width=0.7pt] (2.8,1.5) -- (2.2,0.6) -- (3.4,0.6) -- cycle;
  \draw[fill=green!30, rounded corners=2pt] (2.2,0.6) rectangle (3.4,1.1) node[midway, font=\bfseries\footnotesize] {$45$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Giá trị của $x$ biết $x - 32 = 45$ là:
\begin{multicols}{4}
\choice
{$76$}
{\True $77$}
{$78$}
{$79$}
\end{multicols}
\loigiai{
Ta có số bị trừ $x = 45 + 32 = 77$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Máy trừ tìm y
\begin{ex} %[1D8V33]
Một máy tính nhận số đầu vào $86$, trừ đi số bí mật $y$ và cho kết quả $42$:
\begin{center}\vspace{-1mm}
\begin{tikzpicture}[scale=0.65]
  \node[font=\bfseries\small, color=blue!90!black] at (-2.8,0.4) {Vào: $86$};
  \draw[->, line width=1.1pt, blue!80] (-1.6,0.4) -- (-0.7,0.4);
  \draw[fill=pink!30, draw=red!70, line width=0.8pt, rounded corners=4pt] (-0.7,-0.2) rectangle (1.2,1.0);
  \node[font=\bfseries\small, color=red!85] at (0.25,0.4) {$- y$};
  \draw[->, line width=1.1pt, green!70!black] (1.2,0.4) -- (2.0,0.4);
  \node[font=\bfseries\small, color=green!60!black] at (3.1,0.4) {Ra: $42$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Số bí mật $y$ trong chiếc máy là:
\begin{multicols}{4}
\choice
{$43$}
{\True $44$}
{$45$}
{$46$}
\end{multicols}
\loigiai{
Số trừ $y = 86 - 42 = 44$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Viên bi của Bình và An
\begin{ex} %[1D8V33]
Số viên bi đựng trong hai túi của bạn Bình và bạn An:
\begin{center}\vspace{-1mm}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=blue!20, draw=blue!80, line width=0.8pt, rounded corners=5pt] (-3.5,-0.4) rectangle (-0.5,0.6);
  \node[font=\bfseries\footnotesize, color=blue!90!black] at (-2.0,0.1) {Bình: $45$ viên};
  \node[font=\bfseries\Large, color=red!85] at (0,0.1) {$+$};
  \draw[fill=orange!20, draw=orange!80, line width=0.8pt, rounded corners=5pt] (0.5,-0.4) rectangle (3.5,0.6);
  \node[font=\bfseries\footnotesize, color=orange!90!black] at (2.0,0.1) {An: $23$ viên};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Cả hai bạn có tất cả số viên bi là:
\begin{multicols}{4}
\choice
{$67$ viên}
{\True $68$ viên}
{$69$ viên}
{$70$ viên}
\end{multicols}
\loigiai{
Tổng số viên bi của hai bạn là: $45 + 23 = 68$ (viên bi).\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Tính nhanh nhóm tròn chục
\begin{ex} %[1D8C33]
Ghép các cặp số tròn chục trên các cánh hoa:
\begin{center}\vspace{-1mm}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=yellow!40, draw=orange!80, line width=0.8pt] (0,0) circle (0.9cm);
  \node[font=\bfseries\tiny, color=red!85] at (0,0) {Tổng = ?};
  \node[draw=blue!70, fill=blue!15, rounded corners=2pt, font=\bfseries\tiny] at (-2.0,0.8) {$32 + 18 = 50$};
  \node[draw=green!70!black, fill=green!15, rounded corners=2pt, font=\bfseries\tiny] at (2.0,0.8) {$24 + 26 = 50$};
  \draw[->, line width=0.7pt, blue!80] (-1.0,0.5) -- (-0.6,0.3);
  \draw[->, line width=0.7pt, green!70!black] (1.0,0.5) -- (0.6,0.3);
\end{tikzpicture}
\vspace{-2mm}\end{center}
Kết quả tính nhanh của biểu thức $32 + 24 + 18 + 26$ là:
\begin{multicols}{4}
\choice
{$90$}
{\True $100$}
{$95$}
{$85$}
\end{multicols}
\loigiai{
Ta nhóm: $(32 + 18) + (24 + 26) = 50 + 50 = 100$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: PHẦN 2 - TRẮC NGHIỆM ĐÚNG SAI (4 CÂU) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Xét tính đúng sai của 4 phép tính
\begin{ex} %[1D8H33]
Quan sát bảng $4$ phép tính cộng, trừ trong phạm vi $100$:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.65]
  \node at (-4.2,0) {\VeDatTinhCongDoc{0,0}{52}{35}{87}};
  \node at (-1.4,0) {\VeDatTinhTruDocLT{0,0}{87}{52}{35}};
  \node at (1.4,0) {\VeDatTinhCongDoc{0,0}{60}{40}{90}};
  \node at (4.2,0) {\VeDatTinhCongDoc{0,0}{60}{40}{100}};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Xét tính đúng, sai của các phép toán trên:
\choiceTF
{\True Phép tính $52 + 35 = 87$ là đúng.}
{\True Phép tính $87 - 52 = 35$ là đúng.}
{Phép tính $60 + 40 = 90$ là đúng.}
{\True Phép tính $60 + 40 = 100$ là đúng.}
\loigiai{
\begin{itemize}
    \item a) Đúng vì $52 + 35 = 87$.
    \item b) Đúng vì $87 - 52 = 35$.
    \item c) Sai vì $60 + 40 = 100 \neq 90$.
    \item d) Đúng vì $6$ chục $+ 4$ chục $= 10$ chục $= 100$.
\end{itemize}
}
\end{ex}

% CÂU 14: Xưởng may công nhân
\begin{ex} %[1D8V33]
Một xưởng may có $68$ công nhân, trong đó có $35$ công nhân nữ:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=pink!25, draw=purple!80, line width=0.8pt, rounded corners=4pt] (-3.8,-0.45) rectangle (3.8,0.65);
  \node[font=\bfseries\footnotesize, color=blue!90!black] at (-2.0,0.1) {Tổng số: $68$ công nhân};
  \node[font=\bfseries\footnotesize, color=purple!85] at (2.0,0.1) {Nữ: $35$ công nhân};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Xét tính đúng, sai của các nhận định sau:
\choiceTF
{\True Xưởng may có $33$ công nhân nam vì $68 - 35 = 33$.}
{\True Số công nhân nữ nhiều hơn công nhân nam là $2$ người.}
{Xưởng may có tất cả $70$ công nhân.}
{\True Xưởng may có số công nhân nam ít hơn công nhân nữ.}
\loigiai{
\begin{itemize}
    \item a) Đúng: Số công nhân nam là $68 - 35 = 33$ người.
    \item b) Đúng: $35 - 33 = 2$ người.
    \item c) Sai: Xưởng may có $68$ công nhân, không phải $70$.
    \item d) Đúng: $33 < 35$ nên số nam ít hơn số nữ.
\end{itemize}
}
\end{ex}

% CÂU 15: So sánh giá trị ba giỏ trái cây
\begin{ex} %[1D8H33]
Ba giỏ trái cây mang các phép tính cộng, trừ:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75]
  \draw[fill=orange!15, draw=orange!80, rounded corners=3pt] (-3.6,0) rectangle (-1.3,0.7) node[midway, font=\bfseries\footnotesize] {Giỏ $A: 42 + 25$};
  \draw[fill=teal!15, draw=teal!80, rounded corners=3pt] (-1.1,0) rectangle (1.2,0.7) node[midway, font=\bfseries\footnotesize] {Giỏ $B: 98 - 31$};
  \draw[fill=blue!15, draw=blue!80, rounded corners=3pt] (1.4,0) rectangle (3.7,0.7) node[midway, font=\bfseries\footnotesize] {Giỏ $C: 50 + 17$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Xét tính đúng, sai của các khẳng định sau:
\choiceTF
{\True Giỏ $A$ có kết quả là $67$.}
{\True Giỏ $B$ có kết quả là $67$.}
{\True Cả ba giỏ $A, B, C$ đều có giá trị bằng nhau.}
{Giỏ $C$ có giá trị lớn hơn giỏ $A$.}
\loigiai{
\begin{itemize}
    \item a) Đúng: $42 + 25 = 67$.
    \item b) Đúng: $98 - 31 = 67$.
    \item c) Đúng: Giỏ $C = 50 + 17 = 67$, vậy cả $3$ giỏ đều bằng $67$.
    \item d) Sai: Cả hai giỏ bằng nhau ($67 = 67$).
\end{itemize}
}
\end{ex}

% CÂU 16: Bảng hoa điểm tốt
\begin{ex} %[1D8V33]
Bảng hoa điểm tốt tuần này của Lớp 1A và Lớp 1B:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.75]
  \draw[fill=cyan!15, draw=cyan!80, line width=0.8pt] (0,0) rectangle (7.0,1.1);
  \draw[line width=0.6pt, cyan!80] (0,0.55) -- (7.0,0.55);
  \draw[line width=0.6pt, cyan!80] (3.5,0) -- (3.5,1.1);
  \node[font=\bfseries\footnotesize] at (1.75,0.82) {Lớp 1A: $46$ bông hoa};
  \node[font=\bfseries\footnotesize] at (5.25,0.82) {Lớp 1B: $42$ bông hoa};
  \node[font=\bfseries\footnotesize, color=blue!90!black] at (3.5,0.28) {Tổng cả hai lớp: $88$ bông hoa};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Xét tính đúng, sai của các phát biểu sau:
\choiceTF
{\True Cả hai lớp có tất cả $88$ bông hoa điểm tốt.}
{\True Lớp 1A có nhiều hơn Lớp 1B là $4$ bông hoa.}
{Lớp 1B có nhiều hoa điểm tốt hơn Lớp 1A.}
{\True Nếu Lớp 1B được thêm $4$ bông hoa thì số hoa hai lớp bằng nhau.}
\loigiai{
\begin{itemize}
    \item a) Đúng: $46 + 42 = 88$ bông.
    \item b) Đúng: $46 - 42 = 4$ bông.
    \item c) Sai: Lớp 1A ($46$) nhiều hơn Lớp 1B ($42$).
    \item d) Đúng: $42 + 4 = 46$ bông.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: PHẦN 3 - CÂU HỎI TRẢ LỜI NGẮN (4 CÂU) ---

\textbf{Phần 3. Câu hỏi trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Tính 43 + 36
\begin{ex} %[1D8H33]
Quan sát phép tính cộng đặt theo cột dọc:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeDatTinhCongDoc{0,0}{43}{36}{79}
\end{tikzpicture}
\vspace{-2mm}\end{center}
Kết quả của phép tính $43 + 36$ là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$79$}}
\loigiai{
Hàng đơn vị: $3 + 6 = 9$; Hàng chục: $4 + 3 = 7$. Vậy $43 + 36 = 79$.\\
\textbf{Đáp số: $79$.}
}
\end{ex}

% CÂU 18: Tính 85 - 41
\begin{ex} %[1D8H33]
Quan sát phép tính trừ đặt theo cột dọc:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}
  \VeDatTinhTruDocLT{0,0}{85}{41}{44}
\end{tikzpicture}
\vspace{-2mm}\end{center}
Kết quả của phép tính $85 - 41$ là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$44$}}
\loigiai{
Hàng đơn vị: $5 - 1 = 4$; Hàng chục: $8 - 4 = 4$. Vậy $85 - 41 = 44$.\\
\textbf{Đáp số: $44$.}
}
\end{ex}

% CÂU 19: Tủ sách 78 quyển phát 45 quyển
\begin{ex} %[1D8V33]
Tủ sách thư viện có $78$ quyển truyện, cô giáo đã phát cho học sinh mượn $45$ quyển:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.7]
  \draw[fill=amber!20, draw=brown!80, line width=0.8pt, rounded corners=4pt] (-3.5,-0.4) rectangle (3.5,0.6);
  \node[font=\bfseries\footnotesize, color=blue!90!black] at (-1.8,0.1) {Có tất cả: $78$ quyển};
  \node[font=\bfseries\footnotesize, color=red!85] at (1.8,0.1) {Đã mượn: $45$ quyển};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Hỏi trong tủ thư viện còn lại bao nhiêu quyển truyện?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$33$}}
\loigiai{
Trong tủ thư viện còn lại: $78 - 45 = 33$ (quyển truyện).\\
\textbf{Đáp số: $33$ quyển.}
}
\end{ex}

% CÂU 20: Tính nhanh 45 + 23 + 15 + 17
\begin{ex} %[1D8C33]
Bốn ngôi sao mang các số tạo thành cặp số tròn chục:
\begin{center}\vspace{-2mm}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!30, draw=orange!80, rounded corners=3pt] (-3.6,-0.4) rectangle (-1.4,0.5);
  \node[font=\bfseries\small, color=blue!90!black] at (-2.5,0.05) {$45 + 15 = 60$};
  \node[font=\bfseries\Large, color=red!85] at (0,0.05) {$+$};
  \draw[fill=green!20, draw=green!70!black, rounded corners=3pt] (1.4,-0.4) rectangle (3.6,0.5);
  \node[font=\bfseries\small, color=green!80!black] at (2.5,0.05) {$23 + 17 = 40$};
\end{tikzpicture}
\vspace{-2mm}\end{center}
Giá trị tính nhanh của biểu thức $45 + 23 + 15 + 17$ là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$100$}}
\loigiai{
Ta nhóm các cặp tròn chục: $(45 + 15) + (23 + 17) = 60 + 40 = 100$.\\
\textbf{Đáp số: $100$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 8 Bai 33
tex_path = os.path.abspath('CHỦ ĐỀ 8 - PHÉP CỘNG, PHÉP TRỪ (KHÔNG NHỚ) TRONG PHẠM VI 100/Chuong8_Bai33_LuyenTapChung.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_33_preview.tex độc lập 5 trang
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 33: LUYỆN TẬP CHUNG},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 8: Phép cộng, phép trừ PV 100}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-33}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_33_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_33_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_33_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_33_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_33_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    if num_pages == 5:
        # Sao chép vào PDF_DeThi_TungBai
        out_dir = os.path.abspath('PDF_DeThi_TungBai')
        os.makedirs(out_dir, exist_ok=True)
        out_pdf = os.path.join(out_dir, 'Bai_33_Luyen_tap_chung.pdf')
        import shutil
        shutil.copy2('Bai_33_preview.pdf', out_pdf)
        print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
    else:
        print(f"CẢNH BÁO: Số trang hiện tại là {num_pages}, chưa khớp chuẩn 5 trang!")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
