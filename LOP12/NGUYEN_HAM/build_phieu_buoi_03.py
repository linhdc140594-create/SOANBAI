import os
import subprocess
import pymupdf
import numpy as np

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def create_tex():
    tex = r'''\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath,amssymb}
\usepackage{tabularx}
\usepackage{array}
\usepackage{xcolor}
\usepackage{tikz}
\usepackage[top=0.55cm, bottom=0.55cm, left=0.75cm, right=0.75cm]{geometry}

\setlength{\parskip}{0pt}
\setlength{\parindent}{0pt}
\setlength{\fboxsep}{3pt}
\setlength{\fboxrule}{0.5pt}

% Dòng kẻ chấm mờ cự ly chuẩn viết tay học sinh THPT (18.5pt)
\newcommand{\dongke}[1]{%
  \begingroup%
  \setlength{\parskip}{0pt}%
  \baselineskip=18.5pt%
  \vspace{0.7mm}%
  \foreach \i in {1,...,#1}{%
    \noindent{\color{gray!55}\dotfill}\par%
  }%
  \vspace{0.2mm}%
  \endgroup%
}

% Ô bài tập có dòng kẻ
\newcommand{\oBaiTap}[3][5]{%
  \vspace{0.5mm}%
  \noindent\textbf{#2} #3\par%
  \dongke{#1}%
}

% Khung ghi nhớ / phương pháp nổi bật đầu trang
\newcommand{\khungGhiNho}[2]{%
  \noindent\fbox{%
    \parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}{%
      \textbf{\color{blue!80!black}#1: }#2%
    }%
  }%
  \vspace{0.8mm}%
}

\begin{document}
\pagestyle{empty}

% =============================================================================
% TRANG 1: PHƯƠNG PHÁP ĐỔI BIẾN SỐ -- ĐA THỨC VÀ PHÂN THỨC HỮU TỈ
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ} & \textbf{Trang 1/8} \\
\textit{Trung tâm Toán Thầy Lĩnh -- Chuyên đề Lớp 12 GDPT 2018} & \textit{Tập 3: Đổi biến loại 1 \& Vi phân} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\noindent
\begin{tabularx}{\linewidth}{|X|p{3.2cm}|p{3.2cm}|}
\hline
\rule[-1.2mm]{0pt}{6.0mm}\textbf{Họ và tên:} \dotfill & \textbf{Lớp:} \dotfill & \textbf{Điểm số:} \dotfill \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{CÔNG THỨC ĐỔI BIẾN SỐ LOẠI 1 \& 4 BƯỚC THỰC HIỆN}{%
$\displaystyle\int f(u(x)) \cdot u'(x) \, dx = \int f(u) \, du = F(u) + C = F(u(x)) + C$.\\
\textit{Quy trình 4 bước:} \textbf{B1.} Đặt ẩn phụ $t = u(x)$ $\implies$ \textbf{B2.} Vi phân $dt = u'(x)dx$ $\implies$ \textbf{B3.} Đổi toàn bộ tích phân sang biến $t$ $\implies$ \textbf{B4.} Lấy nguyên hàm theo $t$ và trả về biến $x$.
}

\noindent\textbf{Bài 1 (4,0 điểm). Tính các nguyên hàm đa thức lũy thừa bậc cao sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int 2x(x^2 + 1)^4 \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int 3x^2(x^3 - 2)^5 \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int x(2x^2 + 3)^6 \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int x^2(1 - 2x^3)^4 \, dx$} \\
\hline
\end{tabularx}

\vspace{13.5mm}

\noindent\textbf{Bài 2 (4,0 điểm). Tính các nguyên hàm phân thức hữu tỉ có mẫu lũy thừa sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \frac{2x}{(x^2 + 1)^2} \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \frac{x}{(2x^2 + 3)^3} \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \frac{3x^2}{(x^3 - 1)^4} \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \frac{x - 1}{(x^2 - 2x + 5)^3} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 2: ĐỔI BIẾN CĂN THỨC & RÚT THỪA SỐ LŨY THỪA
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ} & \textbf{Trang 2/8} \\
\textit{Chuyên đề: Kỹ thuật đổi biến căn thức \& rút thừa số bậc cao} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{KỸ THUẬT ĐẶT ẨN PHỤ CĂN THỨC}{%
$\bullet$ \textit{Khẩu quyết:} Gặp căn thức $\sqrt{u(x)}$, thường đặt $t = \text{căn}$. Sau đó \textbf{bình phương 2 vế} rồi mới lấy vi phân:\\
\phantom{$\bullet$} $t = \sqrt{u(x)} \implies t^2 = u(x) \implies 2t\,dt = u'(x)dx \implies t\,dt = \frac{1}{2}u'(x)dx$ (tránh phân số vi phân).\\
$\bullet$ Khi biểu thức thừa $x^3, x^5$: Tách $x^3 = x^2 \cdot x$ hoặc $x^5 = x^4 \cdot x$, rút $x^2 = t^2 - c$ thế vào.
}

\noindent\textbf{Bài 3 (4,0 điểm). Tính các nguyên hàm chứa căn thức bậc hai cơ bản sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int 2x\sqrt{x^2 + 1} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int x\sqrt{3 - x^2} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{x}{\sqrt{x^2 + 4}} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{x}{\sqrt{1 - 2x^2}} \, dx$} \\
\hline
\end{tabularx}

\vspace{3.0mm}

\noindent\textbf{Bài 4 (4,0 điểm). Tính các nguyên hàm căn thức bậc cao \& rút thừa số sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int x^3\sqrt{x^2 + 1} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int x^3(x^2 - 2)^5 \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int x^2\sqrt[3]{x^3 + 1} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{x^3}{\sqrt{x^2 + 2}} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 3: ĐỔI BIẾN HÀM SỐ MŨ (e^x VÀ a^x)
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ} & \textbf{Trang 3/8} \\
\textit{Chuyên đề: Đổi biến số hàm số mũ $e^x$ và $a^x$} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{DẤU HIỆU ĐỔI BIẾN HÀM MŨ}{%
$\bullet$ Bản chất: $(e^x)' = e^x$. Do đó khi thấy $e^x$ đi kèm với cụm $e^x dx \implies$ Đặt $t = e^x$ hoặc $t = \sqrt{e^x + c}$.\\
$\bullet$ Mũ biến đổi lũy thừa: $\displaystyle\int \frac{e^{2x}}{e^x + 1}dx = \int \frac{e^x \cdot e^x dx}{e^x + 1}$; \quad Mũ phức tạp $\displaystyle\int x e^{x^2} dx \implies t = x^2$.
}

\noindent\textbf{Bài 5 (4,0 điểm). Tính các nguyên hàm hàm số mũ trực diện \& phân thức sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int e^x (e^x + 2)^3 \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \frac{e^x}{e^x + 3} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{e^x}{(e^x + 1)^2} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{e^x}{2e^x - 1} \, dx$} \\
\hline
\end{tabularx}

\vspace{3.0mm}

\noindent\textbf{Bài 6 (4,0 điểm). Tính các nguyên hàm hàm mũ chứa căn \& mũ nâng cao sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int e^x \sqrt{e^x + 1} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \frac{e^x}{\sqrt{2e^x + 3}} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int x e^{x^2 + 1} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{e^{2x}}{e^x + 1} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 4: ĐỔI BIẾN HÀM SỐ LOGARIT (ln x)
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ} & \textbf{Trang 4/8} \\
\textit{Chuyên đề: Đổi biến số hàm số logarit tự nhiên $\ln x$} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{DẤU HIỆU ĐỔI BIẾN LOGARIT $\ln x$}{%
$\bullet$ Bản chất: $(\ln x)' = \dfrac{1}{x}$.\\
$\bullet$ \textit{Khẩu quyết:} Cứ thấy $\ln x$ xuất hiện đồng thời với mẫu số có $x$ (tức cụm $\dfrac{dx}{x}$) $\implies$ Đặt $t = \ln x$ (hoặc $t = a\ln x + b$, hoặc $t = \sqrt{a\ln x + b}$). Khi đó vi phân xuất hiện ngay: $dt = \dfrac{dx}{x}$.
}

\noindent\textbf{Bài 7 (4,0 điểm). Tính các nguyên hàm chứa $\ln x$ và $\dfrac{1}{x}$ cơ bản sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \frac{\ln x}{x} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \frac{(\ln x)^3 + 1}{x} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{1}{x \ln x} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{2\ln x + 3}{x} \, dx$} \\
\hline
\end{tabularx}

\vspace{6.5mm}

\noindent\textbf{Bài 8 (4,0 điểm). Tính các nguyên hàm logarit chứa mẫu lũy thừa và căn thức sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \frac{1}{x(\ln x + 1)^2} \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \frac{\sqrt{\ln x + 2}}{x} \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \frac{1}{x\sqrt{2\ln x + 1}} \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \frac{\ln x}{x(\ln^2 x + 1)} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 5: ĐỔI BIẾN HÀM LƯỢNG GIÁC (sin x VÀ cos x BẬC LẺ)
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ} & \textbf{Trang 5/8} \\
\textit{Chuyên đề: Đổi biến lượng giác bậc lẻ \& phân thức lượng giác} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{KỸ THUẬT LƯỢNG GIÁC BẬC LẺ}{%
$\bullet$ Biểu thức chứa $\sin x$ bậc lẻ $\longrightarrow$ tách $1$ lượng $\sin x\,dx = -d(\cos x)$, đưa lượng còn lại về $\cos x$ bằng $\sin^2 x = 1 - \cos^2 x$, đặt $t = \cos x$.\\
$\bullet$ Biểu thức chứa $\cos x$ bậc lẻ $\longrightarrow$ tách $1$ lượng $\cos x\,dx = d(\sin x)$, đưa lượng còn lại về $\sin x$ bằng $\cos^2 x = 1 - \sin^2 x$, đặt $t = \sin x$.
}

\noindent\textbf{Bài 9 (4,0 điểm). Tính các nguyên hàm lượng giác tích lũy thừa bậc lẻ sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \sin x \cos^4 x \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \cos x \sin^5 x \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \sin^3 x \cos^2 x \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \cos^3 x \, dx$} \\
\hline
\end{tabularx}

\vspace{3.5mm}

\noindent\textbf{Bài 10 (4,0 điểm). Tính các nguyên hàm phân thức lượng giác và căn thức sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \frac{\cos x}{\sin x + 2} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \frac{\sin x}{(2\cos x + 1)^2} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \sin x \sqrt{\cos x + 1} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{\cos x}{\sqrt{3\sin x + 1}} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 6: ĐỔI BIẾN LƯỢNG GIÁC tan x, cot x & KỸ THUẬT PHỤ
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ} & \textbf{Trang 6/8} \\
\textit{Chuyên đề: Đổi biến chứa $\tan x, \cot x$ \& Lượng giác nhân tử} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{DẤU HIỆU ĐỔI BIẾN $\tan x$ VÀ $\cot x$}{%
$\bullet$ $(\tan x)' = \dfrac{1}{\cos^2 x} = 1 + \tan^2 x \implies$ Thấy $\dfrac{dx}{\cos^2 x}$ đặt $t = \tan x$.\\
$\bullet$ $(\cot x)' = -\dfrac{1}{\sin^2 x} = -(1 + \cot^2 x) \implies$ Thấy $\dfrac{dx}{\sin^2 x}$ đặt $t = \cot x$.\\
$\bullet$ Kỹ thuật nhân liên hợp lượng giác: $\displaystyle\int \frac{1}{\sin x}dx = \int \frac{\sin x \, dx}{\sin^2 x} = \int \frac{\sin x \, dx}{1 - \cos^2 x}$ (đặt $t = \cos x$).
}

\noindent\textbf{Bài 11 (4,0 điểm). Tính các nguyên hàm chứa $\tan x, \cot x$ sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[7]{a)}{$\displaystyle\int \tan x \, dx = \int \frac{\sin x}{\cos x} \, dx$} & 
\oBaiTap[7]{b)}{$\displaystyle\int \cot x \, dx = \int \frac{\cos x}{\sin x} \, dx$} \\
\hline
\oBaiTap[7]{c)}{$\displaystyle\int \frac{\tan x + 1}{\cos^2 x} \, dx$} & 
\oBaiTap[7]{d)}{$\displaystyle\int \frac{\sqrt{\tan x}}{\cos^2 x} \, dx$} \\
\hline
\end{tabularx}

\vspace{8.5mm}

\noindent\textbf{Bài 12 (4,0 điểm). Tính các nguyên hàm lượng giác nhân tử và nâng cao sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[6]{a)}{$\displaystyle\int \frac{e^{\tan x}}{\cos^2 x} \, dx$} & 
\oBaiTap[6]{b)}{$\displaystyle\int \frac{\sin 2x}{1 + \cos^2 x} \, dx$} \\
\hline
\oBaiTap[6]{c)}{$\displaystyle\int \frac{\sin 2x}{(2 + \sin^2 x)^2} \, dx$} & 
\oBaiTap[6]{d)}{$\displaystyle\int \frac{1}{\sin x} \, dx$} \\
\hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 7: KỸ THUẬT VI PHÂN SIÊU TỐC (du) & BÀI TOÁN HÀM ẨN
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ} & \textbf{Trang 7/8} \\
\textit{Chuyên đề: Kỹ thuật vi phân nhẩm nhanh \& Bài toán hàm ẩn 8+} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{BỘ 4 CÔNG THỨC VI PHÂN SIÊU TỐC TRẮC NGHIỆM}{%
1) $\displaystyle\int [u(x)]^n \cdot u'(x) \, dx = \frac{[u(x)]^{n+1}}{n+1} + C$; \qquad
2) $\displaystyle\int \frac{u'(x)}{u(x)} \, dx = \ln|u(x)| + C$;\\
3) $\displaystyle\int \frac{u'(x)}{\sqrt{u(x)}} \, dx = 2\sqrt{u(x)} + C$; \qquad\quad\;
4) $\displaystyle\int e^{u(x)} \cdot u'(x) \, dx = e^{u(x)} + C$.
}

\noindent\textbf{Bài 13 (4,0 điểm). Điền kết quả trực tiếp bằng kỹ thuật vi phân nhẩm (không đặt $t$):}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[4]{a)}{$\displaystyle\int 4x(2x^2 + 1)^5 \, dx =$} & 
\oBaiTap[4]{b)}{$\displaystyle\int \frac{2x + 1}{x^2 + x + 1} \, dx =$} \\
\hline
\oBaiTap[4]{c)}{$\displaystyle\int \frac{2x}{\sqrt{x^2 + 5}} \, dx =$} & 
\oBaiTap[4]{d)}{$\displaystyle\int 3x^2 e^{x^3} \, dx =$} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 14 (4,0 điểm). Giải các bài toán hàm ẩn mức vận dụng (8+) sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|}
\hline
\vspace{0.3mm}
\textbf{a) (2,0 điểm)} Cho hàm số $f(x)$ liên tục và nhận giá trị dương trên $\mathbb{R}$ thỏa mãn hệ thức:
\[ f'(x) \cdot \sqrt{f(x)} = 3x^2 \quad (\forall x \in \mathbb{R}) \quad \text{và} \quad f(0) = 4. \]
Hãy xác định công thức tường minh của hàm số $f(x)$.
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{7}
\\ \hline
\vspace{0.3mm}
\textbf{b) (2,0 điểm)} Cho hàm số $f(x)$ có đạo hàm liên tục và nhận giá trị dương trên $\mathbb{R}$ thỏa mãn:
\[ \frac{f'(x)}{f(x)} = 2x - 4 \quad (\forall x \in \mathbb{R}) \quad \text{và} \quad f(1) = e^{-3}. \]
Hãy xác định hàm số $f(x)$ và tìm giá trị nhỏ nhất của $f(x)$ trên $\mathbb{R}$.
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{7}
\\ \hline
\end{tabularx}

\newpage

% =============================================================================
% TRANG 8: TÌM HẰNG SỐ C & TOÁN THỰC TẾ LIÊN MÔN
% =============================================================================
\noindent
\begin{tabularx}{\linewidth}{|X|c|}
\hline
\textbf{PHIẾU HỌC TẬP TOÁN 12 -- BUỔI 3: PHƯƠNG PHÁP ĐỔI BIẾN SỐ} & \textbf{Trang 8/8} \\
\textit{Chuyên đề: Tìm nguyên hàm $F(x)$ thỏa mãn $F(x_0)=y_0$ \& Toán thực tế} & \textit{Lớp Toán Thầy Lĩnh} \\
\hline
\end{tabularx}

\vspace{0.8mm}

\khungGhiNho{MỐI LIÊN HỆ ĐẠO HÀM -- NGUYÊN HÀM TRONG THỰC TẾ}{%
$\bullet$ Vật lý phi tuyến: Quãng đường $s(t) = \displaystyle\int v(t) \, dt + C_1$; \quad Vận tốc $v(t) = \displaystyle\int a(t) \, dt + C_2$.\\
$\bullet$ Y sinh học: Nồng độ tích lũy thuốc $C(t) = \displaystyle\int C'(t) \, dt + C_0$; \quad Dân số $P(t) = \displaystyle\int P'(t) \, dt + P_0$.
}

\noindent\textbf{Bài 15 (4,0 điểm). Tìm nguyên hàm $F(x)$ thỏa mãn điều kiện điểm thuộc:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\oBaiTap[9]{a)}{Tìm $F(x)$ của $f(x) = \dfrac{2x + 1}{\sqrt{x^2 + x + 2}}$, biết rằng $F(1) = 6$.} & 
\oBaiTap[9]{b)}{Tìm $F(x)$ của $f(x) = \dfrac{e^x}{e^x + 1}$, biết rằng đồ thị đi qua $M(0; \ln 2 + 3)$.} \\
\hline
\end{tabularx}

\vspace{1.0mm}

\noindent\textbf{Bài 16 (4,0 điểm). Giải quyết các bài toán thực tế liên môn (Vật lý \& Y học) sau:}
\vspace{0.3mm}

\noindent
\begin{tabularx}{\linewidth}{|X|}
\hline
\vspace{0.4mm}
\textbf{a) (2,0 điểm) [Vật lý -- Chuyển động biến đổi phi tuyến]} Một vật chuyển động thẳng có vận tốc tức thời phụ thuộc thời gian $t$ (giây) theo công thức $v(t) = t\sqrt{t^2 + 9}\text{ (m/s)}$. Biết tại thời điểm ban đầu $t = 0$, vật ở gốc tọa độ $s(0) = 0\text{ m}$.\par
\textit{1)} Thiết lập phương trình quãng đường $s(t)$ của vật theo thời gian $t$.\par
\textit{2)} Tính quãng đường vật di chuyển được sau $4$ giây đầu tiên.
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{7}
\\ \hline
\vspace{0.4mm}
\textbf{b) (2,0 điểm) [Y học -- Dược động học nồng độ kháng sinh]} Sau khi tiêm kháng sinh, tốc độ thay đổi nồng độ thuốc trong máu sau $t$ giờ là $C'(t) = \dfrac{20t}{(t^2 + 1)^2}\text{ (mg/L/giờ)}$. Biết ban đầu tiêm ($t = 0$), nồng độ trong máu $C(0) = 0$.\par
\textit{1)} Xác định hàm nồng độ thuốc $C(t)$ theo thời gian $t$.\par
\textit{2)} Tính nồng độ thuốc trong máu sau $3$ giờ (làm tròn đến hàng phần trăm).
\par\vspace{0.2mm}
\noindent\textit{Bài giải:}\dongke{7}
\\ \hline
\end{tabularx}

\end{document}
'''
    tex_path = os.path.join(CUR_DIR, 'Phieu_Luyen_Tap_Nguyen_Ham_Buoi_03.tex')
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex)
    print("Wrote", tex_path)

