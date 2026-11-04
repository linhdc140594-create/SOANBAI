# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": 8,
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I - MÔN TOÁN 8 - ĐỀ SỐ 08",
    "thoi_gian": "90 phút (không kể thời gian phát đề)",
    "phan_I": [
        {
            "cau": 1,
            "de": "Giá trị của biểu thức $A = x^2 + 2y - 1$ tại $x = 1$ và $y = -1$ là:",
            "a": "$-1$",
            "b": "$-2$",
            "c": "$1$",
            "d": "$2$",
            "da": "B",
            "loigiai": "Thay $x = 1$ và $y = -1$ vào biểu thức $A$: $A = 1^2 + 2(-1) - 1 = 1 - 2 - 1 = -2$."
        },
        {
            "cau": 2,
            "de": "Trong các đơn thức sau, đơn thức nào đồng dạng với đơn thức $5x^2y$?",
            "a": "$5xy$",
            "b": "$4xy^2$",
            "c": "$7a^2b$",
            "d": "$-3x^2y$",
            "da": "D",
            "loigiai": "Hai đơn thức đồng dạng có hệ số khác 0 và có cùng phần biến. Đơn thức $-3x^2y$ có phần biến là $x^2y$, trùng với phần biến của $5x^2y$."
        },
        {
            "cau": 3,
            "de": "Kết quả của phép nhân $(a + 2)(a - 2)$ bằng:",
            "a": "$a^2 + 4$",
            "b": "$a^2 - 4$",
            "c": "$a^2 - 2$",
            "d": "$a^2 - 1$",
            "da": "B",
            "loigiai": "Áp dụng hằng đẳng thức hiệu hai bình phương: $(a + 2)(a - 2) = a^2 - 2^2 = a^2 - 4$."
        },
        {
            "cau": 4,
            "de": "Giá trị của đa thức $-x^3y^2 + 2x$ tại $x = -1; y = 0$ là:",
            "a": "$2$",
            "b": "$-2$",
            "c": "$-1$",
            "d": "$1$",
            "da": "B",
            "loigiai": "Thay $x = -1$ và $y = 0$ vào đa thức: $-(-1)^3 \\cdot 0^2 + 2(-1) = 0 - 2 = -2$."
        },
        {
            "cau": 5,
            "de": "Biểu thức $(2x - y)^2$ có biểu thức khai triển là:",
            "a": "$x^2 + 2xy + 2y^2$",
            "b": "$x^2 - 2xy + 2y^2$",
            "c": "$x^2 + 4xy + 4y^2$",
            "d": "$4x^2 - 4xy + y^2$",
            "da": "D",
            "loigiai": "Áp dụng hằng đẳng thức bình phương của một hiệu: $(2x - y)^2 = (2x)^2 - 2 \\cdot 2x \\cdot y + y^2 = 4x^2 - 4xy + y^2$."
        },
        {
            "cau": 6,
            "de": "Đơn thức nào sau đây đồng dạng với đơn thức $-3x^2y$?",
            "a": "$\\dfrac{1}{2}xy$",
            "b": "$3x^2yz$",
            "c": "$-2x^2y$",
            "d": "$-3x^2z$",
            "da": "C",
            "loigiai": "Đơn thức $-2x^2y$ có cùng phần biến $x^2y$ với đơn thức $-3x^2y$ nên đồng dạng."
        },
        {
            "cau": 7,
            "de": "Tích $(2x - 3)(2x + 3)$ có kết quả bằng:",
            "a": "$4x^2 + 12x + 9$",
            "b": "$4x^2 - 9$",
            "c": "$2x - 3$",
            "d": "$4x - 9$",
            "da": "B",
            "loigiai": "Áp dụng hằng đẳng thức hiệu hai bình phương: $(2x - 3)(2x + 3) = (2x)^2 - 3^2 = 4x^2 - 9$."
        },
        {
            "cau": 8,
            "de": "Các góc của một tứ giác có thể là:",
            "a": "Bốn góc nhọn",
            "b": "Bốn góc tù",
            "c": "Bốn góc vuông",
            "d": "Một góc vuông, ba góc nhọn",
            "da": "C",
            "loigiai": "Tổng bốn góc của tứ giác luôn bằng $360^\\circ$. Nếu tứ giác có 4 góc vuông thì tổng số đo là $90^\\circ \\cdot 4 = 360^\\circ$ (thỏa mãn)."
        },
        {
            "cau": 9,
            "de": "Hình chữ nhật có hai đường chéo như thế nào?",
            "a": "Bằng nhau và cắt nhau tại trung điểm mỗi đường",
            "b": "Bằng nhau",
            "c": "Cắt nhau tại trung điểm mỗi đường",
            "d": "Vuông góc với nhau",
            "da": "A",
            "loigiai": "Theo tính chất hình chữ nhật, hai đường chéo bằng nhau và cắt nhau tại trung điểm của mỗi đường."
        },
        {
            "cau": 10,
            "de": "Cho tam giác $ABC$ vuông tại $A$ như hình vẽ bên. Tính $x$:",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.18, >=stealth]\n  \\coordinate (A) at (0,0);\n  \\coordinate (C) at (24,0);\n  \\coordinate (B) at (0,10);\n  \\draw[thick] (A)--(C)--(B)--cycle;\n  \\draw (1.5,0) |- (0,1.5);\n  \\fill (A) circle (1.5pt) node[below left] {$A$};\n  \\fill (B) circle (1.5pt) node[above left] {$B$};\n  \\fill (C) circle (1.5pt) node[below right] {$C$};\n  \\node[left] at ($(A)!0.5!(B)$) {$x$};\n  \\node[below] at ($(A)!0.5!(C)$) {$24\\text{ cm}$};\n  \\node[above right] at ($(B)!0.5!(C)$) {$26\\text{ cm}$};\n\\end{tikzpicture}\n\\end{center}",
            "a": "$x = 13\\text{ cm}$",
            "b": "$x = 10\\text{ cm}$",
            "c": "$x = 20\\text{ cm}$",
            "d": "$x = 2\\text{ cm}$",
            "da": "B",
            "loigiai": "Áp dụng định lý Pythagore trong tam giác vuông $ABC$: $AB^2 + AC^2 = BC^2 \\Rightarrow x^2 + 24^2 = 26^2 \\Rightarrow x^2 = 676 - 576 = 100 \\Rightarrow x = 10\\text{ cm}$."
        },
        {
            "cau": 11,
            "de": "Tam giác nào là tam giác vuông trong các tam giác có độ dài ba cạnh sau?",
            "a": "$10\\text{ m}; 13\\text{ m}; 15\\text{ m}$",
            "b": "$7\\text{ mm}; 8\\text{ mm}; 10\\text{ mm}$",
            "c": "$6\\text{ dm}; 7\\text{ dm}; 9\\text{ dm}$",
            "d": "$9\\text{ cm}; 12\\text{ cm}; 15\\text{ cm}$",
            "da": "D",
            "loigiai": "Ta có: $15^2 = 225$ và $9^2 + 12^2 = 81 + 144 = 225$. Vì $9^2 + 12^2 = 15^2$ nên theo định lý Pythagore đảo, đây là tam giác vuông."
        },
        {
            "cau": 12,
            "de": "Cho hình chóp tứ giác đều có cạnh đáy bằng $10\\text{ cm}$, chiều cao bằng $9\\text{ cm}$. Thể tích của hình chóp tứ giác đều là:",
            "a": "$30\\text{ cm}^3$",
            "b": "$45\\text{ cm}^3$",
            "c": "$300\\text{ cm}^3$",
            "d": "$450\\text{ cm}^3$",
            "da": "C",
            "loigiai": "Diện tích đáy: $S = 10 \\cdot 10 = 100\\text{ cm}^2$. Thể tích: $V = \\dfrac{1}{3} S \\cdot h = \\dfrac{1}{3} \\cdot 100 \\cdot 9 = 300\\text{ cm}^3$."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho hai biểu thức $A = (x - 2)^2 - (x - 1)(x + 3)$ và $B = x^3 - 6x^2y + 12xy^2 - 8y^3$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Khai triển hằng đẳng thức $(x - 2)^2$ ta được $x^2 - 4x + 4$.",
                "da": "D",
                "giai": "\\textbf{Đúng.} Áp dụng hằng đẳng thức bình phương của một hiệu: $(x - 2)^2 = x^2 - 4x + 4$."
            },
            "y_b": {
                "noi_dung": "Kết quả rút gọn của biểu thức $A$ là $-6x + 7$.",
                "da": "D",
                "giai": "\\textbf{Đúng.} $A = (x^2 - 4x + 4) - (x^2 + 2x - 3) = -6x + 7$."
            },
            "y_c": {
                "noi_dung": "Viết đa thức $B$ dưới dạng lập phương của một hiệu ta được $(x - 2y)^3$.",
                "da": "D",
                "giai": "\\textbf{Đúng.} $B = x^3 - 3 \\cdot x^2 \\cdot (2y) + 3 \\cdot x \\cdot (2y)^2 - (2y)^3 = (x - 2y)^3$."
            },
            "y_d": {
                "noi_dung": "Tại $x = 1$, giá trị của biểu thức $A$ bằng $-1$.",
                "da": "S",
                "giai": "\\textbf{Sai.} Thay $x = 1$ vào $A$: $A = -6(1) + 7 = 1 \\neq -1$."
            }
        },
        {
            "cau": 2,
            "de": "Cho hình chữ nhật $ABCD$ có $AB = 2AD$. Gọi $M$ là trung điểm của cạnh $AB$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Hai đường chéo $AC$ và $BD$ có độ dài bằng nhau.",
                "da": "D",
                "giai": "\\textbf{Đúng.} Theo tính chất hình chữ nhật, hai đường chéo bằng nhau ($AC = BD$)."
            },
            "y_b": {
                "noi_dung": "Tam giác $ADM$ là tam giác vuông cân tại $A$.",
                "da": "D",
                "giai": "\\textbf{Đúng.} Tam giác $ADM$ vuông tại $A$ và có $AM = \\dfrac{1}{2}AB = AD$ nên vuông cân tại $A$."
            },
            "y_c": {
                "noi_dung": "Số đo góc $\\widehat{AMD}$ bằng $60^\\circ$.",
                "da": "S",
                "giai": "\\textbf{Sai.} Vì $\\Delta ADM$ vuông cân tại $A$ nên $\\widehat{AMD} = 45^\\circ \\neq 60^\\circ$."
            },
            "y_d": {
                "noi_dung": "Hai đường thẳng $DM$ và $MC$ vuông góc với nhau.",
                "da": "D",
                "giai": "\\textbf{Đúng.} Tương tự, $\\Delta BCM$ vuông cân tại $B$ nên $\\widehat{BMC} = 45^\\circ$. Suy ra $\\widehat{DMC} = 180^\\circ - 45^\\circ - 45^\\circ = 90^\\circ$, tức là $DM \\perp MC$."
            }
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Tìm $x$, biết: $x^2 - 16 - 2(x + 4) = 0$.",
            "da": "$x = -4$ hoặc $x = 6$",
            "loigiai": "Phân tích vế trái thành nhân tử:\n\n$(x - 4)(x + 4) - 2(x + 4) = 0 \\Leftrightarrow (x + 4)(x - 4 - 2) = 0 \\Leftrightarrow (x + 4)(x - 6) = 0$.\n\n- Trường hợp 1: $x + 4 = 0 \\Leftrightarrow x = -4$.\n\n- Trường hợp 2: $x - 6 = 0 \\Leftrightarrow x = 6$.\n\nVậy $x = -4$ hoặc $x = 6$."
        },
        {
            "cau": 2,
            "de": "Cho hình thoi $ABCD$ có $\\widehat{A} = 60^\\circ$ và độ dài cạnh $AB = 5\\text{ cm}$. Tính độ dài đường chéo $BD$.",
            "da": "$5\\text{ cm}$",
            "loigiai": "Trong hình thoi $ABCD$, hai cạnh kề bằng nhau: $AB = AD = 5\\text{ cm}$. Tam giác $ABD$ cân tại $A$ có $\\widehat{A} = 60^\\circ$ nên là tam giác đều. Do đó: $BD = AB = 5\\text{ cm}$."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "1,0 điểm",
            "de": "Rút gọn các biểu thức sau:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "$2x(x^2 + y) - x(2y + 1) - x(2x^2 - 21y)$",
                    "loigiai": "$2x(x^2 + y) - x(2y + 1) - x(2x^2 - 21y) = 2x^3 + 2xy - 2xy - x - 2x^3 + 21xy = 21xy - x$."
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "$5x(6y - x^2) + 3y(y - 10x) - 3y(y - 1) + 15x^3$",
                    "loigiai": "$5x(6y - x^2) + 3y(y - 10x) - 3y(y - 1) + 15x^3 = 30xy - 5x^3 + 3y^2 - 30xy - 3y^2 + 3y + 15x^3 = 10x^3 + 3y$."
                }
            ]
        },
        {
            "cau": 2,
            "diem": "0,75 điểm",
            "de": "Tìm $x$, biết:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,35",
                    "noi_dung": "$x(x - 2) - x^2 + 6 = 0$",
                    "loigiai": "$x(x - 2) - x^2 + 6 = 0 \\Leftrightarrow x^2 - 2x - x^2 + 6 = 0 \\Leftrightarrow -2x = -6 \\Leftrightarrow x = 3$."
                },
                {
                    "y": "b",
                    "diem_y": "0,4",
                    "noi_dung": "$(x + 3)^2 - (x - 1)(x + 1) = 16$",
                    "loigiai": "$(x + 3)^2 - (x - 1)(x + 1) = 16 \\Leftrightarrow (x^2 + 6x + 9) - (x^2 - 1) = 16 \\Leftrightarrow 6x + 10 = 16 \\Leftrightarrow 6x = 6 \\Leftrightarrow x = 1$."
                }
            ]
        },
        {
            "cau": 3,
            "diem": "0,75 điểm",
            "de": "Cho tam giác $ABC$, trung tuyến $AM$. Qua $M$ kẻ đường thẳng song song với $AC$ cắt $AB$ ở $E$, qua $M$ kẻ đường thẳng song song với $AB$ cắt $AC$ ở $F$.",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.9, >=stealth]\n  \\coordinate (A) at (1.5,3);\n  \\coordinate (B) at (0,0);\n  \\coordinate (C) at (5,0);\n  \\coordinate (M) at ($(B)!0.5!(C)$);\n  \\coordinate (E) at ($(A)!0.5!(B)$);\n  \\coordinate (F) at ($(A)!0.5!(C)$);\n  \\draw[thick] (A)--(B)--(C)--cycle;\n  \\draw[thick] (A)--(M);\n  \\draw[thick, blue] (M)--(E);\n  \\draw[thick, blue] (M)--(F);\n  \\fill (A) circle (1.5pt) node[above] {$A$};\n  \\fill (B) circle (1.5pt) node[left] {$B$};\n  \\fill (C) circle (1.5pt) node[right] {$C$};\n  \\fill (M) circle (1.5pt) node[below] {$M$};\n  \\fill (E) circle (1.5pt) node[above left] {$E$};\n  \\fill (F) circle (1.5pt) node[above right] {$F$};\n\\end{tikzpicture}\n\\end{center}",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,4",
                    "noi_dung": "Chứng minh tứ giác $AEMF$ là hình bình hành.",
                    "loigiai": "Ta có $ME \\parallel AC$ nên $ME \\parallel AF$ (do $F \\in AC$), và $MF \\parallel AB$ nên $MF \\parallel AE$ (do $E \\in AB$). Tứ giác $AEMF$ có các cặp cạnh đối song song nên là hình bình hành."
                },
                {
                    "y": "b",
                    "diem_y": "0,35",
                    "noi_dung": "Nếu $\\widehat{BAC} = 90^\\circ$, chứng minh tứ giác $AEMF$ là hình chữ nhật. Từ đó suy ra $EF = \\dfrac{1}{2}BC$.",
                    "loigiai": "Hình bình hành $AEMF$ có một góc vuông ($\\widehat{EAF} = \\widehat{BAC} = 90^\\circ$) nên là hình chữ nhật. Do đó hai đường chéo bằng nhau: $EF = AM$. Trong tam giác vuông $ABC$ vuông tại $A$, trung tuyến $AM = \\dfrac{1}{2}BC$, suy ra $EF = \\dfrac{1}{2}BC$."
                }
            ]
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Chứng minh rằng giá trị biểu thức sau không phụ thuộc vào giá trị của biến $x$:\n$$A = (x + 2)^3 - (x - 2)^3 - 12(x + 1)(x - 1)$$",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Chứng minh giá trị của $A$ không phụ thuộc vào $x$.",
                    "loigiai": "Khai triển biểu thức $A$:\n\n$A = (x^3 + 6x^2 + 12x + 8) - (x^3 - 6x^2 + 12x - 8) - 12(x^2 - 1)$\n\n$= x^3 + 6x^2 + 12x + 8 - x^3 + 6x^2 - 12x + 8 - 12x^2 + 12$\n\n$= (x^3 - x^3) + (6x^2 + 6x^2 - 12x^2) + (12x - 12x) + (8 + 8 + 12) = 28$.\n\nVì $A = 28$ là một hằng số nên giá trị của biểu thức $A$ không phụ thuộc vào giá trị của biến $x$."
                }
            ]
        }
    ]
}

work_dir = r'd:\GitHub\SOANBAI-main\LOP8\DETHIGHK1\DE_08'
json_path = os.path.join(work_dir, 'de_08.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Đã tạo thành công de_08.json!")

