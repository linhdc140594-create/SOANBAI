# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": 3,
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I - MÔN TOÁN 8 - ĐỀ SỐ 03",
    "thoi_gian": "90 phút (không kể thời gian phát đề)",
    "phan_I": [
        {
            "cau": 1,
            "de": "Biểu thức nào sau đây là đơn thức?",
            "a": "$x^3(1 + x)$",
            "b": "$3xy^2z^5$",
            "c": "$(xy + z)t$",
            "d": "$\\dfrac{2}{x} + y$",
            "da": "B",
            "loigiai": "Đơn thức là biểu thức đại số chỉ gồm một số, hoặc một biến, hoặc một tích giữa các số và các biến. Biểu thức $3xy^2z^5$ là đơn thức."
        },
        {
            "cau": 2,
            "de": "Cặp đơn thức nào sau đây là đồng dạng với nhau?",
            "a": "$\\dfrac{1}{2}x^2y$ và $2xy^2$",
            "b": "$3xy$ và $-5x$",
            "c": "$x^2y^4$ và $2x^2y^4$",
            "d": "$-3xy$ và $-3xy^2$",
            "da": "C",
            "loigiai": "Hai đơn thức đồng dạng có hệ số khác 0 và có cùng phần biến. Cặp đơn thức $x^2y^4$ và $2x^2y^4$ có cùng phần biến $x^2y^4$."
        },
        {
            "cau": 3,
            "de": "Thực hiện phép chia đơn thức $5x^2y^2z$ cho $5xyz$ ta được kết quả là:",
            "a": "$5xy$",
            "b": "$xy$",
            "c": "$yz$",
            "d": "$25x^3y^3z^2$",
            "da": "B",
            "loigiai": "Ta có: $5x^2y^2z : 5xyz = (5 : 5)(x^2 : x)(y^2 : y)(z : z) = xy$."
        },
        {
            "cau": 4,
            "de": "Hằng đẳng thức $A^2 - B^2 = (A - B)(A + B)$ có tên là:",
            "a": "Bình phương của một tổng",
            "b": "Bình phương của một hiệu",
            "c": "Tổng hai bình phương",
            "d": "Hiệu hai bình phương",
            "da": "D",
            "loigiai": "Công thức $A^2 - B^2 = (A - B)(A + B)$ là hằng đẳng thức hiệu hai bình phương."
        },
        {
            "cau": 5,
            "de": "Tứ giác nào dưới đây là hình thoi?",
            "a": "Tứ giác có 4 cạnh bằng nhau",
            "b": "Tứ giác có hai đường chéo vuông góc",
            "c": "Hình bình hành có hai đường chéo bằng nhau",
            "d": "Tứ giác có hai đường chéo cắt nhau tại trung điểm mỗi đường",
            "da": "A",
            "loigiai": "Theo định nghĩa, hình thoi là tứ giác có 4 cạnh bằng nhau."
        },
        {
            "cau": 6,
            "de": "Hai đường chéo của hình chữ nhật có tính chất nào sau đây?",
            "a": "Chúng vuông góc với nhau",
            "b": "Chúng bằng nhau",
            "c": "Chúng cắt nhau tại trung điểm của mỗi đường",
            "d": "Chúng bằng nhau và cắt nhau tại trung điểm của mỗi đường",
            "da": "D",
            "loigiai": "Trong hình chữ nhật, hai đường chéo bằng nhau và cắt nhau tại trung điểm của mỗi đường."
        },
        {
            "cau": 7,
            "de": "Hình bình hành $ABCD$ có $\\widehat{A} = 65^\\circ$. Số đo góc $\\widehat{C}$ là:",
            "a": "$125^\\circ$",
            "b": "$95^\\circ$",
            "c": "$115^\\circ$",
            "d": "$65^\\circ$",
            "da": "D",
            "loigiai": "Trong hình bình hành, hai góc đối diện bằng nhau nên $\\widehat{C} = \\widehat{A} = 65^\\circ$."
        },
        {
            "cau": 8,
            "de": "Cho tam giác $ABC$ vuông tại $A$ có $M$ là trung điểm của $BC$, biết $BC = 10\\text{ cm}$. Khi đó độ dài đoạn thẳng $AM$ bằng:",
            "a": "$5\\text{ cm}$",
            "b": "$10\\text{ cm}$",
            "c": "$15\\text{ cm}$",
            "d": "$20\\text{ cm}$",
            "da": "A",
            "loigiai": "Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng một nửa cạnh huyền: $AM = \\dfrac{1}{2}BC = \\dfrac{1}{2} \\cdot 10 = 5\\text{ cm}$."
        },
        {
            "cau": 9,
            "de": "Cho các tam giác có độ dài ba cạnh như sau. Tam giác nào là tam giác vuông?",
            "a": "$15\\text{ cm}; 8\\text{ cm}; 10\\text{ cm}$",
            "b": "$6\\text{ dm}; 8\\text{ dm}; 9\\text{ dm}$",
            "c": "$5\\text{ cm}; 4\\text{ cm}; 3\\text{ cm}$",
            "d": "$2\\text{ cm}; 3\\text{ cm}; 4\\text{ cm}$",
            "da": "C",
            "loigiai": "Theo định lý Pythagoras đảo: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$, do đó tam giác có độ dài ba cạnh $3\\text{ cm}, 4\\text{ cm}, 5\\text{ cm}$ là tam giác vuông."
        },
        {
            "cau": 10,
            "de": "Cho hình chữ nhật $ABCD$. Đoạn thẳng $AC$ bằng đoạn thẳng nào sau đây?",
            "a": "$AB$",
            "b": "$BC$",
            "c": "$AD$",
            "d": "$BD$",
            "da": "D",
            "loigiai": "Trong hình chữ nhật $ABCD$, hai đường chéo $AC$ và $BD$ bằng nhau: $AC = BD$."
        },
        {
            "cau": 11,
            "de": "Cho tứ giác $ABCD$, trong đó $\\widehat{A} + \\widehat{B} = 140^\\circ$. Tổng $\\widehat{C} + \\widehat{D}$ bằng:",
            "a": "$220^\\circ$",
            "b": "$200^\\circ$",
            "c": "$160^\\circ$",
            "d": "$130^\\circ$",
            "da": "A",
            "loigiai": "Tổng 4 góc của tứ giác bằng $360^\\circ$. Do đó: $\\widehat{C} + \\widehat{D} = 360^\\circ - (\\widehat{A} + \\widehat{B}) = 360^\\circ - 140^\\circ = 220^\\circ$."
        },
        {
            "cau": 12,
            "de": "Thể tích của một hình chóp tam giác đều có diện tích đáy bằng $15\\text{ cm}^2$ và chiều cao bằng $6\\text{ cm}$ là:",
            "a": "$90\\text{ cm}^3$",
            "b": "$30\\text{ cm}^3$",
            "c": "$45\\text{ cm}^3$",
            "d": "$15\\text{ cm}^3$",
            "da": "B",
            "loigiai": "Thể tích hình chóp là: $V = \\dfrac{1}{3} S_{\\text{đáy}} \\cdot h = \\dfrac{1}{3} \\cdot 15 \\cdot 6 = 30\\text{ (cm}^3\\text{)}$."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho hai biểu thức $A = (2x - 1)(x + 3) - 2x(x + 2)$ và $B = (6x^3y^2 - 9x^2y^3) : 3x^2y$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Khai triển tích $(2x - 1)(x + 3)$ ta được $2x^2 + 5x - 3$.",
                "da": "D",
                "giai": "Đúng. $(2x - 1)(x + 3) = 2x^2 + 6x - x - 3 = 2x^2 + 5x - 3$."
            },
            "y_b": {
                "noi_dung": "Kết quả rút gọn của biểu thức $A$ là $x - 3$.",
                "da": "D",
                "giai": "Đúng. $A = (2x^2 + 5x - 3) - (2x^2 + 4x) = x - 3$."
            },
            "y_c": {
                "noi_dung": "Kết quả của phép chia biểu thức $B$ là $2xy - 3y^2$.",
                "da": "D",
                "giai": "Đúng. $B = (6x^3y^2 - 9x^2y^3) : 3x^2y = 2xy - 3y^2$."
            },
            "y_d": {
                "noi_dung": "Tại $x = 2$ và $y = 1$, giá trị của biểu thức $A$ gấp 2 lần giá trị của biểu thức $B$.",
                "da": "S",
                "giai": "Sai. Tại $x = 2, y = 1$: $A = 2 - 3 = -1$ và $B = 2 \\cdot 2 \\cdot 1 - 3 \\cdot 1^2 = 1$. Vì $-1 \\ne 2 \\cdot 1$ nên khẳng định là sai."
            }
        },
        {
            "cau": 2,
            "de": "Cho hai đa thức $P = x^2 - 6x + 9 - y^2$ và $Q = 8x^3 - 27$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Biến đổi $x^2 - 6x + 9$ thành bình phương của một hiệu ta được $(x - 3)^2$.",
                "da": "D",
                "giai": "Đúng. $x^2 - 6x + 9 = (x - 3)^2$."
            },
            "y_b": {
                "noi_dung": "Phân tích đa thức $P$ thành nhân tử ta được $(x - y - 3)(x + y - 3)$.",
                "da": "D",
                "giai": "Đúng. $P = (x - 3)^2 - y^2 = (x - 3 - y)(x - 3 + y) = (x - y - 3)(x + y - 3)$."
            },
            "y_c": {
                "noi_dung": "Phân tích đa thức $Q$ thành nhân tử theo hằng đẳng thức hiệu hai lập phương ta được $(2x - 3)(4x^2 + 6x + 9)$.",
                "da": "D",
                "giai": "Đúng. $Q = (2x)^3 - 3^3 = (2x - 3)(4x^2 + 6x + 9)$."
            },
            "y_d": {
                "noi_dung": "Tại $x = 5$ và $y = 2$, giá trị của đa thức $P$ bằng 8.",
                "da": "S",
                "giai": "Sai. Thay $x = 5, y = 2$ vào $P$: $P = (5 - 3)^2 - 2^2 = 2^2 - 4 = 0 \\ne 8$."
            }
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Rút gọn biểu thức: $A = (2x - 1)(x + 3) - 2x(x + 2)$.",
            "da": "$x - 3$",
            "loigiai": "Ta có:\n$$A = (2x^2 + 6x - x - 3) - (2x^2 + 4x) = 2x^2 + 5x - 3 - 2x^2 - 4x = x - 3.$$\nĐáp số: $x - 3$."
        },
        {
            "cau": 2,
            "de": "Phân tích đa thức sau thành nhân tử: $x^2 - y^2 + 2x + 1$.",
            "da": "$(x - y + 1)(x + y + 1)$",
            "loigiai": "Nhóm các hạng tử tạo hằng đẳng thức:\n$$x^2 + 2x + 1 - y^2 = (x + 1)^2 - y^2 = (x + 1 - y)(x + 1 + y) = (x - y + 1)(x + y + 1).$$\nĐáp số: $(x - y + 1)(x + y + 1)$."
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
                    "noi_dung": "Thu gọn và tính giá trị biểu thức $A = 5x^2y - 2xy + 3x^2y - xy$ tại $x = -1, y = 2$.",
                    "loigiai": "Thu gọn đa thức: $A = (5x^2y + 3x^2y) + (-2xy - xy) = 8x^2y - 3xy$.\nThay $x = -1, y = 2$: $A = 8(-1)^2(2) - 3(-1)(2) = 16 + 6 = 22$."
                },
                {
                    "y": "b",
                    "diem_y": "0,75",
                    "noi_dung": "Thực hiện phép nhân: $B = 3xy(2x^2 - 5y^3)$.",
                    "loigiai": "$B = 3xy \\cdot 2x^2 - 3xy \\cdot 5y^3 = 6x^3y - 15xy^4$."
                },
                {
                    "y": "c",
                    "diem_y": "0,75",
                    "noi_dung": "Thực hiện phép chia: $C = (6x^3y^2 - 9x^2y^3) : 3x^2y^2$.",
                    "loigiai": "$C = 6x^3y^2 : 3x^2y^2 - 9x^2y^3 : 3x^2y^2 = 2x - 3y$."
                }
            ]
        },
        {
            "cau": 2,
            "diem": "1,5 điểm",
            "de": "Cho hai đa thức: $P = 2x^2y + 5x^3 - 2xy^2 + 6$ và $Q = x^3 + xy^2 - x^2y - 2$.",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,75",
                    "noi_dung": "Tính tổng của hai đa thức $P$ và $Q$.",
                    "loigiai": "$\\begin{aligned}[t] P + Q &= (5x^3 + x^3) + (2x^2y - x^2y) + (-2xy^2 + xy^2) + (6 - 2) \\\\ &= 6x^3 + x^2y - xy^2 + 4. \\end{aligned}$"
                },
                {
                    "y": "b",
                    "diem_y": "0,75",
                    "noi_dung": "Tìm đa thức $N$ sao cho $Q = P + N$.",
                    "loigiai": "Ta có $N = Q - P$:\n$$\\begin{aligned} N &= (x^3 + xy^2 - x^2y - 2) - (2x^2y + 5x^3 - 2xy^2 + 6) \\\\ &= x^3 + xy^2 - x^2y - 2 - 2x^2y - 5x^3 + 2xy^2 - 6 \\\\ &= -4x^3 - 3x^2y + 3xy^2 - 8. \\end{aligned}$$"
                }
            ]
        },
        {
            "cau": 3,
            "diem": "1,0 điểm",
            "de": "Khu vườn của nhà bác Hoa có dạng hình vuông. Bác Hoa muốn dành một mảnh đất hình chữ nhật ở góc khu vườn làm nhà để dụng cụ làm vườn (hình vẽ).",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.8, baseline=(current bounding box.center)]\n  \\draw[thick, fill=green!10] (0,0) rectangle (4,4);\n  \\draw[thick, fill=orange!25] (0,0) rectangle (2.2,1.3);\n  \\node at (1.1,0.65) {\\small Nhà kho};\n  \\node at (2.5,2.6) {\\small Khu vườn};\n  \\draw[<->] (0,-0.3) -- (4,-0.3) node[midway, below] {\\small $x$};\n  \\draw[<->] (-0.3,0) -- (-0.3,4) node[midway, left] {\\small $x$};\n  \\draw[<->] (2.2,-0.3) -- (4,-0.3) node[midway, below] {\\small $15\\text{ m}$};\n  \\draw[<->] (-0.3,1.3) -- (-0.3,4) node[midway, left] {\\small $25\\text{ m}$};\n\\end{tikzpicture}\n\\end{center}",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Viết đa thức biểu thị chu vi của mảnh đất làm nhà.",
                    "loigiai": "Mảnh đất hình chữ nhật có chiều dài là $x - 15\\text{ (m)}$ và chiều rộng là $x - 25\\text{ (m)}$.\nĐa thức biểu thị chu vi mảnh đất là:\n$$C = 2 \\cdot [(x - 15) + (x - 25)] = 2(2x - 40) = 4x - 80\\text{ (m)}.$$"
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "Biết chu vi của mảnh đất làm nhà bằng $40\\text{ m}$. Tính diện tích khu vườn hình vuông ban đầu.",
                    "loigiai": "Theo bài ra: $4x - 80 = 40 \\Rightarrow 4x = 120 \\Rightarrow x = 30\\text{ (m)}$.\nCạnh khu vườn hình vuông ban đầu là $30\\text{ m}$.\nDiện tích khu vườn ban đầu là: $S = 30 \\times 30 = 900\\text{ (m}^2\\text{)}$."
                }
            ]
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Cho các số thực $x, y$ thỏa mãn $x + y = 1$. Tìm giá trị nhỏ nhất của biểu thức $A = x^3 + y^3 + xy$.",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Tìm GTNN của $A$.",
                    "loigiai": "Biến đổi biểu thức $A$:\n$$\\begin{aligned} A &= (x + y)(x^2 - xy + y^2) + xy \\\\ &= 1 \\cdot (x^2 - xy + y^2) + xy \\\\ &= x^2 + y^2. \\end{aligned}$$\nThay $y = 1 - x$ vào biểu thức, ta được:\n$$\\begin{aligned} A &= x^2 + (1 - x)^2 = x^2 + 1 - 2x + x^2 \\\\ &= 2x^2 - 2x + 1 = 2\\left(x^2 - x + \\dfrac{1}{4}\\right) + \\dfrac{1}{2} \\\\ &= 2\\left(x - \\dfrac{1}{2}\\right)^2 + \\dfrac{1}{2}. \\end{aligned}$$\nVì $2\\left(x - \\dfrac{1}{2}\\right)^2 \\ge 0$ với mọi $x$, nên $A \\ge \\dfrac{1}{2}$.\nDấu \"$=\"$ xảy ra khi $x = \\dfrac{1}{2} \\Rightarrow y = 1 - \\dfrac{1}{2} = \\dfrac{1}{2}$.\nVậy giá trị nhỏ nhất của $A$ là $\\dfrac{1}{2}$, đạt được khi $x = y = \\dfrac{1}{2}$."
                }
            ]
        }
    ]
}

out_path = r"d:\GitHub\SOANBAI-main\LOP8\DETHIGHK1\DE_03\de_03.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Ghi thanh cong de_03.json!")

