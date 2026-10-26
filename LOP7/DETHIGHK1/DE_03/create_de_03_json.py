import json
import os

c2_tikz = r'''\begin{tikzpicture}[scale=0.9, line cap=round, line join=round]
  \coordinate (O) at (0,0);
  \draw[thick] (-2.6,0) node[above=2pt] {$x$} -- (2.6,0) node[below=2pt] {$x'$};
  \draw[thick] (-2.2,-1.54) node[above left=1pt] {$y$} -- (2.2,1.54) node[above right=1pt] {$y'$};
  \node[above=3pt] at (O) {$O$};
\end{tikzpicture}'''

c4_tikz = r'''\begin{tikzpicture}[scale=0.72, line cap=round, line join=round, thick]
  % Hình 1
  \begin{scope}[shift={(0,0)}]
    \coordinate (O) at (0,0);
    \draw (O) -- (1.8,0) node[below=2pt] {$t$};
    \draw (O) -- (60:1.8) node[above right=1pt] {$y$};
    \draw (O) -- (120:1.8) node[above left=1pt] {$x$};
    \node[font=\footnotesize] at (30:0.8) {$60^\circ$};
    \node[font=\footnotesize] at (90:0.8) {$60^\circ$};
    \node[below=3pt] at (O) {$O$};
    \node[below=14pt] at (0.9,0) {Hình 1};
  \end{scope}
  % Hình 2
  \begin{scope}[shift={(4.5,0)}]
    \coordinate (O) at (0,0);
    \draw (O) -- (0,1.8) node[above=2pt] {$x$};
    \draw (O) -- (25:1.8) node[above right=1pt] {$t$};
    \draw (O) -- (-20:1.8) node[right=2pt] {$y$};
    \node[font=\footnotesize] at (55:0.85) {$60^\circ$};
    \node[font=\footnotesize] at (5:0.85) {$45^\circ$};
    \node[below=3pt] at (O) {$O$};
    \node[below=14pt] at (0.9,0) {Hình 2};
  \end{scope}
  % Hình 3
  \begin{scope}[shift={(9.2,0)}]
    \coordinate (O) at (0,0);
    \draw (-1.6,0) node[below=2pt] {$x$} -- (1.6,0) node[above=2pt] {$t$};
    \draw (O) -- (116:1.8) node[above=2pt] {$y$};
    \node[font=\footnotesize] at (55:0.8) {$116^\circ$};
    \node[font=\footnotesize] at (145:0.8) {$64^\circ$};
    \node[below=3pt] at (O) {$O$};
    \node[below=14pt] at (0,0) {Hình 3};
  \end{scope}
  % Hình 4
  \begin{scope}[shift={(13.8,0)}]
    \coordinate (O) at (0,0);
    \draw (O) -- (0,1.8) node[above=2pt] {$t$};
    \draw (O) -- (145:1.8) node[above left=1pt] {$x$};
    \draw (O) -- (35:1.8) node[above right=1pt] {$y$};
    \node[font=\footnotesize] at (115:1.1) {$30^\circ$};
    \node[font=\footnotesize] at (65:1.1) {$30^\circ$};
    \node[below=3pt] at (O) {$O$};
    \node[below=14pt] at (0,0) {Hình 4};
  \end{scope}
\end{tikzpicture}'''

p2c1_tikz = r'''\begin{tikzpicture}[scale=0.9, line cap=round, line join=round]
  \coordinate (O) at (0,0);
  \coordinate (A) at (2.4,0);
  \coordinate (B) at ($(A)+(68:2.4)$);
  \coordinate (C) at ($(O)+(68:3.2)$);
  \draw[thick] (O) -- (3.8,0) node[above=2pt] {$x$};
  \draw[thick] (O) -- ($(O)+(68:3.8)$) node[above left=1pt] {$y$};
  \draw[thick] (A) -- ($(A)+(68:3.3)$) node[above right=1pt] {$z$};
  \draw[thick] (C) -- (B);
  \fill[gray!30] (O) -- (0.5,0) arc (0:68:0.5) -- cycle;
  \draw[thick] (0.5,0) arc (0:68:0.5);
  \node[font=\footnotesize] at (34:0.85) {$70^\circ$};
  \fill[gray!30] (A) -- ++(0:0.5) arc (0:68:0.5) -- cycle;
  \draw[thick] (A) ++(0:0.5) arc (0:68:0.5);
  \node[font=\footnotesize] at ($(A)+(34:0.85)$) {$70^\circ$};
  \fill[gray!30] (B) -- ++(147:0.45) arc (147:248:0.45) -- cycle;
  \draw[thick] (B) ++(147:0.45) arc (147:248:0.45);
  \node[font=\footnotesize] at ($(B)+(-0.55,-0.12)$) {$110^\circ$};
  \node[below left=1pt] at (O) {$O$};
  \node[below=2pt] at (A) {$A$};
  \node[right=2pt] at (B) {$B$};
  \node[above left=1pt] at (C) {$C$};
\end{tikzpicture}'''

