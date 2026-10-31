# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding='utf-8')

content = r'''% =========================================================================
% BÀI 27: THỰC HÀNH ƯỚC LƯỢNG VÀ ĐO ĐỘ DÀI (CHỦ ĐỀ 7 - ĐỘ DÀI VÀ ĐO ĐỘ DÀI - TOÁN LỚP 1)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ 2D & 3D
% =========================================================================

% --- CÁC HÀM VẼ HÌNH TRỰC QUAN ĐẶC TRƯNG CHO BÀI 27 ---

% 1. Thước kẻ chia cm có đoạn thẳng đặt trên thước
\providecommand{\VeThuocVaDoanThang}[6][cyan]{% #1=màu thước, #2=max cm, #3=vạch đầu, #4=vạch cuối, #5=tên đầu, #6=tên cuối
  \begin{scope}[scale=0.65]
    % Thước kẻ
    \draw[fill=#1!20, draw=black!80, line width=0.7pt, rounded corners=2pt] (-0.4,-0.5) rectangle (#2+0.5,0.5);
    \node[font=\bfseries\tiny, color=#1!80!black] at (-0.1,-0.25) {cm};
    \foreach \x in {0,1,...,#2} {
      \draw[black!85, line width=0.5pt] (\x,0.5) -- (\x,0.18);
      \node[below, font=\tiny\bfseries] at (\x,0.18) {\x};
      \ifnum\x<#2
        \draw[black!60, line width=0.3pt] (\x+0.5,0.5) -- (\x+0.5,0.3);
      \fi
    }
    % Đoạn thẳng phía trên thước
    \draw[line width=2.5pt, red!85] (#3,0.9) -- (#4,0.9);
    \fill[blue!90!black] (#3,0.9) circle (0.12cm) node[above=2pt, font=\bfseries\scriptsize] {#5};
    \fill[blue!90!black] (#4,0.9) circle (0.12cm) node[above=2pt, font=\bfseries\scriptsize] {#6};
    \draw[line width=0.6pt, red!80, dashed] (#3,0.5) -- (#3,1.05);
    \draw[line width=0.6pt, red!80, dashed] (#4,0.5) -- (#4,1.05);
  \end{scope}
}

% 2. Đồ vật đặt trên thước đo
\providecommand{\VeThuocVaDoVat}[6][cyan]{% #1=màu thước, #2=max cm, #3=vạch đầu, #4=chiều dài, #5=màu vật, #6=tên vật
  \begin{scope}[scale=0.65]
    \draw[fill=#1!20, draw=black!80, line width=0.7pt, rounded corners=2pt] (-0.4,-0.5) rectangle (#2+0.5,0.5);
    \node[font=\bfseries\tiny, color=#1!80!black] at (-0.1,-0.25) {cm};
    \foreach \x in {0,1,...,#2} {
      \draw[black!85, line width=0.5pt] (\x,0.5) -- (\x,0.18);
      \node[below, font=\tiny\bfseries] at (\x,0.18) {\x};
      \ifnum\x<#2
        \draw[black!60, line width=0.3pt] (\x+0.5,0.5) -- (\x+0.5,0.3);
      \fi
    }
    \draw[fill=#5!60, draw=black!80, line width=0.6pt, rounded corners=2pt] (#3,0.6) rectangle (#3+#4,1.0);
    \node[font=\bfseries\tiny, color=black] at (#3+#4/2,0.8) {#6};
    \draw[line width=0.6pt, red!80, dashed] (#3,0.5) -- (#3,1.1);
    \draw[line width=0.6pt, red!80, dashed] (#3+#4,0.5) -- (#3+#4,1.1);
  \end{scope}
}

% =========================================================================
% BẮT ĐẦU NỘI DUNG 20 CÂU HỎI
% =========================================================================

\textbf{Phần 1. Trắc nghiệm lựa chọn}
\setcounterpageref{ex}{0}

% --- TRANG 1: CÂU 1 ĐẾN CÂU 4 ---

% CÂU 1: Vạch đặt điểm đầu của đoạn thẳng
\begin{ex} %[1H7N27]
Quan sát cách đặt thước kẻ đo độ dài đoạn thẳng:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeThuocVaDoanThang[cyan]{7}{0}{5}{$A$}{$B$}
  \draw[line width=1.2pt, red!85, ->] (0,-0.7) -- (0,0.1) node[below=14pt, font=\bfseries\tiny, color=red!85] {Đặt tại vạch $0$};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Khi đặt thước đo độ dài, ta phải đặt vạch số nào của thước trùng với một đầu đoạn thẳng?
\begin{multicols}{4}
\choice
{Vạch số $1$}
{\True Vạch số $0$}
{Vạch số $2$}
{Mép ngoài thước}
\end{multicols}
\loigiai{
Quy tắc đo: Phải đặt vạch số $0$ của thước trùng với một đầu của đoạn thẳng.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 2: Đọc độ dài đoạn thẳng từ vạch 0 đến vạch 8
\begin{ex} %[1H7N27]
Đoạn thẳng có một đầu ở vạch $0$, đầu kia ở vạch số $8$ của thước kẻ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}
  \VeThuocVaDoanThang[cyan]{10}{0}{8}{$C$}{$D$}
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Đoạn thẳng $CD$ dài bao nhiêu xăng-ti-mét?
\begin{multicols}{4}
\choice
{$7\text{ cm}$}
{\True $8\text{ cm}$}
{$9\text{ cm}$}
{$10\text{ cm}$}
\end{multicols}
\loigiai{
Vì điểm đầu ở vạch số $0$ và điểm cuối ở vạch số $8$ nên đoạn thẳng dài $8\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 3: Ước lượng độ dài gang tay học sinh lớp 1
\begin{ex} %[1H7H27]
Hình vẽ bàn tay học sinh lớp 1 mở rộng để đo gang tay:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=pink!30, draw=orange!80, line width=0.8pt, rounded corners=3pt] (0,0) rectangle (4.5,0.6);
  \node[font=\bfseries\tiny, color=blue!90!black] at (2.25,0.3) {Một gang tay của em};
  \draw[line width=0.8pt, stealth-stealth, red!85] (0,-0.3) -- (4.5,-0.3) node[midway, below, font=\bfseries\tiny] {Khoảng ? cm};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Một gang tay của học sinh lớp 1 dài khoảng bao nhiêu?
\begin{multicols}{2}
\choice
{$3\text{ cm}$}
{\True $12\text{ cm}$ (khoảng $10 - 14\text{ cm}$)}
{$50\text{ cm}$}
{$100\text{ cm}$}
\end{multicols}
\loigiai{
Gang tay của học sinh lớp 1 dài khoảng $12\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 4: Ước lượng chiều dài bút chì mới gọt
\begin{ex} %[1H7H27]
Cây bút chì gỗ mới gọt đặt cạnh thước kẻ:
\begin{center}\vspace{-2.5mm}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=yellow!50, draw=black!80, line width=0.6pt] (0,0) rectangle (5.0,0.5);
  \draw[fill=yellow!40!brown, draw=black] (5.0,0) -- (5.6,0.25) -- (5.0,0.5) -- cycle;
  \draw[fill=black] (5.4,0.18) -- (5.6,0.25) -- (5.4,0.32) -- cycle;
  \draw[fill=pink, draw=black] (-0.4,0) rectangle (0,0.5);
  \draw[line width=0.8pt, stealth-stealth, blue!85] (-0.4,-0.3) -- (5.6,-0.3) node[midway, below, font=\bfseries\tiny] {Dài khoảng ? cm};
\end{tikzpicture}
\vspace{-2.5mm}\end{center}
Chiếc bút chì mới gọt dài khoảng bao nhiêu?
\begin{multicols}{4}
\choice
{$2\text{ cm}$}
{\True $15\text{ cm}$}
{$50\text{ cm}$}
{$80\text{ cm}$}
\end{multicols}
\loigiai{
Bút chì mới thường dài khoảng $15\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 2: CÂU 5 ĐẾN CÂU 8 ---

% CÂU 5: Ước lượng chiều cao hộp sữa tươi
\begin{ex} %[1H7H27]
Hộp sữa bột / hộp sữa tươi đặt đứng:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=blue!15, draw=blue!80, line width=0.8pt, rounded corners=2pt] (0,0) rectangle (1.4,2.2);
  \node[font=\bfseries\tiny, color=blue!90!black, align=center] at (0.7,1.2) {SỮA\\TƯƠI};
  \draw[fill=red!50, draw=black] (0.5,2.2) rectangle (0.9,2.4);
  \draw[line width=0.8pt, stealth-stealth, orange!90!black] (1.8,0) -- (1.8,2.2) node[midway, right, font=\bfseries\tiny] {Cao khoảng ? cm};
\end{tikzpicture}
\end{center}
Hộp sữa trên cao khoảng bao nhiêu xăng-ti-mét?
\begin{multicols}{4}
\choice
{$2\text{ cm}$}
{\True $18\text{ cm}$}
{$80\text{ cm}$}
{$100\text{ cm}$}
\end{multicols}
\loigiai{
Hộp sữa học sinh cao khoảng $18\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 6: Ước lượng chiều dài cục tẩy
\begin{ex} %[1H7H27]
Cục tẩy học sinh nhỏ gọn:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=white, draw=black!80, line width=0.7pt, rounded corners=2pt] (0,0) rectangle (2.0,0.8);
  \draw[fill=blue!60, draw=black] (0,0) rectangle (0.8,0.8) node[midway, font=\tiny\bfseries, color=white] {ER};
  \draw[line width=0.8pt, stealth-stealth, red!85] (0,-0.35) -- (2.0,-0.35) node[midway, below, font=\bfseries\tiny] {Dài khoảng ? cm};
\end{tikzpicture}
\end{center}
Cục tẩy học sinh dài khoảng bao nhiêu?
\begin{multicols}{4}
\choice
{$15\text{ cm}$}
{\True $3\text{ cm}$}
{$30\text{ cm}$}
{$50\text{ cm}$}
\end{multicols}
\loigiai{
Cục tẩy nhỏ gọn chỉ dài khoảng $3\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 7: Đoạn thẳng không bắt đầu từ vạch 0 (từ 2 đến 9)
\begin{ex} %[1H7V27]
Đoạn thẳng $MN$ đặt trên thước kẻ từ vạch $2\text{ cm}$ đến vạch $9\text{ cm}$:
\begin{center}
\begin{tikzpicture}
  \VeThuocVaDoanThang[cyan]{10}{2}{9}{$M$}{$N$}
\end{tikzpicture}
\end{center}
Độ dài đoạn thẳng $MN$ là:
\begin{multicols}{4}
\choice
{$9\text{ cm}$}
{\True $7\text{ cm}$}
{$8\text{ cm}$}
{$11\text{ cm}$}
\end{multicols}
\loigiai{
Độ dài đoạn thẳng $MN$ là: $9 - 2 = 7\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 8: Đoạn thẳng đặt từ vạch 3 đến vạch 10
\begin{ex} %[1H7V27]
Đoạn thẳng $PQ$ đặt trên thước kẻ từ vạch $3\text{ cm}$ đến vạch $10\text{ cm}$:
\begin{center}
\begin{tikzpicture}
  \VeThuocVaDoanThang[cyan]{11}{3}{10}{$P$}{$Q$}
\end{tikzpicture}
\end{center}
Độ dài đoạn thẳng $PQ$ là:
\begin{multicols}{4}
\choice
{$10\text{ cm}$}
{\True $7\text{ cm}$}
{$8\text{ cm}$}
{$13\text{ cm}$}
\end{multicols}
\loigiai{
Độ dài đoạn thẳng $PQ$ là: $10 - 3 = 7\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 3: CÂU 9 ĐẾN CÂU 12 ---

% CÂU 9: Độ chênh lệch giữa ước lượng và đo thật
\begin{ex} %[1H7V27]
Hộp bút của bạn Mai:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!25, draw=orange!80, line width=0.8pt, rounded corners=3pt] (-3,-0.5) rectangle (3,0.5);
  \node[font=\bfseries\tiny, color=blue!90!black] at (0,0.15) {Ước lượng: $20\text{ cm}$ \quad | \quad Đo thật: $22\text{ cm}$};
  \node[below, font=\bfseries\tiny, color=red!85] at (0,-0.1) {Chênh lệch: ? cm};
\end{tikzpicture}
\end{center}
Ước lượng chênh lệch so với đo thật là bao nhiêu xăng-ti-mét?
\begin{multicols}{4}
\choice
{$1\text{ cm}$}
{\True $2\text{ cm}$}
{$3\text{ cm}$}
{$4\text{ cm}$}
\end{multicols}
\loigiai{
Độ chênh lệch là: $22 - 20 = 2\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 10: Ước lượng bề dày cuốn sách Toán 1
\begin{ex} %[1H7V27]
Gáy cuốn sách Toán 1 đặt đứng:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=blue!35, draw=black!80, line width=0.7pt] (-0.3,0) rectangle (0.3,2.0);
  \node[rotate=90, font=\bfseries\tiny, color=white] at (0,1.0) {TOÁN 1};
  \draw[line width=0.8pt, stealth-stealth, red!85] (-0.3,-0.3) -- (0.3,-0.3) node[midway, below, font=\bfseries\tiny] {Bề dày ?};
\end{tikzpicture}
\end{center}
Bề dày cuốn sách giáo khoa Toán 1 khoảng bao nhiêu?
\begin{multicols}{4}
\choice
{$10\text{ cm}$}
{\True $1\text{ cm}$}
{$5\text{ cm}$}
{$20\text{ cm}$}
\end{multicols}
\loigiai{
Bề dày cuốn sách giáo khoa mỏng khoảng $1\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 11: Đo quyển vở bằng 2 gang tay
\begin{ex} %[1H7V27]
Đo chiều dài quyển vở bằng $2$ gang tay (mỗi gang tay dài $10\text{ cm}$):
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=cyan!20, draw=blue!80, line width=0.7pt, rounded corners=2pt] (0,0) rectangle (2.5,0.6) node[midway, font=\bfseries\tiny] {Gang 1: $10\text{ cm}$};
  \draw[fill=cyan!20, draw=blue!80, line width=0.7pt, rounded corners=2pt] (2.5,0) rectangle (5.0,0.6) node[midway, font=\bfseries\tiny] {Gang 2: $10\text{ cm}$};
  \draw[line width=0.8pt, stealth-stealth, orange!90!black] (0,-0.3) -- (5.0,-0.3) node[midway, below, font=\bfseries\tiny] {Quyển vở dài khoảng ? cm};
\end{tikzpicture}
\end{center}
Quyển vở dài khoảng bao nhiêu xăng-ti-mét?
\begin{multicols}{4}
\choice
{$15\text{ cm}$}
{\True $20\text{ cm}$}
{$25\text{ cm}$}
{$30\text{ cm}$}
\end{multicols}
\loigiai{
Quyển vở dài khoảng: $10 + 10 = 20\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

% CÂU 12: Vận dụng cao - Chú kiến bò trên thước kẻ
\begin{ex} %[1H7C27]
Con kiến bò từ vạch $1\text{ cm}$ đến vạch $6\text{ cm}$ rồi quay lại vạch $4\text{ cm}$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \VeThuocChiaCm[cyan]{7}{0,0}
  % Đường bò lượt đi
  \draw[line width=1.2pt, red!85, ->] (0.7,0.7) -- (4.2,0.7) node[midway, above, font=\tiny\bfseries] {Đi $5\text{ cm}$};
  % Đường bò quay lại
  \draw[line width=1.2pt, blue!85, ->] (4.2,1.2) -- (2.8,1.2) node[midway, above, font=\tiny\bfseries] {Về $2\text{ cm}$};
  \fill[black] (0.7,0.7) circle (0.08cm);
  \fill[red] (4.2,0.7) circle (0.08cm);
  \fill[blue] (2.8,1.2) circle (0.08cm);
\end{tikzpicture}
\end{center}
Tổng quãng đường con kiến đã bò là:
\begin{multicols}{4}
\choice
{$5\text{ cm}$}
{\True $7\text{ cm}$}
{$6\text{ cm}$}
{$8\text{ cm}$}
\end{multicols}
\loigiai{
Lượt đi từ vạch $1$ đến $6$: $6 - 1 = 5\text{ cm}$.\\
Lượt về từ vạch $6$ về $4$: $6 - 4 = 2\text{ cm}$.\\
Tổng quãng đường: $5 + 2 = 7\text{ cm}$.\\
\textbf{Đáp án: B.}
}
\end{ex}

\newpage
% --- TRANG 4: CÂU 13 ĐẾN CÂU 16 (ĐÚNG / SAI) ---

\textbf{Phần 2. Trắc nghiệm đúng sai}
\setcounterpageref{ex}{0}

% CÂU 13: Quy tắc đo độ dài
\begin{ex} %[1H7H27]
Quy trình các bước đo độ dài bằng thước kẻ chia cm:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[fill=yellow!20, draw=black!80, line width=0.6pt, rounded corners=2pt] (-4,-0.5) rectangle (4,0.5);
  \node[font=\bfseries\scriptsize, color=blue!90!black] at (0,0) {Đặt mép thước -- Đặt vạch $0$ -- Đọc vạch cuối};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các khẳng định về cách đo:
\choiceTF
{\True Đặt mép thước dọc theo đoạn thẳng cần đo.}
{\True Đặt vạch số $0$ của thước trùng với một đầu đoạn thẳng.}
{Có thể đặt bất kì vạch nào mà không cần nhìn vạch số $0$.}
{\True Nhìn vạch số ở đầu kia của đoạn thẳng để đọc số đo chính xác.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Mép thước phải áp sát đoạn thẳng.
  \item b) \textbf{Đúng}: Điểm đầu luôn trùng vạch $0$.
  \item c) \textbf{Sai}: Phải đặt đúng vạch số $0$.
  \item d) \textbf{Đúng}: Đọc số vạch ở điểm cuối.
\end{itemize}
}
\end{ex}

% CÂU 14: Đoạn AB và BC
\begin{ex} %[1H7V27]
Đoạn thẳng $AB$ dài $10\text{ cm}$ và đoạn thẳng $BC$ dài $8\text{ cm}$:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \draw[line width=2pt, blue!80] (0,0) -- (4,0) node[midway, above, font=\bfseries\tiny] {$AB = 10\text{ cm}$};
  \draw[line width=2pt, orange!90] (4,0) -- (7.2,0) node[midway, above, font=\bfseries\tiny] {$BC = 8\text{ cm}$};
  \fill[red] (0,0) circle (0.1cm);
  \fill[red] (4,0) circle (0.1cm);
  \fill[red] (7.2,0) circle (0.1cm);
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các nhận xét sau:
\choiceTF
{\True Đoạn thẳng $AB$ dài hơn đoạn thẳng $BC$ là $2\text{ cm}$.}
{\True Cả hai đoạn thẳng dài tất cả là $18\text{ cm}$.}
{Đoạn thẳng $BC$ dài hơn đoạn thẳng $AB$.}
{\True Đoạn thẳng $BC$ ngắn hơn đoạn thẳng $AB$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $10 - 8 = 2\text{ cm}$.
  \item b) \textbf{Đúng}: $10 + 8 = 18\text{ cm}$.
  \item c) \textbf{Sai}: $BC$ ngắn hơn $AB$ ($8 < 10$).
  \item d) \textbf{Đúng}: $BC$ ngắn hơn $AB$.
\end{itemize}
}
\end{ex}

% CÂU 15: Ước lượng đồ dùng quen thuộc
\begin{ex} %[1H7V27]
Ước lượng chiều dài ba đồ dùng học tập:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (-3,0) {Hộp bút: $20\text{ cm}$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (0,0) {Thước kẻ: $20\text{ cm}$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (3,0) {Cục tẩy: $3\text{ cm}$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các ước lượng sau:
\choiceTF
{\True Chiếc thước kẻ dài khoảng $20\text{ cm}$.}
{\True Chiếc hộp bút dài khoảng $20\text{ cm}$.}
{Cục tẩy học sinh dài khoảng $30\text{ cm}$.}
{\True Chiều dài cục tẩy khoảng $3\text{ cm}$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: Thước kẻ học sinh thông dụng dài $20\text{ cm}$.
  \item b) \textbf{Đúng}: Hộp bút dài khoảng $20\text{ cm}$.
  \item c) \textbf{Sai}: Cục tẩy $30\text{ cm}$ là quá dài (bằng cả cây thước dài).
  \item d) \textbf{Đúng}: Cục tẩy dài khoảng $3\text{ cm}$.
\end{itemize}
}
\end{ex}

% CÂU 16: So sánh độ dài các đoạn trên thước
\begin{ex} %[1H7V27]
Các đoạn thẳng trên cùng một cây thước chia cm:
\begin{center}
\begin{tikzpicture}[scale=0.6]
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (-3,0) {Đoạn $1$: từ $0$ đến $6\text{ cm}$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (0,0) {Đoạn $2$: từ $2$ đến $8\text{ cm}$};
  \node[draw=blue!80, fill=cyan!15, rounded corners=2pt, font=\bfseries\tiny] at (3,0) {Đoạn $3$: từ $1$ đến $5\text{ cm}$};
\end{tikzpicture}
\end{center}
Xét tính đúng hoặc sai của các so sánh sau:
\choiceTF
{\True Đoạn $1$ dài $6\text{ cm}$ ($6 - 0 = 6$).}
{\True Đoạn $2$ dài $6\text{ cm}$ ($8 - 2 = 6$).}
{\True Đoạn $1$ và Đoạn $2$ dài bằng nhau.}
{Đoạn $3$ dài $5\text{ cm}$.}
\loigiai{
\begin{itemize}
  \item a) \textbf{Đúng}: $6 - 0 = 6\text{ cm}$.
  \item b) \textbf{Đúng}: $8 - 2 = 6\text{ cm}$.
  \item c) \textbf{Đúng}: Cả hai đoạn đều dài $6\text{ cm}$.
  \item d) \textbf{Sai}: Đoạn $3$ dài $5 - 1 = 4\text{ cm}$ (chứ không phải $5\text{ cm}$).
\end{itemize}
}
\end{ex}

\newpage
% --- TRANG 5: CÂU 17 ĐẾN CÂU 20 (TRẢ LỜI NGẮN / ĐIỀN SỐ) ---

\textbf{Phần 3. Trả lời ngắn}
\setcounterpageref{ex}{0}

% CÂU 17: Đoạn thẳng từ 0 đến 9
\begin{ex} %[1H7H27]
Đoạn thẳng $AB$ có điểm đầu trùng vạch $0$, điểm cuối trùng vạch số $9$ của thước:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \VeThuocVaDoanThang[cyan]{10}{0}{9}{$A$}{$B$}
\end{tikzpicture}
\end{center}
Đoạn thẳng $AB$ dài bao nhiêu xăng-ti-mét?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$9$}}
\loigiai{
Đoạn thẳng $AB$ dài đúng $9\text{ cm}$.\\
\textbf{Đáp số: $9$.}
}
\end{ex}

% CÂU 18: Đoạn thẳng từ 2 đến 8
\begin{ex} %[1H7H27]
Đoạn thẳng $CD$ có điểm đầu ở vạch $2\text{ cm}$, điểm cuối ở vạch $8\text{ cm}$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \VeThuocVaDoanThang[cyan]{10}{2}{8}{$C$}{$D$}
\end{tikzpicture}
\end{center}
Đoạn thẳng $CD$ dài bao nhiêu xăng-ti-mét?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$6$}}
\loigiai{
Độ dài đoạn thẳng $CD$ là: $8 - 2 = 6\text{ cm}$.\\
\textbf{Đáp số: $6$.}
}
\end{ex}

% CÂU 19: Nối hai que tính
\begin{ex} %[1H7V27]
Nối hai que tính: que thứ nhất dài $6\text{ cm}$, que thứ hai dài $8\text{ cm}$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[fill=yellow!35, draw=black] (0,0) rectangle (3.0,0.5) node[midway, font=\tiny\bfseries] {$6\text{ cm}$};
  \draw[fill=orange!35, draw=black] (3.0,0) rectangle (7.0,0.5) node[midway, font=\tiny\bfseries] {$8\text{ cm}$};
  \draw[line width=0.8pt, stealth-stealth, red!85] (0,-0.35) -- (7.0,-0.35) node[midway, below, font=\bfseries\tiny] {Tổng độ dài = ? cm};
\end{tikzpicture}
\end{center}
Tổng độ dài của hai que tính sau khi nối là bao nhiêu xăng-ti-mét?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$14$}}
\loigiai{
Tổng độ dài là: $6 + 8 = 14\text{ cm}$.\\
\textbf{Đáp số: $14$.}
}
\end{ex}

% CÂU 20: Vận dụng cao - Điểm nằm giữa đoạn thẳng
\begin{ex} %[1H7C27]
Đoạn thẳng $AB$ dài $15\text{ cm}$. Điểm $M$ nằm giữa $A$ và $B$ sao cho $AM = 7\text{ cm}$:
\begin{center}
\begin{tikzpicture}[scale=0.65]
  \draw[line width=2.5pt, blue!85] (0,0) -- (3.5,0) node[midway, above, font=\bfseries\tiny] {$7\text{ cm}$};
  \draw[line width=2.5pt, orange!90] (3.5,0) -- (7.5,0) node[midway, above, font=\bfseries\tiny] {? cm};
  \fill[red] (0,0) circle (0.12cm) node[below=2pt, font=\bfseries\scriptsize] {$A$};
  \fill[red] (3.5,0) circle (0.12cm) node[below=2pt, font=\bfseries\scriptsize] {$M$};
  \fill[red] (7.5,0) circle (0.12cm) node[below=2pt, font=\bfseries\scriptsize] {$B$};
  \draw[line width=0.8pt, stealth-stealth, black!70] (0,-0.4) -- (7.5,-0.4) node[midway, below, font=\bfseries\tiny] {Đoạn $AB = 15\text{ cm}$};
\end{tikzpicture}
\end{center}
Độ dài đoạn thẳng $MB$ là bao nhiêu xăng-ti-mét?
\textit{Trả lời:} \raisebox{-2pt}{\tcbox[colframe=blue!80!black,colback=white,size=small,arc=3pt]{$8$}}
\loigiai{
Độ dài đoạn thẳng $MB$ là: $15 - 7 = 8\text{ cm}$.\\
\textbf{Đáp số: $8$.}
}
\end{ex}
'''