def compile_and_check():
    tex_file = 'Phieu_Luyen_Tap_Nguyen_Ham_Buoi_03.tex'
    pdf_file = 'Phieu_Luyen_Tap_Nguyen_Ham_Buoi_03.pdf'
    
    cmd = ['pdflatex', '-interaction=nonstopmode', tex_file]
    p = subprocess.run(cmd, cwd=CUR_DIR, capture_output=True)
    if p.returncode != 0:
        print("Compilation FAILED!")
        return False
    
    pdf_path = os.path.join(CUR_DIR, pdf_file)
    if os.path.exists(pdf_path):
        doc = pymupdf.open(pdf_path)
        total_pages = len(doc)
        print(f"Total pages: {total_pages}")
        margins = []
        for i, page in enumerate(doc):
            pix = page.get_pixmap(dpi=150)
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
            gray = np.mean(img, axis=2) if pix.n >= 3 else img[:,:,0]
            non_white = np.where(gray < 250)
            if len(non_white[0]) > 0:
                last_y = np.max(non_white[0])
                m = ((pix.h - last_y) / 150.0) * 25.4
                margins.append(m)
                print(f"Page {i+1}: bottom margin = {m:.2f} mm")
            else:
                print(f"Page {i+1}: empty page!")

        # Render preview pngs for Pages 1 to 4
        for p_no in range(min(4, total_pages)):
            pix = doc[p_no].get_pixmap(dpi=150)
            out_img = os.path.join(CUR_DIR, f"page_buoi03_{p_no+1}.png")
            pix.save(out_img)
            print(f"Rendered {out_img}")

        doc.close()
        return total_pages == 8
    else:
        print("PDF not found!")
        return False

if __name__ == '__main__':
    create_tex()
    compile_and_check()