de_03_data = {
  "de_so": 3,
  "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I 2026 – 2027",
  "mon": "Toán 7",
  "thoi_gian": "90 phút",
  "phan_I_trac_nghiem": [
    {
      "cau": 1,
      "noi_dung": "Số đối của số $\\dfrac{1}{3}$ là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$3$",
        "B": "$-\\dfrac{1}{3}$",
        "C": "$\\dfrac{3}{5}$",
        "D": "$-0{,}2$"
      },
      "dap_an": "B",
      "loi_giai": "Số đối của số $a$ là $-a$. Do đó, số đối của $\\dfrac{1}{3}$ là $-\\dfrac{1}{3}$."
    },
    {
      "cau": 2,
      "noi_dung": "Từ hình sau, góc $x'Oy'$ đối đỉnh với góc nào?",
      "hinh_tikz": c2_tikz,
      "lua_chon": {
        "A": "$\\widehat{xOy}$",
        "B": "$\\widehat{y'Ox}$",
        "C": "$\\widehat{x'Oy}$",
        "D": "$\\widehat{xOy'}$"
      },
      "dap_an": "A",
      "loi_giai": "Ta có tia đối của tia $Ox'$ là $Ox$ và tia đối của tia $Oy'$ là $Oy$. Do đó, góc đối đỉnh với góc $\\widehat{x'Oy'}$ là góc $\\widehat{xOy}$."
    },
    {
      "cau": 3,
      "noi_dung": "Cho bài toán $x + \\dfrac{1}{2} = 5$, khi chuyển số hạng $\\dfrac{1}{2}$ từ vế trái sang vế phải ta được:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$x = 5 + \\dfrac{1}{2}$",
        "B": "$x = -5 + \\dfrac{1}{2}$",
        "C": "$x = 5 - \\dfrac{1}{2}$",
        "D": "$x = -5 - \\dfrac{1}{2}$"
      },
      "dap_an": "C",
      "loi_giai": "Theo quy tắc chuyển vế, khi chuyển một số hạng từ vế này sang vế kia ta phải đổi dấu số hạng đó: $+\\dfrac{1}{2}$ chuyển sang vế phải thành $-\\dfrac{1}{2}$. Vậy $x = 5 - \\dfrac{1}{2}$."
    },
    {
      "cau": 4,
      "noi_dung": "Tia $Ot$ nào trong các hình dưới đây là tia phân giác của góc $\\widehat{xOy}$?",
      "hinh_tikz": c4_tikz,
      "lua_chon": {
        "A": "Hình 1",
        "B": "Hình 2",
        "C": "Hình 3",
        "D": "Hình 4"
      },
      "dap_an": "D",
      "loi_giai": "Tia phân giác $Ot$ của góc $\\widehat{xOy}$ phải nằm giữa hai tia $Ox, Oy$ và tạo với hai tia này hai góc bằng nhau ($\\widehat{xOt} = \\widehat{yOt}$). Trong Hình 4, tia $Ot$ nằm giữa hai tia $Ox, Oy$ và $\\widehat{xOt} = \\widehat{yOt} = 30^\\circ$ nên $Ot$ là tia phân giác của góc $\\widehat{xOy}$."
    },
    {
      "cau": 5,
      "noi_dung": "Kết quả của phép tính $7^{10} : 7$ viết dưới dạng lũy thừa là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$7^9$",
        "B": "$7^{11}$",
        "C": "$7^{10}$",
        "D": "$1^{10}$"
      },
      "dap_an": "A",
      "loi_giai": "Ta có: $7^{10} : 7 = 7^{10} : 7^1 = 7^{10 - 1} = 7^9$."
    },
    {
      "cau": 6,
      "noi_dung": "Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc so le trong:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "Bằng nhau",
        "B": "Phụ nhau",
        "C": "Kề nhau",
        "D": "Kề bù"
      },
      "dap_an": "A",
      "loi_giai": "Tính chất hai đường thẳng song song: Nếu một đường thẳng cắt hai đường thẳng song song thì hai góc so le trong bằng nhau."
    },
    {
      "cau": 7,
      "noi_dung": "Cho các số thập phân sau: $0{,}12222\\dots$; $4{,}(5)$; $1{,}2184218$; $-11{,}2(312)$. Số thập phân hữu hạn là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$1{,}2184218$",
        "B": "$0{,}12222\\dots$",
        "C": "$4{,}(5)$",
        "D": "$-11{,}2(312)$"
      },
      "dap_an": "A",
      "loi_giai": "Số $1{,}2184218$ là số thập phân hữu hạn vì phần thập phân có hữu hạn chữ số. Các số còn lại là số thập phân vô hạn tuần hoàn."
    },
    {
      "cau": 8,
      "noi_dung": "Qua một điểm ở ngoài một đường thẳng, có bao nhiêu đường thẳng song song với đường thẳng đó?",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "Không có",
        "B": "Có vô số",
        "C": "Có ít nhất một",
        "D": "Chỉ có một"
      },
      "dap_an": "D",
      "loi_giai": "Theo Tiên đề Euclid: Qua một điểm ở ngoài một đường thẳng chỉ có một đường thẳng song song với đường thẳng đó."
    },
    {
      "cau": 9,
      "noi_dung": "Số hữu tỉ $x$ thỏa mãn $x^2 = 25$ là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$625$",
        "B": "$-5$",
        "C": "$5$",
        "D": "$5$ hoặc $-5$"
      },
      "dap_an": "D",
      "loi_giai": "Ta có $x^2 = 25 = (\\pm 5)^2 \\Rightarrow x = 5$ hoặc $x = -5$."
    },
    {
      "cau": 10,
      "noi_dung": "Mô tả quy tắc chuyển vế qua đẳng thức $x - \\dfrac{1}{2} = -\\dfrac{5}{6}$ ta được:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$x - \\dfrac{5}{6} = \\dfrac{1}{2}$",
        "B": "$x = \\dfrac{5}{6} + \\dfrac{1}{2}$",
        "C": "$x = -\\dfrac{5}{6} + \\dfrac{1}{2}$",
        "D": "$x = -\\dfrac{5}{6} - \\dfrac{1}{2}$"
      },
      "dap_an": "C",
      "loi_giai": "Khi chuyển số hạng $-\\dfrac{1}{2}$ từ vế trái sang vế phải, ta đổi dấu thành $+\\dfrac{1}{2}$. Do đó $x = -\\dfrac{5}{6} + \\dfrac{1}{2}$."
    },
    {
      "cau": 11,
      "noi_dung": "Cho 3 đường thẳng phân biệt $a, b, c$. Biết $a \\perp b$ và $b \\perp c$, khi đó:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$a \\perp c$",
        "B": "$b \\parallel c$",
        "C": "$a \\parallel b$",
        "D": "$a \\parallel c$"
      },
      "dap_an": "D",
      "loi_giai": "Hai đường thẳng phân biệt cùng vuông góc với một đường thẳng thứ ba thì chúng song song với nhau: $\\begin{cases} a \\perp b \\\\ b \\perp c \\end{cases} \\Rightarrow a \\parallel c$."
    },
    {
      "cau": 12,
      "noi_dung": "Căn bậc hai số học của $64$ là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$32$",
        "B": "$8$ và $-8$",
        "C": "$-8$",
        "D": "$8$"
      },
      "dap_an": "D",
      "loi_giai": "Căn bậc hai số học của một số $a \\ge 0$ là số không âm $x$ sao cho $x^2 = a$. Vì $8 \\ge 0$ và $8^2 = 64$ nên $\\sqrt{64} = 8$."
    }
  ],
  "phan_II_dung_sai": [
    {
      "cau": 1,
      "noi_dung": "Cho $\\widehat{xOy} = 70^\\circ$. Trên tia $Ox$ lấy điểm $A$. Kẻ tia $Az$ sao cho $\\widehat{xAz} = 70^\\circ$. Trên tia $Az$ lấy điểm $B$, kẻ tia $Bt$ cắt $Oy$ tại $C$ sao cho $\\widehat{CBA} = 110^\\circ$. Xét tính đúng sai của các mệnh đề sau:",
      "hinh_tikz": p2c1_tikz,
      "menh_de": [
        {
          "y": "a",
          "noi_dung": "$\\widehat{ABC}$ và $\\widehat{CBz}$ là hai góc kề bù.",
          "dap_an": "Đúng",
          "loi_giai": "Tia $BA$ và tia $Bz$ là hai tia đối nhau nên $\\widehat{ABC}$ và $\\widehat{CBz}$ là hai góc kề bù."
        },
        {
          "y": "b",
          "noi_dung": "$\\widehat{CBz} = 70^\\circ$.",
          "dap_an": "Đúng",
          "loi_giai": "Vì $\\widehat{ABC}$ và $\\widehat{CBz}$ kề bù nên $\\widehat{CBz} = 180^\\circ - \\widehat{CBA} = 180^\\circ - 110^\\circ = 70^\\circ$."
        },
        {
          "y": "c",
          "noi_dung": "$Oy$ song song với $Az$.",
          "dap_an": "Đúng",
          "loi_giai": "Ta có $\\widehat{xOy} = \\widehat{xAz} = 70^\\circ$. Mà hai góc này ở vị trí đồng vị nên $Oy \\parallel Az$."
        },
        {
          "y": "d",
          "noi_dung": "$\\widehat{BCO} = 110^\\circ$.",
          "dap_an": "Sai",
          "loi_giai": "Vì $Oy \\parallel Az$ nên $\\widehat{BCO}$ và $\\widehat{CBz}$ là hai góc so le trong $\\Rightarrow \\widehat{BCO} = \\widehat{CBz} = 70^\\circ \\neq 110^\\circ$."
        }
      ]
    },
    {
      "cau": 2,
      "noi_dung": "Cho biểu thức $M = \\left(-\\dfrac{1}{2}\\right)^3 \\cdot \\dfrac{8}{3} + \\left|-\\dfrac{3}{4}\\right|$. Xét tính đúng sai của các mệnh đề sau:",
      "hinh_tikz": None,
      "menh_de": [
        {
          "y": "a",
          "noi_dung": "Giá trị của lũy thừa $\\left(-\\dfrac{1}{2}\\right)^3$ bằng $-\\dfrac{1}{8}$.",
          "dap_an": "Đúng",
          "loi_giai": "Ta có $\\left(-\\dfrac{1}{2}\\right)^3 = \\dfrac{(-1)^3}{2^3} = -\\dfrac{1}{8}$."
        },
        {
          "y": "b",
          "noi_dung": "Giá trị tuyệt đối $\\left|-\\dfrac{3}{4}\\right|$ bằng $-\\dfrac{3}{4}$.",
          "dap_an": "Sai",
          "loi_giai": "Theo định nghĩa giá trị tuyệt đối của số âm: $\\left|-\\dfrac{3}{4}\\right| = \\dfrac{3}{4} \\neq -\\dfrac{3}{4}$."
        },
        {
          "y": "c",
          "noi_dung": "Giá trị của biểu thức $M$ bằng $-\\dfrac{1}{4}$.",
          "dap_an": "Sai",
          "loi_giai": "Ta có: $M = \\left(-\\dfrac{1}{8}\\right) \\cdot \\dfrac{8}{3} + \\dfrac{3}{4} = -\\dfrac{1}{3} + \\dfrac{3}{4} = \\dfrac{-4 + 9}{12} = \\dfrac{5}{12} \\neq -\\dfrac{1}{4}$."
        },
        {
          "y": "d",
          "noi_dung": "Giá trị $M$ tìm được là một số hữu tỉ âm.",
          "dap_an": "Sai",
          "loi_giai": "Vì $M = \\dfrac{5}{12} > 0$ nên $M$ là số hữu tỉ dương."
        }
      ]
    }
  ],
  "phan_III_tra_loi_ngan": [
    {
      "cau": 1,
      "noi_dung": "Tìm số hữu tỉ $x$, biết: $\\left(x - \\dfrac{1}{3}\\right)^2 = \\dfrac{4}{9}$.",
      "hinh_tikz": None,
      "dap_an": "$x \\in \\left\\{1; -\\dfrac{1}{3}\\right\\}$",
      "loi_giai": "Ta có $\\left(x - \\dfrac{1}{3}\\right)^2 = \\dfrac{4}{9} = \\left(\\pm \\dfrac{2}{3}\\right)^2$.\n\nTrường hợp 1: $x - \\dfrac{1}{3} = \\dfrac{2}{3} \\Rightarrow x = \\dfrac{2}{3} + \\dfrac{1}{3} = 1$.\n\nTrường hợp 2: $x - \\dfrac{1}{3} = -\\dfrac{2}{3} \\Rightarrow x = -\\dfrac{2}{3} + \\dfrac{1}{3} = -\\dfrac{1}{3}$.\n\nVậy $x \\in \\left\\{1; -\\dfrac{1}{3}\\right\\}$."
    },
    {
      "cau": 2,
      "noi_dung": "Cho hai đường thẳng $xx'$ và $yy'$ cắt nhau tại điểm $O$. Biết $\\widehat{xOy} = 60^\\circ$. Tính số đo góc đối đỉnh $\\widehat{x'Oy'}$ và góc kề bù $\\widehat{x'Oy}$ với góc $\\widehat{xOy}$.",
      "hinh_tikz": None,
      "dap_an": "$\\widehat{x'Oy'} = 60^\\circ; \\widehat{x'Oy} = 120^\\circ$",
      "loi_giai": "Góc đối đỉnh: Vì $\\widehat{x'Oy'}$ và $\\widehat{xOy}$ là hai góc đối đỉnh nên:\n\\[ \\widehat{x'Oy'} = \\widehat{xOy} = 60^\\circ. \\]\nGóc kề bù: Vì $\\widehat{x'Oy}$ và $\\widehat{xOy}$ là hai góc kề bù nên:\n\\[ \\widehat{x'Oy} + \\widehat{xOy} = 180^\\circ \\Rightarrow \\widehat{x'Oy} = 180^\\circ - 60^\\circ = 120^\\circ. \\]\nĐáp án: $\\widehat{x'Oy'} = 60^\\circ$ và $\\widehat{x'Oy} = 120^\\circ$."
    }
  ],
  "phan_IV_tu_luan": [
    {
      "cau": 1,
      "noi_dung": "Thực hiện phép tính:",
      "hinh_tikz": None,
      "cac_y": [
        {
          "y": "a",
          "cau_hoi": "$(-0{,}25) \\cdot 40 + 3 + 2026^0$",
          "loi_giai": "Ta có:\n\\[ (-0{,}25) \\cdot 40 + 3 + 2026^0 = -10 + 3 + 1 = -7 + 1 = -6. \\]"
        },
        {
          "y": "b",
          "cau_hoi": "$\\dfrac{1}{7} \\cdot \\dfrac{-3}{8} + \\dfrac{-13}{8} \\cdot \\dfrac{1}{7}$",
          "loi_giai": "Ta có:\n\\[ \\dfrac{1}{7} \\cdot \\dfrac{-3}{8} + \\dfrac{-13}{8} \\cdot \\dfrac{1}{7} = \\dfrac{1}{7} \\left( \\dfrac{-3}{8} + \\dfrac{-13}{8} \\right) = \\dfrac{1}{7} \\cdot \\left(-\\dfrac{16}{8}\\right) = \\dfrac{1}{7} \\cdot (-2) = -\\dfrac{2}{7}. \\]"
        },
        {
          "y": "c",
          "cau_hoi": "$\\left[ \\left(\\dfrac{2}{3} - \\dfrac{7}{6}\\right)^2 + (-2)^3 \\cdot 3 \\right] : 4\\dfrac{3}{4} - 1$",
          "loi_giai": "Ta có:\n\\begin{align*}\n\\left[ \\left(\\dfrac{2}{3} - \\dfrac{7}{6}\\right)^2 + (-2)^3 \\cdot 3 \\right] : 4\\dfrac{3}{4} - 1 &= \\left[ \\left(\\dfrac{4 - 7}{6}\\right)^2 + (-8) \\cdot 3 \\right] : \\dfrac{19}{4} - 1 \\\\\n&= \\left[ \\left(-\\dfrac{3}{6}\\right)^2 - 24 \\right] \\cdot \\dfrac{4}{19} - 1 \\\\\n&= \\left[ \\left(-\\dfrac{1}{2}\\right)^2 - 24 \\right] \\cdot \\dfrac{4}{19} - 1 \\\\\n&= \\left( \\dfrac{1}{4} - 24 \\right) \\cdot \\dfrac{4}{19} - 1 \\\\\n&= -\\dfrac{95}{4} \\cdot \\dfrac{4}{19} - 1 \\\\\n&= -5 - 1 = -6.\n\\end{align*}"
        }
      ]
    },
    {
      "cau": 2,
      "noi_dung": "Tìm $x$ biết:",
      "hinh_tikz": None,
      "cac_y": [
        {
          "y": "a",
          "cau_hoi": "$x + 4{,}5 = 9{,}5$",
          "loi_giai": "Ta có:\n\\[ x = 9{,}5 - 4{,}5 \\Rightarrow x = 5. \\]"
        },
        {
          "y": "b",
          "cau_hoi": "$\\dfrac{2}{5} \\cdot x - \\dfrac{1}{2} = \\dfrac{3}{8}$",
          "loi_giai": "Ta có:\n\\begin{align*}\n\\dfrac{2}{5} \\cdot x &= \\dfrac{3}{8} + \\dfrac{1}{2} = \\dfrac{3}{8} + \\dfrac{4}{8} = \\dfrac{7}{8} \\\\\nx &= \\dfrac{7}{8} : \\dfrac{2}{5} = \\dfrac{7}{8} \\cdot \\dfrac{5}{2} = \\dfrac{35}{16}.\n\\end{align*}"
        },
        {
          "y": "c",
          "cau_hoi": "$|3x - 1| + \\dfrac{1}{3} = \\dfrac{1}{2}$",
          "loi_giai": "Ta có:\n\\[ |3x - 1| = \\dfrac{1}{2} - \\dfrac{1}{3} = \\dfrac{1}{6}. \\]\nTrường hợp 1:\n\\[ 3x - 1 = \\dfrac{1}{6} \\Rightarrow 3x = \\dfrac{7}{6} \\Rightarrow x = \\dfrac{7}{18}. \\]\nTrường hợp 2:\n\\[ 3x - 1 = -\\dfrac{1}{6} \\Rightarrow 3x = \\dfrac{5}{6} \\Rightarrow x = \\dfrac{5}{18}. \\]\nVậy $x \\in \\left\\{\\dfrac{7}{18}; \\dfrac{5}{18}\\right\\}$."
        }
      ]
    },
    {
      "cau": 3,
      "noi_dung": "Hai người thợ cùng làm một công việc. Nếu làm riêng thì người thứ nhất phải mất 3 giờ, người thứ hai phải mất 5 giờ mới hoàn thành công việc. Hỏi nếu làm chung trong 45 phút thì hai người làm được mấy phần công việc?",
      "hinh_tikz": None,
      "cac_y": [],
      "loi_giai": "Đổi 45 phút = $\\dfrac{45}{60}$ giờ = $\\dfrac{3}{4}$ giờ.\n\nTrong 1 giờ, người thứ nhất làm được:\n\\[ 1 : 3 = \\dfrac{1}{3} \\text{ (công việc)}. \\]\nTrong 1 giờ, người thứ hai làm được:\n\\[ 1 : 5 = \\dfrac{1}{5} \\text{ (công việc)}. \\]\nTrong 1 giờ, cả hai người làm chung được:\n\\[ \\dfrac{1}{3} + \\dfrac{1}{5} = \\dfrac{8}{15} \\text{ (công việc)}. \\]\nTrong 45 phút ($\\dfrac{3}{4}$ giờ), cả hai người làm chung được:\n\\[ \\dfrac{8}{15} \\cdot \\dfrac{3}{4} = \\dfrac{2}{5} \\text{ (công việc)}. \\]\n\nĐáp số: $\\dfrac{2}{5}$ công việc."
    }
  ]
}

target_file = r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_03\de_03.json'
with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(de_03_data, f, ensure_ascii=False, indent=2)

print('Updated de_03.json with standard schema!')
