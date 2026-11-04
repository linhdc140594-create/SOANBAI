import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": "10",
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I 2026 – 2027",
    "mon": "Toán 6",
    "thoi_gian": "90 phút",
    "phan_I": [
        {
            "cau": 1,
            "de": "Cho hai tập hợp $A = \\{1; 2; 3; 4; 5\\}$ và $B = \\{a; b; c; d\\}$. Có bao nhiêu tập hợp gồm hai phần tử thỏa mãn có một phần tử thuộc tập hợp $A$ và một phần tử thuộc tập hợp $B$?",
            "a": "$16$.",
            "b": "$18$.",
            "c": "$20$.",
            "d": "$9$.",
            "da": "C",
            "loigiai": "Tập $A$ có 5 phần tử, tập $B$ có 4 phần tử. Số cách chọn 1 phần tử thuộc $A$ là 5 cách, số cách chọn 1 phần tử thuộc $B$ là 4 cách. Số tập hợp thỏa mãn là: $5 \\times 4 = 20$ (tập hợp)."
        },
        {
            "cau": 2,
            "de": "Tìm số tự nhiên $x$, biết $x + 20 = 42$:",
            "a": "$22$.",
            "b": "$62$.",
            "c": "$2$.",
            "d": "$18$.",
            "da": "A",
            "loigiai": "Ta có: $x = 42 - 20 = 22$."
        },
        {
            "cau": 3,
            "de": "Số $308$ đọc là:",
            "a": "Ba trăm tám mươi.",
            "b": "Ba mươi tám.",
            "c": "Ba trăm linh tám.",
            "d": "Ba linh tám.",
            "da": "C",
            "loigiai": "Số $308$ có chữ số hàng trăm là 3, chữ số hàng chục là 0, chữ số hàng đơn vị là 8 nên được đọc là \"Ba trăm linh tám\"."
        },
        {
            "cau": 4,
            "de": "Hợp số là:",
            "a": "Số tự nhiên có nhiều hơn 2 ước.",
            "b": "Số tự nhiên có 4 ước.",
            "c": "Số tự nhiên lớn hơn 1, có nhiều hơn 2 ước.",
            "d": "Số tự nhiên lớn hơn 1, chỉ có hai ước là 1 và chính nó.",
            "da": "C",
            "loigiai": "Theo định nghĩa SGK, hợp số là số tự nhiên lớn hơn 1, có nhiều hơn 2 ước."
        },
        {
            "cau": 5,
            "de": "Trong tam giác đều, mỗi góc có số đo bằng:",
            "a": "$60^\\circ$.",
            "b": "$45^\\circ$.",
            "c": "$90^\\circ$.",
            "d": "$30^\\circ$.",
            "da": "A",
            "loigiai": "Tam giác đều có 3 góc ở các đỉnh bằng nhau và mỗi góc bằng $60^\\circ$."
        },
        {
            "cau": 6,
            "de": "Khẳng định nào dưới đây là đúng?",
            "a": "Hình bình hành có 4 góc bằng nhau.",
            "b": "Hình lục giác đều có 3 đường chéo chính cùng đi qua một điểm.",
            "c": "Tam giác đều là tam giác có 3 góc vuông.",
            "d": "Hình chữ nhật có hai đường chéo bằng nhau và vuông góc với nhau.",
            "da": "B",
            "loigiai": "Hình lục giác đều có 3 đường chéo chính bằng nhau và cùng đi qua một điểm (tâm của lục giác đều)."
        },
        {
            "cau": 7,
            "de": "Kết quả của phép tính $7^{12} \\cdot 7^2 \\cdot 7^0$ dưới dạng một lũy thừa là:",
            "a": "$7^{14}$.",
            "b": "$7^{24}$.",
            "c": "$7^{32}$.",
            "d": "$7^7$.",
            "da": "A",
            "loigiai": "$7^{12} \\cdot 7^2 \\cdot 7^0 = 7^{12 + 2 + 0} = 7^{14}$."
        },
        {
            "cau": 8,
            "de": "Cho hình bình hành $ABCD$ có $AB = 3\\text{ cm}, BC = 2\\text{ cm}$. Chu vi hình bình hành $ABCD$ là:",
            "a": "$6\\text{ cm}$.",
            "b": "$10\\text{ cm}$.",
            "c": "$12\\text{ cm}$.",
            "d": "$5\\text{ cm}$.",
            "da": "B",
            "loigiai": "Chu vi hình bình hành $ABCD$ là: $(3 + 2) \\times 2 = 10\\text{ (cm)}$."
        },
        {
            "cau": 9,
            "de": "Tập hợp nào sau đây là tập hợp các số nguyên $\\mathbb{Z}$?",
            "a": "$\\{1; 2; 3; 4; 5\\}$.",
            "b": "$\\{\\dots; -3; -2; -1; 0; 1; 2; 3; \\dots\\}$.",
            "c": "$\\{0; 1; 2; 3; 4; 5\\}$.",
            "d": "$\\{0; -1; -2; -3; \\dots\\}$.",
            "da": "B",
            "loigiai": "Tập hợp các số nguyên gồm các số nguyên âm, số 0 và các số nguyên dương: $\\mathbb{Z} = \\{\\dots; -3; -2; -1; 0; 1; 2; 3; \\dots\\}$."
        },
        {
            "cau": 10,
            "de": "Số 18 được viết bằng chữ số La Mã là:",
            "a": "XII.",
            "b": "XV.",
            "c": "XVIII.",
            "d": "XX.",
            "da": "C",
            "loigiai": "$18 = 10 + 5 + 1 + 1 + 1$ tương ứng viết thành XVIII."
        },
        {
            "cau": 11,
            "de": "Số nào sau đây là bội của $17$?",
            "a": "$51$.",
            "b": "$54$.",
            "c": "$56$.",
            "d": "$63$.",
            "da": "A",
            "loigiai": "Ta có $51 : 17 = 3$ (chia hết) nên 51 là bội của 17."
        },
        {
            "cau": 12,
            "de": "Cho hình thoi có độ dài hai đường chéo là $2\\text{ cm}$ và $4\\text{ cm}$. Diện tích của hình thoi đó là:",
            "a": "$4\\text{ cm}^2$.",
            "b": "$6\\text{ cm}^2$.",
            "c": "$8\\text{ cm}^2$.",
            "d": "$2\\text{ cm}^2$.",
            "da": "A",
            "loigiai": "Diện tích hình thoi là: $S = \\dfrac{2 \\times 4}{2} = 4\\text{ (cm}^2\\text{)}$."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho tập hợp $B = \\{x \\in \\mathbb{N} \\mid 12 \\le x < 18\\}$. Xét tính đúng/sai của các khẳng định sau:",
            "y_a": {"noi_dung": "Tập hợp $B$ gồm các phần tử là $12; 13; 14; 15; 16; 17$.", "da": "D", "giai": "Đúng. Các số tự nhiên lớn hơn hoặc bằng 12 và nhỏ hơn 18 là 12, 13, 14, 15, 16, 17."},
            "y_b": {"noi_dung": "Số $18$ thuộc tập hợp $B$ (kí hiệu là $18 \\in B$).", "da": "S", "giai": "Sai. Vì điều kiện là $x < 18$ nên $18 \\notin B$."},
            "y_c": {"noi_dung": "Trong tập hợp $B$, chỉ có duy nhất một số chia hết cho 5 là số $15$.", "da": "D", "giai": "Đúng. Trong các phần tử của $B$, chỉ có số 15 có tận cùng là 5 nên chia hết cho 5."},
            "y_d": {"noi_dung": "Tổng của phần tử bé nhất và phần tử lớn nhất trong tập hợp $B$ là $29$.", "da": "D", "giai": "Đúng. Phần tử bé nhất là 12, phần tử lớn nhất là 17. Tổng: $12 + 17 = 29$."}
        },
        {
            "cau": 2,
            "de": "Cho hình thang cân $ABCD$ có độ dài đáy nhỏ $AB = 4\\text{ cm}$, đáy lớn $CD = 10\\text{ cm}$ và chiều cao $h = 5\\text{ cm}$. Xét tính đúng/sai của các khẳng định sau:",
            "y_a": {"noi_dung": "Hai cạnh bên $AD$ và $BC$ có độ dài bằng nhau.", "da": "D", "giai": "Đúng. Trong hình thang cân, hai cạnh bên luôn có độ dài bằng nhau."},
            "y_b": {"noi_dung": "Hai góc kề một đáy của hình thang cân $ABCD$ bằng nhau.", "da": "D", "giai": "Đúng. Đây là tính chất đặc trưng cơ bản của hình thang cân."},
            "y_c": {"noi_dung": "Hai đường chéo $AC$ và $BD$ vuông góc với nhau.", "da": "S", "giai": "Sai. Trong hình thang cân, hai đường chéo bằng nhau chứ không nhất thiết vuông góc với nhau."},
            "y_d": {"noi_dung": "Diện tích của hình thang cân $ABCD$ là $35\\text{ cm}^2$.", "da": "D", "giai": "Đúng. Diện tích hình thang cân là: $S = \\dfrac{(4 + 10) \\cdot 5}{2} = 35\\text{ (cm}^2\\text{)}$."}
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Tìm số tự nhiên $x$ sao cho $24 \\ \\vdots \\ x$ và $10 \\le x < 15$.",
            "da": "12",
            "loigiai": "Vì $24 \\ \\vdots \\ x$ nên $x \\in Ư(24) = \\{1; 2; 3; 4; 6; 8; 12; 24\\}$.\\\\Vì $10 \\le x < 15$ nên $x = 12$."
        },
        {
            "cau": 2,
            "de": "Một hình thang cân có độ dài hai đáy lần lượt là $6\\text{ cm}$ và $10\\text{ cm}$, chiều cao bằng $4\\text{ cm}$. Tính diện tích của hình thang cân đó (theo đơn vị $\\text{cm}^2$).",
            "da": "32",
            "loigiai": "Diện tích hình thang cân là: $S = \\dfrac{(6 + 10) \\cdot 4}{2} = 32\\text{ (cm}^2\\text{)}$."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "1,0 điểm",
            "de": "Thực hiện phép tính (Tính hợp lí nếu có thể):",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,3",
                    "noi_dung": "$6^2 : 4 + 2^3 \\cdot 5$",
                    "loigiai": "$6^2 : 4 + 2^3 \\cdot 5 = 36 : 4 + 8 \\cdot 5 = 9 + 40 = 49$."
                },
                {
                    "y": "b",
                    "diem_y": "0,35",
                    "noi_dung": "$47 \\cdot 31 + 69 \\cdot 47 - 200$",
                    "loigiai": "$47 \\cdot (31 + 69) - 200 = 47 \\cdot 100 - 200 = 4700 - 200 = 4500$."
                },
                {
                    "y": "c",
                    "diem_y": "0,35",
                    "noi_dung": "$12 \\cdot \\{390 : [500 - (125 + 245)]\\}$",
                    "loigiai": "$12 \\cdot \\{390 : [500 - 370]\\} = 12 \\cdot \\{390 : 130\\} = 12 \\cdot 3 = 36$."
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
                    "diem_y": "0,3",
                    "noi_dung": "$x + 35 = 98$",
                    "loigiai": "$x = 98 - 35 \\Rightarrow x = 63$."
                },
                {
                    "y": "b",
                    "diem_y": "0,35",
                    "noi_dung": "$3x - 45 = 60$",
                    "loigiai": "$3x = 60 + 45 \\Rightarrow 3x = 105 \\Rightarrow x = 105 : 3 = 35$."
                },
                {
                    "y": "c",
                    "diem_y": "0,35",
                    "noi_dung": "$(6 - x)^3 + 11 = 19$",
                    "loigiai": "$(6 - x)^3 = 19 - 11 \\Rightarrow (6 - x)^3 = 8 \\Rightarrow (6 - x)^3 = 2^3 \\Rightarrow 6 - x = 2 \\Rightarrow x = 4$."
                }
            ]
        },
        {
            "cau": 3,
            "diem": "0,5 điểm",
            "de": "Bác Minh muốn lát nền cho một căn phòng hình chữ nhật có chiều dài $16\\text{ m}$, chiều rộng $5\\text{ m}$. Loại gạch lát nền được sử dụng là gạch hình vuông có cạnh dài $40\\text{ cm}$. Hỏi bác Minh phải sử dụng bao nhiêu viên gạch (coi mạch vữa không đáng kể)?",
            "loigiai": "Diện tích căn phòng là: $16 \\times 5 = 80\\text{ (m}^2\\text{)} = 800\\,000\\text{ (cm}^2\\text{)}$.\\\\Diện tích một viên gạch lát nền là: $40 \\times 40 = 1600\\text{ (cm}^2\\text{)}$.\\\\Số viên gạch bác Minh cần sử dụng là: $800\\,000 : 1600 = 500\\text{ (viên)}$."
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Chứng tỏ rằng biểu thức sau chia hết cho 21:\\\\$A = 1 + 4 + 4^2 + 4^3 + \\dots + 4^{2024}$",
            "loigiai": "Tổng $A$ có $2024 - 0 + 1 = 2025$ số hạng. Vì $2025 \\ \\vdots \\ 3$, ta nhóm 3 số hạng liên tiếp vào một nhóm:\n\\begin{align*}\nA &= (1 + 4 + 4^2) + 4^3(1 + 4 + 4^2) + \\dots + 4^{2022}(1 + 4 + 4^2)\\\\\n&= (1 + 4 + 16) + 4^3 \\cdot (1 + 4 + 16) + \\dots + 4^{2022} \\cdot (1 + 4 + 16)\\\\\n&= 21 + 4^3 \\cdot 21 + \\dots + 4^{2022} \\cdot 21\\\\\n&= 21 \\cdot (1 + 4^3 + \\dots + 4^{2022})\n\\end{align*}\nVì tích có thừa số 21 nên $A \\ \\vdots \\ 21$ (đpcm)."
        }
    ]
}

out_path = r"d:\GitHub\SOANBAI-main\LOP6\DE_THI_GHK1\DE_10\de_10.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved de_10.json successfully!")

