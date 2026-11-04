import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": "06",
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I 2026 – 2027",
    "mon": "Toán 6",
    "thoi_gian": "90 phút",
    "phan_I": [
        {
            "cau": 1,
            "de": "Khẳng định nào sau đây là sai?\\\\Trong hình vuông:",
            "a": "Bốn cạnh bằng nhau.",
            "b": "Hai đường chéo song song với nhau.",
            "c": "Bốn góc ở các đỉnh là góc vuông.",
            "d": "Hai cạnh đối song song.",
            "da": "B",
            "loigiai": "Hai đường chéo của hình vuông cắt nhau và vuông góc với nhau tại trung điểm của mỗi đường, chứ không song song với nhau. Do đó, khẳng định \"Hai đường chéo song song với nhau\" là sai."
        },
        {
            "cau": 2,
            "de": "Cho tập hợp $A = \\{0; 2; 4; a; b\\}$. Khẳng định nào dưới đây sai?",
            "a": "$5 \\in A$.",
            "b": "$a \\in A$.",
            "c": "$0 \\in A$.",
            "d": "$1 \\notin A$.",
            "da": "A",
            "loigiai": "Số 5 không có trong tập hợp $A$, nên viết $5 \\in A$ là khẳng định sai."
        },
        {
            "cau": 3,
            "de": "Cho tập hợp $A = \\{x \\in \\mathbb{N}^* \\mid x \\le 4\\}$. Số nào dưới đây là phần tử của $A$?",
            "a": "0.",
            "b": "4.",
            "c": "5.",
            "d": "6.",
            "da": "B",
            "loigiai": "Tập hợp các số tự nhiên khác 0 nhỏ hơn hoặc bằng 4 là $A = \\{1; 2; 3; 4\\}$. Do đó, 4 là một phần tử thuộc $A$."
        },
        {
            "cau": 4,
            "de": "Với $a, m, n$ là các số tự nhiên, khẳng định nào sau đây đúng?",
            "a": "$a^m : a^n = a^{m-n}$ ($a \\ne 0, m \\ge n$).",
            "b": "$a^m : a^n = a^{m+n}$ ($a \\ne 0$).",
            "c": "$a^m : a^n = a^{m \\cdot n}$ ($a \\ne 0$).",
            "d": "$a^m : a^n = m - n$ ($a \\ne 0$).",
            "da": "A",
            "loigiai": "Công thức chia hai lũy thừa cùng cơ số là: $a^m : a^n = a^{m-n}$ (với $a \\ne 0, m \\ge n$)."
        },
        {
            "cau": 5,
            "de": "Kết quả của phép tính $256 - 98 + 137$ là:",
            "a": "21.",
            "b": "217.",
            "c": "259.",
            "d": "295.",
            "da": "D",
            "loigiai": "Thực hiện phép tính từ trái sang phải: $256 - 98 + 137 = 158 + 137 = 295$."
        },
        {
            "cau": 6,
            "de": "Đối với biểu thức không có dấu ngoặc và chỉ có các phép tính cộng, trừ, nhân, chia, lũy thừa, thì thứ tự thực hiện phép tính đúng là:",
            "a": "Nhân và chia $\\to$ Lũy thừa $\\to$ Cộng và trừ.",
            "b": "Lũy thừa $\\to$ Nhân và chia $\\to$ Cộng và trừ.",
            "c": "Lũy thừa $\\to$ Cộng và trừ $\\to$ Nhân và chia.",
            "d": "Cộng và trừ $\\to$ Nhân và chia $\\to$ Lũy thừa.",
            "da": "B",
            "loigiai": "Thứ tự thực hiện các phép tính chuẩn là: Lũy thừa $\\to$ Nhân và chia $\\to$ Cộng và trừ."
        },
        {
            "cau": 7,
            "de": "Cho các số $3; 15; 29$. Số không là số nguyên tố trong các số đó là:",
            "a": "3.",
            "b": "15.",
            "c": "29.",
            "d": "Cả 3 số trên.",
            "da": "B",
            "loigiai": "Số 15 ngoài ước 1 và 15 còn chia hết cho 3 và 5, nên 15 là hợp số."
        },
        {
            "cau": 8,
            "de": "Trong các số sau, số nào chia hết cho 9?",
            "a": "144.",
            "b": "249.",
            "c": "379.",
            "d": "199.",
            "da": "A",
            "loigiai": "Xét tổng các chữ số: số 144 có tổng các chữ số là $1 + 4 + 4 = 9 \\ \\vdots \\ 9$. Các số còn lại có tổng chữ số không chia hết cho 9."
        },
        {
            "cau": 9,
            "de": "Bạn An có ngày sinh là số nguyên tố lớn nhất nhỏ hơn 20, tháng sinh của bạn là số nguyên tố nhỏ nhất. Vậy bạn An có ngày và tháng sinh là:",
            "a": "Ngày 19 tháng 3.",
            "b": "Ngày 19 tháng 2.",
            "c": "Ngày 7 tháng 2.",
            "d": "Ngày 7 tháng 3.",
            "da": "B",
            "loigiai": "Số nguyên tố lớn nhất nhỏ hơn 20 là 19. Số nguyên tố nhỏ nhất là 2. Vậy bạn An sinh ngày 19 tháng 2."
        },
        {
            "cau": 10,
            "de": "Hình nào dưới đây là tam giác đều?",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.75, font=\\small]\n  % Hinh 1: Tam giac deu ABC\n  \\begin{scope}[shift={(0,0)}]\n    \\coordinate (C) at (0,0);\n    \\coordinate (B) at (2.4,0);\n    \\coordinate (A) at (1.2, 2.078);\n    \\draw[thick] (A) -- (B) -- (C) -- cycle;\n    \\filldraw[blue] (A) circle (1.5pt) node[above] {$A$};\n    \\filldraw[blue] (B) circle (1.5pt) node[right] {$B$};\n    \\filldraw[blue] (C) circle (1.5pt) node[left] {$C$};\n    \\draw ($(A)!0.5!(B) + (-0.08,0.05)$) -- ($(A)!0.5!(B) + (0.08,-0.05)$);\n    \\draw ($(A)!0.5!(C) + (-0.08,-0.05)$) -- ($(A)!0.5!(C) + (0.08,0.05)$);\n    \\draw ($(B)!0.5!(C) + (0,-0.09)$) -- ($(B)!0.5!(C) + (0,0.09)$);\n    \\node at (1.2, -0.6) {\\textbf{Hình 1}};\n  \\end{scope}\n  % Hinh 2: Tam giac vuong\n  \\begin{scope}[shift={(3.8,0)}]\n    \\coordinate (V) at (0,0);\n    \\coordinate (X) at (2.4,0);\n    \\coordinate (Y) at (0,2);\n    \\draw[thick] (V) -- (X) -- (Y) -- cycle;\n    \\draw (0,0.3) -- (0.3,0.3) -- (0.3,0);\n    \\node[left] at (0,1) {$a$};\n    \\node[below] at (1.2,0) {$b$};\n    \\node[above right] at (1.2,1) {$c$};\n    \\node at (1.2, -0.6) {\\textbf{Hình 2}};\n  \\end{scope}\n  % Hinh 3: Hinh vuong ABCD\n  \\begin{scope}[shift={(7.6,0)}]\n    \\coordinate (D) at (0,0);\n    \\coordinate (C3) at (2,0);\n    \\coordinate (B3) at (2,2);\n    \\coordinate (A3) at (0,2);\n    \\draw[thick] (A3) -- (B3) -- (C3) -- (D) -- cycle;\n    \\draw (0,1.75) -- (0.25,1.75) -- (0.25,2);\n    \\draw (2,1.75) -- (1.75,1.75) -- (1.75,2);\n    \\draw (0,0.25) -- (0.25,0.25) -- (0.25,0);\n    \\node[above left] at (A3) {$A$};\n    \\node[above right] at (B3) {$B$};\n    \\node[below right] at (C3) {$C$};\n    \\node[below left] at (D) {$D$};\n    \\node at (1, -0.6) {\\textbf{Hình 3}};\n  \\end{scope}\n  % Hinh 4: Hinh binh hanh ABCD\n  \\begin{scope}[shift={(11.2,0)}]\n    \\coordinate (D4) at (0,0);\n    \\coordinate (C4) at (2,0);\n    \\coordinate (B4) at (2.6,1.8);\n    \\coordinate (A4) at (0.6,1.8);\n    \\draw[thick] (A4) -- (B4) -- (C4) -- (D4) -- cycle;\n    \\node[above left] at (A4) {$A$};\n    \\node[above right] at (B4) {$B$};\n    \\node[below right] at (C4) {$C$};\n    \\node[below left] at (D4) {$D$};\n    \\node at (1.2, -0.6) {\\textbf{Hình 4}};\n  \\end{scope}\n\\end{tikzpicture}\n\\end{center}",
            "a": "Hình 1.",
            "b": "Hình 2.",
            "c": "Hình 3.",
            "d": "Hình 4.",
            "da": "A",
            "loigiai": "Quan sát hình vẽ thấy rằng Hình 1 có ký hiệu ba cạnh bằng nhau nên là tam giác đều."
        },
        {
            "cau": 11,
            "de": "Mỗi góc của lục giác đều có số đo bằng:",
            "a": "$90^\\circ$.",
            "b": "$180^\\circ$.",
            "c": "$120^\\circ$.",
            "d": "$60^\\circ$.",
            "da": "C",
            "loigiai": "Lục giác đều có 6 góc ở các đỉnh bằng nhau, số đo mỗi góc bằng $120^\\circ$."
        },
        {
            "cau": 12,
            "de": "Một mảnh giấy hình chữ nhật có diện tích $120\\text{ cm}^2$, độ dài một cạnh là $8\\text{ cm}$. Chu vi của mảnh giấy là:",
            "a": "$34\\text{ cm}$.",
            "b": "$40\\text{ cm}$.",
            "c": "$46\\text{ cm}$.",
            "d": "$54\\text{ cm}$.",
            "da": "C",
            "loigiai": "Độ dài cạnh còn lại của mảnh giấy là: $120 : 8 = 15\\text{ (cm)}$. Chu vi mảnh giấy là: $(15 + 8) \\cdot 2 = 46\\text{ (cm)}$."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho hình vuông $ABCD$ có cạnh bằng $4\\text{ cm}$. Xét tính đúng/sai của các khẳng định sau:",
            "y_a": {"noi_dung": "$AB = BC = CD = DA = 4\\text{ cm}$.", "da": "D", "giai": "Đúng. Hình vuông có 4 cạnh bằng nhau."},
            "y_b": {"noi_dung": "$AB$ và $BD$ song song với nhau.", "da": "S", "giai": "Sai. Cạnh $AB$ và đường chéo $BD$ cắt nhau tại đỉnh $B$, không song song với nhau."},
            "y_c": {"noi_dung": "Mỗi góc ở các đỉnh của hình vuông bằng nhau và bằng $60^\\circ$.", "da": "S", "giai": "Sai. Hình vuông có 4 góc ở các đỉnh bằng nhau và bằng $90^\\circ$."},
            "y_d": {"noi_dung": "Vẽ cạnh $AB = 4\\text{ cm}$. Dùng thước êke vẽ các đường vuông góc với $AB$ tại $A$ và $B$, sau đó lần lượt lấy các điểm $D, C$ trên các đường đó sao cho $AD = BC = 4\\text{ cm}$. Nối $C$ với $D$ ta được hình vuông $ABCD$ có cạnh $4\\text{ cm}$ như đã cho.", "da": "D", "giai": "Đúng. Đây là các bước quy chuẩn để vẽ hình vuông khi biết độ dài cạnh bằng thước và êke."}
        },
        {
            "cau": 2,
            "de": "Cho tập hợp $A = \\{x \\in \\mathbb{N} \\mid 10 < x \\le 15\\}$. Xét tính đúng/sai của các khẳng định sau:",
            "y_a": {"noi_dung": "Tập hợp $A$ được viết dưới dạng liệt kê các phần tử là: $A = \\{11; 12; 13; 14; 15\\}$.", "da": "D", "giai": "Đúng. Các số tự nhiên $x$ lớn hơn 10 và nhỏ hơn hoặc bằng 15 là 11, 12, 13, 14, 15."},
            "y_b": {"noi_dung": "Số 10 thuộc tập hợp $A$ (kí hiệu là $10 \\in A$).", "da": "S", "giai": "Sai. Vì điều kiện là $x > 10$ nên $10 \\notin A$."},
            "y_c": {"noi_dung": "Trong tập hợp $A$, có đúng 2 phần tử là số nguyên tố.", "da": "D", "giai": "Đúng. Trong tập hợp $A$, chỉ có 11 và 13 là số nguyên tố. Các số còn lại là hợp số."},
            "y_d": {"noi_dung": "Tổng của phần tử lớn nhất và phần tử bé nhất trong tập hợp $A$ là một số chia hết cho 3.", "da": "S", "giai": "Sai. Phần tử lớn nhất là 15, bé nhất là 11. Tổng: $15 + 11 = 26$. Vì tổng chữ số $2 + 6 = 8$ không chia hết cho 3 nên 26 không chia hết cho 3."}
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Tìm số tự nhiên $x$ thỏa mãn $2^x \\cdot 4 = 32$.",
            "da": "3",
            "loigiai": "Ta có: $4 = 2^2$ và $32 = 2^5$. Phương trình trở thành: $2^x \\cdot 2^2 = 2^5 \\Rightarrow 2^{x+2} = 2^5 \\Rightarrow x + 2 = 5 \\Rightarrow x = 3$."
        },
        {
            "cau": 2,
            "de": "Một hình chữ nhật có chu vi bằng $28\\text{ cm}$ và chiều dài bằng $8\\text{ cm}$. Tính diện tích của hình chữ nhật đó (theo đơn vị $\\text{cm}^2$).",
            "da": "48",
            "loigiai": "Nửa chu vi của hình chữ nhật là: $28 : 2 = 14\\text{ (cm)}$.\\\\Chiều rộng của hình chữ nhật là: $14 - 8 = 6\\text{ (cm)}$.\\\\Diện tích hình chữ nhật là: $8 \\times 6 = 48\\text{ (cm}^2\\text{)}$."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "1,5 điểm",
            "de": "Thực hiện phép tính (Tính hợp lí nếu có thể):",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "$12 \\cdot 25 + 85 : 17 - 205$",
                    "loigiai": "$12 \\cdot 25 + 85 : 17 - 205 = 300 + 5 - 205 = 305 - 205 = 100$."
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "$5^2 \\cdot 13 - 5^2 \\cdot 3$",
                    "loigiai": "$5^2 \\cdot 13 - 5^2 \\cdot 3 = 25 \\cdot (13 - 3) = 25 \\cdot 10 = 250$."
                },
                {
                    "y": "c",
                    "diem_y": "0,5",
                    "noi_dung": "$57 - [250 : (7 - 2)^2 - 3] \\cdot 2025^0$",
                    "loigiai": "$57 - [250 : 5^2 - 3] \\cdot 1 = 57 - [250 : 25 - 3] = 57 - [10 - 3] = 57 - 7 = 50$."
                }
            ]
        },
        {
            "cau": 2,
            "diem": "1,5 điểm",
            "de": "Tìm số tự nhiên $x$, biết:",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "$x + 12 = 45$",
                    "loigiai": "$x = 45 - 12 \\Rightarrow x = 33$."
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "$333 - x = 5^6 : 5^3$",
                    "loigiai": "$333 - x = 5^3 \\Rightarrow 333 - x = 125 \\Rightarrow x = 333 - 125 \\Rightarrow x = 208$."
                },
                {
                    "y": "c",
                    "diem_y": "0,5",
                    "noi_dung": "$(2x + 2)^3 = 12 \\cdot 144$",
                    "loigiai": "$(2x + 2)^3 = 12 \\cdot 12^2 = 12^3 \\Rightarrow 2x + 2 = 12 \\Rightarrow 2x = 10 \\Rightarrow x = 5$."
                }
            ]
        },
        {
            "cau": 3,
            "diem": "1,5 điểm",
            "de": "Kích thước chuẩn của sân bóng đá mini cho 5 người là sân hình chữ nhật có chiều dài tối thiểu $25\\text{ m}$ và tối đa $42\\text{ m}$, chiều rộng tối thiểu $15\\text{ m}$ và tối đa $25\\text{ m}$. Trường THCS A xây dựng sân bóng đá cỏ nhân tạo hình chữ nhật có chiều dài $30\\text{ m}$, chiều rộng $20\\text{ m}$.",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,75",
                    "noi_dung": "Vẽ minh họa sân bóng đá hình chữ nhật $ABCD$ có cạnh $AB = 3\\text{ cm}$ và cạnh $BC = 2\\text{ cm}$.",
                    "loigiai": "\\textbf{Cách vẽ hình chữ nhật $ABCD$ ($AB = 3\\text{ cm}, BC = 2\\text{ cm}$):}\n\\begin{itemize}[leftmargin=1.5cm, topsep=1pt, itemsep=1pt]\n  \\item Vẽ đoạn thẳng $AB = 3\\text{ cm}$.\n  \\item Vẽ đường thẳng vuông góc với $AB$ tại $A$, trên đó lấy điểm $D$ sao cho $AD = 2\\text{ cm}$.\n  \\item Vẽ đường thẳng vuông góc với $AB$ tại $B$, trên đó lấy điểm $C$ sao cho $BC = 2\\text{ cm}$.\n  \\item Nối $C$ với $D$ ta được hình chữ nhật $ABCD$.\n\\end{itemize}\n\\begin{center}\n\\begin{tikzpicture}[scale=0.9, font=\\small]\n  \\coordinate (A) at (0,2);\n  \\coordinate (B) at (3,2);\n  \\coordinate (C) at (3,0);\n  \\coordinate (D) at (0,0);\n  \\draw[thick, fill=green!10] (A) -- (B) -- (C) -- (D) -- cycle;\n  \\draw (0,1.75) -- (0.25,1.75) -- (0.25,2);\n  \\draw (3,1.75) -- (2.75,1.75) -- (2.75,2);\n  \\draw (3,0.25) -- (2.75,0.25) -- (2.75,0);\n  \\draw (0,0.25) -- (0.25,0.25) -- (0.25,0);\n  \\node[above left] at (A) {$A$};\n  \\node[above right] at (B) {$B$};\n  \\node[below right] at (C) {$C$};\n  \\node[below left] at (D) {$D$};\n  \\node[above] at (1.5,2) {$3\\text{ cm}$};\n  \\node[right] at (3,1) {$2\\text{ cm}$};\n\\end{tikzpicture}\n\\end{center}"
                },
                {
                    "y": "b",
                    "diem_y": "0,75",
                    "noi_dung": "Tính diện tích sân bóng đó.",
                    "loigiai": "Diện tích sân bóng đá của trường THCS A là:\\\\$S = 30 \\cdot 20 = 600\\text{ (m}^2\\text{)}$."
                }
            ]
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Một người bán 6 giỏ cam và xoài. Mỗi giỏ chỉ đựng hoặc cam hoặc xoài với số lượng sau: 34 quả, 39 quả, 40 quả, 41 quả, 42 quả, 46 quả. Sau khi bán một giỏ xoài thì số cam còn lại gấp 4 lần số xoài còn lại. Hãy cho biết giỏ nào đựng cam, giỏ nào đựng xoài?",
            "loigiai": "Tổng số quả trong 6 giỏ là:\\\\$34 + 39 + 40 + 41 + 42 + 46 = 242\\text{ (quả)}$.\\\\Vì số cam còn lại gấp 4 lần số xoài còn lại nên tổng số quả còn lại chia hết cho $1 + 4 = 5$.\\\\Do 242 chia cho 5 dư 2 nên giỏ xoài đã bán phải chứa số quả chia cho 5 dư 2.\\\\Trong 6 giỏ đã cho, chỉ có số $42$ chia cho 5 dư 2 ($42 = 5 \\cdot 8 + 2$). Do đó giỏ xoài đã bán là giỏ 42 quả.\\\\Tổng số quả còn lại là: $242 - 42 = 200\\text{ (quả)}$.\\\\Số quả xoài còn lại là: $200 : 5 = 40\\text{ (quả)}$.\\\\Vậy:\\\\-- Các giỏ đựng xoài gồm: giỏ 42 quả và giỏ 40 quả.\\\\-- Các giỏ đựng cam gồm: giỏ 34 quả, giỏ 39 quả, giỏ 41 quả và giỏ 46 quả."
        }
    ]
}

out_path = r"d:\GitHub\SOANBAI-main\LOP6\DE_THI_GHK1\DE_06\de_06.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved de_06.json successfully!")

