import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": "08",
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I 2026 – 2027",
    "mon": "Toán 6",
    "thoi_gian": "90 phút",
    "phan_I": [
        {
            "cau": 1,
            "de": "Trong các số $23\\,755; 10\\,230; 17\\,280; 18\\,711$, số nào chia hết cho cả $2; 3; 5; 9$?",
            "a": "$23\\,755$.",
            "b": "$10\\,230$.",
            "c": "$17\\,280$.",
            "d": "$18\\,711$.",
            "da": "C",
            "loigiai": "Số chia hết cho cả 2 và 5 có chữ số tận cùng là 0, do đó chỉ xét $10\\,230$ và $17\\,280$.\\\\Xét tổng các chữ số:\\\\-- Số $10\\,230$ có tổng chữ số là $1 + 0 + 2 + 3 + 0 = 6$ (không chia hết cho 9).\\\\-- Số $17\\,280$ có tổng chữ số là $1 + 7 + 2 + 8 + 0 = 18$ (chia hết cho 9).\\\\Vậy số chia hết cho cả $2; 3; 5; 9$ là $17\\,280$."
        },
        {
            "cau": 2,
            "de": "Cho $A = \\{x \\in \\mathbb{N}^* \\mid x \\le 12\\}$. Tập hợp $A$ có số phần tử là:",
            "a": "$10$.",
            "b": "$11$.",
            "c": "$12$.",
            "d": "$13$.",
            "da": "C",
            "loigiai": "Các số tự nhiên khác 0 nhỏ hơn hoặc bằng 12 là $A = \\{1; 2; 3; \\dots; 12\\}$. Tập hợp $A$ có 12 phần tử."
        },
        {
            "cau": 3,
            "de": "Cho $18 \\ \\vdots \\ x$ và $7 \\le x < 18$. Khi đó $x$ có giá trị là:",
            "a": "$2$.",
            "b": "$3$.",
            "c": "$6$.",
            "d": "$9$.",
            "da": "D",
            "loigiai": "Các ước của 18 là $\\{1; 2; 3; 6; 9; 18\\}$. Giá trị thỏa mãn $7 \\le x < 18$ là $x = 9$."
        },
        {
            "cau": 4,
            "de": "Số nào sau đây không phải số nguyên tố?",
            "a": "$11$.",
            "b": "$33$.",
            "c": "$17$.",
            "d": "$31$.",
            "da": "B",
            "loigiai": "Số $33$ chia hết cho 3 và 11 nên là hợp số."
        },
        {
            "cau": 5,
            "de": "Phân tích số $40$ ra thừa số nguyên tố ta được kết quả đúng là:",
            "a": "$2 \\cdot 4 \\cdot 5$.",
            "b": "$2^3 \\cdot 5$.",
            "c": "$5 \\cdot 8$.",
            "d": "$4 \\cdot 10$.",
            "da": "B",
            "loigiai": "Ta có: $40 = 8 \\cdot 5 = 2^3 \\cdot 5$."
        },
        {
            "cau": 6,
            "de": "Cho hình lục giác đều $ABCDEG$ tâm $O$. Khẳng định nào sau đây là đúng?",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.9, font=\\small]\n  \\coordinate (O) at (0,0);\n  \\foreach \\i/\\name in {0/C, 60/D, 120/E, 180/G, 240/A, 300/B} {\n    \\coordinate (\\name) at (\\i:1.8);\n  }\n  \\draw[thick, fill=orange!5] (A) -- (B) -- (C) -- (D) -- (E) -- (G) -- cycle;\n  \\draw[thick] (A) -- (D);\n  \\draw[thick] (B) -- (E);\n  \\draw[thick] (C) -- (G);\n  \\filldraw (O) circle (1.5pt) node[below=2pt] {$O$};\n  \\filldraw (A) circle (1.5pt) node[below left] {$A$};\n  \\filldraw (B) circle (1.5pt) node[below right] {$B$};\n  \\filldraw (C) circle (1.5pt) node[right] {$C$};\n  \\filldraw (D) circle (1.5pt) node[above right] {$D$};\n  \\filldraw (E) circle (1.5pt) node[above left] {$E$};\n  \\filldraw (G) circle (1.5pt) node[left] {$G$};\n\\end{tikzpicture}\n\\end{center}",
            "a": "$OA = OB = OC = OD = OE = OG$.",
            "b": "$OA < OB < OC < OD < OE < OG$.",
            "c": "$OA > OB > OC > OD > OE > OG$.",
            "d": "$OA \\ne OB \\ne OC \\ne OD \\ne OE \\ne OG$.",
            "da": "A",
            "loigiai": "Trong lục giác đều, khoảng cách từ tâm $O$ đến các đỉnh đều bằng nhau: $OA = OB = OC = OD = OE = OG$."
        },
        {
            "cau": 7,
            "de": "Khẳng định nào sau đây là sai?",
            "a": "Hình chữ nhật và hình thoi có các cặp cạnh đối song song với nhau.",
            "b": "Hình lục giác đều có ba đường chéo chính bằng nhau.",
            "c": "Hình bình hành có các cạnh đối bằng nhau.",
            "d": "Hình thoi có hai đường chéo bằng nhau.",
            "da": "D",
            "loigiai": "Hai đường chéo của hình thoi vuông góc với nhau tại trung điểm mỗi đường chứ nói chung không bằng nhau (chỉ bằng nhau khi hình thoi là hình vuông)."
        },
        {
            "cau": 8,
            "de": "Hình nào sau đây có tất cả các góc ở đỉnh bằng nhau?",
            "a": "Hình thoi.",
            "b": "Hình chữ nhật.",
            "c": "Hình bình hành.",
            "d": "Hình thang cân.",
            "da": "B",
            "loigiai": "Hình chữ nhật có bốn góc ở đỉnh bằng nhau và đều bằng $90^\\circ$."
        },
        {
            "cau": 9,
            "de": "Một hình thang cân có độ dài hai đáy là $a, b$ và chiều cao là $h$. Công thức tính diện tích hình thang đó là:",
            "a": "$S = \\dfrac{(a+b) \\cdot h}{2}$.",
            "b": "$S = \\dfrac{(a-b) \\cdot h}{2}$.",
            "c": "$S = 2(a+b) \\cdot h$.",
            "d": "$S = \\dfrac{a+b}{2} \\cdot h^2$.",
            "da": "A",
            "loigiai": "Diện tích hình thang bằng tổng độ dài hai đáy nhân với chiều cao rồi chia cho 2: $S = \\dfrac{(a+b) \\cdot h}{2}$."
        },
        {
            "cau": 10,
            "de": "Cho hình thoi $ABCD$, hai đường chéo $AC$ và $BD$ của hình thoi:",
            "a": "Bằng nhau.",
            "b": "Không vuông góc.",
            "c": "Vuông góc với nhau.",
            "d": "Cả A và B đều đúng.",
            "da": "C",
            "loigiai": "Hai đường chéo của hình thoi luôn vuông góc với nhau."
        },
        {
            "cau": 11,
            "de": "Viết gọn tích $8 \\cdot 8 \\cdot 2 \\cdot 4$ dưới dạng lũy thừa cơ số 8 là:",
            "a": "$8$.",
            "b": "$8^2$.",
            "c": "$8^3$.",
            "d": "$8^4$.",
            "da": "C",
            "loigiai": "Ta có $2 \\cdot 4 = 8$, do đó: $8 \\cdot 8 \\cdot 2 \\cdot 4 = 8 \\cdot 8 \\cdot 8 = 8^3$."
        },
        {
            "cau": 12,
            "de": "Một mảnh vườn hình chữ nhật có chiều dài $5\\text{ m}$, chiều rộng $3\\text{ m}$. Bác Bình muốn rào kín xung quanh mảnh vườn. Hỏi chiều dài hàng rào cần dùng là bao nhiêu mét?",
            "hinh_ve": "\\begin{center}\n\\begin{tikzpicture}[scale=0.8, font=\\small]\n  \\coordinate (A) at (0,2);\n  \\coordinate (B) at (3.5,2);\n  \\coordinate (C) at (3.5,0);\n  \\coordinate (D) at (0,0);\n  \\draw[thick, fill=green!15] (A) -- (B) -- (C) -- (D) -- cycle;\n  \\node[above] at (1.75,2) {$5\\text{ m}$};\n  \\node[right] at (3.5,1) {$3\\text{ m}$};\n\\end{tikzpicture}\n\\end{center}",
            "a": "$16\\text{ m}$.",
            "b": "$10\\text{ m}$.",
            "c": "$8\\text{ m}$.",
            "d": "$6\\text{ m}$.",
            "da": "A",
            "loigiai": "Chiều dài hàng rào chính là chu vi của mảnh vườn hình chữ nhật:\\\\$\\mathcal{P} = (5 + 3) \\cdot 2 = 16\\text{ (m)}$."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho các hình sau: tam giác đều, hình vuông, lục giác đều, hình chữ nhật, hình thoi, hình bình hành, hình thang cân. Xét tính đúng/sai của các khẳng định sau:",
            "y_a": {"noi_dung": "Hình tam giác đều, hình vuông, hình lục giác đều có tất cả các cạnh bằng nhau.", "da": "D", "giai": "Đúng. Tam giác đều, hình vuông và lục giác đều đều có đặc điểm là tất cả các cạnh bằng nhau."},
            "y_b": {"noi_dung": "Có đúng 2 hình có hai đường chéo vuông góc với nhau.", "da": "D", "giai": "Đúng. Hai hình có hai đường chéo vuông góc với nhau là hình vuông và hình thoi."},
            "y_c": {"noi_dung": "Có đúng 3 hình có các cạnh đối song song và hai đường chéo bằng nhau.", "da": "D", "giai": "Đúng. Ba hình thỏa mãn điều kiện có hai cạnh đối song song và hai đường chéo bằng nhau là hình chữ nhật, hình vuông và hình thang cân."},
            "y_d": {"noi_dung": "Hình lục giác đều có độ dài mọi đường chéo đều gấp đôi độ dài cạnh.", "da": "S", "giai": "Sai. Trong lục giác đều, chỉ có 3 đường chéo chính mới có độ dài gấp đôi cạnh, các đường chéo phụ không có tính chất này."}
        },
        {
            "cau": 2,
            "de": "Một chiếc ô tô đang di chuyển với vận tốc ban đầu là $10\\text{ km/h}$. Sau mỗi giờ, vận tốc tăng gấp đôi. Xét tính đúng/sai của các khẳng định sau:",
            "y_a": {"noi_dung": "Sau 1 giờ, vận tốc ô tô là $20\\text{ km/h}$.", "da": "D", "giai": "Đúng. Vận tốc ban đầu là $10\\text{ km/h}$, sau 1 giờ đạt $10 \\cdot 2 = 20\\text{ km/h}$."},
            "y_b": {"noi_dung": "Sau 2 giờ, vận tốc ô tô là $30\\text{ km/h}$.", "da": "S", "giai": "Sai. Sau 2 giờ, vận tốc tăng gấp đôi so với giờ thứ nhất, đạt $20 \\cdot 2 = 40\\text{ km/h}$."},
            "y_c": {"noi_dung": "Sau 3 giờ, vận tốc ô tô là $80\\text{ km/h}$.", "da": "D", "giai": "Đúng. Sau 3 giờ, vận tốc đạt $40 \\cdot 2 = 80\\text{ km/h}$."},
            "y_d": {"noi_dung": "Sau 4 giờ, vận tốc ô tô là $160\\text{ km/h}$.", "da": "D", "giai": "Đúng. Sau 4 giờ, vận tốc đạt $80 \\cdot 2 = 160\\text{ km/h}$."}
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Có bao nhiêu số tự nhiên $m$ sao cho $5 < m < 10$ và $m$ chia hết cho 3?",
            "da": "2",
            "loigiai": "Các số tự nhiên $m$ thỏa mãn $5 < m < 10$ là $\\{6; 7; 8; 9\\}$.\\\\Trong các số trên, các số chia hết cho 3 là 6 và 9.\\\\Vậy có 2 số tự nhiên thỏa mãn đề bài."
        },
        {
            "cau": 2,
            "de": "Một hình chữ nhật có diện tích là $120\\text{ cm}^2$ và có chiều dài là $12\\text{ cm}$. Tính độ dài chiều rộng của hình chữ nhật đó (theo đơn vị $\\text{cm}$).",
            "da": "10",
            "loigiai": "Độ dài chiều rộng của hình chữ nhật là: $120 : 12 = 10\\text{ (cm)}$."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "1,0 điểm",
            "de": "Thực hiện phép tính (Tính nhanh nếu có thể):",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "$127 + 156 + 73 + 144$",
                    "loigiai": "$(127 + 73) + (156 + 144) = 200 + 300 = 500$."
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "$2026 - (20 \\cdot 3^2 + 16 : 2^2)$",
                    "loigiai": "$2026 - (20 \\cdot 9 + 16 : 4) = 2026 - (180 + 4) = 2026 - 184 = 1842$."
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
                    "diem_y": "0,5",
                    "noi_dung": "$x - 18 = 15$",
                    "loigiai": "$x = 15 + 18 \\Rightarrow x = 33$."
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "$18 + 2(x - 1) = 40$",
                    "loigiai": "$2(x - 1) = 40 - 18 \\Rightarrow 2(x - 1) = 22 \\Rightarrow x - 1 = 11 \\Rightarrow x = 12$."
                }
            ]
        },
        {
            "cau": 3,
            "diem": "0,5 điểm",
            "de": "Một hình chữ nhật có diện tích là $220\\text{ cm}^2$ và có chiều dài là $22\\text{ cm}$. Tính độ dài chiều rộng của hình chữ nhật (theo đơn vị $\\text{cm}$).",
            "loigiai": "Chiều rộng của hình chữ nhật là:\\\\$220 : 22 = 10\\text{ (cm)}$."
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Không thực hiện tính tổng, chứng minh rằng biểu thức sau chia hết cho 21:\\\\$A = 1 + 4 + 4^2 + 4^3 + \\dots + 4^{2021}$",
            "loigiai": "Tổng $A$ có $2021 - 0 + 1 = 2022$ số hạng. Vì 2022 chia hết cho 3 nên ta nhóm 3 số hạng liên tiếp vào một nhóm:\n\\begin{align*}\nA &= (1 + 4 + 4^2) + (4^3 + 4^4 + 4^5) + \\dots + (4^{2019} + 4^{2020} + 4^{2021})\\\\\n&= (1 + 4 + 16) + 4^3 \\cdot (1 + 4 + 16) + \\dots + 4^{2019} \\cdot (1 + 4 + 16)\\\\\n&= 21 + 4^3 \\cdot 21 + \\dots + 4^{2019} \\cdot 21\\\\\n&= 21 \\cdot (1 + 4^3 + \\dots + 4^{2019})\n\\end{align*}\nVì tích có thừa số 21 nên $A \\ \\vdots \\ 21$ (đpcm)."
        }
    ]
}

out_path = r"d:\GitHub\SOANBAI-main\LOP6\DE_THI_GHK1\DE_08\de_08.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved de_08.json successfully!")

