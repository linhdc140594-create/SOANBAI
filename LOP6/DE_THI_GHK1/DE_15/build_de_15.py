# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

data = {
    "de_so": 15,
    "tieu_de": "ĐỀ ÔN TẬP GIỮA KÌ I - MÔN TOÁN 6 - ĐỀ SỐ 15",
    "thoi_gian": "90 phút (không kể thời gian phát đề)",
    "phan_I": [
        {
            "cau": 1,
            "de": "Cho tập hợp $A = \\{a; 5; b; 7\\}$. Cách viết nào sau đây là đúng?",
            "a": "$5 \\in A$",
            "b": "$0 \\in A$",
            "c": "$7 \\notin A$",
            "d": "$a \\notin A$",
            "da": "A",
            "loigiai": "Số 5 là một phần tử thuộc tập hợp $A$ nên cách viết $5 \\in A$ là đúng. Các cách viết còn lại sai vì: $0 \\notin A$, $7 \\in A$, $a \\in A$."
        },
        {
            "cau": 2,
            "de": "Cho hình vẽ sau:\n\\begin{center}\n\\includegraphics[width=0.45\\linewidth]{crops/test_p57_xref3497.png}\n\\end{center}\nTrong hình vẽ trên có:",
            "a": "2 hình thang, 3 hình lục giác đều, 3 hình tam giác đều",
            "b": "2 hình thoi, 3 hình lục giác đều, 2 hình thang cân",
            "c": "3 hình lục giác đều, 2 hình thang cân, 2 hình tam giác đều",
            "d": "2 hình tam giác đều, 1 hình lục giác đều, 4 hình thoi",
            "da": "C",
            "loigiai": "Quan sát các hình cấu tạo nên hình vẽ:\n- 3 hình lục giác đều (phần đầu, ngực, mông).\n- 2 hình thang cân (phần thân giữa).\n- 2 hình tam giác đều (phần chân)."
        },
        {
            "cau": 3,
            "de": "Các số La Mã $\\text{XII; XXIII; XXIX}$ được đọc lần lượt là:",
            "a": "12; 23; 29",
            "b": "12; 23; 28",
            "c": "11; 23; 28",
            "d": "11; 23; 29",
            "da": "A",
            "loigiai": "Ta có:\n- $\\text{XII} = 10 + 2 = 12$.\n- $\\text{XXIII} = 10 + 10 + 3 = 23$.\n- $\\text{XXIX} = 10 + 10 + (10 - 1) = 29$."
        },
        {
            "cau": 4,
            "de": "Cho tập hợp $M = \\{1; 2; 3; 4; 5; 6\\}$. Khẳng định nào sau đây là đúng?",
            "a": "$5 \\in M$",
            "b": "$4 \\notin M$",
            "c": "$8 \\in M$",
            "d": "$6 \\notin M$",
            "da": "A",
            "loigiai": "Số 5 có mặt trong tập hợp $M$ nên khẳng định $5 \\in M$ là đúng."
        },
        {
            "cau": 5,
            "de": "Trong các khẳng định sau, khẳng định nào sai?",
            "a": "$2^3 \\cdot 2^4 = 2^7$",
            "b": "$201^0 = 0$",
            "c": "$5^7 : 5^5 = 25$",
            "d": "$2^4 = 16$",
            "da": "B",
            "loigiai": "Quy ước mọi số tự nhiên khác 0 lũy thừa 0 đều bằng 1 ($a^0 = 1$ với $a \\ne 0$). Do đó $201^0 = 1$, khẳng định \"$201^0 = 0$\" là sai."
        },
        {
            "cau": 6,
            "de": "Giá trị của biểu thức $22 - 2 \\cdot (3^2 + 1)$ bằng:",
            "a": "8",
            "b": "140",
            "c": "200",
            "d": "2",
            "da": "D",
            "loigiai": "Thực hiện phép tính trong ngoặc trước:\n$22 - 2 \\cdot (3^2 + 1) = 22 - 2 \\cdot (9 + 1) = 22 - 2 \\cdot 10 = 22 - 20 = 2$."
        },
        {
            "cau": 7,
            "de": "Số nào sau đây là số nguyên tố?",
            "a": "6",
            "b": "1",
            "c": "7",
            "d": "0",
            "da": "C",
            "loigiai": "Số 7 là số tự nhiên lớn hơn 1 và chỉ có đúng 2 ước là 1 và 7, nên 7 là số nguyên tố."
        },
        {
            "cau": 8,
            "de": "$\\text{ƯCLN}(8, 20, 4)$ là:",
            "a": "1",
            "b": "20",
            "c": "4",
            "d": "8",
            "da": "C",
            "loigiai": "Vì 8 và 20 đều chia hết cho 4 ($8 \\ \\vdots \\ 4$ và $20 \\ \\vdots \\ 4$), nên $\\text{ƯCLN}(8, 20, 4) = 4$."
        },
        {
            "cau": 9,
            "de": "Cho tập hợp $A$ gồm các số tự nhiên nhỏ hơn 5. Tập $A$ được viết là:",
            "a": "$A = \\{1; 2; 3; 4\\}$",
            "b": "$A = \\{0; 1; 2; 3; 4\\}$",
            "c": "$A = \\{1; 2; 3; 4; 5\\}$",
            "d": "$A = \\{0; 1; 2; 3; 4; 5\\}$",
            "da": "B",
            "loigiai": "Các số tự nhiên nhỏ hơn 5 là $0; 1; 2; 3; 4$. Vậy $A = \\{0; 1; 2; 3; 4\\}$."
        },
        {
            "cau": 10,
            "de": "Cho hình vuông $ABCD$. Khẳng định nào sau đây là sai?",
            "a": "Hình vuông $ABCD$ có bốn cạnh bằng nhau: $AB = BC = CD = DA$",
            "b": "Hình vuông $ABCD$ có bốn góc ở mỗi đỉnh $A, B, C, D$ bằng nhau",
            "c": "Hình vuông $ABCD$ có hai đường chéo bằng nhau: $AC = BD$",
            "d": "Hình vuông $ABCD$ có hai cặp cạnh đối song song: $AB$ và $BC$; $CD$ và $DA$",
            "da": "D",
            "loigiai": "$AB$ và $BC$ là hai cạnh kề vuông góc với nhau, không phải hai cạnh đối song song. Hai cặp cạnh đối song song của hình vuông $ABCD$ phải là $AB \\parallel CD$ và $AD \\parallel BC$."
        },
        {
            "cau": 11,
            "de": "Hình thang cân không có tính chất nào dưới đây?",
            "a": "Hai cạnh bên bằng nhau",
            "b": "Hai đường chéo bằng nhau",
            "c": "Hai cạnh đáy song song",
            "d": "Hai góc kề một cạnh bên bằng nhau",
            "da": "D",
            "loigiai": "Trong hình thang cân, hai góc kề một đáy bằng nhau, còn hai góc kề một cạnh bên có tổng bằng $180^\\circ$ (bù nhau). Do đó khẳng định \"Hai góc kề một cạnh bên bằng nhau\" là sai."
        },
        {
            "cau": 12,
            "de": "Trong các số sau: 2; 7; 11; 21, số nào là hợp số?",
            "a": "2",
            "b": "7",
            "c": "21",
            "d": "11",
            "da": "C",
            "loigiai": "Số 21 chia hết cho 1; 3; 7; 21 (có nhiều hơn 2 ước) nên 21 là hợp số. Các số 2; 7; 11 đều là các số nguyên tố."
        }
    ],
    "phan_II": [
        {
            "cau": 1,
            "de": "Cho tập hợp $X = \\{x \\in \\mathbb{N} \\mid 5 \\le x < 10\\}$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Tập hợp $X$ gồm 5 phần tử.",
                "da": "D",
                "giai": "Đúng. Các phần tử của $X$ là $5, 6, 7, 8, 9$, gồm đúng 5 phần tử."
            },
            "y_b": {
                "noi_dung": "Số 10 là một phần tử thuộc tập hợp $X$.",
                "da": "S",
                "giai": "Sai. Vì điều kiện $x < 10$ nên $10 \\notin X$."
            },
            "y_c": {
                "noi_dung": "Giá trị của biểu thức $3^2 + 4^2$ là một phần tử thuộc tập hợp $X$.",
                "da": "S",
                "giai": "Sai. $3^2 + 4^2 = 9 + 16 = 25$. Vì $25 > 10$ nên $25 \\notin X$."
            },
            "y_d": {
                "noi_dung": "Tổng tất cả các phần tử trong tập hợp $X$ bằng 35.",
                "da": "D",
                "giai": "Đúng. Tổng các phần tử là $5 + 6 + 7 + 8 + 9 = 35$."
            }
        },
        {
            "cau": 2,
            "de": "Cho hình tam giác đều $ABC$ có chu vi bằng $18\\text{ cm}$. Xét tính đúng sai của các mệnh đề sau:",
            "y_a": {
                "noi_dung": "Độ dài mỗi cạnh của tam giác $ABC$ là $6\\text{ cm}$.",
                "da": "D",
                "giai": "Đúng. Tam giác đều $ABC$ có 3 cạnh bằng nhau nên mỗi cạnh có độ dài $18 : 3 = 6\\text{ (cm)}$."
            },
            "y_b": {
                "noi_dung": "Ba góc tại các đỉnh $A, B, C$ của tam giác $ABC$ bằng nhau.",
                "da": "D",
                "giai": "Đúng. Tam giác đều có 3 góc ở 3 đỉnh bằng nhau và cùng bằng $60^\\circ$."
            },
            "y_c": {
                "noi_dung": "Ghép 6 tam giác đều bằng nhau có cạnh $6\\text{ cm}$ ta sẽ tạo thành một hình lục giác đều cạnh $6\\text{ cm}$.",
                "da": "D",
                "giai": "Đúng. Ghép 6 tam giác đều bằng nhau chung một đỉnh tạo thành hình lục giác đều có độ dài cạnh bằng cạnh tam giác đều ($6\\text{ cm}$)."
            },
            "y_d": {
                "noi_dung": "Chu vi của hình lục giác đều được tạo thành ở trên là $48\\text{ cm}$.",
                "da": "S",
                "giai": "Sai. Hình lục giác đều có 6 cạnh bằng nhau nên chu vi là $6 \\times 6 = 36\\text{ (cm)}$, không phải $48\\text{ cm}$."
            }
        }
    ],
    "phan_III": [
        {
            "cau": 1,
            "de": "Một trường Trung học cơ sở có 220 học sinh đi tham quan. Nhà trường cần thuê ít nhất bao nhiêu xe ô tô 45 chỗ ngồi để đủ chỗ cho tất cả học sinh?",
            "da": "5",
            "loigiai": "Ta có: $220 : 45 = 4$ (dư 40). Nếu thuê 4 xe thì chỉ chở được 180 học sinh, còn dư 40 học sinh chưa có chỗ ngồi. Do đó nhà trường cần thuê ít nhất $4 + 1 = 5$ xe ô tô. Đáp số: 5."
        },
        {
            "cau": 2,
            "de": "Hình chữ nhật có chiều dài và chiều rộng lần lượt là $6\\text{ cm}$ và $4\\text{ cm}$. Chu vi hình chữ nhật đó là bao nhiêu centimét?",
            "da": "20",
            "loigiai": "Chu vi hình chữ nhật là: $(6 + 4) \\times 2 = 20\\text{ (cm)}$. Đáp số: 20."
        }
    ],
    "phan_IV": [
        {
            "cau": 1,
            "diem": "2,0 điểm",
            "de": "Thực hiện các phép tính sau (tính hợp lý nếu có thể):",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "$270 : 3 : 5 - 4$",
                    "loigiai": "$270 : 3 : 5 - 4 = 90 : 5 - 4 = 18 - 4 = 14$."
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "$9^3 \\cdot 2^3 - 4^2 : 2^4$",
                    "loigiai": "$\\begin{aligned}[t] 9^3 \\cdot 2^3 - 4^2 : 2^4 &= (9 \\cdot 2)^3 - (2^2)^2 : 2^4 \\\\ &= 18^3 - 2^4 : 2^4 \\\\ &= 5832 - 1 = 5831. \\end{aligned}$"
                },
                {
                    "y": "c",
                    "diem_y": "0,5",
                    "noi_dung": "$867 - (167 + 80)$",
                    "loigiai": "$867 - (167 + 80) = 867 - 167 - 80 = 700 - 80 = 620$."
                },
                {
                    "y": "d",
                    "diem_y": "0,5",
                    "noi_dung": "$600 : \\{450 : [450 - (4 \\cdot 5^3 - 2^3 \\cdot 5^2)]\\}$",
                    "loigiai": "$\\begin{aligned}[t] 600 : \\{450 : [450 - (4 \\cdot 5^3 - 2^3 \\cdot 5^2)]\\} &= 600 : \\{450 : [450 - (4 \\cdot 125 - 8 \\cdot 25)]\\} \\\\ &= 600 : \\{450 : [450 - (500 - 200)]\\} \\\\ &= 600 : \\{450 : [450 - 300]\\} \\\\ &= 600 : \\{450 : 150\\} \\\\ &= 600 : 3 = 200. \\end{aligned}$"
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
                    "diem_y": "0,25",
                    "noi_dung": "$x - 15 = 35$",
                    "loigiai": "$x = 35 + 15 \\Rightarrow x = 50$."
                },
                {
                    "y": "b",
                    "diem_y": "0,25",
                    "noi_dung": "$2(x + 15) = 5^2 \\cdot 2$",
                    "loigiai": "$2(x + 15) = 25 \\cdot 2 = 50 \\Rightarrow x + 15 = 50 : 2 = 25 \\Rightarrow x = 25 - 15 = 10$."
                },
                {
                    "y": "c",
                    "diem_y": "0,5",
                    "noi_dung": "$128 - 3(x + 4) = 23$",
                    "loigiai": "$\\begin{aligned}[t] 3(x + 4) &= 128 - 23 = 105 \\\\ x + 4 &= 105 : 3 = 35 \\\\ x &= 35 - 4 = 31. \\end{aligned}$"
                },
                {
                    "y": "d",
                    "diem_y": "0,5",
                    "noi_dung": "$x \\ \\vdots \\ 15$ và $0 < x \\le 60$",
                    "loigiai": "Vì $x \\ \\vdots \\ 15$ nên $x \\in \\text{B}(15) = \\{0; 15; 30; 45; 60; 75; \\dots\\}$.\nKết hợp điều kiện $0 < x \\le 60$, ta được $x \\in \\{15; 30; 45; 60\\}$."
                }
            ]
        },
        {
            "cau": 3,
            "diem": "1,0 điểm",
            "de": "Một nền nhà hình chữ nhật của gia đình bác An có chiều dài là $12\\text{ m}$, chiều rộng là $8\\text{ m}$.",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Tính diện tích nền nhà hình chữ nhật đó.",
                    "loigiai": "Diện tích nền nhà hình chữ nhật là:\n$$S = 12 \\times 8 = 96\\text{ (m}^2\\text{).}$$\nĐáp số: $96\\text{ m}^2$."
                },
                {
                    "y": "b",
                    "diem_y": "0,5",
                    "noi_dung": "Bác An dự định lát nền bằng những viên gạch men hình vuông có cạnh là $40\\text{ cm}$. Hỏi bác An phải dùng hết bao nhiêu viên gạch men để lát kín nền nhà đó? (biết diện tích mạch vữa là không đáng kể).",
                    "loigiai": "Đổi: $96\\text{ m}^2 = 960\\,000\\text{ cm}^2$.\nDiện tích một viên gạch men hình vuông là:\n$$40 \\times 40 = 1600\\text{ (cm}^2\\text{).}$$\nSố viên gạch men bác An cần dùng để lát kín nền nhà là:\n$$960\\,000 : 1600 = 600\\text{ (viên).}$$\nĐáp số: 600 viên gạch."
                }
            ]
        },
        {
            "cau": 4,
            "diem": "0,5 điểm",
            "de": "Cho biểu thức $B = 2 + 21^{21} + 25^{120}$. Chứng minh rằng $B$ là hợp số.",
            "cac_y": [
                {
                    "y": "a",
                    "diem_y": "0,5",
                    "noi_dung": "Chứng minh $B$ là hợp số.",
                    "loigiai": "Xét chữ số tận cùng của từng số hạng trong biểu thức $B$:\n\\begin{itemize}[leftmargin=0.6cm, itemsep=1pt]\n\\item Số 2 có chữ số tận cùng là 2.\n\\item $21^{21}$ có chữ số tận cùng là 1 (vì số có chữ số tận cùng là 1 khi nâng lên lũy thừa bất kỳ luôn tận cùng là 1).\n\\item $25^{120}$ có chữ số tận cùng là 5 (vì số có chữ số tận cùng là 5 khi nâng lên lũy thừa bất kỳ luôn tận cùng là 5).\n\\end{itemize}\nChữ số tận cùng của biểu thức $B$ là chữ số tận cùng của tổng $2 + 1 + 5 = 8$.\nVì $B$ có chữ số tận cùng là 8 nên $B \\ \\vdots \\ 2$.\nMặt khác, $B > 2$ và $B \\ \\vdots \\ 2$ nên ngoài 1 và chính nó, $B$ còn có ước là 2.\nVậy $B$ là hợp số."
                }
            ]
        }
    ]
}

out_path = r"d:\GitHub\SOANBAI-main\LOP6\DE_THI_GHK1\DE_15\de_15.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Ghi thanh cong de_15.json!")

