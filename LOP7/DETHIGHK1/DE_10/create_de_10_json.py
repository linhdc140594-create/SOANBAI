import json

tikz_c2_p1 = r'''\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]
    \draw[thick, ->] (-3.2, 0) -- (5.4, 0);
    \foreach \x in {-2.4, -1.6, -0.8, 0, 0.8, 1.6, 2.4, 3.2, 4.0, 4.8} {
        \draw[gray!50] (\x, -0.25) -- (\x, 0.25);
        \draw[thick] (\x, 0.08) -- (\x, -0.08);
    }
    \node[above=3pt] at (-2.4, 0) {$-1$};
    \node[above=3pt] at (0, 0) {$0$};
    \node[above=3pt] at (2.4, 0) {$1$};
    \node[above=3pt] at (4.8, 0) {$2$};
    \filldraw[black] (-2.4, 0) circle (1.4pt);
    \filldraw[black] (0, 0) circle (1.4pt);
    \filldraw[black] (0.8, 0) circle (1.4pt);
    \filldraw[black] (1.6, 0) circle (1.5pt) node[below=4pt, font=\bfseries] {$A$};
    \filldraw[black] (2.4, 0) circle (1.4pt);
    \filldraw[black] (4.8, 0) circle (1.4pt);
\end{tikzpicture}'''

tikz_c3_p1 = r'''\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]
    \coordinate (B) at (0, 0);
    \coordinate (C) at (4.0, 0);
    \coordinate (A) at (1.5, 2.5);
    \coordinate (D) at (1.81, 0);
    \coordinate (E) at (2.55, 1.45);

    \draw[thick] (A) -- (B) -- (C) -- cycle;
    \draw[thick] (A) -- (D);
    \draw[thick] (B) -- (E);

    \filldraw[black] (A) circle (1.2pt) node[above=2pt] {$A$};
    \filldraw[black] (B) circle (1.2pt) node[below left=2pt] {$B$};
    \filldraw[black] (C) circle (1.2pt) node[below right=2pt] {$C$};
    \filldraw[black] (D) circle (1.2pt) node[below=2pt] {$D$};
    \filldraw[black] (E) circle (1.2pt) node[above right=2pt] {$E$};

    % Bisector arcs at A
    \draw[thick] (A) ++(-121:0.42) arc (-121:-83:0.42);
    \draw[thick] (A) ++(-83:0.42) arc (-83:-45:0.42);
    % Bisector arcs at B
    \draw[thick] (B) ++(0:0.4) arc (0:29.5:0.4);
    \draw[thick] (B) ++(0:0.48) arc (0:29.5:0.48);
    \draw[thick] (B) ++(29.5:0.4) arc (29.5:59:0.4);
    \draw[thick] (B) ++(29.5:0.48) arc (29.5:59:0.48);
\end{tikzpicture}'''

tikz_c8_p1 = r'''\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]
    \coordinate (D) at (0, 0);
    \coordinate (C) at (3.5, 0);
    \coordinate (A) at (1.2, 1.6);
    \coordinate (B) at (3.0, 1.6);
    \coordinate (x) at ($(D)!1.65!(A)$);

    \draw[thick, blue!80!black] (D) -- (C);
    \draw[thick, blue!80!black] (A) -- (B);
    \draw[thick, blue!80!black] (B) -- (C);
    \draw[thick, blue!80!black] (D) -- (x);

    \filldraw[red] (A) circle (1.2pt) node[left=2pt, black] {$A$};
    \filldraw[red] (B) circle (1.2pt) node[above right=1pt, black] {$B$};
    \filldraw[red] (C) circle (1.2pt) node[right=2pt, black] {$C$};
    \filldraw[red] (D) circle (1.2pt) node[below left=1pt, black] {$D$};
    \node[left=2pt] at (x) {$x$};

    \node[font=\footnotesize, above right=1pt] at ($(D)+(0.2, 0.05)$) {$60^\circ$};
\end{tikzpicture}'''

