import os

content = r'''% =========================================================================
% BÀI 08: THỰC HÀNH LẮP GHÉP, XẾP HÌNH (CHỦ ĐỀ 2)
% TOÀN BỘ CÂU HỎI ĐƯỢC VẼ HÌNH MINH HỌA TRỰC QUAN 100% BẰNG TIKZ
% =========================================================================

% --- HÀM VẼ THANH QUE TÍNH CHO HỌC SINH LỚP 1 ---
\newcommand{\VeQue}[5]{% #1=x1, #2=y1, #3=x2, #4=y2, #5=màu
  \draw[line width=3.5pt, #5, line cap=round] (#1,#2) -- (#3,#4);
  \fill[red!85!black] (#3,#4) circle (0.09cm);
}

% =========================================================================
% PHẦN 1: TRẮC NGHIỆM LỰA CHỌN (12 CÂU)
% =========================================================================
\textbf{Phần 1. Trắc nghiệm lựa chọn (Học sinh quan sát hình và chọn đáp án đúng)}
\setcounterpageref{ex}{0}

% --- CÂU 1 ---
\begin{ex} %[1H2N08]
Dùng các que tính để xếp hình tam giác như hình dưới, cần ít nhất bao nhiêu que tính?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \VeQue{-1.4}{-0.7}{1.4}{-0.7}{orange!85!black}
  \VeQue{1.4}{-0.7}{0}{1.2}{blue!80!black}
  \VeQue{0}{1.2}{-1.4}{-0.7}{green!70!black}
  \node[font=\footnotesize\bfseries\color{orange!90!black}] at (0,-1.05) {que 1};
  \node[font=\footnotesize\bfseries\color{blue!90!black}, rotate=53] at (0.95,0.4) {que 2};
  \node[font=\footnotesize\bfseries\color{green!70!black}, rotate=-53] at (-0.95,0.4) {que 3};
\end{tikzpicture}
\end{center}
\choice
{$2$ que}
{\True $3$ que}
{$4$ que}
{$5$ que}
\loigiai{
Cần ít nhất $3$ que tính để xếp được một hình tam giác.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 2 ---
\begin{ex} %[1H2N08]
Dùng các que tính bằng nhau để xếp hình vuông như hình dưới, cần ít nhất bao nhiêu que tính?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \VeQue{-1.0}{-1.0}{1.0}{-1.0}{orange!85!black}
  \VeQue{1.0}{-1.0}{1.0}{1.0}{blue!80!black}
  \VeQue{1.0}{1.0}{-1.0}{1.0}{green!70!black}
  \VeQue{-1.0}{1.0}{-1.0}{-1.0}{purple!80!black}
\end{tikzpicture}
\end{center}
\choice
{$3$ que}
{\True $4$ que}
{$5$ que}
{$6$ que}
\loigiai{
Cần ít nhất $4$ que tính bằng nhau để xếp được một hình vuông.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 3 ---
\begin{ex} %[1H2H08]
Dùng 6 que tính có thể xếp được bao nhiêu hình tam giác riêng biệt như hình dưới đây?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Tam giác 1
  \VeQue{-2.6}{-0.6}{-0.6}{-0.6}{orange!85!black}
  \VeQue{-0.6}{-0.6}{-1.6}{0.9}{blue!80!black}
  \VeQue{-1.6}{0.9}{-2.6}{-0.6}{green!70!black}
  \node[font=\bfseries\color{blue!85!black}] at (-1.6,-1.0) {Hình 1};
  % Tam giác 2
  \VeQue{0.6}{-0.6}{2.6}{-0.6}{orange!85!black}
  \VeQue{2.6}{-0.6}{1.6}{0.9}{blue!80!black}
  \VeQue{1.6}{0.9}{0.6}{-0.6}{green!70!black}
  \node[font=\bfseries\color{blue!85!black}] at (1.6,-1.0) {Hình 2};
\end{tikzpicture}
\end{center}
\choice
{$1$ hình}
{\True $2$ hình}
{$3$ hình}
{$4$ hình}
\loigiai{
Mỗi hình tam giác cần 3 que tính. 6 que tính xếp được: $6 : 3 = 2$ hình tam giác.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 4 ---
\begin{ex} %[1H2H08]
Dùng 8 que tính bằng nhau có thể xếp được bao nhiêu hình vuông riêng biệt như hình dưới?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Hình vuông 1
  \VeQue{-2.5}{-0.8}{-1.1}{-0.8}{orange!85!black}
  \VeQue{-1.1}{-0.8}{-1.1}{0.6}{blue!80!black}
  \VeQue{-1.1}{0.6}{-2.5}{0.6}{green!70!black}
  \VeQue{-2.5}{0.6}{-2.5}{-0.8}{purple!80!black}
  \node[font=\bfseries\color{blue!85!black}] at (-1.8,-1.15) {Hình 1};
  % Hình vuông 2
  \VeQue{1.1}{-0.8}{2.5}{-0.8}{orange!85!black}
  \VeQue{2.5}{-0.8}{2.5}{0.6}{blue!80!black}
  \VeQue{2.5}{0.6}{1.1}{0.6}{green!70!black}
  \VeQue{1.1}{0.6}{1.1}{-0.8}{purple!80!black}
  \node[font=\bfseries\color{blue!85!black}] at (1.8,-1.15) {Hình 2};
\end{tikzpicture}
\end{center}
\choice
{$1$ hình}
{\True $2$ hình}
{$3$ hình}
{$4$ hình}
\loigiai{
Mỗi hình vuông cần 4 que tính. 8 que tính xếp được: $8 : 4 = 2$ hình vuông.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% --- CÂU 5 ---
\begin{ex} %[1H2H08]
Ghép hai hình vuông nhỏ bằng nhau cạnh nhau như hình vẽ, ta được một:
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \draw[fill=yellow!35, draw=orange!90!black, line width=1.4pt] (-1.6,-0.8) rectangle (0,0.8);
  \node[font=\bfseries\color{orange!90!black}] at (-0.8,0) {Hình vuông};
  \draw[fill=cyan!30, draw=blue!90!black, line width=1.4pt] (0,-0.8) rectangle (1.6,0.8);
  \node[font=\bfseries\color{blue!90!black}] at (0.8,0) {Hình vuông};
  \draw[line width=1.4pt, red!80!black, dashed] (0,-0.8) -- (0,0.8);
\end{tikzpicture}
\end{center}
\choice
{Hình vuông lớn}
{\True Hình chữ nhật}
{Hình tam giác}
{Hình tròn}
\loigiai{
Ghép 2 hình vuông cạnh nhau ta được một \textbf{hình chữ nhật}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 6 ---
\begin{ex} %[1H2H08]
Muốn ghép thành một hình vuông lớn từ các hình vuông nhỏ bằng nhau như hình vẽ, cần ít nhất mấy hình vuông nhỏ?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \draw[fill=yellow!30, draw=orange!80, line width=1.2pt] (-1.2,0) rectangle (0,1.2);
  \draw[fill=cyan!30, draw=blue!80, line width=1.2pt] (0,0) rectangle (1.2,1.2);
  \draw[fill=green!30, draw=green!70!black, line width=1.2pt] (-1.2,-1.2) rectangle (0,0);
  \draw[fill=pink!40, draw=magenta!70, line width=1.2pt] (0,-1.2) rectangle (1.2,0);
  \draw[line width=1.6pt, blue!90!black] (-1.2,-1.2) rectangle (1.2,1.2);
  \node[font=\bfseries] at (-0.6,0.6) {1};
  \node[font=\bfseries] at (0.6,0.6) {2};
  \node[font=\bfseries] at (-0.6,-0.6) {3};
  \node[font=\bfseries] at (0.6,-0.6) {4};
\end{tikzpicture}
\end{center}
\choice
{$2$ hình}
{\True $4$ hình}
{$3$ hình}
{$5$ hình}
\loigiai{
Cần ít nhất \textbf{4 hình vuông nhỏ} (xếp 2 hàng, 2 cột) để ghép thành một hình vuông lớn.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 7 ---
\begin{ex} %[1H2V08]
Để xếp hình chiếc thuyền buồm như hình dưới đây, em cần bao nhiêu hình phẳng?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Thân thuyền
  \draw[fill=brown!55!black, draw=brown!90!black, line width=1.4pt] (-1.8,-0.5) -- (1.8,-0.5) -- (1.2,-1.1) -- (-1.2,-1.1) -- cycle;
  \node[font=\footnotesize\bfseries\color{white}] at (0,-0.8) {1. Thân thuyền};
  % Cánh buồm 1
  \draw[fill=red!75, draw=red!90!black, line width=1.2pt] (0.1,-0.3) -- (1.5,-0.3) -- (0.1,1.3) -- cycle;
  \node[font=\tiny\bfseries\color{white}] at (0.55,0.2) {2. Buồm};
  % Cánh buồm 2
  \draw[fill=yellow!85, draw=orange!90!black, line width=1.2pt] (-0.1,-0.3) -- (-1.3,-0.3) -- (-0.1,1.0) -- cycle;
  \node[font=\tiny\bfseries\color{black}] at (-0.5,0.15) {3. Buồm};
\end{tikzpicture}
\end{center}
\choice
{$2$ hình}
{\True $3$ hình}
{$4$ hình}
{$5$ hình}
\loigiai{
Gồm 3 hình phẳng ghép lại: 1 thân thuyền và 2 cánh buồm tam giác.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 8 ---
\begin{ex} %[1H2V08]
Bé An có 7 que tính. Sau khi xếp được 1 hình vuông (hết 4 que), An còn thừa mấy que tính?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Hình vuông 4 que
  \VeQue{-2.2}{-0.7}{-0.8}{-0.7}{blue!80!black}
  \VeQue{-0.8}{-0.7}{-0.8}{0.7}{blue!80!black}
  \VeQue{-0.8}{0.7}{-2.2}{0.7}{blue!80!black}
  \VeQue{-2.2}{0.7}{-2.2}{-0.7}{blue!80!black}
  \node[font=\footnotesize\bfseries\color{blue!85!black}] at (-1.5,-1.1) {Đã dùng 4 que};
  % 3 que thừa
  \VeQue{0.6}{-0.5}{0.6}{0.7}{orange!85!black}
  \VeQue{1.3}{-0.5}{1.3}{0.7}{orange!85!black}
  \VeQue{2.0}{-0.5}{2.0}{0.7}{orange!85!black}
  \node[font=\footnotesize\bfseries\color{orange!90!black}] at (1.3,-1.1) {Còn thừa: ? que};
\end{tikzpicture}
\end{center}
\choice
{$2$ que}
{\True $3$ que}
{$4$ que}
{$1$ que}
\loigiai{
$7 - 4 = 3$. An còn thừa \textbf{3 que tính}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% --- CÂU 9 ---
\begin{ex} %[1H2V08]
Với 3 que tính còn thừa đó, An có thể xếp thêm được 1 hình gì?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \VeQue{-1.3}{-0.6}{1.3}{-0.6}{orange!85!black}
  \VeQue{1.3}{-0.6}{0}{1.1}{blue!80!black}
  \VeQue{0}{1.1}{-1.3}{-0.6}{green!70!black}
\end{tikzpicture}
\end{center}
\choice
{Hình vuông}
{\True Hình tam giác}
{Hình chữ nhật}
{Hình tròn}
\loigiai{
Với 3 que tính có thể xếp được 1 \textbf{hình tam giác}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 10 ---
\begin{ex} %[1H2V08]
Có 10 que tính, xếp được 2 hình vuông riêng biệt (hết 8 que). Hỏi còn thừa bao nhiêu que tính?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Hình vuông 1
  \VeQue{-3.2}{-0.6}{-2.0}{-0.6}{blue!80!black}
  \VeQue{-2.0}{-0.6}{-2.0}{0.6}{blue!80!black}
  \VeQue{-2.0}{0.6}{-3.2}{0.6}{blue!80!black}
  \VeQue{-3.2}{0.6}{-3.2}{-0.6}{blue!80!black}
  % Hình vuông 2
  \VeQue{-1.4}{-0.6}{-0.2}{-0.6}{blue!80!black}
  \VeQue{-0.2}{-0.6}{-0.2}{0.6}{blue!80!black}
  \VeQue{-0.2}{0.6}{-1.4}{0.6}{blue!80!black}
  \VeQue{-1.4}{0.6}{-1.4}{-0.6}{blue!80!black}
  \node[font=\footnotesize\bfseries\color{blue!85!black}] at (-1.7,-1.0) {2 hình vuông (8 que)};
  % 2 que thừa
  \VeQue{1.2}{-0.5}{1.2}{0.6}{orange!85!black}
  \VeQue{2.0}{-0.5}{2.0}{0.6}{orange!85!black}
  \node[font=\footnotesize\bfseries\color{orange!90!black}] at (1.6,-1.0) {Thừa: ? que};
\end{tikzpicture}
\end{center}
\choice
{$1$ que}
{\True $2$ que}
{$3$ que}
{$4$ que}
\loigiai{
$10 - 8 = 2$ que tính. Còn thừa \textbf{2 que tính}.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 11 ---
\begin{ex} %[1H2V08]
Xếp một hình con cá gồm 1 hình vuông làm thân và 1 hình tam giác làm đuôi như hình vẽ. Cần tất cả mấy hình phẳng?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Thân cá hình vuông xoay 45 độ
  \draw[fill=yellow!40, draw=orange!90!black, line width=1.4pt, rotate=45] (-0.8,-0.8) rectangle (0.8,0.8);
  \fill[black] (0.5,0.2) circle (0.08cm);
  \node[font=\footnotesize\bfseries\color{orange!90!black}] at (0, -0.1) {Thân cá};
  % Đuôi cá tam giác
  \draw[fill=cyan!35, draw=blue!90!black, line width=1.4pt] (-1.13,0) -- (-2.3,0.8) -- (-2.3,-0.8) -- cycle;
  \node[font=\footnotesize\bfseries\color{blue!90!black}] at (-1.8, 0) {Đuôi};
\end{tikzpicture}
\end{center}
\choice
{$1$ hình}
{\True $2$ hình}
{$3$ hình}
{$4$ hình}
\loigiai{
Cần \textbf{2 hình phẳng}: 1 hình vuông làm thân và 1 hình tam giác làm đuôi.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

% --- CÂU 12 ---
\begin{ex} %[1H2C08]
Để xếp 2 hình tam giác dính liền chung nhau 1 cạnh như hình dưới, cần ít nhất bao nhiêu que tính?
\begin{center}
\begin{tikzpicture}[scale=0.9, baseline=(current bounding box.center)]
  \VeQue{-1.4}{-0.7}{0}{-0.7}{orange!85!black}
  \VeQue{0}{-0.7}{1.4}{-0.7}{orange!85!black}
  \VeQue{1.4}{-0.7}{0}{1.1}{blue!80!black}
  \VeQue{0}{1.1}{-1.4}{-0.7}{green!70!black}
  % Cạnh chung
  \VeQue{0}{-0.7}{0}{1.1}{red!85!black}
  \node[font=\tiny\bfseries\color{red!85!black}] at (0.45,0.2) {Cạnh chung};
\end{tikzpicture}
\end{center}
\choice
{$6$ que}
{\True $5$ que}
{$4$ que}
{$3$ que}
\loigiai{
Vì có 1 cạnh chung nên số que tính cần là: $3 + 3 - 1 = \textbf{5 que tính}$.\\
\textbf{Đáp án của câu hỏi là B}
}
\end{ex}

\newpage
% =========================================================================
% PHẦN 2: TRẮC NGHIỆM ĐÚNG SAI
% =========================================================================
\textbf{Phần 2. Trắc nghiệm đúng sai (Quan sát hình vẽ và xét tính đúng/sai)}
\setcounterpageref{ex}{0}

% --- CÂU 13 ---
\begin{ex} %[1H2H08]
Quan sát các hình được xếp bằng que tính dưới đây:
\begin{center}
\setlength{\tabcolsep}{10pt}
\begin{tabular}{ccc}
  % Tam giác 3 que
  \begin{tikzpicture}[scale=0.65]
    \VeQue{-1.1}{-0.6}{1.1}{-0.6}{orange!85!black}
    \VeQue{1.1}{-0.6}{0}{1.0}{blue!80!black}
    \VeQue{0}{1.0}{-1.1}{-0.6}{green!70!black}
    \node[font=\footnotesize\bfseries\color{blue!85!black}] at (0,-1.0) {Tam giác (3 que)};
  \end{tikzpicture}
  &
  % Hình vuông 4 que
  \begin{tikzpicture}[scale=0.65]
    \VeQue{-0.85}{-0.85}{0.85}{-0.85}{orange!85!black}
    \VeQue{0.85}{-0.85}{0.85}{0.85}{blue!80!black}
    \VeQue{0.85}{0.85}{-0.85}{0.85}{green!70!black}
    \VeQue{-0.85}{0.85}{-0.85}{-0.85}{purple!80!black}
    \node[font=\footnotesize\bfseries\color{blue!85!black}] at (0,-1.2) {Hình vuông (4 que)};
  \end{tikzpicture}
  &
  % Hình tròn
  \begin{tikzpicture}[scale=0.65]
    \draw[fill=orange!15, draw=orange!90!black, line width=1.5pt] (0,0) circle (0.85cm);
    \node[font=\footnotesize\bfseries\color{orange!90!black}] at (0,-1.2) {Hình tròn (viền cong)};
  \end{tikzpicture}
\end{tabular}
\end{center}
Xét tính đúng sai của các câu sau:
\choiceTF
{\True Dùng 3 que tính có thể xếp được 1 hình tam giác}
{\True Dùng 4 que tính bằng nhau có thể xếp được 1 hình vuông}
{Dùng các que tính thẳng có thể xếp được 1 hình tròn}
{\True Hình tròn có viền cong nên không thể xếp bằng các que tính thẳng}
\loigiai{
\begin{itemize}
    \item 3 que tính xếp được 1 tam giác: \textbf{Đúng}.
    \item 4 que tính bằng nhau xếp được 1 hình vuông: \textbf{Đúng}.
    \item Que tính thẳng không thể uốn thành đường tròn cong kín: \textbf{Sai}.
    \item Hình tròn cong kín không xếp bằng que thẳng: \textbf{Đúng}.
\end{itemize}
}
\end{ex}

% --- CÂU 14 ---
\begin{ex} %[1H2V08]
Bạn Nam có 9 que tính màu sắc như hình dưới đây:
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \draw[fill=yellow!10, draw=orange!70, line width=1pt, rounded corners=4pt] (-3.8,-0.9) rectangle (3.8,0.9);
  \foreach \x/\c in {-3.2/purple!70, -2.4/purple!70, -1.6/purple!70, -0.8/orange!85!black, 0/orange!85!black, 0.8/orange!85!black, 1.6/teal!70, 2.4/teal!70, 3.2/teal!70} {
    \VeQue{\x}{-0.6}{\x}{0.6}{\c}
  }
\end{tikzpicture}\\[4pt]
{\bfseries\color{orange!90!black} Nam có 9 que tính}
\end{center}
Xét tính đúng sai của các câu sau:
\choiceTF
{\True Nam có thể xếp được 3 hình tam giác riêng biệt ($3 \times 3 = 9$)}
{\True Nếu xếp 2 hình vuông riêng biệt, Nam còn thừa 1 que tính ($9 - 8 = 1$)}
{Nam có thể xếp được 3 hình vuông riêng biệt}
{\True Xếp 3 hình vuông cần 12 que tính (Nam chỉ có 9 que nên không đủ)}
\loigiai{
\begin{itemize}
    \item 3 hình tam giác cần $3 \times 3 = 9$ que tính: \textbf{Đúng}.
    \item 2 hình vuông cần $4 \times 2 = 8$ que tính, thừa $9 - 8 = 1$ que: \textbf{Đúng}.
    \item 3 hình vuông cần 12 que tính > 9 que, không đủ: \textbf{Sai}.
    \item Nam không đủ que để xếp 3 hình vuông: \textbf{Đúng}.
\end{itemize}
}
\end{ex}

% =========================================================================
% PHẦN 3: TRẢ LỜI NGẮN (ĐIỀN SỐ THÍCH HỢP)
% =========================================================================
\textbf{Phần 3. Trả lời ngắn (Quan sát hình vẽ và điền số thích hợp)}
\setcounterpageref{ex}{0}

% --- CÂU 15 ---
\begin{ex} %[1H2H08]
Đếm xem hình tam giác dưới đây được xếp từ bao nhiêu que tính?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeQue{-1.4}{-0.7}{1.4}{-0.7}{orange!85!black}
  \VeQue{1.4}{-0.7}{0}{1.2}{blue!80!black}
  \VeQue{0}{1.2}{-1.4}{-0.7}{green!70!black}
  \node[font=\bfseries\color{orange!90!black}] at (0, -1.05) {Que 1};
  \node[font=\bfseries\color{blue!90!black}, rotate=53] at (0.95, 0.45) {Que 2};
  \node[font=\bfseries\color{green!70!black}, rotate=-53] at (-0.95, 0.45) {Que 3};
\end{tikzpicture}
\end{center}
\shortans{3}
\loigiai{
\textbf{Đáp số:} $3$\\
Hình tam giác được xếp từ $3$ que tính.
}
\end{ex}

% --- CÂU 16 ---
\begin{ex} %[1H2H08]
Đếm xem hình vuông dưới đây được xếp từ bao nhiêu que tính bằng nhau?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  \VeQue{-1.0}{-1.0}{1.0}{-1.0}{orange!85!black}
  \VeQue{1.0}{-1.0}{1.0}{1.0}{blue!80!black}
  \VeQue{1.0}{1.0}{-1.0}{1.0}{green!70!black}
  \VeQue{-1.0}{1.0}{-1.0}{-1.0}{purple!80!black}
  \node[font=\bfseries\color{orange!90!black}] at (0, -1.35) {Que 1};
  \node[font=\bfseries\color{blue!80!black}] at (1.45, 0) {Que 2};
  \node[font=\bfseries\color{green!70!black}] at (0, 1.35) {Que 3};
  \node[font=\bfseries\color{purple!80!black}] at (-1.45, 0) {Que 4};
\end{tikzpicture}
\end{center}
\shortans{4}
\loigiai{
\textbf{Đáp số:} $4$\\
Hình vuông được xếp từ $4$ que tính bằng nhau.
}
\end{ex}

\newpage
% --- CÂU 17 ---
\begin{ex} %[1H2V08]
Quan sát 9 que tính dưới đây. Xếp được bao nhiêu hình tam giác riêng biệt?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \foreach \i in {0, 1, 2} {
    \begin{scope}[shift={(\i*2.6-2.6, 0)}]
      \VeQue{-1.0}{-0.6}{1.0}{-0.6}{orange!85!black}
      \VeQue{1.0}{-0.6}{0}{0.9}{blue!80!black}
      \VeQue{0}{0.9}{-1.0}{-0.6}{green!70!black}
    \end{scope}
  }
\end{tikzpicture}
\end{center}
\shortans{3}
\loigiai{
\textbf{Đáp số:} $3$\\
$9 : 3 = 3$ hình tam giác.
}
\end{ex}

% --- CÂU 18 ---
\begin{ex} %[1H2V08]
Quan sát 8 que tính dưới đây. Xếp được bao nhiêu hình vuông riêng biệt?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  \foreach \i in {0, 1} {
    \begin{scope}[shift={(\i*2.8-1.4, 0)}]
      \VeQue{-0.8}{-0.8}{0.8}{-0.8}{orange!85!black}
      \VeQue{0.8}{-0.8}{0.8}{0.8}{blue!80!black}
      \VeQue{0.8}{0.8}{-0.8}{0.8}{green!70!black}
      \VeQue{-0.8}{0.8}{-0.8}{-0.8}{purple!80!black}
    \end{scope}
  }
\end{tikzpicture}
\end{center}
\shortans{2}
\loigiai{
\textbf{Đáp số:} $2$\\
$8 : 4 = 2$ hình vuông.
}
\end{ex}

% --- CÂU 19 ---
\begin{ex} %[1H2V08]
Có 10 que tính, Nam xếp 1 hình vuông và 1 hình tam giác như hình dưới. Nam còn thừa mấy que tính?
\begin{center}
\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]
  % Hình vuông 4 que
  \VeQue{-2.8}{-0.7}{-1.4}{-0.7}{blue!80!black}
  \VeQue{-1.4}{-0.7}{-1.4}{0.7}{blue!80!black}
  \VeQue{-1.4}{0.7}{-2.8}{0.7}{blue!80!black}
  \VeQue{-2.8}{0.7}{-2.8}{-0.7}{blue!80!black}
  % Tam giác 3 que
  \VeQue{-0.6}{-0.7}{1.2}{-0.7}{green!70!black}
  \VeQue{1.2}{-0.7}{0.3}{0.8}{green!70!black}
  \VeQue{0.3}{0.8}{-0.6}{-0.7}{green!70!black}
  % 3 que thừa
  \VeQue{2.0}{-0.6}{2.0}{0.6}{orange!85!black}
  \VeQue{2.6}{-0.6}{2.6}{0.6}{orange!85!black}
  \VeQue{3.2}{-0.6}{3.2}{0.6}{orange!85!black}
  \node[font=\footnotesize\bfseries\color{orange!90!black}] at (2.6,-1.05) {Thừa: ? que};
\end{tikzpicture}
\end{center}
\shortans{3}
\loigiai{
\textbf{Đáp số:} $3$\\
Đã dùng: $4 + 3 = 7$ que tính. Còn thừa: $10 - 7 = 3$ que tính.
}
\end{ex}

% --- CÂU 20 ---
\begin{ex} %[1H2C08]
Xếp 2 hình vuông dính liền chung nhau 1 cạnh như hình vẽ dưới đây. Cần tất cả bao nhiêu que tính?
\begin{center}
\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]
  % Đáy 2 hình vuông
  \VeQue{-1.6}{-0.8}{0}{-0.8}{orange!85!black}
  \VeQue{0}{-0.8}{1.6}{-0.8}{orange!85!black}
  % Cạnh trên 2 hình vuông
  \VeQue{-1.6}{0.8}{0}{0.8}{green!70!black}
  \VeQue{0}{0.8}{1.6}{0.8}{green!70!black}
  % Cạnh trái & phải
  \VeQue{-1.6}{-0.8}{-1.6}{0.8}{purple!80!black}
  \VeQue{1.6}{-0.8}{1.6}{0.8}{purple!80!black}
  % Cạnh chung ở giữa
  \VeQue{0}{-0.8}{0}{0.8}{red!85!black}
  \node[font=\tiny\bfseries\color{red!85!black}] at (0, -1.15) {Cạnh chung};
\end{tikzpicture}
\end{center}
\shortans{7}
\loigiai{
\textbf{Đáp số:} $7$\\
Gồm 6 cạnh ngoài và 1 cạnh chung ở giữa: $6 + 1 = 7$ que tính.
}
\end{ex}
'''

# Write to lesson file
file_path = 'CHỦ ĐỀ 2 - LÀM QUEN VỚI MỘT SỐ HÌNH PHẲNG/Chuong2_Bai08_ThucHanhLapGhepXepHinh.tex'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Wrote Bai 08 successfully')

# Assemble test_bai08.tex
with open('Bai_01_preview.tex', 'r', encoding='utf-8') as f:
    t1 = f.read()

# Replace header box title
t1 = t1.replace('BÀI 01: CÁC SỐ 0, 1, 2, 3, 4, 5', 'BÀI 08: THỰC HÀNH LẮP GHÉP, XẾP HÌNH')
t1 = t1.replace('CHỦ ĐỀ 1 -- CÁC SỐ TỪ 0 ĐẾN 10', 'CHỦ ĐỀ 2 -- LÀM QUEN VỚI MỘT SỐ HÌNH PHẲNG')
t1 = t1.replace('bai-01', 'bai-08')

preamble = t1.split(r'\begin{document}')[0] + "\\begin{document}\n"
postamble = "\n\\end{document}\n"

with open('test_bai08.tex', 'w', encoding='utf-8') as f:
    f.write(preamble + content + postamble)
print('Assembled test_bai08.tex')
