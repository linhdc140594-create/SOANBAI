# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": 1,
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I - MÔN TOÁN 8 - ĐỀ SỐ 01",
    "thoi_gian": "90 phút (không kể thời gian phát đề)",
    "phan_I": [
        {
            "cau": 1,
            "de": "Biểu thức nào sau đây là đơn thức?",
            "a": "$5x^2y$",
            "b": "$2xy + 1$",
            "c": "$3x - 2$",
            "d": "$x^2 + 7$",
            "da": "A",
            "loigiai": "Đơn thức là biểu thức đại số chỉ gồm một số, một biến, hoặc một tích giữa các số và các biến. Do đó $5x^2y$ là đơn thức; các biểu thức còn lại đều là đa thức chứa phép cộng hoặc trừ."
        },
        {
            "cau": 2,
            "de": "Đơn thức đồng dạng với đơn thức $5x^3yz$ là:",
            "a": "$-30x^2yz$",
            "b": "$x^3yz$",
            "c": "$-30xyz$",
            "d": "$40x^3y^5z$",
            "da": "B",
            "loigiai": "Hai đơn thức đồng dạng là hai đơn thức có hệ số khác 0 và có cùng phần biến. Đơn thức $x^3yz$ có cùng phần biến $x^3yz$ với đơn thức đã cho."
        },
        {
            "cau": 3,
            "de": "Bậc của đa thức $A = 5x^3yz + \\dfrac{1}{2}xy - 0{,}5x^4y^2$ là:",
            "a": "3",
            "b": "4",
            "c": "5",
            "d": "6",
            "da": "D",
            "loigiai": "Ta xác định bậc của từng hạng tử trong đa thức:\n- Hạng tử $5x^3yz$ có bậc là $3 + 1 + 1 = 5$.\n- Hạng tử $\\dfrac{1}{2}xy$ có bậc là $1 + 1 = 2$.\n- Hạng tử $-0{,}5x^4y^2$ có bậc là $4 + 2 = 6$.\nBậc của đa thức là bậc của hạng tử có bậc cao nhất, tức là 6."
        },
        {
            "cau": 4,
            "de": "Cho hình chóp tam giác đều $A.BCD$ như hình vẽ bên. Đoạn thẳng nào sau đây là trung đoạn của hình chóp?",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]\n  \\coordinate (B) at (0,0);\n  \\coordinate (D) at (3.8,0.3);\n  \\coordinate (C) at (1.5,-1.2);\n  \\coordinate (A) at (1.9,2.8);\n  \\coordinate (M) at ($(B)!0.5!(C)$);\n  \\draw[thick] (A) -- (B) -- (C) -- (D) -- (A) -- (C);\n  \\draw[dashed, thick] (B) -- (D);\n  \\draw[thick, blue!80!black] (A) -- (M);\n  \\node[above] at (A) {$A$};\n  \\node[left] at (B) {$B$};\n  \\node[below] at (C) {$C$};\n  \\node[right] at (D) {$D$};\n  \\node[below left] at (M) {$M$};\n\\end{tikzpicture}\n\\end{center}",
            "a": "$AC$",
            "b": "$AM$",
            "c": "$BN$",
            "d": "$AP$",
            "da": "B",
            "loigiai": "Trung đoạn của hình chóp đều là đường cao vẽ từ đỉnh của mặt bên xuống cạnh đáy tương ứng. Trong hình vẽ, đoạn thẳng $AM$ vuông góc với cạnh đáy $BC$ tại trung điểm $M$ của $BC$, do đó $AM$ là trung đoạn của hình chóp."
        },
        {
            "cau": 5,
            "de": "Tổng các góc của một tứ giác lồi bằng:",
            "a": "$360^\\circ$",
            "b": "$180^\\circ$",
            "c": "$270^\\circ$",
            "d": "$120^\\circ$",
            "da": "A",
            "loigiai": "Theo định lý về tổng các góc trong một tứ giác, tổng số đo 4 góc của một tứ giác luôn bằng $360^\\circ$."
        },
        {
            "cau": 6,
            "de": "Giá trị của biểu thức $x^3 - 3x^2 + 3x - 1$ tại $x = 2$ là:",
            "a": "0",
            "b": "1",
            "c": "2",
            "d": "16",
            "da": "B",
            "loigiai": "Ta nhận thấy hằng đẳng thức lập phương của một hiệu:\n$$x^3 - 3x^2 + 3x - 1 = (x - 1)^3.$$\nThay $x = 2$ vào biểu thức, ta được: $(2 - 1)^3 = 1^3 = 1$."
        },
        {
            "cau": 7,
            "de": "Kết quả của phép tính $\\dfrac{a - 2}{a - b} - \\dfrac{2 - b}{b - a}$ là:",
            "a": "$-1$",
            "b": "1",
            "c": "$\\dfrac{a - b}{b - a}$",
            "d": "$\\dfrac{a + b - 4}{a - b}$",
            "da": "B",
            "loigiai": "Đổi dấu phân thức thứ hai:\n$$\\dfrac{a - 2}{a - b} - \\dfrac{2 - b}{b - a} = \\dfrac{a - 2}{a - b} + \\dfrac{2 - b}{a - b} = \\dfrac{(a - 2) + (2 - b)}{a - b} = \\dfrac{a - b}{a - b} = 1.$$"
        },
        {
            "cau": 8,
            "de": "Cho tam giác $ABC$ vuông tại $A$ có $AB = 3\\text{ cm}, AC = 4\\text{ cm}$. Độ dài cạnh $BC$ bằng:",
            "a": "$5\\text{ cm}$",
            "b": "$6\\text{ cm}$",
            "c": "$7\\text{ cm}$",
            "d": "$8\\text{ cm}$",
            "da": "A",
            "loigiai": "Áp dụng định lý Pythagoras cho tam giác $ABC$ vuông tại $A$:\n$$BC^2 = AB^2 + AC^2 = 3^2 + 4^2 = 9 + 16 = 25 \\Rightarrow BC = \\sqrt{25} = 5\\text{ cm}.$$"
        },
        {
            "cau": 9,
            "de": "Hình chữ nhật là tứ giác có:",
            "a": "4 góc vuông",
            "b": "2 góc kề một cạnh bằng nhau",
            "c": "2 góc kề một cạnh cùng bằng $90^\\circ$",
            "d": "2 góc kề một cạnh bù nhau",
            "da": "A",
            "loigiai": "Theo định nghĩa chuẩn, hình chữ nhật là tứ giác có bốn góc vuông."
        },
        {
            "cau": 10,
            "de": "Hình bình hành có hai cạnh kề bằng nhau là hình gì?",
            "a": "Hình chữ nhật",
            "b": "Hình vuông",
            "c": "Hình thoi",
            "d": "Hình thang",
            "da": "C",
            "loigiai": "Theo dấu hiệu nhận biết các tứ giác, hình bình hành có hai cạnh kề bằng nhau là hình thoi."
        },
        {
            "cau": 11,
            "de": "Cho hình thang cân $ABCD$ có $AB \\parallel CD$ và $\\widehat{A} = 125^\\circ$. Số đo của $\\widehat{C}$ là:",
            "a": "$125^\\circ$",
            "b": "$65^\\circ$",
            "c": "$90^\\circ$",
            "d": "$55^\\circ$",
            "da": "D",
            "loigiai": "Do $AB \\parallel CD$ nên $\\widehat{A} + \\widehat{D} = 180^\\circ$ (hai góc trong cùng phía bù nhau).\nSuy ra: $\\widehat{D} = 180^\\circ - 125^\\circ = 55^\\circ$.\nDo $ABCD$ là hình thang cân nên hai góc kề đáy bằng nhau: $\\widehat{C} = \\widehat{D} = 55^\\circ$."
        },
        {
            "cau": 12,
            "de": "Tìm khẳng định sai trong các khẳng định sau:",
            "a": "Hình chữ nhật có hai cạnh kề bằng nhau là hình vuông",
            "b": "Hình chữ nhật có hai đường chéo vuông góc là hình vuông",
            "c": "Hình chữ nhật có một đường chéo là đường phân giác của một góc vuông là hình vuông",
            "d": "Hình chữ nhật có bốn góc vuông là hình vuông",
            "da": "D",
            "loigiai": "Khẳng định D sai vì bản thân mọi hình chữ nhật đều có 4 góc vuông theo định nghĩa, điều này không đủ để biến nó thành hình vuông (hình vuông cần thêm điều kiện 4 cạnh bằng nhau hoặc 2 đường chéo vuông góc)."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho hai đa thức $A = 3x^2y - 2xy^2 + 5$ và $B = x^2y + xy^2 - 1$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Bậc của đa thức $A$ bằng 3.",
                "da": "D",
                "giai": "Đúng. Đa thức $A$ gồm các hạng tử có bậc lần lượt là 3, 3 và 0; do đó bậc cao nhất là 3."
            },
            "y_b": {
                "noi_dung": "Tổng của hai đa thức là $A + B = 4x^2y - xy^2 + 4$.",
                "da": "D",
                "giai": "Đúng. $A + B = (3x^2y + x^2y) + (-2xy^2 + xy^2) + (5 - 1) = 4x^2y - xy^2 + 4$."
            },
            "y_c": {
                "noi_dung": "Tại $x = 1$ và $y = -1$, giá trị của đa thức $B$ bằng 1.",
                "da": "S",
                "giai": "Sai. Thay $x = 1, y = -1$ vào $B$: $B = 1^2 \\cdot (-1) + 1 \\cdot (-1)^2 - 1 = -1 + 1 - 1 = -1 \\ne 1$."
            },
            "y_d": {
                "noi_dung": "Tích của đa thức $A$ với đơn thức $2xy$ là $6x^3y^2 - 4x^2y^3 + 10xy$.",
                "da": "D",
                "giai": "Đúng. $A \\cdot 2xy = (3x^2y - 2xy^2 + 5) \\cdot 2xy = 6x^3y^2 - 4x^2y^3 + 10xy$."
            }
        },
        {
            "cau": 2,
            "de": "Cho biểu thức $P = (x + 3)^2 - (x - 3)(x + 3)$ và đa thức $Q = x^3 - 4x$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Khai triển hằng đẳng thức $(x + 3)^2$ ta được $x^2 + 6x + 9$.",
                "da": "D",
                "giai": "Đúng. Áp dụng $(a+b)^2 = a^2 + 2ab + b^2$, ta có $(x+3)^2 = x^2 + 6x + 9$."
            },
            "y_b": {
                "noi_dung": "Kết quả rút gọn của biểu thức $P$ là $6x + 18$.",
                "da": "D",
                "giai": "Đúng. $P = (x^2 + 6x + 9) - (x^2 - 9) = x^2 + 6x + 9 - x^2 + 9 = 6x + 18$."
            },
            "y_c": {
                "noi_dung": "Phân tích đa thức $Q$ thành nhân tử ta được $x(x - 2)(x + 2)$.",
                "da": "D",
                "giai": "Đúng. $Q = x(x^2 - 4) = x(x - 2)(x + 2)$."
            },
            "y_d": {
                "noi_dung": "Tại $x = -3$, giá trị của biểu thức $P$ bằng 12.",
                "da": "S",
                "giai": "Sai. Thay $x = -3$ vào $P$: $P = 6 \\cdot (-3) + 18 = -18 + 18 = 0 \\ne 12$."
            }
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Cho hai đa thức $A = 2x^2y - 3xy + 5$ và $B = x^2y + 3xy - 2$. Tính $A + B$.",
            "da": "$3x^2y + 3$",
            "loigiai": "Thực hiện phép cộng hai đa thức:\n$$\\begin{aligned} A + B &= (2x^2y - 3xy + 5) + (x^2y + 3xy - 2) \\\\ &= (2x^2y + x^2y) + (-3xy + 3xy) + (5 - 2) \\\\ &= 3x^2y + 3. \\end{aligned}$$\nĐáp số: $3x^2y + 3$."
        },
        {
            "cau": 2,
            "de": "Rút gọn biểu thức $P = (x + 3)^2 - (x - 3)(x + 3)$.",
            "da": "$6x + 18$",
            "loigiai": "Áp dụng các hằng đẳng thức đáng nhớ:\n- $(x + 3)^2 = x^2 + 6x + 9$\n- $(x - 3)(x + 3) = x^2 - 9$\nKhi đó:\n$$P = (x^2 + 6x + 9) - (x^2 - 9) = x^2 + 6x + 9 - x^2 + 9 = 6x + 18.$$\nĐáp số: $6x + 18$."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "2,0 điểm",
            "de": "Thực hiện phép tính:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "$xy(x + y)$",
                    "loigiai": "$xy(x + y) = xy \\cdot x + xy \\cdot y = x^2y + xy^2$."
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "$(x - 2)^2 + 2x(x - 6)$",
                    "loigiai": "$\\begin{aligned}[t] (x - 2)^2 + 2x(x - 6) &= (x^2 - 4x + 4) + (2x^2 - 12x) \\\\ &= 3x^2 - 16x + 4. \\end{aligned}$"
                },
                {
                    "y": "c",
                    "diem_y": "1,0",
                    "noi_dung": "$(2x^2 - 5xy - 4y^2)x - (2x^4y - 3x^3y^2 + 4x^2y^3) : xy$",
                    "loigiai": "$\\begin{aligned}[t] &\\quad (2x^2 - 5xy - 4y^2)x - (2x^4y - 3x^3y^2 + 4x^2y^3) : xy \\\\ &= (2x^3 - 5x^2y - 4xy^2) - (2x^3 - 3x^2y + 4xy^2) \\\\ &= 2x^3 - 5x^2y - 4xy^2 - 2x^3 + 3x^2y - 4xy^2 \\\\ &= -2x^2y - 8xy^2. \\end{aligned}$"
                }
            ]
        },
        {
            "cau": 2,
            "diem": "1,5 điểm",
            "de": "Phân tích các đa thức sau thành nhân tử:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,25",
                    "noi_dung": "$4x^2 - 12x$",
                    "loigiai": "$4x^2 - 12x = 4x(x - 3)$."
                },
                {
                    "y": "b",
                    "diem_y": "0,25",
                    "noi_dung": "$x^3 - 4x^2 + 4x$",
                    "loigiai": "$x^3 - 4x^2 + 4x = x(x^2 - 4x + 4) = x(x - 2)^2$."
                },
                {
                    "y": "c",
                    "diem_y": "0,5",
                    "noi_dung": "$x^2 - y^2 - 5x - 5y$",
                    "loigiai": "$\\begin{aligned}[t] x^2 - y^2 - 5x - 5y &= (x^2 - y^2) - (5x + 5y) \\\\ &= (x - y)(x + y) - 5(x + y) \\\\ &= (x + y)(x - y - 5). \\end{aligned}$"
                },
                {
                    "y": "d",
                    "diem_y": "0,5",
                    "noi_dung": "$x^2 + 2xy + y^2 - 16$",
                    "loigiai": "$\\begin{aligned}[t] x^2 + 2xy + y^2 - 16 &= (x + y)^2 - 4^2 \\\\ &= (x + y - 4)(x + y + 4). \\end{aligned}$"
                }
            ]
        },
        {
            "cau": 3,
            "diem": "1,0 điểm",
            "de": "Cho tam giác $ABC$ vuông tại $A$ ($AB < AC$). Gọi $I$ là trung điểm của $BC$. Qua $I$ vẽ $IM \\perp AB$ tại $M$, $IN \\perp AC$ tại $N$.",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.75, baseline=(current bounding box.center)]\n  \\coordinate (A) at (0,0);\n  \\coordinate (B) at (0,3);\n  \\coordinate (C) at (4.5,0);\n  \\coordinate (I) at ($(B)!0.5!(C)$);\n  \\coordinate (M) at (0,1.5);\n  \\coordinate (N) at (2.25,0);\n  \\coordinate (D) at ($(N)!-1!(I)$);\n  \\coordinate (H) at ($(B)!(A)!(C)$);\n  \\draw[thick] (A) -- (B) -- (C) -- cycle;\n  \\draw[thick] (I) -- (M);\n  \\draw[thick] (I) -- (D);\n  \\draw[thick] (A) -- (D) -- (C);\n  \\draw[thick, dashed] (A) -- (I);\n  \\draw[thick, red!70!black] (A) -- (H);\n  \\draw[thick, blue!70!black] (M) -- (H) -- (N);\n  \\draw (0,0.25) -- (0.25,0.25) -- (0.25,0);\n  \\draw (0,1.75) -- (0.25,1.75) -- (0.25,1.5);\n  \\draw (2.25,0.25) -- (2.5,0.25) -- (2.5,0);\n  \\node[below left] at (A) {$A$};\n  \\node[above left] at (B) {$B$};\n  \\node[below right] at (C) {$C$};\n  \\node[above right] at (I) {$I$};\n  \\node[left] at (M) {$M$};\n  \\node[below] at (N) {$N$};\n  \\node[below] at (D) {$D$};\n  \\node[above right] at (H) {$H$};\n\\end{tikzpicture}\n\\end{center}",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Chứng minh rằng tứ giác $AMIN$ là hình chữ nhật.",
                    "loigiai": "Xét tứ giác $AMIN$, ta có:\n- $\\widehat{MAN} = 90^\\circ$ (do tam giác $ABC$ vuông tại $A$),\n- $\\widehat{AMI} = 90^\\circ$ (do $IM \\perp AB$),\n- $\\widehat{ANI} = 90^\\circ$ (do $IN \\perp AC$).\nTứ giác $AMIN$ có 3 góc vuông nên $AMIN$ là hình chữ nhật."
                },
                {
                    "y": "b",
                    "diem_y": "0,25",
                    "noi_dung": "Lấy điểm $D$ trên tia đối của tia $NI$ sao cho $N$ là trung điểm của $ID$. Chứng minh tứ giác $ADCI$ là hình thoi.",
                    "loigiai": "Trong tam giác $ABC$, $I$ là trung điểm $BC$ và $IN \\parallel AB$ (cùng vuông góc với $AC$), suy ra $N$ là trung điểm của $AC$.\nTứ giác $ADCI$ có hai đường chéo $AC$ và $ID$ cắt nhau tại trung điểm $N$ của mỗi đường, nên $ADCI$ là hình bình hành.\nMặt khác, $AC \\perp ID$ tại $N$ (vì $IN \\perp AC$).\nHình bình hành $ADCI$ có hai đường chéo vuông góc nên $ADCI$ là hình thoi."
                },
                {
                    "y": "c",
                    "diem_y": "0,25",
                    "noi_dung": "Kẻ $AH \\perp BC$ tại $H$. Chứng minh $MH \\perp HN$.",
                    "loigiai": "Vì $AMIN$ là hình chữ nhật nên 4 điểm $A, M, I, N$ cùng nằm trên đường tròn đường kính $AI$.\nXét tam giác $AHI$ vuông tại $H$ ($AH \\perp BC$), điểm $H$ cũng nằm trên đường tròn đường kính $AI$.\nDo đó 5 điểm $A, M, H, I, N$ cùng nằm trên đường tròn đường kính $AI$, hay cũng chính là đường tròn đường kính $MN$ (vì trong hình chữ nhật $AMIN$, $AI = MN$).\nĐiểm $H$ nhìn đoạn $MN$ dưới một góc vuông, suy ra $\\widehat{MHN} = 90^\\circ$, hay $MH \\perp HN$."
                }
            ]
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Cho các số thực $x, y$ thỏa mãn điều kiện:\n$$2x^2 + 10y^2 - 6xy - 6x - 2y + 10 = 0.$$\nTính giá trị của biểu thức $A = \\dfrac{(x + y - 4)^{2018} - y^{2018}}{x}$.",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Tính giá trị biểu thức $A$.",
                    "loigiai": "Biến đổi phương trình ban đầu thành tổng các bình phương:\n$$\\begin{aligned} &\\quad 2x^2 + 10y^2 - 6xy - 6x - 2y + 10 = 0 \\\\ &\\Leftrightarrow (x^2 - 6xy + 9y^2) + (x^2 - 6x + 9) + (y^2 - 2y + 1) = 0 \\\\ &\\Leftrightarrow (x - 3y)^2 + (x - 3)^2 + (y - 1)^2 = 0. \\end{aligned}$$\nVì $(x - 3y)^2 \\ge 0$, $(x - 3)^2 \\ge 0$, $(y - 1)^2 \\ge 0$ với mọi $x, y$.\nDo đó đẳng thức xảy ra khi và chỉ khi:\n$$\\begin{cases} x - 3y = 0 \\\\ x - 3 = 0 \\\\ y - 1 = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = 3 \\\\ y = 1. \\end{cases}$$\nThay $x = 3, y = 1$ vào biểu thức $A$, ta được:\n$$A = \\dfrac{(3 + 1 - 4)^{2018} - 1^{2018}}{3} = \\dfrac{0^{2018} - 1}{3} = -\\dfrac{1}{3}.$$\nVậy $A = -\\dfrac{1}{3}$."
                }
            ]
        }
    ]
}

out_path = r"d:\GitHub\SOANBAI-main\LOP8\DETHIGHK1\DE_01\de_01.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Ghi thanh cong de_01.json!")
