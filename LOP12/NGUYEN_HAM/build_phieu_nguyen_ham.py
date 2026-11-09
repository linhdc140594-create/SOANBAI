import subprocess
import os
import pypdf

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def create_tex():
    tex = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{array}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage[top=0.6cm, bottom=0.6cm, left=0.75cm, right=0.75cm]{geometry}

\setlength{\parskip}{0pt}
\setlength{\parindent}{0pt}
\setlength{\fboxsep}{3pt}
\setlength{\fboxrule}{0.5pt}

% Dòng kẻ chấm mờ cự ly chuẩn viết tay học sinh THPT (18.5pt)
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18.5pt%
  \vspace{0.8mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!55}\dotfill}\par%
  }%
  \vspace{0.3mm}%
  \endgroup%
}

% Ô bài tập có dòng kẻ
\newcommand{\oBaiTap}[3][5]{%
  \vspace{0.6mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

% Khung ghi nhớ / khẩu quyết nổi bật đầu trang
\newcommand{\khungGhiNho}[2]{%
  \noindent\fbox{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \textbf{\color{blue!80!black}#1: }#2%
    }%
  }%
  \vspace{1.0mm}%
}

\begin{document}
\pagestyle{empty}

% =============================================================================
% TRANG 1: DẠNG 1 -- NGUYÊN HÀM ĐƠN THỨC VÀ ĐA THỨC CƠ BẢN
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- CHUYÊN ĐỀ: NGUYÊN HÀM CƠ BẢN} & \textbf{Trang 1/8} \\
\textit{Trung tâm Toán Thầy Lĩnh -- Chuyên đề Lớp 12} & \textit{Tập 1: Từ cơ bản đến thành thạo} \\
\hline
\end{tabularx}

\vspace{1mm}

\noindent
\begin{tabularx}{\linewidth}{|X|p{3.5cm}|p{3.5cm}|}
\hline
\rule[-1.5mm]{0pt}{6.5mm}\textbf{Họ và tên:} \dotfill & \textbf{Lớp:} \makebox[2cm]{\dotfill} & \textbf{Điểm số:} \makebox[2cm]{\dotfill} \\
\hline
\end{tabularx}

\vspace{1mm}

\khungGhiNho{CÔNG THỨC GHI NHỚ DẠNG 1}{%
$\displaystyle\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \; (n \ne -1)$. \textit{Khẩu quyết: "Mũ cộng 1, chia mũ mới!"}\\
Quy tắc tuyến tính: $\displaystyle\int [f(x) \pm g(x)] \, dx = \int f(x) \, dx \pm \int g(x) \, dx$ \quad và \quad $\displaystyle\int k \cdot f(x) \, dx = k \int f(x) \, dx$.
}

\noindent\textbf{Bài 1 (3,0 điểm). Tính nguyên hàm của các đơn thức cơ bản sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[3]{a)}{$\displaystyle\int 4x \, dx$} & 
\oBaiTap[3]{b)}{$\displaystyle\int 6x^2 \, dx$} \\
\hline
\oBaiTap[3]{c)}{$\displaystyle\int 8x^3 \, dx$} & 
\oBaiTap[3]{d)}{$\displaystyle\int 5x^4 \, dx$} \\
\hline
\oBaiTap[3]{e)}{$\displaystyle\int 9x^8 \, dx$} & 
\oBaiTap[3]{f)}{$\displaystyle\int 7 \, dx$} \\
\hline
\end{tabularx}

\vspace{1.2mm}