tikz_c2_p2 = r'''\begin{tikzpicture}[scale=0.85, line cap=round, line join=round]
    \coordinate (O) at (0, 0);
    \coordinate (x) at (-2.6, 1.2);
    \coordinate (x_prime) at (2.6, -1.2);
    \coordinate (y) at (-2.6, -0.8);
    \coordinate (y_prime) at (2.6, 0.8);

    \draw[thick, cyan!70!blue] (x) -- (x_prime);
    \draw[thick, cyan!70!blue] (y) -- (y_prime);

    \filldraw[red] (O) circle (1.5pt) node[below=3pt, black] {$O$};
    \node[above right=1pt] at (x) {$x$};
    \node[above=2pt] at (x_prime) {$x'$};
    \node[above left=1pt] at (y) {$y$};
    \node[above left=1pt] at (y_prime) {$y'$};

    % Arc for xOy
    \draw[thick] (O) ++(155.3:0.55) arc (155.3:197.1:0.55);
\end{tikzpicture}'''

data = {
    "de_so": 10,
    "tieu_de": "BỘ ĐỀ ÔN TẬP GIỮA KÌ I TOÁN 7 - ĐỀ SỐ 10",
    "thoi_gian": 90,
    "phan_I_trac_nghiem": [
        {
            "cau": 1,
            "noi_dung": "Số nào dưới đây là số thập phân vô hạn tuần hoàn?",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "$\\dfrac{1}{2}$",
                "B": "$0{,}123123$",
                "C": "$0{,}(3)$",
                "D": "$0{,}3$"
            },
            "dap_an": "C",
            "loi_giai": "Số $0{,}(3) = 0{,}333\\ldots$ là số thập phân vô hạn tuần hoàn với chu kỳ $3$."
        },
        {
            "cau": 2,
            "noi_dung": "Điểm $A$ trên trục số ở hình bên biểu diễn số hữu tỉ nào?",
            "hinh_tikz": tikz_c2_p1,
            "lua_chon": {
                "A": "$-\\dfrac{2}{3}$",
                "B": "$\\dfrac{1}{3}$",
                "C": "$\\dfrac{2}{3}$",
                "D": "$\\dfrac{4}{3}$"
            },
            "dap_an": "C",
            "loi_giai": "Đoạn đơn vị từ $0$ đến $1$ được chia thành $3$ phần bằng nhau. Điểm $A$ nằm ở vạch chia thứ hai theo chiều dương tính từ điểm gốc $0$ nên biểu diễn số hữu tỉ $\\dfrac{2}{3}$."
        },
        {
            "cau": 3,
            "noi_dung": "Đọc tên các tia phân giác trong hình vẽ sau:",
            "hinh_tikz": tikz_c3_p1,
            "lua_chon": {
                "A": "$AB, BE$ là các tia phân giác",
                "B": "$AD, BC$ là các tia phân giác",
                "C": "$AD, BE$ là các tia phân giác",
                "D": "$AD, AB$ là các tia phân giác"
            },
            "dap_an": "C",
            "loi_giai": "Ký hiệu trên hình cho thấy tia $AD$ chia góc $\\widehat{BAC}$ thành hai góc bằng nhau và tia $BE$ chia góc $\\widehat{ABC}$ thành hai góc bằng nhau. Do đó $AD, BE$ là các tia phân giác."
        },
        {
            "cau": 4,
            "noi_dung": "Hình nào dưới đây là hình lăng trụ đứng tam giác?",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "Hình có hai đáy là tam giác và ba mặt bên là hình chữ nhật",
                "B": "Hình có hai đáy là tứ giác và bốn mặt bên là hình chữ nhật",
                "C": "Hình có hai đáy là hình vuông và bốn mặt bên là hình vuông",
                "D": "Hình có một đáy là tam giác, một đỉnh chung"
            },
            "dap_an": "A",
            "loi_giai": "Theo định nghĩa, hình lăng trụ đứng tam giác có hai đáy là hình tam giác và ba mặt bên là các hình chữ nhật."
        },
        {
            "cau": 5,
            "noi_dung": "Kết quả của phép tính $\\left(-\\dfrac{2}{5}\\right)^2$ là:",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "$-\\dfrac{4}{25}$",
                "B": "$\\dfrac{4}{25}$",
                "C": "$-\\dfrac{2}{5}$",
                "D": "$\\dfrac{4}{10}$"
            },
            "dap_an": "B",
            "loi_giai": "Áp dụng quy tắc tính lũy thừa của một phân số: $\\left(-\\dfrac{2}{5}\\right)^2 = \\dfrac{(-2)^2}{5^2} = \\dfrac{4}{25}$."
        },
        {
            "cau": 6,
            "noi_dung": "Số có thể viết dưới dạng số thập phân vô hạn tuần hoàn là:",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "$\\dfrac{3}{24}$",
                "B": "$-\\dfrac{6}{25}$",
                "C": "$\\dfrac{2}{15}$",
                "D": "$\\dfrac{-5}{-8}$"
            },
            "dap_an": "C",
            "loi_giai": "Ta có $\\dfrac{3}{24} = \\dfrac{1}{8} = 0{,}125$; $-\\dfrac{6}{25} = -0{,}24$; $\\dfrac{-5}{-8} = \\dfrac{5}{8} = 0{,}625$ là các số thập phân hữu hạn. Phân số tối giản $\\dfrac{2}{15}$ có mẫu $15 = 3 \\cdot 5$ chứa thừa số nguyên tố $3 \\neq 2, 5$ nên viết được dưới dạng số thập phân vô hạn tuần hoàn."
        },
        {
            "cau": 7,
            "noi_dung": "Giá trị của $x$ thỏa mãn $|x| = 3$ là:",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "$x = 3$",
                "B": "$x = -3$",
                "C": "$x = 3$ hoặc $x = -3$",
                "D": "$x = 9$"
            },
            "dap_an": "C",
            "loi_giai": "Giá trị tuyệt đối của một số bằng $3$ khi số đó bằng $3$ hoặc bằng $-3$."
        },
        {
            "cau": 8,
            "noi_dung": "Cho hình vẽ bên, cần thêm điều kiện gì thì $AB \\parallel DC$?",
            "hinh_tikz": tikz_c8_p1,
            "lua_chon": {
                "A": "$\\widehat{BCD} = 60^\\circ$",
                "B": "$\\widehat{BCD} = 120^\\circ$",
                "C": "$\\widehat{BAD} = 60^\\circ$",
                "D": "$\\widehat{xAB} = 60^\\circ$"
            },
            "dap_an": "D",
            "loi_giai": "Hai đường thẳng $AB$ và $DC$ cùng cắt đường thẳng $Dx$. Hai góc $\\widehat{xAB}$ và $\\widehat{ADC}$ nằm ở vị trí đồng vị. Để $AB \\parallel DC$ thì hai góc đồng vị phải bằng nhau, tức là $\\widehat{xAB} = \\widehat{ADC} = 60^\\circ$."
        },
        {
            "cau": 9,
            "noi_dung": "Hãy so sánh hai số hữu tỉ $-0{,}2$ và $\\dfrac{-2}{5}$:",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "$-0{,}2 < \\dfrac{-2}{5}$",
                "B": "$-0{,}2 > \\dfrac{-2}{5}$",
                "C": "$-0{,}2 = \\dfrac{-2}{5}$",
                "D": "$-0{,}2 \\ge \\dfrac{-2}{5}$"
            },
            "dap_an": "B",
            "loi_giai": "Đổi $\\dfrac{-2}{5} = -0{,}4$. Do $-0{,}2 > -0{,}4$ nên $-0{,}2 > \\dfrac{-2}{5}$."
        },
        {
            "cau": 10,
            "noi_dung": "Căn bậc hai số học của $49$ là:",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "$-7$",
                "B": "$7$",
                "C": "$-7$ và $7$",
                "D": "$-49$"
            },
            "dap_an": "B",
            "loi_giai": "Căn bậc hai số học của $49$ là số không âm $x$ thỏa mãn $x^2 = 49$. Do $7 > 0$ và $7^2 = 49$ nên $\\sqrt{49} = 7$."
        },
        {
            "cau": 11,
            "noi_dung": "Qua một điểm $M$ nằm ngoài đường thẳng $a$, kẻ được bao nhiêu đường thẳng song song với đường thẳng $a$?",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "Có vô số đường thẳng",
                "B": "Không có đường thẳng nào",
                "C": "Có hai đường thẳng",
                "D": "Chỉ có một đường thẳng"
            },
            "dap_an": "D",
            "loi_giai": "Theo tiên đề Euclid, qua một điểm nằm ngoài một đường thẳng chỉ có một đường thẳng song song với đường thẳng đó."
        },
        {
            "cau": 12,
            "noi_dung": "Kết quả của phép tính $\\dfrac{-3}{20} + \\dfrac{-2}{15}$ là:",
            "hinh_tikz": None,
            "lua_chon": {
                "A": "$-\\dfrac{1}{35}$",
                "B": "$-\\dfrac{17}{60}$",
                "C": "$-\\dfrac{5}{35}$",
                "D": "$-\\dfrac{1}{60}$"
            },
            "dap_an": "B",
            "loi_giai": "Quy đồng mẫu số chung $60$: $\\dfrac{-3}{20} + \\dfrac{-2}{15} = \\dfrac{-9}{60} + \\dfrac{-8}{60} = -\\dfrac{17}{60}$."
        }
    ],
    "phan_II_dung_sai": [
        {
            "cau": 1,
            "noi_dung": "Cho biểu thức $A = \\left(-\\dfrac{1}{2}\\right)^3 + \\dfrac{3}{4} \\cdot \\left(-\\dfrac{2}{3}\\right) + \\left|-\\dfrac{5}{8}\\right|$. Xét tính đúng sai của các mệnh đề sau:",
            "hinh_tikz": None,
            "menh_de": [
                {
                    "y": "a",
                    "noi_dung": "Giá trị của lũy thừa $\\left(-\\dfrac{1}{2}\\right)^3$ bằng $-\\dfrac{1}{8}$.",
                    "dap_an": "Đúng",
                    "loi_giai": "Ta có $\\left(-\\dfrac{1}{2}\\right)^3 = \\left(-\\dfrac{1}{2}\\right) \\cdot \\left(-\\dfrac{1}{2}\\right) \\cdot \\left(-\\dfrac{1}{2}\\right) = -\\dfrac{1}{8}$."
                },
                {
                    "y": "b",
                    "noi_dung": "Giá trị của phép tính $\\dfrac{3}{4} \\cdot \\left(-\\dfrac{2}{3}\\right)$ bằng $-\\dfrac{1}{2}$.",
                    "dap_an": "Đúng",
                    "loi_giai": "Thực hiện phép nhân hai số hữu tỉ: $\\dfrac{3}{4} \\cdot \\left(-\\dfrac{2}{3}\\right) = \\dfrac{3 \\cdot (-2)}{4 \\cdot 3} = -\\dfrac{2}{4} = -\\dfrac{1}{2}$."
                },
                {
                    "y": "c",
                    "noi_dung": "Giá trị tuyệt đối $\\left|-\\dfrac{5}{8}\\right|$ bằng $-\\dfrac{5}{8}$.",
                    "dap_an": "Sai",
                    "loi_giai": "Giá trị tuyệt đối của một số luôn không âm, do đó $\\left|-\\dfrac{5}{8}\\right| = \\dfrac{5}{8}$."
                },
                {
                    "y": "d",
                    "noi_dung": "Giá trị của biểu thức $A$ bằng $0$.",
                    "dap_an": "Đúng",
                    "loi_giai": "Thay các giá trị vừa tính vào biểu thức $A$ ta được: $A = -\\dfrac{1}{8} + \\left(-\\dfrac{1}{2}\\right) + \\dfrac{5}{8} = -\\dfrac{1}{8} - \\dfrac{4}{8} + \\dfrac{5}{8} = \\dfrac{-1 - 4 + 5}{8} = 0$."
                }
            ]
        },
        {
            "cau": 2,
            "noi_dung": "Quan sát hình vẽ bên, hai đường thẳng $xx'$ và $yy'$ cắt nhau tại điểm $O$. Biết số đo góc $\\widehat{xOy} = 45^\\circ$. Xét tính đúng sai của các mệnh đề sau:",
            "hinh_tikz": tikz_c2_p2,
            "menh_de": [
                {
                    "y": "a",
                    "noi_dung": "Góc $\\widehat{xOy}$ và góc $\\widehat{x'Oy'}$ là hai góc đối đỉnh.",
                    "dap_an": "Đúng",
                    "loi_giai": "Tia $Ox'$ là tia đối của tia $Ox$ và tia $Oy'$ là tia đối của tia $Oy$, do đó hai góc $\\widehat{xOy}$ và $\\widehat{x'Oy'}$ nằm đối diện nhau qua đỉnh $O$ nên là hai góc đối đỉnh."
                },
                {
                    "y": "b",
                    "noi_dung": "Số đo của góc $\\widehat{x'Oy'}$ bằng $45^\\circ$.",
                    "dap_an": "Đúng",
                    "loi_giai": "Hai góc đối đỉnh thì bằng nhau, suy ra $\\widehat{x'Oy'} = \\widehat{xOy} = 45^\\circ$."
                },
                {
                    "y": "c",
                    "noi_dung": "Góc $\\widehat{xOy'}$ kề bù với góc $\\widehat{xOy}$ và có số đo bằng $135^\\circ$.",
                    "dap_an": "Đúng",
                    "loi_giai": "Hai góc $\\widehat{xOy'}$ và $\\widehat{xOy}$ có chung cạnh $Ox$ và hai cạnh $Oy, Oy'$ là hai tia đối nhau nên là hai góc kề bù. Số đo góc $\\widehat{xOy'} = 180^\\circ - \\widehat{xOy} = 180^\\circ - 45^\\circ = 135^\\circ$."
                },
                {
                    "y": "d",
                    "noi_dung": "Tổng số đo của hai góc đối đỉnh $\\widehat{xOy}$ và $\\widehat{x'Oy'}$ bằng $180^\\circ$.",
                    "dap_an": "Sai",
                    "loi_giai": "Tổng số đo của hai góc đối đỉnh này là $\\widehat{xOy} + \\widehat{x'Oy'} = 45^\\circ + 45^\\circ = 90^\\circ \\neq 180^\\circ$."
                }
            ]
        }
    ],
    "phan_III_tra_loi_ngan": [
        {
            "cau": 1,
            "noi_dung": "Tìm số hữu tỉ $x$, biết: $\\left(x - \\dfrac{3}{4}\\right)^2 = \\dfrac{1}{16}$.",
            "dap_an": "$x = 1$ hoặc $x = \\dfrac{1}{2}$",
            "loi_giai": "Vì $\\left(\\dfrac{1}{4}\\right)^2 = \\dfrac{1}{16}$ và $\\left(-\\dfrac{1}{4}\\right)^2 = \\dfrac{1}{16}$ nên ta có hai trường hợp:\n\\begin{itemize}\n    \\item Trường hợp 1: $x - \\dfrac{3}{4} = \\dfrac{1}{4} \\implies x = \\dfrac{1}{4} + \\dfrac{3}{4} = 1$.\n    \\item Trường hợp 2: $x - \\dfrac{3}{4} = -\\dfrac{1}{4} \\implies x = -\\dfrac{1}{4} + \\dfrac{3}{4} = \\dfrac{2}{4} = \\dfrac{1}{2}$.\n\\end{itemize}\nVậy $x = 1$ hoặc $x = \\dfrac{1}{2}$."
        },
        {
            "cau": 2,
            "noi_dung": "Cho góc $\\widehat{mOn} = 140^\\circ$, tia $Ot$ là tia phân giác của $\\widehat{mOn}$. Tính số đo góc kề bù với góc $\\widehat{mOt}$.",
            "dap_an": "$110^\\circ$",
            "loi_giai": "Vì $Ot$ là tia phân giác của góc $\\widehat{mOn}$ nên:\n\\[ \\widehat{mOt} = \\dfrac{\\widehat{mOn}}{2} = \\dfrac{140^\\circ}{2} = 70^\\circ. \\]\nGóc kề bù với góc $\\widehat{mOt}$ có số đo là: $180^\\circ - 70^\\circ = 110^\\circ$."
        }
    ],
    "phan_IV_tu_luan": [
        {
            "cau": 1,
            "diem": "1,5 điểm",
            "noi_dung": "Thực hiện phép tính:",
            "hinh_tikz": None,
            "cac_y": [
                {
                    "y": "a",
                    "cau_hoi": "$\\dfrac{5}{12} + \\left(-\\dfrac{7}{24}\\right) : \\dfrac{3}{8}$;",
                    "loi_giai": "$\\dfrac{5}{12} + \\left(-\\dfrac{7}{24}\\right) : \\dfrac{3}{8} = \\dfrac{5}{12} + \\left(-\\dfrac{7}{24}\\right) \\cdot \\dfrac{8}{3} = \\dfrac{5}{12} + \\left(-\\dfrac{7}{9}\\right) = \\dfrac{15}{36} - \\dfrac{28}{36} = -\\dfrac{13}{36}$."
                },
                {
                    "y": "b",
                    "cau_hoi": "$\\dfrac{4}{5} \\cdot \\dfrac{3}{7} - \\dfrac{-4}{7} : \\sqrt{\\dfrac{25}{16}} - |-1|$.",
                    "loi_giai": "$\\dfrac{4}{5} \\cdot \\dfrac{3}{7} - \\dfrac{-4}{7} : \\sqrt{\\dfrac{25}{16}} - |-1| = \\dfrac{12}{35} - \\dfrac{-4}{7} : \\dfrac{5}{4} - 1 = \\dfrac{12}{35} - \\dfrac{-4}{7} \\cdot \\dfrac{4}{5} - 1 = \\dfrac{12}{35} - \\left(-\\dfrac{16}{35}\\right) - 1 = \\dfrac{12}{35} + \\dfrac{16}{35} - 1 = \\dfrac{28}{35} - 1 = \\dfrac{4}{5} - 1 = -\\dfrac{1}{5}$."
                }
            ]
        },
        {
            "cau": 2,
            "diem": "1,5 điểm",
            "noi_dung": "Tìm $x$ biết:",
            "hinh_tikz": None,
            "cac_y": [
                {
                    "y": "a",
                    "cau_hoi": "$2x - \\dfrac{1}{3} = \\dfrac{5}{3}$;",
                    "loi_giai": "$2x - \\dfrac{1}{3} = \\dfrac{5}{3} \\implies 2x = \\dfrac{5}{3} + \\dfrac{1}{3} = \\dfrac{6}{3} = 2 \\implies x = 2 : 2 = 1$. Vậy $x = 1$."
                },
                {
                    "y": "b",
                    "cau_hoi": "$(2x + 3)^2 = 25$.",
                    "loi_giai": "$(2x + 3)^2 = 25$. Vì $5^2 = 25$ và $(-5)^2 = 25$ nên ta có hai trường hợp:\n\\begin{itemize}\n    \\item TH 1: $2x + 3 = 5 \\implies 2x = 2 \\implies x = 1$.\n    \\item TH 2: $2x + 3 = -5 \\implies 2x = -8 \\implies x = -4$.\n\\end{itemize}\nVậy $x = 1$ hoặc $x = -4$."
                }
            ]
        },
        {
            "cau": 3,
            "diem": "1,5 điểm",
            "noi_dung": "Một hồ bơi dạng hình hộp chữ nhật có kích thước là chiều dài $12\\text{ m}$, chiều rộng $5\\text{ m}$ và chiều sâu $3\\text{ m}$.",
            "hinh_tikz": None,
            "cac_y": [
                {
                    "y": "a",
                    "cau_hoi": "Tính thể tích nước khi bể bơi đầy nước.",
                    "loi_giai": "Thể tích nước khi bể bơi đầy nước là:\n\\[ V = 12 \\cdot 5 \\cdot 3 = 180\\text{ (m}^3\\text{)}. \\]"
                },
                {
                    "y": "b",
                    "cau_hoi": "Người ta cần lát gạch bên trong lòng hồ (mặt đáy và bốn mặt xung quanh). Biết gạch hình vuông có cạnh $50\\text{ cm}$. Hỏi cần mua ít nhất bao nhiêu viên gạch để lát bên trong lòng hồ bơi? (Coi diện tích mạch vữa lát không đáng kể).",
                    "loi_giai": "Diện tích xung quanh bên trong lòng hồ là:\n\\[ S_{xq} = 2 \\cdot (12 + 5) \\cdot 3 = 102\\text{ (m}^2\\text{)}. \\]\nDiện tích đáy hồ là:\n\\[ S_{\\text{đáy}} = 12 \\cdot 5 = 60\\text{ (m}^2\\text{)}. \\]\nTổng diện tích cần lát gạch là:\n\\[ S = S_{xq} + S_{\\text{đáy}} = 102 + 60 = 162\\text{ (m}^2\\text{)}. \\]\nĐổi $50\\text{ cm} = 0{,}5\\text{ m}$. Diện tích của một viên gạch là:\n\\[ S_{\\text{gạch}} = 0{,}5 \\cdot 0{,}5 = 0{,}25\\text{ (m}^2\\text{)}. \\]\nSố viên gạch ít nhất cần dùng là:\n\\[ 162 : 0{,}25 = 648\\text{ (viên)}. \\]"
                }
            ]
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "noi_dung": "Cho $A = \\dfrac{1}{2^2} + \\dfrac{1}{3^2} + \\dfrac{1}{3^4} + \\dfrac{1}{3^6} + \\ldots + \\dfrac{1}{3^{100}}$. Chứng minh rằng $A < \\dfrac{3}{8}$.",
            "hinh_tikz": None,
            "cac_y": None,
            "loi_giai": "Ta tách biểu thức $A = \\dfrac{1}{4} + B$, trong đó:\n\\[ B = \\dfrac{1}{3^2} + \\dfrac{1}{3^4} + \\dfrac{1}{3^6} + \\ldots + \\dfrac{1}{3^{100}}. \\]\nNhân cả hai vế của $B$ với $3^2 = 9$:\n\\[ 9B = 9 \\cdot \\left(\\dfrac{1}{3^2} + \\dfrac{1}{3^4} + \\ldots + \\dfrac{1}{3^{100}}\\right) = 1 + \\dfrac{1}{3^2} + \\dfrac{1}{3^4} + \\ldots + \\dfrac{1}{3^{98}}. \\]\nTrừ từng vế $9B$ cho $B$:\n\\[ 9B - B = \\left(1 + \\dfrac{1}{3^2} + \\ldots + \\dfrac{1}{3^{98}}\\right) - \\left(\\dfrac{1}{3^2} + \\dfrac{1}{3^4} + \\ldots + \\dfrac{1}{3^{100}}\\right) \\]\n\\[ 8B = 1 - \\dfrac{1}{3^{100}}. \\]\nVì $\\dfrac{1}{3^{100}} > 0$ nên $1 - \\dfrac{1}{3^{100}} < 1$. Do đó $8B < 1 \\implies B < \\dfrac{1}{8}$.\n\nThay $B < \\dfrac{1}{8}$ vào biểu thức $A$:\n\\[ A = \\dfrac{1}{4} + B < \\dfrac{1}{4} + \\dfrac{1}{8} = \\dfrac{2}{8} + \\dfrac{1}{8} = \\dfrac{3}{8}. \\]\nVậy $A < \\dfrac{3}{8}$."
        }
    ]
}

with open("de_10.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved de_10.json with standard schema!")
