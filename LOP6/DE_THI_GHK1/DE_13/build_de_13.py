import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": "13",
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I 2026 – 2027",
    "mon": "Toán 6",
    "thoi_gian": "90 phút",
    "phan_I": [
        {
            "cau": 1,
            "de": "Số vừa chia hết cho 2 vừa chia hết cho 3 là:",
            "a": "$5019$.",
            "b": "$5020$.",
            "c": "$5021$.",
            "d": "$5022$.",
            "da": "D",
            "loigiai": "Số 5022 có tận cùng là số chẵn nên chia hết cho 2; tổng các chữ số $5 + 0 + 2 + 2 = 9 \\ \\vdots \\ 3$ nên chia hết cho 3."
        },
        {
            "cau": 2,
            "de": "Hình vuông $ABCD$ có cạnh $AB = 3\\text{ cm}$. Diện tích của hình vuông đó bằng:",
            "a": "$3\\text{ cm}^2$.",
            "b": "$9\\text{ cm}^2$.",
            "c": "$12\\text{ cm}^2$.",
            "d": "$81\\text{ cm}^2$.",
            "da": "B",
            "loigiai": "Diện tích hình vuông là: $3 \\times 3 = 9\\text{ (cm}^2\\text{)}$."
        },
        {
            "cau": 3,
            "de": "Số nào sau đây không phải số nguyên tố?",
            "a": "$11$.",
            "b": "$33$.",
            "c": "$17$.",
            "d": "$31$.",
            "da": "B",
            "loigiai": "Số 33 chia hết cho 3 và 11 nên là hợp số."
        },
        {
            "cau": 4,
            "de": "Ước chung lớn nhất của 13 và 4 là:",
            "a": "$1$.",
            "b": "$3$.",
            "c": "$4$.",
            "d": "$12$.",
            "da": "A",
            "loigiai": "Vì 13 là số nguyên tố và không chia hết cho 4, nên $ƯCLN(13, 4) = 1$."
        },
        {
            "cau": 5,
            "de": "Chọn câu khẳng định đúng nhất:",
            "a": "Hình thang cân là hình thang có hai góc kề một đáy bằng nhau.",
            "b": "Trong hình thang cân, hai cạnh bên bằng nhau.",
            "c": "Trong hình thang cân, hai đường chéo bằng nhau.",
            "d": "Cả A, B, C đều đúng.",
            "da": "D",
            "loigiai": "Cả 3 phương án A, B, C đều là các định nghĩa và tính chất cơ bản của hình thang cân."
        },
        {
            "cau": 6,
            "de": "Tập hợp $\\mathbb{N}$ tất cả các số tự nhiên là:",
            "a": "$\\{0; 1; 2\\}$.",
            "b": "$\\{0; 1; 2; 3; 4\\}$.",
            "c": "$\\{0; 1; 2; 3; \\dots\\}$.",
            "d": "$\\{0; 1; 2; 3; 4; 5; 6; 7; 8; 9\\}$.",
            "da": "C",
            "loigiai": "Tập hợp các số tự nhiên $\\mathbb{N} = \\{0; 1; 2; 3; \\dots\\}$."
        },
        {
            "cau": 7,
            "de": "Thứ tự thực hiện phép tính nào sau đây là đúng đối với biểu thức có dấu ngoặc?",
            "a": "$[] \\to () \\to \\{\\}$.",
            "b": "$[] \\to \\{\\} \\to ()$.",
            "c": "$\\{\\} \\to [] \\to ()$.",
            "d": "$() \\to [] \\to \\{\\}$.",
            "da": "D",
            "loigiai": "Thứ tự thực hiện đúng đối với biểu thức có ngoặc là: ngoặc tròn () $\\to$ ngoặc vuông [] $\\to$ ngoặc nhọn \\{\\}."
        },
        {
            "cau": 8,
            "de": "Điều kiện của số tự nhiên $x$ để biểu thức $A = 12 + 14 + 16 + x$ chia hết cho 2 là:",
            "a": "$x$ là số tự nhiên chẵn.",
            "b": "$x$ là số tự nhiên lẻ.",
            "c": "$x$ là số tự nhiên bất kì.",
            "d": "$x \\in \\{0; 2; 4; 6; 8\\}$.",
            "da": "A",
            "loigiai": "Vì 12, 14, 16 đều chia hết cho 2 nên để $A \\ \\vdots \\ 2$ thì $x$ phải là số tự nhiên chẵn."
        },
        {
            "cau": 9,
            "de": "Khẳng định nào sau đây là sai?",
            "a": "Hình chữ nhật và hình thoi có các cặp cạnh đối song song với nhau.",
            "b": "Hình lục giác đều có ba đường chéo chính bằng nhau.",
            "c": "Hình bình hành có các cạnh đối bằng nhau.",
            "d": "Hình thoi có hai đường chéo bằng nhau.",
            "da": "D",
            "loigiai": "Hình thoi có hai đường chéo vuông góc với nhau tại trung điểm mỗi đường chứ nói chung không bằng nhau."
        },
        {
            "cau": 10,
            "de": "Phát biểu nào sau đây là sai?\\\\Trong một hình bình hành:",
            "a": "Hai đường chéo cắt nhau tại trung điểm mỗi đường.",
            "b": "Các cạnh đối song song với nhau.",
            "c": "Bốn góc ở các đỉnh bằng nhau.",
            "d": "Các cạnh đối bằng nhau.",
            "da": "C",
            "loigiai": "Hình bình hành có các góc đối bằng nhau, không phải 4 góc bằng nhau (chỉ có hình chữ nhật và hình vuông mới có 4 góc bằng nhau)."
        },
        {
            "cau": 11,
            "de": "Trong các số sau, số nào chia hết cho 2?",
            "a": "$803$.",
            "b": "$135$.",
            "c": "$1975$.",
            "d": "$358$.",
            "da": "D",
            "loigiai": "Số 358 có chữ số tận cùng là 8 (số chẵn) nên chia hết cho 2."
        },
        {
            "cau": 12,
            "de": "Giá một chiếc khẩu trang N95 là $30\\,000$ đồng. Số tiền cần có để mua 20 chiếc khẩu trang N95 đó là:",
            "a": "$30\\,020$ đồng.",
            "b": "$60\\,000$ đồng.",
            "c": "$600\\,000$ đồng.",
            "d": "$500\\,000$ đồng.",
            "da": "C",
            "loigiai": "Số tiền cần có là: $30\\,000 \\times 20 = 600\\,000$ (đồng)."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho hình vuông $ABCD$ có cạnh $AB = 30\\text{ cm}$. Xét tính đúng/sai của các khẳng định sau:",
            "y_a": {"noi_dung": "Các góc của hình vuông bằng nhau và bằng $90^\\circ$.", "da": "D", "giai": "Đúng. Bốn góc của hình vuông đều bằng $90^\\circ$."},
            "y_b": {"noi_dung": "Độ dài đường chéo $AC$ lớn hơn $BD$.", "da": "S", "giai": "Sai. Trong hình vuông, hai đường chéo luôn bằng nhau: $AC = BD$."},
            "y_c": {"noi_dung": "Độ dài cạnh $BC = 20\\text{ cm}$.", "da": "S", "giai": "Sai. Bốn cạnh hình vuông bằng nhau nên $BC = AB = 30\\text{ cm}$."},
            "y_d": {"noi_dung": "Biết hình vuông $ABCD$ được ghép bởi 4 hình vuông nhỏ bằng nhau, cạnh của mỗi hình vuông nhỏ có độ dài là $15\\text{ dm}$.", "da": "S", "giai": "Sai. Cạnh hình vuông nhỏ là $30 : 2 = 15\\text{ cm} = 1{,}5\\text{ dm}$, không phải $15\\text{ dm}$."}
        },
        {
            "cau": 2,
            "de": "Cho biểu thức $P = 2 \\cdot 5^2 - 32 : 2^3$. Xét tính đúng/sai của các khẳng định sau:",
            "y_a": {"noi_dung": "Giá trị của lũy thừa $5^2$ bằng 10.", "da": "S", "giai": "Sai. $5^2 = 5 \\cdot 5 = 25$."},
            "y_b": {"noi_dung": "Biểu thức $P$ có giá trị bằng 46.", "da": "D", "giai": "Đúng. $P = 2 \\cdot 25 - 32 : 8 = 50 - 4 = 46$."},
            "y_c": {"noi_dung": "Giá trị của biểu thức $P$ chia hết cho cả 2 và 5.", "da": "S", "giai": "Sai. 46 có chữ số tận cùng là 6 nên không chia hết cho 5."},
            "y_d": {"noi_dung": "Giá trị của biểu thức $P$ là một hợp số.", "da": "D", "giai": "Đúng. Số 46 chia hết cho 1; 2; 23; 46 nên là hợp số."}
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Tìm số tự nhiên $x$ lớn nhất thỏa mãn $48 \\ \\vdots \\ x$ và $72 \\ \\vdots \\ x$.",
            "da": "24",
            "loigiai": "Số tự nhiên $x$ lớn nhất thỏa mãn $48 \\ \\vdots \\ x$ và $72 \\ \\vdots \\ x$ chính là $ƯCLN(48, 72)$.\\\\Ta có: $48 = 2^4 \\cdot 3$ và $72 = 2^3 \\cdot 3^2 \\Rightarrow ƯCLN(48, 72) = 2^3 \\cdot 3 = 24$."
        },
        {
            "cau": 2,
            "de": "Một hình thoi có diện tích bằng $30\\text{ cm}^2$ và độ dài một đường chéo bằng $6\\text{ cm}$. Tính độ dài đường chéo còn lại của hình thoi (theo đơn vị $\\text{cm}$).",
            "da": "10",
            "loigiai": "Độ dài đường chéo còn lại là: $\\dfrac{30 \\times 2}{6} = 10\\text{ (cm)}$."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "1,0 điểm",
            "de": "Thực hiện các phép tính sau (Tính nhanh nếu có thể):",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,25",
                    "noi_dung": "$15 + 187 + 85$",
                    "loigiai": "$(15 + 85) + 187 = 100 + 187 = 287$."
                },
                {
                    "y": "b",
                    "diem_y": "0,25",
                    "noi_dung": "$2024 - [38 - (4 - 1)^3]$",
                    "loigiai": "$2024 - [38 - 3^3] = 2024 - [38 - 27] = 2024 - 11 = 2013$."
                },
                {
                    "y": "c",
                    "diem_y": "0,25",
                    "noi_dung": "$27 \\cdot 39 + 27 \\cdot 63 - 2 \\cdot 27$",
                    "loigiai": "$27 \\cdot (39 + 63 - 2) = 27 \\cdot 100 = 2700$."
                },
                {
                    "y": "d",
                    "diem_y": "0,25",
                    "noi_dung": "$210 : \\{38 - [12 + 3 \\cdot (32 : 2^3)]\\}$",
                    "loigiai": "$210 : \\{38 - [12 + 3 \\cdot (32 : 8)]\\} = 210 : \\{38 - [12 + 12]\\} = 210 : \\{38 - 24\\} = 210 : 14 = 15$."
                }
            ]
        },
        {
            "cau": 2,
            "diem": "1,0 điểm",
            "de": "Tìm số tự nhiên $x$, biết:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,25",
                    "noi_dung": "$19 - x = 5$",
                    "loigiai": "$x = 19 - 5 = 14$."
                },
                {
                    "y": "b",
                    "diem_y": "0,25",
                    "noi_dung": "$2 \\cdot 3^x - 5 = 7^2$",
                    "loigiai": "$2 \\cdot 3^x = 49 + 5 = 54 \\Rightarrow 3^x = 27 = 3^3 \\Rightarrow x = 3$."
                },
                {
                    "y": "c",
                    "diem_y": "0,25",
                    "noi_dung": "$81 - (3x + 5) = 4^3$",
                    "loigiai": "$81 - (3x + 5) = 64 \\Rightarrow 3x + 5 = 81 - 64 = 17 \\Rightarrow 3x = 12 \\Rightarrow x = 4$."
                },
                {
                    "y": "d",
                    "diem_y": "0,25",
                    "noi_dung": "$(19x + 2 \\cdot 5^2) : 14 = (13 - 8)^2 - 4^2$",
                    "loigiai": "$(19x + 50) : 14 = 5^2 - 16 = 25 - 16 = 9 \\Rightarrow 19x + 50 = 9 \\cdot 14 = 126 \\Rightarrow 19x = 76 \\Rightarrow x = 4$."
                }
            ]
        },
        {
            "cau": 3,
            "diem": "0,5 điểm",
            "de": "Nhà bạn Nam có mảnh vườn hình chữ nhật, chiều dài $12\\text{ m}$, chiều rộng $8\\text{ m}$. Ở giữa vườn có khu nghỉ ngơi hình chữ nhật chiều dài $6\\text{ m}$, chiều rộng $2\\text{ m}$. Phần còn lại của khu vườn dùng để trồng cây.",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.5, font=\\small]\n  \\draw[thick, fill=green!15] (0,0) rectangle (12,8);\n  \\draw[thick, fill=orange!20] (3,3) rectangle (9,5);\n  \\node at (6,4) {\\footnotesize Khu nghỉ ngơi};\n  \\node[above] at (6,8) {$12\\text{ m}$};\n  \\node[right] at (12,4) {$8\\text{ m}$};\n  \\node[below] at (6,3) {$6\\text{ m}$};\n  \\node[left] at (3,4) {$2\\text{ m}$};\n\\end{tikzpicture}\n\\end{center}",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,25",
                    "noi_dung": "Tính diện tích toàn bộ mảnh vườn?",
                    "loigiai": "Diện tích mảnh vườn hình chữ nhật là: $12 \\times 8 = 96\\text{ (m}^2\\text{)}$."
                },
                {
                    "y": "b",
                    "diem_y": "0,25",
                    "noi_dung": "Biết mỗi mét vuông cây trồng hết $15\\,000$ đồng để chăm bón hàng tháng, hỏi bạn Nam cần bao nhiêu tiền chăm bón hàng tháng?",
                    "loigiai": "Diện tích khu nghỉ ngơi là: $6 \\times 2 = 12\\text{ (m}^2\\text{)}$.\\\\Diện tích phần trồng cây là: $96 - 12 = 84\\text{ (m}^2\\text{)}$.\\\\Số tiền Nam cần để chăm bón hàng tháng là: $84 \\times 15\\,000 = 1\\,260\\,000$ (đồng)."
                }
            ]
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Bài toán nâng cao về lũy thừa và chia hết:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,25",
                    "noi_dung": "Cho số tự nhiên $x$ thỏa mãn $3^{x+1} + 3^{x+2} - 2 \\cdot 3^x = 270$. Hỏi $x$ là số nguyên tố hay hợp số?",
                    "loigiai": "Ta có: $3^x \\cdot 3 + 3^x \\cdot 3^2 - 2 \\cdot 3^x = 270 \\Rightarrow 3^x \\cdot (3 + 9 - 2) = 270 \\Rightarrow 3^x \\cdot 10 = 270 \\Rightarrow 3^x = 27 = 3^3 \\Rightarrow x = 3$.\\\\Vì $x = 3$ chỉ có hai ước là 1 và 3 nên $x$ là số nguyên tố."
                },
                {
                    "y": "b",
                    "diem_y": "0,25",
                    "noi_dung": "Tìm hai số tự nhiên biết tích của chúng bằng 144 và ƯCLN của chúng bằng 6.",
                    "loigiai": "Gọi hai số tự nhiên cần tìm là $a$ và $b$. Giả sử $a \\le b$.\\\\Vì $ƯCLN(a, b) = 6$ nên đặt $a = 6m, b = 6n$ với $m, n \\in \\mathbb{N}^*$, $m \\le n$ và $ƯCLN(m, n) = 1$.\\\\Ta có: $a \\cdot b = 6m \\cdot 6n = 36mn = 144 \\Rightarrow m \\cdot n = 4$.\\\\Vì $ƯCLN(m, n) = 1$ và $m \\le n$ nên $m = 1, n = 4$.\\\\Suy ra: $a = 6 \\cdot 1 = 6$ và $b = 6 \\cdot 4 = 24$.\\\\Vậy hai số tự nhiên cần tìm là $6$ và $24$ (hoặc $24$ và $6$)."
                }
            ]
        }
    ]
}

out_path = r"d:\GitHub\SOANBAI-main\LOP6\DE_THI_GHK1\DE_13\de_13.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved de_13.json successfully!")

