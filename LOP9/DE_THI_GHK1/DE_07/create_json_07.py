import json

de_07 = {
    "ma_de": "07",
    "lop": "9",
    "mon": "Toán 9",
    "thoi_gian": "90 phút",
    "phan_I": [
        {
            "cau": 1,
            "de": "Phương trình nào sau đây là phương trình bậc nhất hai ẩn?",
            "a": "$-x - y = 0$.",
            "b": "$x^2 - 2y + 1 = 0$.",
            "c": "$\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{2}$.",
            "d": "$x + 2xy - y = 1$.",
            "da": "A",
            "loi_giai": "Phương trình bậc nhất hai ẩn có dạng tổng quát là $ax + by = c$, trong đó các hệ số $a, b$ không đồng thời bằng 0 và các ẩn đều có bậc 1. Do đó $-x - y = 0$ là phương trình bậc nhất hai ẩn."
        },
        {
            "cau": 2,
            "de": "Phương trình $0x + 5y = 10$ có nghiệm tổng quát là:",
            "a": "$(x; 2)$ với $x \\in \\mathbb{R}$.",
            "b": "$(2; y)$ với $y \\in \\mathbb{R}$.",
            "c": "$(x; 0)$ với $x \\in \\mathbb{R}$.",
            "d": "$(0; y)$ với $y \\in \\mathbb{R}$.",
            "da": "A",
            "loi_giai": "Phương trình $0x + 5y = 10 \\iff 5y = 10 \\iff y = 2$. Do ẩn $x$ tùy ý nên nghiệm tổng quát là $(x; 2)$ với $x \\in \\mathbb{R}$."
        },
        {
            "cau": 3,
            "de": "Cặp số nào sau đây là nghiệm của hệ phương trình $\\begin{cases} 2x + y = 3 \\\\ y = 1 \\end{cases}$?",
            "a": "$(2; 1)$.",
            "b": "$(2; -1)$.",
            "c": "$(1; -1)$.",
            "d": "$(1; 1)$.",
            "da": "D",
            "loi_giai": "Thay $y = 1$ vào phương trình thứ nhất: $2x + 1 = 3 \\iff 2x = 2 \\iff x = 1$. Vậy hệ phương trình có nghiệm là $(1; 1)$."
        },
        {
            "cau": 4,
            "de": "Trong các hệ phương trình bậc nhất hai ẩn sau, hệ phương trình nào nhận cặp số $(-1; 3)$ làm nghiệm?",
            "a": "$\\begin{cases} 2x + y = 1 \\\\ -x - y = 2 \\end{cases}$",
            "b": "$\\begin{cases} 3x + y = 8 \\\\ -x + y = 5 \\end{cases}$",
            "c": "$\\begin{cases} x + y = 2 \\\\ 3x - y = -6 \\end{cases}$",
            "d": "$\\begin{cases} 2x - y = 5 \\\\ 4x + 2y = 2 \\end{cases}$",
            "da": "C",
            "loi_giai": "Thay $x = -1, y = 3$ vào hệ ở phương án C: $-1 + 3 = 2$ (đúng) và $3(-1) - 3 = -6$ (đúng). Do đó $(-1; 3)$ là nghiệm của hệ phương trình này."
        },
        {
            "cau": 5,
            "de": "Biết rằng hệ phương trình $\\begin{cases} 5x - y = 8 \\\\ 3x - ay = 1 \\end{cases}$ có nghiệm $(2; 2)$. Giá trị của $a$ là:",
            "a": "$a = -\\frac{1}{2}$.",
            "b": "$a = \\frac{5}{2}$.",
            "c": "$a = 1$.",
            "d": "$a = -2$.",
            "da": "B",
            "loi_giai": "Thay $(x; y) = (2; 2)$ vào phương trình thứ hai ta được: $3(2) - a(2) = 1 \\iff 6 - 2a = 1 \\iff 2a = 5 \\iff a = \\frac{5}{2}$."
        },
        {
            "cau": 6,
            "de": "Phương trình $(x - 7)(x + 2) = 0$ có nghiệm là:",
            "a": "$x = 7; x = 2$.",
            "b": "$x = 7; x = -2$.",
            "c": "$x = -7; x = 2$.",
            "d": "$x = -7; x = -2$.",
            "da": "B",
            "loi_giai": "Ta có $(x - 7)(x + 2) = 0 \\iff x - 7 = 0$ hoặc $x + 2 = 0 \\iff x = 7$ hoặc $x = -2$."
        },
        {
            "cau": 7,
            "de": "Cho tam giác $MNP$ vuông tại $N$. Hệ thức nào sau đây là đúng?",
            "a": "$MN = MP \\cdot \\sin P$.",
            "b": "$MN = MP \\cdot \\cos P$.",
            "c": "$MN = MP \\cdot \\tan P$.",
            "d": "$MN = MP \\cdot \\cot P$.",
            "da": "A",
            "loi_giai": "Trong tam giác vuông $MNP$ vuông tại $N$, cạnh đối của góc $P$ là $MN$ và cạnh huyền là $MP$. Khi đó $\\sin P = \\frac{MN}{MP} \\implies MN = MP \\cdot \\sin P$."
        },
        {
            "cau": 8,
            "de": "Cho đường tròn $(O)$ có hai bán kính $OA, OB$ tạo thành góc ở tâm $\\widehat{AOB} = 60^\\circ$. Điểm $n$ nằm trên cung nhỏ $AB$, điểm $m$ nằm trên cung lớn $AB$. Số đo các cung $AnB$ và $AmB$ lần lượt là:",
            "a": "$120^\\circ$ và $300^\\circ$.",
            "b": "$60^\\circ$ và $60^\\circ$.",
            "c": "$60^\\circ$ và $300^\\circ$.",
            "d": "$60^\\circ$ và $120^\\circ$.",
            "da": "C",
            "loi_giai": "Góc ở tâm $\\widehat{AOB} = 60^\\circ$ chắn cung nhỏ $AnB$ nên $\\text{sđ}\\wideparen{AnB} = 60^\\circ$. Số đo cung lớn $AmB$ bằng $360^\\circ - 60^\\circ = 300^\\circ$."
        },
        {
            "cau": 9,
            "de": "Một cột đèn có bóng trên mặt đất dài $7{,}2\\text{ m}$. Các tia nắng mặt trời tạo với mặt đất một góc xấp xỉ $42^\\circ$. Chiều cao xấp xỉ của cột đèn là:",
            "a": "$6{,}48\\text{ m}$.",
            "b": "$8\\text{ m}$.",
            "c": "$4{,}82\\text{ m}$.",
            "d": "$5{,}35\\text{ m}$.",
            "da": "A",
            "loi_giai": "Gọi $h$ là chiều cao cột đèn. Áp dụng tỉ số lượng giác trong tam giác vuông: $h = 7{,}2 \\cdot \\tan 42^\\circ \\approx 7{,}2 \\cdot 0{,}9004 \\approx 6{,}48\\text{ m}$."
        },
        {
            "cau": 10,
            "de": "Kết quả rút gọn của biểu thức $\\sqrt[3]{8} + \\sqrt[3]{-27} + \\sqrt[3]{-64}$ là:",
            "a": "$5$.",
            "b": "$-5$.",
            "c": "$9$.",
            "d": "$-9$.",
            "da": "B",
            "loi_giai": "Ta có $\\sqrt[3]{8} = 2$, $\\sqrt[3]{-27} = -3$, $\\sqrt[3]{-64} = -4$. Thay vào biểu thức: $2 + (-3) + (-4) = -5$."
        },
        {
            "cau": 11,
            "de": "Cho tam giác $MNE$ vuông tại $M$, đường cao $MH$. Hệ thức nào sau đây là đúng?",
            "a": "$\\frac{1}{MH^2} = \\frac{1}{MN^2} + \\frac{1}{ME^2}$.",
            "b": "$MH^2 = MN^2 + ME^2$.",
            "c": "$\\frac{1}{MH} = \\frac{1}{MN} + \\frac{1}{ME}$.",
            "d": "$MH^2 = NE \\cdot HE$.",
            "da": "A",
            "loi_giai": "Theo hệ thức lượng trong tam giác vuông, nghịch đảo bình phương đường cao ứng với cạnh huyền bằng tổng các nghịch đảo bình phương của hai cạnh góc vuông: $\\frac{1}{MH^2} = \\frac{1}{MN^2} + \\frac{1}{ME^2}$."
        },
        {
            "cau": 12,
            "de": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$, có $AB = 12\\text{ cm}, BC = 20\\text{ cm}$. Độ dài $BH, CH$ lần lượt là:",
            "a": "$BH = 7{,}2\\text{ cm}; CH = 11{,}8\\text{ cm}$.",
            "b": "$BH = 9{,}2\\text{ cm}; CH = 10{,}8\\text{ cm}$.",
            "c": "$BH = 7{,}2\\text{ cm}; CH = 12{,}8\\text{ cm}$.",
            "d": "$BH = 7{,}2\\text{ cm}; CH = 12\\text{ cm}$.",
            "da": "C",
            "loi_giai": "Áp dụng hệ thức lượng $AB^2 = BH \\cdot BC \\implies BH = \\frac{AB^2}{BC} = \\frac{12^2}{20} = \\frac{144}{20} = 7{,}2\\text{ cm}$. Khi đó $CH = BC - BH = 20 - 7{,}2 = 12{,}8\\text{ cm}$."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho bất đẳng thức $a > b$. Xét tính Đúng/Sai của các khẳng định sau:",
            "y_a": {"noi_dung": "$a - 4 > b - 4$.", "dung": True, "loi_giai": "Cộng cả hai vế của bất đẳng thức $a > b$ với $-4$ ta được $a - 4 > b - 4$."},
            "y_b": {"noi_dung": "$-3a > -3b$.", "dung": False, "loi_giai": "Nhân cả hai vế của $a > b$ với số âm $-3$ thì bất đẳng thức đổi chiều: $-3a < -3b$. Do đó khẳng định này Sai."},
            "y_c": {"noi_dung": "$-2a + 3 < -2b + 3$.", "dung": True, "loi_giai": "Vì $a > b \\implies -2a < -2b \\implies -2a + 3 < -2b + 3$. Do đó khẳng định này Đúng."},
            "y_d": {"noi_dung": "$5a - 1 > 5b - 2$.", "dung": True, "loi_giai": "Vì $a > b \\implies 5a > 5b$. Lại có $-1 > -2$. Cộng từng vế hai bất đẳng thức cùng chiều: $5a - 1 > 5b - 2$. Do đó khẳng định này Đúng."}
        },
        {
            "cau": 2,
            "de": "Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AC = 6\\text{ cm}, BC = 10\\text{ cm}$. Xét tính Đúng/Sai của các khẳng định sau:",
            "y_a": {"noi_dung": "$\\sin B = \\frac{3}{5}$.", "dung": True, "loi_giai": "Ta có $\\sin B = \\frac{AC}{BC} = \\frac{6}{10} = \\frac{3}{5}$. Khẳng định Đúng."},
            "y_b": {"noi_dung": "$\\tan C = \\frac{3}{4}$.", "dung": False, "loi_giai": "Áp dụng định lí Pythagore: $AB = \\sqrt{BC^2 - AC^2} = \\sqrt{10^2 - 6^2} = 8\\text{ cm}$. Khi đó $\\tan C = \\frac{AB}{AC} = \\frac{8}{6} = \\frac{4}{3} \\neq \\frac{3}{4}$. Khẳng định Sai."},
            "y_c": {"noi_dung": "$AH = 4{,}8\\text{ cm}$.", "dung": True, "loi_giai": "Áp dụng hệ thức lượng $AH \\cdot BC = AB \\cdot AC \\implies AH = \\frac{8 \\cdot 6}{10} = 4{,}8\\text{ cm}$. Khẳng định Đúng."},
            "y_d": {"noi_dung": "Chu vi của tam giác $ABH$ bằng $14{,}4\\text{ cm}$.", "dung": False, "loi_giai": "Ta có $BH = \\frac{AB^2}{BC} = \\frac{8^2}{10} = 6{,}4\\text{ cm}$. Chu vi tam giác $ABH$ bằng $AB + BH + AH = 8 + 6{,}4 + 4{,}8 = 19{,}2\\text{ cm} \\neq 14{,}4\\text{ cm}$. Khẳng định Sai."}
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Trong các phương trình sau:\\par (1) $3\\sqrt{y} - 2x = 0$; \\quad (2) $2x + y = 0$; \\quad (3) $x^2 - y^2 = 12$; \\quad (4) $2x + y + 3z = 0$.\\par Phương trình bậc nhất hai ẩn là phương trình số mấy?",
            "da": "Phương trình (2)",
            "loi_giai": "Phương trình bậc nhất hai ẩn có dạng $ax + by = c$ ($a, b$ không đồng thời bằng 0). Do đó chỉ có phương trình (2) thỏa mãn."
        },
        {
            "cau": 2,
            "de": "Cho tam giác $ABC$ vuông tại $A$, biết $AB = 12\\text{ cm}, AC = 9\\text{ cm}, BC = 15\\text{ cm}$. Tính số đo góc $B$ (làm tròn đến độ).",
            "da": "$37^\\circ$",
            "loi_giai": "Xét tam giác $ABC$ vuông tại $A$, ta có $\\cos B = \\frac{AB}{BC} = \\frac{12}{15} = 0{,}8$. Suy ra $\\widehat{B} = \\arccos(0{,}8) \\approx 37^\\circ$."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "2,0 điểm",
            "de": "Giải các phương trình và hệ phương trình sau:\\par a) $(4x + 5)(3x - 2) = 0$.\\par b) $\\frac{4}{x(x - 1)} + \\frac{3}{x} = \\frac{4}{x - 1}$.\\par c) $\\begin{cases} x - 3y = 4 \\\\ -2x + 6y = -8. \\end{cases}$",
            "loi_giai": "a) $(4x + 5)(3x - 2) = 0 \\iff 4x + 5 = 0$ hoặc $3x - 2 = 0 \\iff x = -\\frac{5}{4}$ hoặc $x = \\frac{2}{3}$.\\par Vậy tập nghiệm của phương trình là $S = \\left\\{-\\frac{5}{4}; \\frac{2}{3}\\right\\}$.\\par b) Điều kiện xác định: $x \\neq 0$ và $x \\neq 1$.\\par Quy đồng mẫu thức chung $x(x - 1)$ và khử mẫu:\\par $4 + 3(x - 1) = 4x \\iff 4 + 3x - 3 = 4x \\iff 3x + 1 = 4x \\iff x = 1$ (không thỏa mãn ĐKXĐ).\\par Vậy phương trình vô nghiệm.\\par c) $\\begin{cases} x - 3y = 4 \\quad (1) \\\\ -2x + 6y = -8 \\quad (2) \\end{cases}$\\par Nhân hai vế của phương trình (1) với 2 ta được: $\\begin{cases} 2x - 6y = 8 \\\\ -2x + 6y = -8 \\end{cases}$\\par Cộng vế theo vế hai phương trình ta được $0x + 0y = 0$ (luôn đúng với mọi $x, y$).\\par Vậy hệ phương trình có vô số nghiệm với nghiệm tổng quát: $\\left(x; \\frac{x - 4}{3}\\right)$ với $x \\in \\mathbb{R}$."
        },
        {
            "cau": 2,
            "diem": "1,5 điểm",
            "de": "Người ta cho thêm $1\\text{ kg}$ nước vào dung dịch $A$ (chứa axit $X$) thì được dung dịch $B$ có nồng độ axit là $20\\%$. Sau đó lại cho thêm $1\\text{ kg}$ axit $X$ vào dung dịch $B$ thì được dung dịch $C$ có nồng độ axit là $33\\frac{1}{3}\\%$. Tính nồng độ axit của dung dịch $A$ ban đầu.",
            "loi_giai": "Gọi khối lượng dung dịch $A$ là $x\\text{ (kg)}$ và khối lượng axit nguyên chất là $y\\text{ (kg)}$ ($x > y > 0$).\\par Khi thêm $1\\text{ kg}$ nước, khối lượng dung dịch $B$ là $x + 1\\text{ (kg)}$. Nồng độ axit trong $B$ là $20\\%$ nên:\\par $\\frac{y}{x + 1} = 20\\% = \\frac{1}{5} \\implies x + 1 = 5y \\iff x - 5y = -1 \\quad (1)$\\par Khi thêm tiếp $1\\text{ kg}$ axit vào dung dịch $B$, khối lượng axit là $y + 1\\text{ (kg)}$ và khối lượng dung dịch $C$ là $x + 1 + 1 = x + 2\\text{ (kg)}$. Nồng độ dung dịch $C$ là $33\\frac{1}{3}\\% = \\frac{1}{3}$ nên:\\par $\\frac{y + 1}{x + 2} = \\frac{1}{3} \\implies 3(y + 1) = x + 2 \\iff x - 3y = 1 \\quad (2)$\\par Từ (1) và (2) ta có hệ phương trình: $\\begin{cases} x - 5y = -1 \\\\ x - 3y = 1 \\end{cases}$\\par Lấy phương trình thứ hai trừ phương trình thứ nhất vế theo vế ta được: $2y = 2 \\implies y = 1$ (kg).\\par Thay $y = 1$ vào (2): $x = 3(1) + 1 = 4$ (kg) (thỏa mãn điều kiện).\\par Nồng độ axit của dung dịch $A$ ban đầu là: $\\frac{y}{x} = \\frac{1}{4} = 25\\%$.\\par Vậy nồng độ axit của dung dịch $A$ là $25\\%$."
        },
        {
            "cau": 3,
            "diem": "1,0 điểm",
            "de": "Một cầu trượt trong công viên có độ dốc là $28^\\circ$ và có độ cao là $2{,}1\\text{ m}$. Tính độ dài của mặt cầu trượt (làm tròn đến chữ số thập phân thứ nhất).",
            "loi_giai": "Mô hình hóa bài toán bằng tam giác $ABC$ vuông tại $A$, trong đó:\\par - $AB$ là chiều cao của cầu trượt: $AB = 2{,}1\\text{ m}$.\\par - Góc nghiêng dốc của cầu trượt là góc nhọn $\\widehat{C} = 28^\\circ$.\\par - $BC$ là độ dài của mặt cầu trượt (cạnh huyền).\\par Xét tam giác $ABC$ vuông tại $A$, ta có:\\par $\\sin C = \\frac{AB}{BC} \\implies BC = \\frac{AB}{\\sin C} = \\frac{2{,}1}{\\sin 28^\\circ} \\approx \\frac{2{,}1}{0{,}4695} \\approx 4{,}47\\text{ m}$.\\par Làm tròn đến chữ số thập phân thứ nhất, độ dài của mặt cầu trượt khoảng $4{,}5\\text{ m}$."
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Cho tam giác $ABC$ vuông tại $A$. Chứng minh rằng $\\sin^2 B + \\sin^2 C = 1$.",
            "loi_giai": "Trong tam giác $ABC$ vuông tại $A$, hai góc nhọn $B$ và $C$ phụ nhau, tức là $\\widehat{B} + \\widehat{C} = 90^\\circ$.\\par Theo tính chất tỉ số lượng giác của hai góc phụ nhau, ta có: $\\sin C = \\cos B$.\\par Thay vào vế trái của biểu thức ta được:\\par $\\sin^2 B + \\sin^2 C = \\sin^2 B + \\cos^2 B$.\\par Mặt khác, theo định nghĩa tỉ số lượng giác trong tam giác vuông $ABC$:\\par $\\sin B = \\frac{AC}{BC},\\; \\cos B = \\frac{AB}{BC} \\implies \\sin^2 B + \\cos^2 B = \\frac{AC^2 + AB^2}{BC^2}$.\\par Áp dụng định lí Pythagore: $AB^2 + AC^2 = BC^2$, suy ra:\\par $\\sin^2 B + \\cos^2 B = \\frac{BC^2}{BC^2} = 1$.\\par Vậy $\\sin^2 B + \\sin^2 C = 1$ (đpcm)."
        }
    ]
}

with open('d:/GitHub/SOANBAI-main/LOP9/DE_THI_GHK1/DE_07/de_07.json', 'w', encoding='utf-8') as f:
    json.dump(de_07, f, ensure_ascii=False, indent=2)

print('Generated DE_07/de_07.json successfully!')