\noindent\textbf{Bài 2 (4,0 điểm). Tính nguyên hàm của các đa thức sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int (4x - 3) \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int (3x^2 - 6x + 2) \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int (6x^2 + 8x - 5) \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int (4x^3 - 9x^2 + 2x - 1) \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 2: DẠNG 2 -- BIẾN ĐỔI KHAI TRIỂN ĐA THỨC
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{CHUYÊN ĐỀ NGUYÊN HÀM TOÁN 12 -- DẠNG 2: BIẾN ĐỔI KHAI TRIỂN ĐA THỨC} & \textbf{Trang 2/8} \\
\hline
\end{tabularx}

\vspace{1.2mm}

\khungGhiNho{CẢNH BÁO \& PHƯƠNG PHÁP}{%
Nguyên hàm \textbf{TUYỆT ĐỐI KHÔNG CÓ} công thức nhân: $\displaystyle\int f(x) \cdot g(x) \, dx \ne \int f(x) \, dx \cdot \int g(x) \, dx$.\\
\textit{Quy tắc vàng: Gặp phép nhân, bình phương, lập phương $\implies$ Bắt buộc nhân phá ngoặc, khai triển hằng đẳng thức về dạng tổng các đơn thức rồi mới lấy nguyên hàm từng đứa!}
}

\noindent\textbf{Bài 3 (4,0 điểm). Nhân phá ngoặc rồi tính các nguyên hàm sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int (x - 2)(x + 3) \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int (2x + 1)(x - 4) \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int (3x - 1)(2x + 5) \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int x(2x^2 - 5x + 3) \, dx$} \\
\hline
\end{tabularx}

\vspace{1.5mm}

\noindent\textbf{Bài 4 (4,0 điểm). Khai triển hằng đẳng thức rồi tính các nguyên hàm sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int (x + 4)^2 \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int (2x - 3)^2 \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int (3x + 1)^2 \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int (x - 2)^3 \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 3: DẠNG 3 -- NGUYÊN HÀM PHÂN THỨC: TÁCH PHÂN SỐ
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{CHUYÊN ĐỀ NGUYÊN HÀM TOÁN 12 -- DẠNG 3: TÁCH PHÂN THỨC ĐA THỨC} & \textbf{Trang 3/8} \\
\hline
\end{tabularx}

\vspace{1.2mm}

\khungGhiNho{CẢNH BÁO \& PHƯƠNG PHÁP}{%
Nguyên hàm \textbf{TUYỆT ĐỐI KHÔNG CÓ} công thức chia: $\displaystyle\int \frac{f(x)}{g(x)} \, dx \ne \frac{\int f(x) \, dx}{\int g(x) \, dx}$.\\
\textit{Quy tắc vàng: Khi mẫu số là đơn thức ($x$ hoặc $x^2$), lấy từng hạng tử ở tử số chia cho mẫu số:\\
$\displaystyle\frac{A + B + C}{M} = \frac{A}{M} + \frac{B}{M} + \frac{C}{M}$ rồi mới lấy nguyên hàm!}
}

\noindent\textbf{Bài 5 (4,0 điểm). Chia đa thức cho $x$ rồi tính các nguyên hàm sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \frac{3x^2 + 4x}{x} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \frac{6x^3 - 8x^2 + 5x}{x} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{x^4 - 6x^3 + 2x^2}{2x} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{(x + 2)^2}{x} \, dx$} \\
\hline
\end{tabularx}

\vspace{1.5mm}

\noindent\textbf{Bài 6 (4,0 điểm). Chia đa thức cho $x^2$ rồi tính các nguyên hàm sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \frac{4x^3 - 5x^2 + 6x}{x^2} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \frac{2x^4 - 3x^3 + 7x^2}{x^2} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{3x^3 - 2x^2 + 4}{x^2} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{(2x - 1)^2}{x^2} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 4: DẠNG 4 -- SỐ MŨ ÂM VÀ PHÂN THỨC BẬC NHẤT 1/x
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{CHUYÊN ĐỀ NGUYÊN HÀM TOÁN 12 -- DẠNG 4: SỐ MŨ ÂM VÀ PHÂN THỨC 1/x} & \textbf{Trang 4/8} \\
\hline
\end{tabularx}

\vspace{1.2mm}

\khungGhiNho{CÔNG THỨC GHI NHỚ DẠNG 4}{%
$\bullet$ Đổi mẫu sang mũ âm: $\displaystyle\frac{1}{x^k} = x^{-k} \implies \int x^{-k} \, dx = \frac{x^{-k+1}}{-k+1} + C$. Thuộc lòng: $\displaystyle\int \frac{1}{x^2} \, dx = -\frac{1}{x} + C$.\\
$\bullet$ Phân thức bậc 1: $\displaystyle\int \frac{1}{x} \, dx = \ln|x| + C$ \textit{(Bắt buộc có dấu giá trị tuyệt đối $|x|$!)}
}

\noindent\textbf{Bài 7 (4,0 điểm). Tính các nguyên hàm chứa số mũ âm sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \left(4x^3 - \frac{3}{x^2}\right) dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \left(2x + 1 + \frac{5}{x^2}\right) dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \frac{6}{x^3} \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \left(\frac{2}{x^2} - \frac{4}{x^3}\right) dx$} \\
\hline
\end{tabularx}

\vspace{1.5mm}

\noindent\textbf{Bài 8 (4,0 điểm). Tính các nguyên hàm chứa $\dfrac{1}{x}$ sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \left(6x^2 + \frac{1}{x}\right) dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \left(3x - 5 + \frac{4}{x}\right) dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \frac{2x^2 - 3x + 5}{x} \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \frac{(x - 3)^2}{x} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 5: DẠNG 5 -- NGUYÊN HÀM CĂN THỨC
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{CHUYÊN ĐỀ NGUYÊN HÀM TOÁN 12 -- DẠNG 5: CĂN THỨC VỀ LŨY THỪA} & \textbf{Trang 5/8} \\
\hline
\end{tabularx}

\vspace{1.2mm}

\khungGhiNho{CÔNG THỨC GHI NHỚ DẠNG 5}{%
$\bullet$ Đổi căn về mũ phân số: $\sqrt[n]{x^m} = x^{\frac{m}{n}}$. Áp dụng khẩu quyết: \textit{"Mũ cộng 1, chia mũ mới!"}\\
$\bullet$ Thuộc lòng 2 công thức hay gặp: $\displaystyle\int \sqrt{x} \, dx = \int x^{1/2} \, dx = \frac{2}{3}x\sqrt{x} + C$ \quad và \quad $\displaystyle\int \frac{1}{\sqrt{x}} \, dx = 2\sqrt{x} + C$.
}

\noindent\textbf{Bài 9 (4,0 điểm). Tính các nguyên hàm chứa căn thức cơ bản sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int 6\sqrt{x} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \left(3x^2 + 4\sqrt{x}\right) dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{6}{\sqrt{x}} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \left(\sqrt{x} + \frac{2}{\sqrt{x}}\right) dx$} \\
\hline
\end{tabularx}

\vspace{1.5mm}

\noindent\textbf{Bài 10 (4,0 điểm). Biến đổi căn thức rồi tính các nguyên hàm sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int x\sqrt{x} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \sqrt{x}(2x - 3) \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{x^2 - 4x + \sqrt{x}}{\sqrt{x}} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \sqrt[3]{x} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 6: DẠNG 6 -- MỞ RỘNG BẬC NHẤT ax + b
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{CHUYÊN ĐỀ NGUYÊN HÀM TOÁN 12 -- DẠNG 6: BIỂU THỨC BẬC NHẤT ax + b} & \textbf{Trang 6/8} \\
\hline
\end{tabularx}

\vspace{1.2mm}

\khungGhiNho{CÔNG THỨC GHI NHỚ DẠNG 6}{%
$\displaystyle\int f(ax + b) \, dx = \frac{1}{a} F(ax + b) + C$. \textit{Khẩu quyết: "Ruột bậc nhất $ax+b$ thì BẮT BUỘC NHÂN THÊM $\dfrac{1}{a}$ ở đầu!"}\\
$\bullet$ $\displaystyle\int (ax + b)^n \, dx = \frac{1}{a} \cdot \frac{(ax+b)^{n+1}}{n+1} + C$ \qquad $\bullet$ $\displaystyle\int \frac{1}{ax + b} \, dx = \frac{1}{a} \ln|ax+b| + C$
}

\noindent\textbf{Bài 11 (4,0 điểm). Tính nguyên hàm của các lũy thừa bậc nhất sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int (2x + 1)^3 \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int (3x - 2)^4 \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int (1 - 4x)^5 \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \sqrt{2x + 5} \, dx$} \\
\hline
\end{tabularx}

\vspace{1.5mm}

\noindent\textbf{Bài 12 (4,0 điểm). Tính nguyên hàm có mẫu số bậc nhất sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \frac{1}{2x + 3} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \frac{1}{3x - 4} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{1}{5 - 2x} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{1}{(3x + 1)^2} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 7: DẠNG 7 -- NGUYÊN HÀM LƯỢNG GIÁC VÀ HÀM SỐ MŨ
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{CHUYÊN ĐỀ NGUYÊN HÀM TOÁN 12 -- DẠNG 7: LƯỢNG GIÁC VÀ HÀM MŨ} & \textbf{Trang 7/8} \\
\hline
\end{tabularx}

\vspace{1.2mm}

\khungGhiNho{CÔNG THỨC GHI NHỚ DẠNG 7}{%
$\bullet$ Lượng giác (ngược đạo hàm): $\displaystyle\int \cos(ax+b) \, dx = \frac{1}{a}\sin(ax+b) + C$; $\displaystyle\int \sin(ax+b) \, dx = -\frac{1}{a}\cos(ax+b) + C$; $\displaystyle\int \frac{1}{\cos^2 x} \, dx = \tan x + C$.\\
$\bullet$ Hàm mũ: $\displaystyle\int e^{ax+b} \, dx = \frac{1}{a} e^{ax+b} + C$; $\displaystyle\int a^x \, dx = \frac{a^x}{\ln a} + C$.
}

\noindent\textbf{Bài 13 (4,0 điểm). Tính các nguyên hàm lượng giác sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int (3\cos x - 2\sin x) \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \cos(3x) \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \sin\left(2x - \frac{\pi}{3}\right) dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{1}{\cos^2(4x)} \, dx$} \\
\hline
\end{tabularx}

\vspace{1.5mm}

\noindent\textbf{Bài 14 (4,0 điểm). Tính các nguyên hàm hàm số mũ sau:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int (3e^x - 4x) \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int e^{4x} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int e^{3x - 2} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int (2^x + 5^x) \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 8: DẠNG 8 -- TÌM NGUYÊN HÀM F(x) VÀ TOÁN THỰC TẾ
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{CHUYÊN ĐỀ NGUYÊN HÀM TOÁN 12 -- DẠNG 8: TÌM HẰNG SỐ C \& BÀI TOÁN THỰC TẾ} & \textbf{Trang 8/8} \\
\hline
\end{tabularx}

\vspace{1.2mm}

\khungGhiNho{PHƯƠNG PHÁP GIẢI DẠNG 8}{%
$\bullet$ Tìm $C$: Tính $F(x) = \int f(x) \, dx + C$, thay điểm $(x_0, y_0)$ vào điều kiện $F(x_0) = y_0 \implies$ tìm ra $C$.\\
$\bullet$ Bài toán chuyển động (Vật lý 12): Vận tốc $v(t) = \int a(t) \, dt$; Quãng đường $s(t) = \int v(t) \, dt$.
}

\noindent\textbf{Bài 15 (4,0 điểm). Tìm nguyên hàm $F(x)$ thỏa mãn điều kiện cho trước:}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{Tìm $F(x)$ của $f(x) = 2x - 5$, biết $F(1) = 3$.} & 
\oBaiTap[6]{b)}{Tìm $F(x)$ của $f(x) = 3x^2 - 4x + 2$, biết $F(2) = 7$.} \\
\hline
\oBaiTap[6]{c)}{Tìm $F(x)$ của $f(x) = \dfrac{1}{2x - 1}$, biết $F(1) = 4$.} & 
\oBaiTap[6]{d)}{Tìm $F(x)$ của $f(x) = 2\cos x + 3e^x$, biết $F(0) = 5$.} \\
\hline
\end{tabularx}

\vspace{1.5mm}

\noindent\textbf{Bài 16 (4,0 điểm). Bài toán thực tế chuyển động (Toán ứng dụng):}
\vspace{0.4mm}

\noindent
\begin{tabularx}{\linewidth}{|X|}
\hline
\vspace{0.5mm}
\textbf{a) (2,0 điểm)} Một chất điểm chuyển động với vận tốc $v(t) = 3t^2 - 4t + 1\text{ (m/s)}$. Biết tại thời điểm ban đầu $t = 0$, chất điểm ở vị trí $s(0) = 5\text{ m}$. Hãy xác định phương trình vị trí $s(t)$ và tính quãng đường vật đi được sau $3$ giây.
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{5}
\\ \hline
\vspace{0.5mm}
\textbf{b) (2,0 điểm)} Một đoàn tàu đang chạy với vận tốc $v_0 = 20\text{ m/s}$ thì người lái tàu hãm phanh với gia tốc $a(t) = -2\text{ m/s}^2$. Tính thời gian từ lúc hãm phanh đến khi tàu dừng hẳn và quãng đường đoàn tàu đi được trong khoảng thời gian đó.
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{5}
\\ \hline
\end{tabularx}

\end{document}
'''
    return tex

def main():
    tex_content = create_tex()
    tex_path = os.path.join(CUR_DIR, "Phieu_Bai_Tap_Nguyen_Ham_Co_Ban.tex")
    pdf_path = os.path.join(CUR_DIR, "Phieu_Bai_Tap_Nguyen_Ham_Co_Ban.pdf")
    
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
    print("Wrote Phieu_Bai_Tap_Nguyen_Ham_Co_Ban.tex")
    
    cmd = ["pdflatex", "-interaction=nonstopmode", "Phieu_Bai_Tap_Nguyen_Ham_Co_Ban.tex"]
    res = subprocess.run(cmd, cwd=CUR_DIR, capture_output=True, text=True)
    
    if not os.path.exists(pdf_path):
        print("Compilation failed!")
        print(res.stdout[-2000:])
        return
        
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    print(f"Total pages: {num_pages}")
    
    if num_pages == 8:
        print("SUCCESS! Exactly 8 pages.")
    else:
        print(f"WARNING: Page count is {num_pages}, expected 8!")

if __name__ == "__main__":
    main()
