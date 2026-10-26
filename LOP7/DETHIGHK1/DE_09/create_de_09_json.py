import json
import os

de_09 = {
  "de_so": 9,
  "tieu_de": "BỘ ĐỀ ÔN TẬP GIỮA KÌ I TOÁN 7 - ĐỀ SỐ 9",
  "thoi_gian": 90,
  "phan_I_trac_nghiem": [
    {
      "cau": 1,
      "noi_dung": "Trong các phân số sau, phân số nào biểu diễn số hữu tỉ $-0{,}5$?",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$\\dfrac{1}{2}$",
        "B": "$-\\dfrac{1}{2}$",
        "C": "$\\dfrac{3}{5}$",
        "D": "$-\\dfrac{3}{5}$"
      },
      "dap_an": "B",
      "loi_giai": "Ta có: $-0{,}5 = -\\dfrac{5}{10} = -\\dfrac{1}{2}$."
    },
    {
      "cau": 2,
      "noi_dung": "Quan sát trục số sau. Điểm $A$ biểu diễn số hữu tỉ nào?",
      "hinh_tikz": "\\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]\n    \\draw[thick, ->] (-3.8, 0) -- (3.8, 0);\n    \\foreach \\x in {-3.0, -2.4, -1.8, -1.2, -0.6, 0, 0.6, 1.2, 1.8, 2.4, 3.0} {\n        \\draw[thick] (\\x, 0.12) -- (\\x, -0.12);\n    }\n    \\node[below=3pt] at (0, -0.12) {$0$};\n    \\node[below=3pt] at (3.0, -0.12) {$1$};\n    \\filldraw[red] (-1.8, 0) circle (1.5pt) node[above=4pt, red, font=\\bfseries] {$A$};\n\\end{tikzpicture}",
      "lua_chon": {
        "A": "$\\dfrac{3}{5}$",
        "B": "$-\\dfrac{3}{4}$",
        "C": "$-3$",
        "D": "$-\\dfrac{3}{5}$"
      },
      "dap_an": "D",
      "loi_giai": "Đoạn đơn vị từ $0$ đến $1$ được chia thành $5$ phần bằng nhau, mỗi vạch chia tương ứng với $\\dfrac{1}{5}$. Điểm $A$ nằm về phía bên trái điểm $0$ và cách điểm $0$ một khoảng bằng $3$ phần, nên điểm $A$ biểu diễn số hữu tỉ $-\\dfrac{3}{5}$."
    },
    {
      "cau": 3,
      "noi_dung": "Phép tính nào sau đây là không đúng?",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$(x^3)^4 = x^{12}$",
        "B": "$x^{18} : x^6 = x^{12}$ ($x \\neq 0$)",
        "C": "$x^2 \\cdot x^6 = x^{12}$",
        "D": "$x^4 \\cdot x^8 = x^{12}$"
      },
      "dap_an": "C",
      "loi_giai": "Theo quy tắc nhân hai lũy thừa cùng cơ số: $x^2 \\cdot x^6 = x^{2+6} = x^8 \\neq x^{12}$. Do đó phép tính $x^2 \\cdot x^6 = x^{12}$ là sai."
    },
    {
      "cau": 4,
      "noi_dung": "Kết quả của phép tính $2^2 \\cdot 2^5$ là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$2^{10}$",
        "B": "$2^3$",
        "C": "$2^5$",
        "D": "$2^7$"
      },
      "dap_an": "D",
      "loi_giai": "Áp dụng quy tắc nhân hai lũy thừa cùng cơ số: $2^2 \\cdot 2^5 = 2^{2+5} = 2^7$."
    },
    {
      "cau": 5,
      "noi_dung": "Một hình vuông có diện tích $81\\text{ cm}^2$. Độ dài cạnh hình vuông đó là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$81\\text{ cm}$",
        "B": "$9\\text{ cm}$",
        "C": "$-9\\text{ cm}$",
        "D": "$\\pm 9\\text{ cm}$"
      },
      "dap_an": "B",
      "loi_giai": "Độ dài cạnh hình vuông là số dương $a$ thỏa mãn $a^2 = 81$. Do $9 > 0$ và $9^2 = 81$ nên $a = 9\\text{ cm}$."
    },
    {
      "cau": 6,
      "noi_dung": "Làm tròn số $1{,}3781$ với độ chính xác $0{,}005$ được kết quả là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$1{,}37$",
        "B": "$1{,}4$",
        "C": "$1$",
        "D": "$1{,}38$"
      },
      "dap_an": "D",
      "loi_giai": "Độ chính xác $0{,}005$ yêu cầu làm tròn số đến hàng phần trăm. Chữ số ở hàng phần nghìn là $8 \\ge 5$, nên ta cộng $1$ vào chữ số hàng phần trăm: $1{,}3781 \\approx 1{,}38$."
    },
    {
      "cau": 7,
      "noi_dung": "Trong các hình sau, hình nào không phải là hình lăng trụ đứng tứ giác?\n\\begin{center}\n\\includegraphics[width=10.5cm]{crops/test_p42_xref3051.png}\n\\end{center}",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "Hình 1",
        "B": "Hình 2",
        "C": "Hình 3",
        "D": "Hình 4"
      },
      "dap_an": "B",
      "loi_giai": "Hình 2 có hai mặt đáy là hình tam giác nên đây là hình lăng trụ đứng tam giác, không phải là hình lăng trụ đứng tứ giác."
    },
    {
      "cau": 8,
      "noi_dung": "Thực hiện phép tính $M = \\dfrac{13}{31} + \\dfrac{4}{15} + \\dfrac{18}{31} + \\dfrac{2024}{2025} - \\dfrac{19}{15}$, ta được kết quả là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$M = \\dfrac{2024}{2025}$",
        "B": "$M = -\\dfrac{2024}{2025}$",
        "C": "$M = 1$",
        "D": "$M = 0$"
      },
      "dap_an": "A",
      "loi_giai": "Nhóm các phân số có cùng mẫu số:\n\\[ M = \\left(\\dfrac{13}{31} + \\dfrac{18}{31}\\right) + \\left(\\dfrac{4}{15} - \\dfrac{19}{15}\\right) + \\dfrac{2024}{2025} = 1 + (-1) + \\dfrac{2024}{2025} = \\dfrac{2024}{2025}. \\]"
    },
    {
      "cau": 9,
      "noi_dung": "Tia phân giác của $\\widehat{xOm}$ và $\\widehat{yOn}$ lần lượt là:",
      "hinh_tikz": "\\begin{tikzpicture}[scale=0.8, line cap=round, line join=round]\n    \\coordinate (O) at (0, 0);\n    \\coordinate (x) at (-2.8, 0);\n    \\coordinate (y) at (2.8, 0);\n    \\coordinate (k) at ({2.5*cos(150)}, {2.5*sin(150)});\n    \\coordinate (m) at ({2.5*cos(120)}, {2.5*sin(120)});\n    \\coordinate (n) at ({2.5*cos(60)}, {2.5*sin(60)});\n    \\coordinate (u) at ({2.5*cos(30)}, {2.5*sin(30)});\n\n    \\draw[thick] (-3.0, 0) -- (3.0, 0);\n    \\draw[thick] (O) -- (k);\n    \\draw[thick] (O) -- (m);\n    \\draw[thick] (O) -- (n);\n    \\draw[thick] (O) -- (u);\n\n    \\node[below] at (O) {$O$};\n    \\node[below left] at (-2.8, 0) {$x$};\n    \\node[below right] at (2.8, 0) {$y$};\n    \\node[above left] at (k) {$k$};\n    \\node[above] at (m) {$m$};\n    \\node[above] at (n) {$n$};\n    \\node[above right] at (u) {$u$};\n\n    % Arcs for xOk and kOm\n    \\draw[thick] (O) ++(180:0.6) arc (180:150:0.6);\n    \\draw[thick] (O) ++(150:0.6) arc (150:120:0.6);\n    \\draw[thick] ($(O)+(165:0.53)$) -- ($(O)+(165:0.67)$);\n    \\draw[thick] ($(O)+(135:0.53)$) -- ($(O)+(135:0.67)$);\n\n    % Arcs for yOu and uOn\n    \\draw[thick] (O) ++(0:0.6) arc (0:30:0.6);\n    \\draw[thick] (O) ++(30:0.6) arc (30:60:0.6);\n    \\draw[thick] ($(O)+(13:0.53)$) -- ($(O)+(13:0.67)$);\n    \\draw[thick] ($(O)+(17:0.53)$) -- ($(O)+(17:0.67)$);\n    \\draw[thick] ($(O)+(43:0.53)$) -- ($(O)+(43:0.67)$);\n    \\draw[thick] ($(O)+(47:0.53)$) -- ($(O)+(47:0.67)$);\n\\end{tikzpicture}",
      "lua_chon": {
        "A": "$Ok$ và $Ou$",
        "B": "$Ox$ và $Oy$",
        "C": "$Ou$ và $Om$",
        "D": "$Ok$ và $On$"
      },
      "dap_an": "A",
      "loi_giai": "Ký hiệu trên hình thể hiện góc $\\widehat{xOk} = \\widehat{kOm}$ nên $Ok$ là tia phân giác của $\\widehat{xOm}$. Ký hiệu trên hình thể hiện góc $\\widehat{yOu} = \\widehat{uOn}$ nên $Ou$ là tia phân giác của $\\widehat{yOn}$."
    },
    {
      "cau": 10,
      "noi_dung": "Tổng ba góc trong một tam giác luôn bằng:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$90^\\circ$",
        "B": "$120^\\circ$",
        "C": "$180^\\circ$",
        "D": "$360^\\circ$"
      },
      "dap_an": "C",
      "loi_giai": "Theo định lí về tổng ba góc trong một tam giác, tổng ba góc của một tam giác luôn bằng $180^\\circ$."
    },
    {
      "cau": 11,
      "noi_dung": "Hai đường thẳng $xy$ và $x'y'$ cắt nhau tại $O$. Biết $\\widehat{xOx'} = 70^\\circ$. $Ot$ là tia phân giác của $\\widehat{xOx'}$, $Ot'$ là tia đối của tia $Ot$. Tính số đo góc $\\widehat{yOt'}$?",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "$35^\\circ$",
        "B": "$70^\\circ$",
        "C": "$145^\\circ$",
        "D": "$110^\\circ$"
      },
      "dap_an": "A",
      "loi_giai": "Do $Ot$ là tia phân giác của $\\widehat{xOx'}$ nên $\\widehat{xOt} = \\dfrac{\\widehat{xOx'}}{2} = \\dfrac{70^\\circ}{2} = 35^\\circ$. Vì tia $Oy$ là tia đối của tia $Ox$ và tia $Ot'$ là tia đối của tia $Ot$ nên hai góc $\\widehat{yOt'}$ và $\\widehat{xOt}$ là hai góc đối đỉnh. Suy ra $\\widehat{yOt'} = \\widehat{xOt} = 35^\\circ$."
    },
    {
      "cau": 12,
      "noi_dung": "Đối với biểu thức không có dấu ngoặc và chỉ có các phép tính: cộng, trừ, nhân, chia, lũy thừa, thì thứ tự thực hiện phép tính đúng là:",
      "hinh_tikz": None,
      "lua_chon": {
        "A": "Lũy thừa $\\to$ Nhân và chia $\\to$ Cộng và trừ",
        "B": "Nhân và chia $\\to$ Lũy thừa $\\to$ Cộng và trừ",
        "C": "Cộng và trừ $\\to$ Nhân và chia $\\to$ Lũy thừa",
        "D": "Lũy thừa $\\to$ Cộng và trừ $\\to$ Nhân và chia"
      },
      "dap_an": "A",
      "loi_giai": "Thứ tự ưu tiên thực hiện phép tính đúng: Lũy thừa $\\to$ Nhân và chia $\\to$ Cộng và trừ."
    }
  ],
  "phan_II_dung_sai": [
    {
      "cau": 1,
      "noi_dung": "Cho biểu thức $P = \\left(-\\dfrac{2}{3}\\right)^2 + \\dfrac{5}{9} : \\left(-\\dfrac{5}{3}\\right) - \\left|-\\dfrac{1}{3}\\right|$. Xét tính đúng sai của các mệnh đề sau:",
      "hinh_tikz": None,
      "menh_de": [
        {
          "y": "a",
          "noi_dung": "Giá trị của lũy thừa $\\left(-\\dfrac{2}{3}\\right)^2$ bằng $\\dfrac{4}{9}$.",
          "dap_an": "Đúng",
          "loi_giai": "Ta có $\\left(-\\dfrac{2}{3}\\right)^2 = \\dfrac{(-2)^2}{3^2} = \\dfrac{4}{9}$."
        },
        {
          "y": "b",
          "noi_dung": "Kết quả của phép chia $\\dfrac{5}{9} : \\left(-\\dfrac{5}{3}\\right)$ bằng $-\\dfrac{1}{3}$.",
          "dap_an": "Đúng",
          "loi_giai": "Thực hiện phép chia: $\\dfrac{5}{9} : \\left(-\\dfrac{5}{3}\\right) = \\dfrac{5}{9} \\cdot \\left(-\\dfrac{3}{5}\\right) = -\\dfrac{3}{9} = -\\dfrac{1}{3}$."
        },
        {
          "y": "c",
          "noi_dung": "Giá trị tuyệt đối $\\left|-\\dfrac{1}{3}\\right|$ bằng $-\\dfrac{1}{3}$.",
          "dap_an": "Sai",
          "loi_giai": "Giá trị tuyệt đối của số âm là số đối của nó: $\\left|-\\dfrac{1}{3}\\right| = \\dfrac{1}{3} \\neq -\\dfrac{1}{3}$."
        },
        {
          "y": "d",
          "noi_dung": "Giá trị của biểu thức $P$ bằng $-\\dfrac{2}{9}$.",
          "dap_an": "Đúng",
          "loi_giai": "Thay các kết quả vào biểu thức $P$: $P = \\dfrac{4}{9} + \\left(-\\dfrac{1}{3}\\right) - \\dfrac{1}{3} = \\dfrac{4}{9} - \\dfrac{6}{9} = -\\dfrac{2}{9}$."
        }
      ]
    },
    {
      "cau": 2,
      "noi_dung": "Cho $\\Delta ABC = \\Delta DEF$ với $AB = 8\\text{ cm}, BC = 6\\text{ cm}, DF = 10\\text{ cm}$; $\\widehat{B} = 90^\\circ, \\widehat{C} = 53^\\circ$. Xét tính đúng sai của các mệnh đề sau:",
      "hinh_tikz": None,
      "menh_de": [
        {
          "y": "a",
          "noi_dung": "Số đo góc $E$ bằng $53^\\circ$.",
          "dap_an": "Sai",
          "loi_giai": "Vì $\\Delta ABC = \\Delta DEF$ nên hai góc tương ứng $\\widehat{E} = \\widehat{B} = 90^\\circ \\neq 53^\\circ$."
        },
        {
          "y": "b",
          "noi_dung": "Độ dài cạnh $AC = 10\\text{ cm}$.",
          "dap_an": "Đúng",
          "loi_giai": "Hai tam giác bằng nhau có các cạnh tương ứng bằng nhau: $AC = DF = 10\\text{ cm}$."
        },
        {
          "y": "c",
          "noi_dung": "Độ dài cạnh $EF = 8\\text{ cm}$.",
          "dap_an": "Sai",
          "loi_giai": "Cạnh tương ứng với cạnh $EF$ là cạnh $BC$, suy ra $EF = BC = 6\\text{ cm} \\neq 8\\text{ cm}$."
        },
        {
          "y": "d",
          "noi_dung": "Tổng số đo $\\widehat{D} + \\widehat{F} = 90^\\circ$.",
          "dap_an": "Đúng",
          "loi_giai": "Xét tam giác $DEF$ vuông tại $E$ (vì $\\widehat{E} = 90^\\circ$), tổng ba góc trong một tam giác bằng $180^\\circ$ nên $\\widehat{D} + \\widehat{F} = 180^\\circ - 90^\\circ = 90^\\circ$."
        }
      ]
    }
  ],
  "phan_III_tra_loi_ngan": [
    {
      "cau": 1,
      "noi_dung": "Tìm số hữu tỉ $x$, biết: $\\dfrac{2}{3} + \\dfrac{1}{3} : x = -\\dfrac{1}{6}$.",
      "dap_an": "$-\\dfrac{2}{5}$",
      "loi_giai": "Ta có:\n\\[ \\dfrac{1}{3} : x = -\\dfrac{1}{6} - \\dfrac{2}{3} = -\\dfrac{5}{6} \\implies x = \\dfrac{1}{3} : \\left(-\\dfrac{5}{6}\\right) = \\dfrac{1}{3} \\cdot \\left(-\\dfrac{6}{5}\\right) = -\\dfrac{2}{5}. \\]"
    },
    {
      "cau": 2,
      "noi_dung": "Cho hình vẽ sau, biết $\\widehat{CFE} = 60^\\circ$ và $\\widehat{E}_1 = 120^\\circ$. Số đo của góc $\\widehat{FEB}$ bằng bao nhiêu độ?",
      "hinh_tikz": "\\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]\n    \\coordinate (E) at (1.1, 0);\n    \\coordinate (F) at (2.4, 1.6);\n\n    \\draw[thick, blue!80!black] (-0.8, 1.6) -- (4.2, 1.6);\n    \\draw[thick, blue!80!black] (-0.8, 0) -- (4.2, 0);\n\n    \\filldraw[black] (-0.3, 1.6) circle (1pt) node[above=2pt] {$C$};\n    \\filldraw[black] (3.8, 1.6) circle (1pt) node[above=2pt] {$D$};\n    \\filldraw[black] (-0.3, 0) circle (1pt) node[below=2pt] {$A$};\n    \\filldraw[black] (3.8, 0) circle (1pt) node[below=2pt] {$B$};\n\n    \\draw[thick, blue!80!black] ($(E)!-0.5!(F)$) -- ($(F)!-0.5!(E)$);\n\n    \\node[above left=1pt] at (E) {$E$};\n    \\node[above left=1pt] at (F) {$F$};\n\n    % Angle CFE = 60 deg\n    \\fill[gray!20] (F) -- ++(180:0.45) arc (180:231:0.45) -- cycle;\n    \\draw[thick] (F) ++(180:0.45) arc (180:231:0.45);\n    \\node[font=\\footnotesize, below left=1pt] at ($(F)+(-0.35, -0.05)$) {$60^\\circ$};\n\n    % Angle E1 = 120 deg\n    \\fill[gray!20] (E) -- ++(0:0.45) arc (0:-129:0.45) -- cycle;\n    \\draw[thick] (E) ++(0:0.45) arc (0:-129:0.45);\n    \\node[font=\\footnotesize, below=2pt] at ($(E)+(0.22, -0.05)$) {$1$};\n    \\node[font=\\footnotesize, below right=1pt] at ($(E)+(0.1, -0.35)$) {$120^\\circ$};\n\\end{tikzpicture}",
      "dap_an": "$60^\\circ$",
      "loi_giai": "Vì $\\widehat{FEB}$ và $\\widehat{E}_1$ là hai góc kề bù nên:\n\\[ \\widehat{FEB} + \\widehat{E}_1 = 180^\\circ \\implies \\widehat{FEB} = 180^\circ - 120^\\circ = 60^\\circ. \\]\n(Hơn nữa, ta thấy $\\widehat{CFE} = \\widehat{FEB} = 60^\\circ$, mà hai góc này ở vị trí so le trong nên $CD \\parallel AB$)."
    }
  ],
  "phan_IV_tu_luan": [
    {
      "cau": 1,
      "noi_dung": "Thực hiện phép tính (tính hợp lí nếu có):",
      "hinh_tikz": None,
      "cac_y": [
        {
          "y": "a",
          "cau_hoi": "$\\dfrac{-4}{12} + \\dfrac{14}{21}$;",
          "loi_giai": "$\\dfrac{-4}{12} + \\dfrac{14}{21} = -\\dfrac{1}{3} + \\dfrac{2}{3} = \\dfrac{1}{3}$."
        },
        {
          "y": "b",
          "cau_hoi": "$\\dfrac{8}{3} \\cdot \\dfrac{9}{4}$.",
          "loi_giai": "$\\dfrac{8}{3} \\cdot \\dfrac{9}{4} = \\dfrac{8 \\cdot 9}{3 \\cdot 4} = 2 \\cdot 3 = 6$."
        }
      ]
    },
    {
      "cau": 2,
      "noi_dung": "Tìm $x$, biết:",
      "hinh_tikz": None,
      "cac_y": [
        {
          "y": "a",
          "cau_hoi": "$x - \\dfrac{2}{3} = \\dfrac{5}{6}$;",
          "loi_giai": "$x = \\dfrac{5}{6} + \\dfrac{2}{3} = \\dfrac{5}{6} + \\dfrac{4}{6} = \\dfrac{9}{6} = \\dfrac{3}{2}$."
        },
        {
          "y": "b",
          "cau_hoi": "$(1 - x)^2 = \\dfrac{4}{9}$.",
          "loi_giai": "Vì $\\left(\\dfrac{2}{3}\\right)^2 = \\dfrac{4}{9}$ và $\\left(-\\dfrac{2}{3}\\right)^2 = \\dfrac{4}{9}$, ta xét hai trường hợp:\n\\begin{itemize}[leftmargin=0.6cm]\n\\item \\textbf{Trường hợp 1:} $1 - x = \\dfrac{2}{3} \\implies x = 1 - \\dfrac{2}{3} = \\dfrac{1}{3}$.\n\\item \\textbf{Trường hợp 2:} $1 - x = -\\dfrac{2}{3} \\implies x = 1 - \\left(-\\dfrac{2}{3}\\right) = \\dfrac{5}{3}$.\n\\end{itemize}\nVậy $x \\in \\left\\{\\dfrac{1}{3}; \\dfrac{5}{3}\\right\\}$."
        }
      ]
    },
    {
      "cau": 3,
      "noi_dung": "Cho hình vẽ, biết rằng: $\\widehat{mAx} = 40^\\circ, \\widehat{ABt} = 140^\\circ$.",
      "hinh_tikz": "\\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]\n    \\coordinate (A) at (1.8, 1.6);\n    \\coordinate (B) at (3.8, 0);\n\n    \\draw[thick, blue!80!black] (-0.5, 1.6) -- (5.8, 1.6);\n    \\draw[thick, blue!80!black] (-0.5, 0) -- (5.8, 0);\n\n    \\node[above] at (-0.3, 1.6) {$x$};\n    \\node[above] at (5.5, 1.6) {$y$};\n    \\node[above] at (-0.3, 0) {$z$};\n    \\node[above] at (5.5, 0) {$t$};\n\n    % Line mB\n    \\draw[thick, blue!80!black] ($(A)!-0.5!(B)$) -- ($(B)!-0.4!(A)$);\n\n    \\node[above right=1pt] at ($(A)!-0.5!(B)$) {$m$};\n    \\filldraw[black] (A) circle (1.2pt) node[above right=2pt] {$A$};\n    \\filldraw[black] (B) circle (1.2pt) node[below=3pt] {$B$};\n\n    % Angle mAx = 40 deg\n    \\draw[thick] (A) ++(180:0.45) arc (180:141:0.45);\n    \\node[font=\\footnotesize] at ($(A)+(-0.65, 0.35)$) {$40^\\circ$};\n\n    % Angle ABt = 140 deg\n    \\draw[thick] (B) ++(0:0.45) arc (0:141:0.45);\n    \\node[font=\\footnotesize] at ($(B)+(0.55, 0.4)$) {$140^\\circ$};\n\\end{tikzpicture}",
      "cac_y": [
        {
          "y": "a",
          "cau_hoi": "Tính số đo góc $\\widehat{mAy}$;",
          "loi_giai": "Vì $\\widehat{mAx}$ và $\\widehat{mAy}$ là hai góc kề bù nên:\n\\[ \\widehat{mAx} + \\widehat{mAy} = 180^\\circ \\implies \\widehat{mAy} = 180^\\circ - 40^\\circ = 140^\\circ. \\]"
        },
        {
          "y": "b",
          "cau_hoi": "Chứng tỏ $xy \\parallel zt$;",
          "loi_giai": "Ta có $\\widehat{mAy} = 140^\\circ$ và $\\widehat{ABt} = 140^\\circ \\implies \\widehat{mAy} = \\widehat{ABt} = 140^\\circ$.\nMà hai góc này ở vị trí đồng vị, do đó $xy \\parallel zt$."
        },
        {
          "y": "c",
          "cau_hoi": "Tia phân giác của góc $\\widehat{xAB}$ cắt đường thẳng $zt$ tại điểm $C$. Tính số đo $\\widehat{ACB}$.",
          "loi_giai": "Vì $\\widehat{mAx}$ và $\\widehat{xAB}$ là hai góc kề bù nên:\n\\[ \\widehat{xAB} = 180^\\circ - \\widehat{mAx} = 180^\\circ - 40^\\circ = 140^\\circ. \\]\nVì $AC$ là tia phân giác của $\\widehat{xAB}$ nên:\n\\[ \\widehat{xAC} = \\dfrac{\\widehat{xAB}}{2} = \\dfrac{140^\\circ}{2} = 70^\\circ. \\]\nDo $xy \\parallel zt$ (theo câu b) nên hai góc so le trong bằng nhau:\n\\[ \\widehat{ACB} = \\widehat{xAC} = 70^\\circ. \\]"
        }
      ]
    },
    {
      "cau": 4,
      "noi_dung": "Cho biểu thức $M = \\dfrac{1}{2^2} + \\dfrac{1}{3^2} + \\dfrac{1}{3^4} + \\dfrac{1}{3^6} + \\dots + \\dfrac{1}{3^{802}}$. Chứng minh rằng $M < \\dfrac{3}{8}$.",
      "hinh_tikz": None,
      "cac_y": None,
      "loi_giai": "Đặt $N = \\dfrac{1}{3^2} + \\dfrac{1}{3^4} + \\dfrac{1}{3^6} + \\dots + \\dfrac{1}{3^{802}}$, khi đó $M = \\dfrac{1}{4} + N$.\nNhân cả hai vế của $N$ với $3^2 = 9$:\n\\[ 9N = 1 + \\dfrac{1}{3^2} + \\dfrac{1}{3^4} + \\dots + \\dfrac{1}{3^{800}}. \\]\nTrừ từng vế cho $N$:\n\\[ 8N = 9N - N = 1 - \\dfrac{1}{3^{802}}. \\]\nVì $\\dfrac{1}{3^{802}} > 0$ nên $1 - \\dfrac{1}{3^{802}} < 1 \\implies 8N < 1 \\implies N < \\dfrac{1}{8}$.\nDo đó: $M = \\dfrac{1}{4} + N < \\dfrac{1}{4} + \\dfrac{1}{8} = \\dfrac{3}{8}$. (đpcm)"
    }
  ]
}

with open(r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\DE_09\de_09.json', 'w', encoding='utf-8') as f:
    json.dump(de_09, f, ensure_ascii=False, indent=2)

print('Saved de_09.json successfully!')