# 1. Ghi file source TeX cho Chuong 7 Bai 27
tex_path = os.path.abspath('CHỦ ĐỀ 7 - ĐỘ DÀI VÀ ĐO ĐỘ DÀI/Chuong7_Bai27_ThucHanhUocLuongVaDoDoDai.tex')
with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Đã ghi: {tex_path}")

# 2. Tạo file xem trước Bai_27_preview.tex độc lập 5 trang
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
\begin{tcolorbox}[colback=blue!5!white,colframe=blue!75!black,title=\textbf{\large ĐỀ KIỂM TRA TOÁN LỚP 1 -- BÀI 27: THỰC HÀNH ƯỚC LƯỢNG VÀ ĐO ĐỘ DÀI},arc=2.5mm,top=1.5mm,bottom=1.5mm]
\begin{minipage}{0.78\textwidth}
  \textbf{Học kì 2 -- Chủ đề 7: Độ dài và đo độ dài}\\
  \textbf{Thời gian làm bài:} 40 phút \quad | \quad \textbf{Hình thức:} 100\% Trực quan hình vẽ\\
  \textit{Họ và tên học sinh:} \dotfill \quad \textit{Lớp:} \dotfill
\end{minipage}
\begin{minipage}{0.20\textwidth}
  \centering
  \qrcode[height=1.5cm]{https://loptoanthaylinh.vn/thi-online/toan-1/bai-27}\\
  \vspace{0.8mm}
  \textbf{\scriptsize Quét mã thi Online}
\end{minipage}
\end{tcolorbox}
\vspace{0.1cm}

''' + content + r'''

\end{document}
'''

preview_path = os.path.abspath('Bai_27_preview.tex')
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(preview_content)
print(f"Đã ghi: {preview_path}")

# 3. Biên dịch Bai_27_preview.tex
res = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'Bai_27_preview.tex'],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='ignore')

if res.returncode == 0 or os.path.exists('Bai_27_preview.pdf'):
    import pypdf
    reader = pypdf.PdfReader('Bai_27_preview.pdf')
    num_pages = len(reader.pages)
    print(f"SỐ TRANG PREVIEW: {num_pages}")
    
    # Sao chép vào PDF_DeThi_TungBai
    out_dir = os.path.abspath('PDF_DeThi_TungBai')
    os.makedirs(out_dir, exist_ok=True)
    out_pdf = os.path.join(out_dir, 'Bai_27_Thuc_hanh_uoc_luong_va_do_do_dai.pdf')
    import shutil
    shutil.copy2('Bai_27_preview.pdf', out_pdf)
    print(f"ĐÃ XUẤT THÀNH CÔNG: {out_pdf} ({num_pages} trang)")
else:
    print("BIÊN DỊCH LỖI:")
    print(res.stdout[-1500:])
