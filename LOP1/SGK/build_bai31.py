# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 31: PHÉP TRỪ SỐ CÓ HAI CHỮ SỐ CHO SỐ CÓ MỘT CHỮ SỐ (KHÔNG NHỚ)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 31 ---

% 1. Mô hình đặt tính trừ cột dọc
\providecommand{\VeDatTinhTruDoc}[4]{% #1=(x,y), #2=số bị trừ, #3=số trừ (1 chữ số), #4=hiệu
  \begin{scope}[shift={(#1)}, scale=0.7]
    \draw[fill=blue!5, draw=blue!70, line width=0.8pt, rounded corners=3pt] (-1.1,-1.2) rectangle (1.1,1.2);
    \node[font=\bfseries\Large, color=black] at (0.3,0.6) {#2};
    \node[font=\bfseries\Large, color=red!85] at (-0.6,0.0) {$-$};
    \node[font=\bfseries\Large, color=black] at (0.3,0.0) {#3};
    \draw[line width=1.2pt, black!80] (-0.8,-0.3) -- (0.8,-0.3);
    \node[font=\bfseries\Large, color=blue!90!black] at (0.3,-0.75) {#4};
  \end{scope}
}

% 2. Thanh chục và khối đơn vị bị gạch chéo bớt (trừ)
\providecommand{\VeKhoiTruDonVi}[4]{% #1=(x,y), #2=số chục, #3=số đv ban đầu, #4=số đv gạch bớt
  \begin{scope}[shift={(#1)}, scale=0.45]
    % Vẽ các thanh chục
    \foreach \c in {1,...,#2} {
      \draw[fill=orange!60, draw=black!80, line width=0.4pt] (\c*0.7-0.7,0) rectangle (\c*0.7-0.2,3.0);
      \foreach \y in {0.3,0.6,...,2.7} {
        \draw[black!50, line width=0.2pt] (\c*0.7-0.7,\y) -- (\c*0.7-0.2,\y);
      }
    }
    % Các khối đơn vị
    \pgfmathsetmacro{\xstart}{#2*0.7 + 0.3}
    \foreach \u in {1,...,#3} {
      \draw[fill=cyan!50, draw=black!80, line width=0.4pt] (\xstart,\u*0.5-0.5) rectangle (\xstart+0.45,\u*0.5-0.05);
      % Nếu nằm trong số lượng gạch bớt
      \ifnum\u>#3-#4
        \draw[line width=1.2pt, red!85] (\xstart,\u*0.5-0.5) -- (\xstart+0.45,\u*0.5-0.05);
        \draw[line width=1.2pt, red!85] (\xstart,\u*0.5-0.05) -- (\xstart+0.45,\u*0.5-0.5);
      \fi
    }
  \end{scope}
}

% 3. Xe tải chở phép tính trừ
\providecommand{\VeXePhepTinhTru}[4]{% #1=(x,y), #2=màu xe, #3=phép tính, #4=kết quả
  \begin{scope}[shift={(#1)}, scale=0.6]
    \draw[fill=#2!40, draw=black!80, line width=0.7pt, rounded corners=3pt] (-1.5,0) rectangle (1.5,0.9);
    \draw[fill=white, draw=black!70, line width=0.5pt, rounded corners=2pt] (-1.3,0.15) rectangle (1.3,0.75);
    \node[font=\bfseries\small, color=blue!90!black] at (0,0.45) {#3 = #4};
    \fill[black!85] (-0.9,-0.12) circle (0.2cm);
    \fill[gray!40] (-0.9,-0.12) circle (0.09cm);
    \fill[black!85] (0.9,-0.12) circle (0.2cm);
    \fill[gray!40] (0.9,-0.12) circle (0.09cm);
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: 38 - 5 bằng mô hình khối
\begin{ex} %[1D8N31]
Mô hình $3$ thanh chục và $8$ khối rời bị bớt đi $5$ khối rời:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeKhoiTruDonVi{0,0}{3}{8}{5}
  \node[below, font=\bfseries\tiny, color=blue!90!black] at (1.0,-0.2) {$3$ chục};
  \node[below, font=\bfseries\tiny, color=red!85] at (2.6,-0.2) {Bớt $5$ đv};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $38 - 5$ là:
\begin{multicols}{4}
\choice
{$32$}
{\True $33$}
{$34$}
{$35$}
\end{multicols}
\loigiai{
Hàng đơn vị: $8 - 5 = 3$. Giữ nguyên $3$ chục. Vậy $38 - 5 = 33$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Đặt tính 57 - 4
\begin{ex} %[1D8N31]
Quan sát phép tính đặt theo cột dọc:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeDatTinhTruDoc{0,0}{57}{4}{53}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $57 - 4$ là:
\begin{multicols}{4}
\choice
{$52$}
{\True $53$}
{$54$}
{$55$}
\end{multicols}
\loigiai{
Hàng đơn vị: $7 - 4 = 3$. Hạ $5$. Vậy $57 - 4 = 53$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Phép tính 69 - 6
\begin{ex} %[1D8H31]
Băng giấy số thực hiện phép trừ $69 - 6$:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (-2,0) {$69$};
  \node[font=\bfseries\Large, color=red!85] at (-0.8,0) {$-$};
  \node[draw=orange!80, fill=yellow!25, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0.2,0) {$6$};
  \node[font=\bfseries\Large, color=blue!80] at (1.2,0) {$=$};
  \node[draw=green!80, fill=lime!25, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (2.2,0) {?};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $69 - 6$ là:
\begin{multicols}{4}
\choice
{$62$}
{\True $63$}
{$64$}
{$65$}
\end{multicols}
\loigiai{
$9 - 6 = 3$; hạ $6$. Vậy $69 - 6 = 63$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Phép tính 78 - 8
\begin{ex} %[1D8H31]
Toa xe lửa chở phép trừ trừ hết hàng đơn vị:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeXePhepTinhTru{0,0}{orange}{$78 - 8$}{~?~}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Kết quả của phép tính $78 - 8$ là:
\begin{multicols}{4}
\choice
{$60$}
{\True $70$}
{$78$}
{$80$}
\end{multicols}
\loigiai{
$8 - 8 = 0$; hạ $7$. Ta được số tròn chục $70$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Tìm x: x + 4 = 48
\begin{ex} %[1D8H31]
Mảnh ghép chứa phép tính tìm số hạng:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=purple!80, fill=pink!20, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {
    $? + 4 = 48$
  };
\end{tikzpicture}
\end{center}
Số thích hợp điền vào dấu \textbf{?} là:
\begin{multicols}{4}
\choice
{$43$}
{\True $44$}
{$45$}
{$46$}
\end{multicols}
\loigiai{
Số cần tìm là: $48 - 4 = 44$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: So sánh hai vế 49 - 6 và 41 + 2
\begin{ex} %[1D8H31]
Cân đĩa so sánh hai phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (-2.2,0) {$49 - 6$};
  \node[draw=orange!90, fill=yellow!30, rounded corners=2pt, font=\bfseries\normalsize, inner sep=3pt] at (0.2,0) {~?~};
  \node[draw=red!80, fill=pink!20, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (2.2,0) {$41 + 2$};
\end{tikzpicture}
\end{center}
Dấu thích hợp để điền vào ô trống là:
\begin{multicols}{4}
\choice
{$>$}
{\True $=$}
{$<$}
{$+$}
\end{multicols}
\loigiai{
Vế trái: $49 - 6 = 43$. Vế phải: $41 + 2 = 43$. Hai vế bằng nhau nên điền dấu $=$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Bán quạt máy
\begin{ex} %[1D8V31]
Cửa hàng có $38$ chiếc quạt máy, đã bán đi $5$ chiếc:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=teal!30, draw=black] (0,0) rectangle (3.8,0.6) node[midway, font=\bfseries\tiny] {Còn lại ? chiếc};
  \draw[fill=gray!30, draw=black, dashed] (3.8,0) rectangle (5.0,0.6) node[midway, font=\bfseries\tiny] {Bán $5$};
  \draw[line width=0.8pt, stealth-stealth, blue!85] (0,-0.35) -- (5.0,-0.35) node[midway, below, font=\bfseries\tiny] {Có tất cả: $38$ chiếc};
\end{tikzpicture}
\end{center}
Cửa hàng còn lại số chiếc quạt là:
\begin{multicols}{4}
\choice
{$32$ chiếc}
{\True $33$ chiếc}
{$34$ chiếc}
{$35$ chiếc}
\end{multicols}
\loigiai{
Cửa hàng còn lại: $38 - 5 = 33$ chiếc quạt.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Đoạn dây bị cắt bớt
\begin{ex} %[1D8V31]
Đoạn dây dài $59\text{ cm}$, người ta cắt bớt $7\text{ cm}$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[line width=2.5pt, green!60!black] (0,0) -- (4.2,0);
  \node[above, font=\bfseries\tiny, color=green!80!black] at (2.1,0.1) {Còn lại ? cm};
  \draw[line width=2pt, gray!60, dashed] (4.2,0) -- (5.6,0);
  \node[above, font=\bfseries\tiny, color=gray!80!black] at (4.9,0.1) {Cắt $7\text{ cm}$};
  \draw[line width=0.8pt, stealth-stealth, black!70] (0,-0.35) -- (5.6,-0.35) node[midway, below, font=\bfseries\tiny] {Đoạn dây $59\text{ cm}$};
\end{tikzpicture}
\end{center}
Đoạn dây còn lại dài là:
\begin{multicols}{4}
\choice
{$51\text{ cm}$}
{\True $52\text{ cm}$}
{$53\text{ cm}$}
{$54\text{ cm}$}
\end{multicols}
\loigiai{
Đoạn dây còn lại dài: $59 - 7 = 52\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Tính biểu thức 68 - 5 - 3
\begin{ex} %[1D8V31]
Băng giấy chứa dãy tính trừ liên tiếp:
\begin{center}
\begin{tikzpicture}[scale=0.7]
  \node[draw=blue!80, fill=cyan!10, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {
    $68 - 5 - 3 = \dots$
  };
\end{tikzpicture}
\end{center}
Giá trị của biểu thức trên là:
\begin{multicols}{4}
\choice
{$59$}
{\True $60$}
{$61$}
{$62$}
\end{multicols}
\loigiai{
Thực hiện từ trái sang phải: $68 - 5 = 63$; sau đó $63 - 3 = 60$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Tìm y: 87 - y = 82
\begin{ex} %[1D8V31]
Tìm số thích hợp để điền vào ô trống:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \node[draw=blue!80, fill=cyan!15, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (-1.8,0) {$87$};
  \node[font=\bfseries\Large, color=red!85] at (-0.8,0) {$-$};
  \node[draw=red!80, fill=yellow!30, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (0,0) {?};
  \node[font=\bfseries\Large, color=blue!80] at (0.8,0) {$=$};
  \node[draw=green!80, fill=lime!25, rounded corners=3pt, font=\bfseries\normalsize, inner sep=4pt] at (1.8,0) {$82$};
\end{tikzpicture}
\end{center}
Số thích hợp điền vào dấu \textbf{?} là:
\begin{multicols}{4}
\choice
{$4$}
{\True $5$}
{$6$}
{$7$}
\end{multicols}
\loigiai{
Vì $7 - 5 = 2$ nên $87 - 5 = 82$. Số cần điền là $5$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Bán gà
\begin{ex} %[1D8V31]
Bà nuôi $46$ con gà, bà đã bán đi $6$ con gà:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=orange!35, draw=black] (0,0) rectangle (3.6,0.6) node[midway, font=\bfseries\tiny] {Còn lại ? con};
  \draw[fill=gray!30, draw=black, dashed] (3.6,0) rectangle (4.6,0.6) node[midway, font=\bfseries\tiny] {Bán $6$};
  \draw[line width=0.8pt, stealth-stealth, blue!85] (0,-0.35) -- (4.6,-0.35) node[midway, below, font=\bfseries\tiny] {Ban đầu $46$ con gà};
\end{tikzpicture}
\end{center}
Bà còn lại số con gà là:
\begin{multicols}{4}
\choice
{$38$ con}
{\True $40$ con}
{$42$ con}
{$44$ con}
\end{multicols}
\loigiai{
Bà còn lại số gà là: $46 - 6 = 40$ con gà.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Vận dụng cao - Tìm số qua hai bước tính
\begin{ex} %[1D8C31]
Mật mã truy tìm số bí ẩn:
\begin{center}
\begin{tikzpicture}
  \draw[fill=yellow!15, draw=orange!80, line width=0.8pt, rounded corners=3pt] (-3.8,-0.6) rectangle (3.8,0.6);
  \node[font=\bfseries\scriptsize, color=blue!90!black, align=center] at (0,0) {
    ``Lấy số đó cộng với $3$ rồi trừ đi $5$ thì được $72$.\\
    Hỏi số đó là số nào?''
  };
\end{tikzpicture}
\end{center}
Số bí ẩn là:
\begin{multicols}{4}
\choice
{$73$}
{\True $74$}
{$75$}
{$76$}
\end{multicols}
\loigiai{
Tính ngược lại từ cuối: $72 + 5 = 77$; sau đó $77 - 3 = 74$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Các phép tính trừ
\begin{ex} %[1D8H31]
Bảng con ghi các phép trừ:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=blue!10, draw=blue!80, line width=1pt, rounded corners=3pt] (-4,-0.6) rectangle (4,0.6);
  \node[font=\bfseries\scriptsize, color=blue!90!black] at (-2,0) {$58 - 6 = 52$};
  \node[font=\bfseries\scriptsize, color=red!90!black] at (2,0) {$79 - 7 = 72$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phép tính sau:
\choiceTF
{\True Phép tính $58 - 6 = 52$ là đúng.}
{\True Phép tính $79 - 7 = 72$ là đúng.}
{Phép tính $86 - 4 = 81$ là đúng.}
{\True Phép tính $86 - 4 = 82$ là đúng.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $58 - 6 = 52$.
  \item b) \textbf{Đúng}: $79 - 7 = 72$.
  \item c) \textbf{Sai}: $86 - 4 = 82$ (chứ không phải $81$).
  \item d) \textbf{Đúng}: $86 - 4 = 82$.
\end{itemize}
}
\end{ex}

% CÂU 14: Bài toán kẹo chia cho bạn
\begin{ex} %[1D8V31]
Có $48$ cái kẹo, chia bớt cho các bạn $6$ cái kẹo:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=pink!35, draw=black] (-3,-0.4) rectangle (0,0.4) node[midway, font=\bfseries\tiny] {Còn ? kẹo};
  \draw[fill=gray!30, draw=black, dashed] (0,-0.4) rectangle (1.5,0.4) node[midway, font=\bfseries\tiny] {Chia $6$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các khẳng định sau:
\choiceTF
{\True Số kẹo còn lại là $42$ cái.}
{\True Số kẹo còn lại nhiều hơn $40$ cái.}
{Số kẹo còn lại là $44$ cái.}
{\True Số kẹo ban đầu gấp $8$ lần số kẹo chia đi.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $48 - 6 = 42$ cái kẹo.
  \item b) \textbf{Đúng}: $42 > 40$.
  \item c) \textbf{Sai}: Còn $42$ cái kẹo.
  \item d) \textbf{Đúng}: $48 : 6 = 8$ lần.
\end{itemize}
}
\end{ex}

% CÂU 15: Quy tắc trừ cột dọc
\begin{ex} %[1D8H31]
Hình minh họa quy tắc trừ cột dọc $37 - 4$:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \VeDatTinhTruDoc{0,0}{37}{4}{33}
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phát biểu về quy tắc trừ:
\choiceTF
{\True Chữ số $4$ viết thẳng cột với chữ số $7$ ở hàng đơn vị.}
{\True Trừ từ phải sang trái: $7$ trừ $4$ bằng $3$, viết $3$.}
{Hạ chữ số $3$ ở hàng chục xuống để được kết quả $33$.}
{\True Kết quả của phép tính trừ gọi là hiệu.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Đơn vị thẳng đơn vị.
  \item b) \textbf{Đúng}: Trừ hàng đơn vị trước.
  \item c) \textbf{Đúng}: Hạ chữ số hàng chục.
  \item d) \textbf{Đúng}: Kết quả phép trừ là hiệu.
\end{itemize}
}
\end{ex}

% CÂU 16: So sánh các hiệu
\begin{ex} %[1D8V31]
Bốn thẻ ghi các phép tính trừ:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (-3,0) {$95 - 3 = 92$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (-1,0) {$67 - 5 = 62$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (1,0) {$88 - 7 = 80$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (3,0) {$76 - 4 = 72$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các phép tính sau:
\choiceTF
{\True $95 - 3 = 92$ là đúng.}
{\True $67 - 5 = 62$ là đúng.}
{Phép tính $88 - 7 = 80$ là đúng.}
{\True $76 - 4 = 72$ là đúng.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $95 - 3 = 92$.
  \item b) \textbf{Đúng}: $67 - 5 = 62$.
  \item c) \textbf{Sai}: $88 - 7 = 81$ (chứ không phải $80$).
  \item d) \textbf{Đúng}: $76 - 4 = 72$.
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN / ĐIỀN SỐ) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Tính 47 - 5
\begin{ex} %[1D8H31]
Tính kết quả phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!30, draw=blue!80, line width=0.7pt, rounded corners=2pt] (-2.0,-0.4) rectangle (2.0,0.4);
  \node[font=\bfseries\normalsize, color=blue!90!black] at (0,0) {$47 - 5 = \dots$};
\end{tikzpicture}
\end{center}
Kết quả của phép tính là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$42$}}
\loigiai{
$47 - 5 = 42$.\\
\textbf{Đáp số: $42$.}
}
\end{ex}

% CÂU 18: Tính 68 - 6
\begin{ex} %[1D8H31]
Tính kết quả phép tính:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=pink!30, draw=red!80, line width=0.7pt, rounded corners=2pt] (-2.0,-0.4) rectangle (2.0,0.4);
  \node[font=\bfseries\normalsize, color=red!90!black] at (0,0) {$68 - 6 = \dots$};
\end{tikzpicture}
\end{center}
Kết quả của phép tính là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$62$}}
\loigiai{
$68 - 6 = 62$.\\
\textbf{Đáp số: $62$.}
}
\end{ex}

% CÂU 19: Bến xe ô tô rời bến
\begin{ex} %[1D8V31]
Bến xe có $36$ chiếc ô tô, có $4$ ô tô rời bến:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=cyan!35, draw=black] (0,0) rectangle (3.2,0.55) node[midway, font=\tiny\bfseries] {Còn lại ? xe};
  \draw[fill=gray!30, draw=black, dashed] (3.2,0) rectangle (4.6,0.55) node[midway, font=\tiny\bfseries] {Rời $4$ xe};
  \draw[line width=0.8pt, stealth-stealth, blue!85] (0,-0.35) -- (4.6,-0.35) node[midway, below, font=\bfseries\tiny] {Ban đầu có $36$ xe};
\end{tikzpicture}
\end{center}
Hỏi trong bến còn lại bao nhiêu chiếc ô tô?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$32$}}
\loigiai{
Trong bến còn lại là: $36 - 4 = 32$ chiếc ô tô.\\
\textbf{Đáp số: $32$ xe.}
}
\end{ex}

% CÂU 20: Vận dụng cao - Biểu thức trừ liên tiếp
\begin{ex} %[1D8C31]
Tính giá trị biểu thức:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!70!orange, draw=black, line width=0.8pt, rounded corners=3pt] (-3.0,-0.45) rectangle (3.0,0.45);
  \node[font=\bfseries\normalsize, color=blue!95!black] at (0,0) {
    $98 - 5 - 3 = \text{\textbf{?}}$
  };
\end{tikzpicture}
\end{center}
Kết quả của biểu thức là bao nhiêu?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$90$}}
\loigiai{
$98 - 5 = 93$; sau đó $93 - 3 = 90$.\\
\textbf{Đáp số: $90$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 8 Bai 31
tex_path = os.path.abspath('CHỦ ĐỀ 8 - PHÉP CỘNG, PHÉP TRỪ (KHÔNG NHỚ) TRONG PHẠM VI 100/Chuong8_Bai31_PhepTruSoCoHaiChuSoChoSoCoMotChuSo.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_31_preview.tex độc lập 5 trang
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 31: TRỪ SỐ CÓ HAI CHỮ SỐ CHO SỐ CÓ MỘT CHỮ SỐ},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 8: Phép cộng, phép trừ PV 100}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-31}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_31_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_31_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_31_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_31_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_31_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    # Sao chép vào PDF_DeThi_TungBai
    out_dir = os.path.abspath('PDF_DeThi_TungBai')
    os.makedirs(out_dir, exist_ok=True)
    out_pdf = os.path.join(out_dir, 'Bai_31_Tru_so_2_chu_so_cho_so_1_chu_so.pdf')
    import shutil
    shutil.copy2('Bai_31_preview.pdf', out_pdf)
    print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
