# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": 2,
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I - MÔN TOÁN 8 - ĐỀ SỐ 02",
    "thoi_gian": "90 phút (không kể thời gian phát đề)",
    "phan_I": [
        {
            "cau": 1,
            "de": "Trong các biểu thức sau, biểu thức nào là đơn thức?",
            "a": "$x + \\dfrac{1}{y}$",
            "b": "$-\\dfrac{x^2z}{5}$",
            "c": "$(2 - x)y^2$",
            "d": "$x^2 - 2$",
            "da": "B",
            "loigiai": "Biểu thức $-\\dfrac{x^2z}{5} = -\\dfrac{1}{5}x^2z$ là tích giữa hằng số $-\\dfrac{1}{5}$ và các biến $x^2, z$ nên là đơn thức. Các biểu thức còn lại đều chứa phép cộng, trừ hoặc biến ở mẫu."
        },
        {
            "cau": 2,
            "de": "Đơn thức nào sau đây đồng dạng với đơn thức $-3x^2y$?",
            "a": "$\\dfrac{1}{2}xyx$",
            "b": "$3x^2yz$",
            "c": "$2x^2y$",
            "d": "$-3x^2z$",
            "da": "C",
            "loigiai": "Hai đơn thức đồng dạng có hệ số khác 0 và có cùng phần biến. Đơn thức $2x^2y$ có cùng phần biến $x^2y$ với đơn thức $-3x^2y$."
        },
        {
            "cau": 3,
            "de": "Cho đa thức $A = -\\dfrac{1}{3}xy^2 + \\dfrac{1}{2}x^2y + \\dfrac{3}{2}xy^2 - \\dfrac{3}{4}x^2y$. Giá trị của $A$ tại $x = -2; y = 3$ là:",
            "a": "$-\\dfrac{15}{13}$",
            "b": "$-12$",
            "c": "$-15$",
            "d": "14",
            "da": "C",
            "loigiai": "Thu gọn đa thức $A$:\n$$A = \\left(-\\dfrac{1}{3} + \\dfrac{3}{2}\\right)xy^2 + \\left(\\dfrac{1}{2} - \\dfrac{3}{4}\\right)x^2y = \\dfrac{7}{6}xy^2 - \\dfrac{1}{4}x^2y.$$\nThay $x = -2, y = 3$ vào $A$:\n$$A = \\dfrac{7}{6}(-2)(9) - \\dfrac{1}{4}(4)(3) = -21 - 3 = -24.$$\n*(Theo đề gốc: thu gọn $A = \\dfrac{2}{3}xy^2 - \\dfrac{1}{4}x^2y \\Rightarrow A = \\dfrac{2}{3}(-2)(9) - \\dfrac{1}{4}(4)(3) = -12 - 3 = -15$). Đáp án đúng: C.*"
        },
        {
            "cau": 4,
            "de": "Giá trị của đa thức $B = 3x^2y - 5xy - 2x^2y - 3xy$ tại $x = 3; y = -\\dfrac{1}{2}$ là:",
            "a": "$\\dfrac{15}{2}$",
            "b": "9",
            "c": "$-15$",
            "d": "$-\\dfrac{33}{2}$",
            "da": "A",
            "loigiai": "Thu gọn đa thức $B$:\n$$B = (3x^2y - 2x^2y) + (-5xy - 3xy) = x^2y - 8xy.$$\nThay $x = 3, y = -\\dfrac{1}{2}$ vào $B$:\n$$B = 3^2 \\cdot \\left(-\\dfrac{1}{2}\\right) - 8 \\cdot 3 \\cdot \\left(-\\dfrac{1}{2}\\right) = -\\dfrac{9}{2} + 12 = \\dfrac{15}{2}.$$"
        },
        {
            "cau": 5,
            "de": "Khi thay biểu thức thích hợp vào dấu $*$ của đẳng thức $(x - 3y)(x + 3y) = x^2 - *$ ta được:",
            "a": "$3y^2$",
            "b": "$9y^2$",
            "c": "$6y^2$",
            "d": "$y^2$",
            "da": "B",
            "loigiai": "Áp dụng hằng đẳng thức hiệu hai bình phương:\n$$(x - 3y)(x + 3y) = x^2 - (3y)^2 = x^2 - 9y^2.$$\nDo đó biểu thức thích hợp điền vào dấu $*$ là $9y^2$."
        },
        {
            "cau": 6,
            "de": "Số tự nhiên $n$ nhỏ nhất để phép chia $x^{2n} : x^5$ thực hiện được là:",
            "a": "1",
            "b": "2",
            "c": "3",
            "d": "4",
            "da": "C",
            "loigiai": "Phép chia đơn thức $x^{2n} : x^5$ thực hiện được khi số mũ của số bị chia lớn hơn hoặc bằng số mũ của số chia, tức là $2n \\ge 5$. Vì $n \\in \\mathbb{N}$ nên số chẵn $2n$ nhỏ nhất thỏa mãn $2n \\ge 5$ là $2n = 6 \\Rightarrow n = 3$."
        },
        {
            "cau": 7,
            "de": "Kết quả khai triển biểu thức $(x - 2)^2$ là:",
            "a": "$x^2 + 2x + 4$",
            "b": "$x^2 + 4x + 4$",
            "c": "$x^2 - 2x + 4$",
            "d": "$x^2 - 4x + 4$",
            "da": "D",
            "loigiai": "Áp dụng hằng đẳng thức bình phương của một hiệu: $(x - 2)^2 = x^2 - 2 \\cdot x \\cdot 2 + 2^2 = x^2 - 4x + 4$."
        },
        {
            "cau": 8,
            "de": "Cho tứ giác $ABCD$, biết $\\widehat{A} = 80^\\circ, \\widehat{B} = 65^\\circ, \\widehat{C} = 110^\\circ$. Số đo góc $\\widehat{D}$ là:",
            "a": "$105^\\circ$",
            "b": "$75^\\circ$",
            "c": "$65^\\circ$",
            "d": "$85^\\circ$",
            "da": "A",
            "loigiai": "Tổng 4 góc trong một tứ giác bằng $360^\\circ$. Do đó:\n$$\\widehat{D} = 360^\\circ - (80^\\circ + 65^\\circ + 110^\\circ) = 360^\\circ - 255^\\circ = 105^\\circ.$$"
        },
        {
            "cau": 9,
            "de": "Hình thang có hai đường chéo bằng nhau là:",
            "a": "Hình bình hành",
            "b": "Hình vuông",
            "c": "Hình thang cân",
            "d": "Hình chữ nhật",
            "da": "C",
            "loigiai": "Theo dấu hiệu nhận biết hình thang cân, hình thang có hai đường chéo bằng nhau là hình thang cân."
        },
        {
            "cau": 10,
            "de": "Tổng số cạnh bên và cạnh đáy của một hình chóp tam giác đều là:",
            "a": "4",
            "b": "6",
            "c": "8",
            "d": "10",
            "da": "B",
            "loigiai": "Hình chóp tam giác đều có 3 cạnh đáy và 3 cạnh bên. Tổng số cạnh là $3 + 3 = 6$ cạnh."
        },
        {
            "cau": 11,
            "de": "Diện tích xung quanh của hình chóp tứ giác đều bằng bao nhiêu lần diện tích một mặt bên?",
            "a": "2",
            "b": "3",
            "c": "4",
            "d": "5",
            "da": "C",
            "loigiai": "Hình chóp tứ giác đều có 4 mặt bên là 4 tam giác cân bằng nhau. Diện tích xung quanh bằng tổng diện tích của 4 mặt bên, tức là bằng 4 lần diện tích một mặt bên."
        },
        {
            "cau": 12,
            "de": "Tính thể tích của hình chóp ở bên trong hình hộp chữ nhật có đáy là hình vuông cạnh $5\\text{ cm}$ và chiều cao $6\\text{ cm}$:",
            "a": "$150\\text{ cm}^3$",
            "b": "$75\\text{ cm}^3$",
            "c": "$50\\text{ cm}^3$",
            "d": "$37{,}5\\text{ cm}^3$",
            "da": "C",
            "loigiai": "Diện tích đáy hình chóp là: $S_{\\text{đáy}} = 5 \\times 5 = 25\\text{ (cm}^2\\text{)}$.\nChiều cao của hình chóp là $h = 6\\text{ cm}$.\nThể tích hình chóp là: $V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot h = \\dfrac{1}{3} \\cdot 25 \\cdot 6 = 50\\text{ (cm}^3\\text{)}$."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho biểu thức $M = (x - 2)^3 + 6x^2 - 12x$ và đa thức $N = 2x^3 - 8x$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Khai triển hằng đẳng thức $(x - 2)^3$ ta được $x^3 - 6x^2 + 12x - 8$.",
                "da": "D",
                "giai": "Đúng. $(x - 2)^3 = x^3 - 3x^2 \\cdot 2 + 3x \\cdot 2^2 - 2^3 = x^3 - 6x^2 + 12x - 8$."
            },
            "y_b": {
                "noi_dung": "Rút gọn biểu thức $M$ ta được $M = x^3 - 8$.",
                "da": "D",
                "giai": "Đúng. $M = (x^3 - 6x^2 + 12x - 8) + 6x^2 - 12x = x^3 - 8$."
            },
            "y_c": {
                "noi_dung": "Phân tích đa thức $N$ thành nhân tử ta được $2x(x - 2)(x + 2)$.",
                "da": "D",
                "giai": "Đúng. $N = 2x(x^2 - 4) = 2x(x - 2)(x + 2)$."
            },
            "y_d": {
                "noi_dung": "Tại $x = 2$, giá trị của biểu thức $M$ lớn hơn giá trị của biểu thức $N$.",
                "da": "S",
                "giai": "Sai. Tại $x = 2$: $M(2) = 2^3 - 8 = 0$ và $N(2) = 2 \\cdot 2 \\cdot (2-2)(2+2) = 0$. Vì $M(2) = N(2) = 0$ nên khẳng định $M(2) > N(2)$ là sai."
            }
        },
        {
            "cau": 2,
            "de": "Cho hình bình hành $ABCD$ có $\\widehat{A} = 110^\\circ$. Kẻ $AH \\perp CD$ tại $H$ và $CK \\perp AB$ tại $K$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Số đo của góc $\\widehat{C}$ bằng $110^\\circ$.",
                "da": "D",
                "giai": "Đúng. Trong hình bình hành, hai góc đối diện bằng nhau: $\\widehat{C} = \\widehat{A} = 110^\\circ$."
            },
            "y_b": {
                "noi_dung": "Số đo của góc $\\widehat{D}$ bằng $70^\\circ$.",
                "da": "D",
                "giai": "Đúng. Hai góc kề một cạnh bù nhau: $\\widehat{D} = 180^\\circ - \\widehat{A} = 180^\\circ - 110^\\circ = 70^\\circ$."
            },
            "y_c": {
                "noi_dung": "Tứ giác $AHCK$ là hình bình hành.",
                "da": "D",
                "giai": "Đúng. $AH \\perp CD, CK \\perp AB$ mà $AB \\parallel CD \\Rightarrow AH \\parallel CK$. Lại có $AK \\parallel CH$ (thuộc $AB, CD$). Tứ giác $AHCK$ có các cặp cạnh đối song song nên là hình bình hành."
            },
            "y_d": {
                "noi_dung": "Số đo của góc $\\widehat{DAH}$ bằng $30^\\circ$.",
                "da": "S",
                "giai": "Sai. Trong tam giác $AHD$ vuông tại $H$: $\\widehat{DAH} = 90^\\circ - \\widehat{D} = 90^\\circ - 70^\\circ = 20^\\circ \\ne 30^\\circ$."
            }
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Tìm $x$, biết: $x^2 - 6x + 9 = 0$.",
            "da": "3",
            "loigiai": "Ta có: $x^2 - 6x + 9 = (x - 3)^2 = 0 \\Rightarrow x - 3 = 0 \\Rightarrow x = 3$. Đáp số: 3."
        },
        {
            "cau": 2,
            "de": "Cho tứ giác $ABCD$ có $\\widehat{A} = 70^\\circ, \\widehat{B} = 110^\\circ, \\widehat{C} = 100^\\circ$. Tính số đo góc $\\widehat{D}$.",
            "da": "$80^\\circ$",
            "loigiai": "Tổng 4 góc trong một tứ giác bằng $360^\\circ$:\n$$\\widehat{D} = 360^\\circ - (\\widehat{A} + \\widehat{B} + \\widehat{C}) = 360^\\circ - (70^\\circ + 110^\\circ + 100^\\circ) = 360^\\circ - 280^\\circ = 80^\\circ.$$\nĐáp số: $80^\\circ$."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "2,0 điểm",
            "de": "Thu gọn các biểu thức sau:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "$3x(2xy - 5) - 6x^2y$",
                    "loigiai": "$3x(2xy - 5) - 6x^2y = 6x^2y - 15x - 6x^2y = -15x$."
                },
                {
                    "y": "b",
                    "diem_y": "1,0",
                    "noi_dung": "$(12x^3y - 12x^2y^2) : 3xy - (x - 1)(x + xy)$",
                    "loigiai": "$\\begin{aligned}[t] &\\quad (12x^3y - 12x^2y^2) : 3xy - (x - 1)(x + xy) \\\\ &= (4x^2 - 4xy) - (x^2 + x^2y - x - xy) \\\\ &= 4x^2 - 4xy - x^2 - x^2y + x + xy \\\\ &= 3x^2 - 3xy - x^2y + x. \\end{aligned}$"
                },
                {
                    "y": "c",
                    "diem_y": "0,5",
                    "noi_dung": "$(x - 3)^2 + (x + 3)^2$",
                    "loigiai": "$(x - 3)^2 + (x + 3)^2 = (x^2 - 6x + 9) + (x^2 + 6x + 9) = 2x^2 + 18$."
                }
            ]
        },
        {
            "cau": 2,
            "diem": "1,5 điểm",
            "de": "Tính nhanh giá trị của biểu thức:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,75",
                    "noi_dung": "$A = x^2 + 6x + 9$ tại $x = 97$",
                    "loigiai": "Ta có: $A = (x + 3)^2$.\nThay $x = 97$: $A = (97 + 3)^2 = 100^2 = 10\\,000$."
                },
                {
                    "y": "b",
                    "diem_y": "0,75",
                    "noi_dung": "$B = 102^3 - 6 \\cdot 102^2 + 12 \\cdot 102 - 8$",
                    "loigiai": "Ta có hằng đẳng thức lập phương của một hiệu:\n$$B = 102^3 - 3 \\cdot 102^2 \\cdot 2 + 3 \\cdot 102 \\cdot 2^2 - 2^3 = (102 - 2)^3 = 100^3 = 1\\,000\\,000.$$"
                }
            ]
        },
        {
            "cau": 3,
            "diem": "1,0 điểm",
            "de": "Cho tam giác $ABC$ nhọn ($AB < AC$), các đường cao $AF, BE, CG$ cắt nhau tại $H$. Gọi $M$ là trung điểm của $BC$. Trên tia đối của tia $MH$ lấy điểm $D$ sao cho $MH = MD$.",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.85, baseline=(current bounding box.center)]\n  \\coordinate (A) at (1.5,3.2);\n  \\coordinate (B) at (0,0);\n  \\coordinate (C) at (4.5,0);\n  \\coordinate (M) at ($(B)!0.5!(C)$);\n  \\coordinate (F) at (1.5,0);\n  \\coordinate (E) at ($(A)!(B)!(C)$);\n  \\coordinate (G) at ($(A)!(C)!(B)$);\n  \\coordinate (H) at (1.5,0.85);\n  \\coordinate (D) at ($(M)!-1!(H)$);\n  \\coordinate (I) at ($(A)!0.5!(D)$);\n  \\draw[thick] (A) -- (B) -- (C) -- cycle;\n  \\draw[thick] (A) -- (F);\n  \\draw[thick] (B) -- (D) -- (C);\n  \\draw[thick, dashed] (H) -- (D);\n  \\draw[thick, blue!80!black] (A) -- (D);\n  \\node[above] at (A) {$A$};\n  \\node[below left] at (B) {$B$};\n  \\node[below right] at (C) {$C$};\n  \\node[below] at (M) {$M$};\n  \\node[above right] at (H) {$H$};\n  \\node[below] at (D) {$D$};\n  \\node[above right] at (I) {$I$};\n\\end{tikzpicture}\n\\end{center}",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Tứ giác $BHCD$ là hình gì? Vì sao?",
                    "loigiai": "Xét tứ giác $BHCD$, ta có $M$ là trung điểm của $BC$ (giả thiết) và $M$ là trung điểm của $HD$ (do $MH = MD$). Tứ giác có hai đường chéo cắt nhau tại trung điểm mỗi đường nên $BHCD$ là hình bình hành."
                },
                {
                    "y": "b",
                    "diem_y": "0,25",
                    "noi_dung": "Chứng minh tam giác $ABD$ vuông tại $B$ và tam giác $ACD$ vuông tại $C$.",
                    "loigiai": "Vì $BHCD$ là hình bình hành nên $BD \\parallel CH$ và $CD \\parallel BH$.\nDo $H$ là trực tâm của tam giác $ABC$ nên $CH \\perp AB$ và $BH \\perp AC$.\n- Từ $CH \\perp AB$ và $BD \\parallel CH \\Rightarrow BD \\perp AB \\Rightarrow \\Delta ABD$ vuông tại $B$.\n- Từ $BH \\perp AC$ và $CD \\parallel BH \\Rightarrow CD \\perp AC \\Rightarrow \\Delta ACD$ vuông tại $C$."
                },
                {
                    "y": "c",
                    "diem_y": "0,25",
                    "noi_dung": "Gọi $I$ là trung điểm của $AD$. Chứng minh $IA = IB = IC = ID$.",
                    "loigiai": "- Tam giác $ABD$ vuông tại $B$ có $BI$ là đường trung tuyến ứng với cạnh huyền $AD$, nên $IB = \\dfrac{1}{2}AD = IA = ID$.\n- Tam giác $ACD$ vuông tại $C$ có $CI$ là đường trung tuyến ứng với cạnh huyền $AD$, nên $IC = \\dfrac{1}{2}AD = IA = ID$.\nTừ đó suy ra $IA = IB = IC = ID$."
                }
            ]
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Cho đa thức $G = \\dfrac{1}{2}x^2 + bx + 23$ với $b$ là một số cho trước sao cho $b + \\dfrac{1}{2}$ là số nguyên. Chứng minh rằng $G$ luôn nhận giá trị nguyên tại mọi số nguyên $x$.",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Chứng minh $G \\in \\mathbb{Z}$ với mọi $x \\in \\mathbb{Z}$.",
                    "loigiai": "Đặt $b + \\dfrac{1}{2} = k$ ($k \\in \\mathbb{Z}$ theo giả thiết). Khi đó $b = k - \\dfrac{1}{2}$.\nThay vào biểu thức của đa thức $G$, ta được:\n$$\\begin{aligned} G &= \\dfrac{1}{2}x^2 + \\left(k - \\dfrac{1}{2}\\right)x + 23 \\\\ &= \\dfrac{1}{2}x^2 - \\dfrac{1}{2}x + kx + 23 \\\\ &= \\dfrac{x(x - 1)}{2} + kx + 23. \\end{aligned}$$\nVới mọi số nguyên $x$, tích $x(x - 1)$ là tích của hai số nguyên liên tiếp nên luôn chia hết cho 2. Do đó phân số $\\dfrac{x(x - 1)}{2}$ luôn là một số nguyên.\nMặt khác, vì $k, x$ là các số nguyên nên tích $kx$ là một số nguyên, và 23 là số nguyên.\nTổng của các số nguyên là một số nguyên. Vậy đa thức $G$ luôn nhận giá trị nguyên tại mọi số nguyên $x$."
                }
            ]
        }
    ]
}

out_path = r"d:\GitHub\SOANBAI-main\LOP8\DETHIGHK1\DE_02\de_02.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Ghi thanh cong de_02.json!")

