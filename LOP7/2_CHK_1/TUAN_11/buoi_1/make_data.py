import json
import os

CUR_DIR = r"d:\4. GitHub\PHIEU_KIEM_TRA_THCS\LOP7\2_CHK_1\TUAN_11\buoi_1"

data = {
    "base_filename": "Phieu_Kiem_Tra_Tuan_11_Buoi_01",
    "title_p1": "PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 11 - BUỔI 01",
    "title_p2": "TOÁN 7 - TUẦN 11 - BUỔI 01",
    "codes": {
        "101": {
            "short": [
                [
                    "Trong $\\Delta ABC$, góc xen giữa hai cạnh $AB$ và $BC$ là:",
                    "\\widehat{B}"
                ],
                [
                    "Để $\\Delta ABC = \\Delta DEF$ (c.g.c) khi $AB=DE, AC=DF$, cần thêm:",
                    "\\widehat{A} = \\widehat{D}"
                ],
                [
                    "Cho $\\Delta ABC = \\Delta MNP$ (c.g.c), $\\widehat{A}=55^\\circ, \\widehat{B}=65^\\circ$. Khi đó $\\widehat{P}$ bằng:",
                    "60^\\circ"
                ],
                [
                    "Cho $\\Delta ABC = \\Delta MNP$ (c.g.c), biết $BC = 7\\text{ cm}$. Độ dài cạnh $NP$ là:",
                    "7\\text{ cm}"
                ],
                [
                    "Giá trị của căn bậc hai số học $\\sqrt{144} - \\sqrt{49}$ bằng:",
                    "5"
                ],
                [
                    "Tìm số hữu tỉ $x > 0$, biết $\\left|x - \\dfrac{1}{2}\\right| = \\dfrac{3}{2}$:",
                    "x = 2"
                ],
                [
                    "Cho $\\Delta ABC, \\Delta DEF$ vuông tại $A, D$, có $AB=DE$. Cần thêm điều kiện:",
                    "AC = DF"
                ],
                [
                    "Cho $\\Delta OAB = \\Delta OCD$, biết $CD = 38\\text{ m}$. Độ dài cạnh $AB$ là:",
                    "38\\text{ m}"
                ],
                [
                    "Giá trị của biểu thức $\\left(-\\dfrac{1}{3}\\right)^2 \\cdot 9 + (-1)^{2026}$ bằng:",
                    "2"
                ],
                [
                    "Cho $AB$ cắt $CD$ tại trung điểm $O$ mỗi đoạn. Khi đó $\\Delta OAC$ bằng:",
                    "\\Delta OBD"
                ]
            ],
            "q11": {
                "a": "$\\dfrac{5}{13} + \\dfrac{4}{7} + \\dfrac{8}{13} - \\dfrac{11}{7}$",
                "b": "$\\dfrac{4}{7} \\cdot \\left(-\\dfrac{2}{5}\\right) + \\dfrac{4}{7} \\cdot \\left(-\\dfrac{3}{5}\\right) + \\dfrac{11}{7}$",
                "c": "$\\left(-\\dfrac{1}{2}\\right)^3 : \\dfrac{1}{4} + \\left(\\dfrac{3}{4}\\right)^0$",
                "d": "$\\sqrt{\\dfrac{16}{25}} - \\left|-\\dfrac{2}{5}\\right| + \\sqrt{\\dfrac{4}{25}}$",
                "e": "$\\dfrac{3}{4} - \\left[ \\dfrac{1}{2} + \\left(\\dfrac{3}{8} - \\dfrac{5}{8}\\right) \\right]$",
                "f": "$\\dfrac{4^3 \\cdot 9^2}{6^4}$"
            },
            "q12": {
                "a": "$x + \\dfrac{2}{5} = \\dfrac{7}{10}$",
                "b": "$\\dfrac{2}{3}x - \\dfrac{1}{2} = \\dfrac{5}{6}$",
                "c": "$\\left(x - \\dfrac{1}{2}\\right)^2 = \\dfrac{9}{16}$",
                "d": "$\\left|2x - \\dfrac{1}{3}\\right| = \\dfrac{5}{3}$"
            },
            "q13": {
                "de": "Cho góc nhọn $\\widehat{xOy}$. Trên tia $Ox$ lấy điểm $A$, trên tia $Oy$ lấy điểm $B$ sao cho $OA = OB$. Gọi $Ot$ là tia phân giác của góc $\\widehat{xOy}$. Trên tia $Ot$ lấy điểm $M$ ($M \\neq O$).",
                "a": "(1,0 điểm) Chứng minh rằng $\\Delta OAM = \\Delta OBM$.",
                "b": "(1,0 điểm) Gọi $H$ là giao điểm của $OM$ và $AB$. Chứng minh rằng $MA = MB$ và $OM \\perp AB$."
            },
            "q14": {
                "de": "Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 2| + |x - 7|$."
            }
        },
        "102": {
            "short": [
                [
                    "Trong $\\Delta MNP$, góc xen giữa hai cạnh $MN$ và $MP$ là:",
                    "\\widehat{M}"
                ],
                [
                    "Để $\\Delta MNP = \\Delta QRS$ (c.g.c) khi $MN=QR, NP=RS$, cần thêm:",
                    "\\widehat{N} = \\widehat{R}"
                ],
                [
                    "Cho $\\Delta ABC = \\Delta MNP$ (c.g.c), $\\widehat{M}=50^\\circ, \\widehat{N}=70^\\circ$. Khi đó $\\widehat{C}$ bằng:",
                    "60^\\circ"
                ],
                [
                    "Cho $\\Delta ABC = \\Delta MNP$ (c.g.c), biết $AC = 6\\text{ cm}$. Độ dài cạnh $MP$ là:",
                    "6\\text{ cm}"
                ],
                [
                    "Giá trị của căn bậc hai số học $\\sqrt{169} - \\sqrt{64}$ bằng:",
                    "5"
                ],
                [
                    "Tìm số hữu tỉ $x > 0$, biết $\\left|x - \\dfrac{3}{2}\\right| = \\dfrac{5}{2}$:",
                    "x = 4"
                ],
                [
                    "Cho $\\Delta MNP, \\Delta DEF$ vuông tại $M, D$, có $MN=DE$. Cần thêm điều kiện:",
                    "MP = DF"
                ],
                [
                    "Cho $\\Delta OAB = \\Delta OCD$, biết $CD = 45\\text{ m}$. Độ dài cạnh $AB$ là:",
                    "45\\text{ m}"
                ],
                [
                    "Giá trị của biểu thức $\\left(-\\dfrac{1}{4}\\right)^2 \\cdot 16 + (-1)^{2024}$ bằng:",
                    "2"
                ],
                [
                    "Cho $MN$ cắt $PQ$ tại trung điểm $I$ mỗi đoạn. Khi đó $\\Delta IMP$ bằng:",
                    "\\Delta INQ"
                ]
            ],
            "q11": {
                "a": "$\\dfrac{3}{11} + \\dfrac{5}{8} + \\dfrac{8}{11} - \\dfrac{13}{8}$",
                "b": "$\\dfrac{5}{9} \\cdot \\left(-\\dfrac{3}{7}\\right) + \\dfrac{5}{9} \\cdot \\left(-\\dfrac{4}{7}\\right) + \\dfrac{14}{9}$",
                "c": "$\\left(-\\dfrac{1}{3}\\right)^2 \\cdot 18 - \\left(\\dfrac{5}{7}\\right)^0$",
                "d": "$\\sqrt{\\dfrac{25}{49}} - \\left|-\\dfrac{3}{7}\\right| + \\sqrt{\\dfrac{9}{49}}$",
                "e": "$\\dfrac{5}{6} - \\left[ \\dfrac{2}{3} + \\left(\\dfrac{1}{4} - \\dfrac{3}{4}\\right) \\right]$",
                "f": "$\\dfrac{8^2 \\cdot 9^3}{6^5}$"
            },
            "q12": {
                "a": "$x + \\dfrac{3}{4} = \\dfrac{7}{8}$",
                "b": "$\\dfrac{3}{4}x - \\dfrac{2}{3} = \\dfrac{5}{6}$",
                "c": "$\\left(x - \\dfrac{1}{3}\\right)^2 = \\dfrac{4}{9}$",
                "d": "$\\left|2x - \\dfrac{1}{2}\\right| = \\dfrac{3}{2}$"
            },
            "q13": {
                "de": "Cho góc nhọn $\\widehat{mIn}$. Trên tia $Im$ lấy điểm $E$, trên tia $In$ lấy điểm $F$ sao cho $IE = IF$. Gọi $It$ là tia phân giác của góc $\\widehat{mIn}$. Trên tia $It$ lấy điểm $K$ ($K \\neq I$).",
                "a": "(1,0 điểm) Chứng minh rằng $\\Delta IEK = \\Delta IFK$.",
                "b": "(1,0 điểm) Gọi $H$ là giao điểm của $IK$ và $EF$. Chứng minh rằng $KE = KF$ và $IK \\perp EF$."
            },
            "q14": {
                "de": "Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 3| + |x - 8|$."
            }
        },
        "103": {
            "short": [
                [
                    "Trong $\\Delta DEF$, góc xen giữa hai cạnh $DE$ và $EF$ là:",
                    "\\widehat{E}"
                ],
                [
                    "Để $\\Delta ABC = \\Delta MNP$ (c.g.c) khi $BC=NP, AC=MP$, cần thêm:",
                    "\\widehat{C} = \\widehat{P}"
                ],
                [
                    "Cho $\\Delta DEF = \\Delta GHK$ (c.g.c), $\\widehat{D}=45^\\circ, \\widehat{E}=75^\\circ$. Khi đó $\\widehat{K}$ bằng:",
                    "60^\\circ"
                ],
                [
                    "Cho $\\Delta DEF = \\Delta MNP$ (c.g.c), biết $EF = 10\\text{ cm}$. Độ dài cạnh $NP$ là:",
                    "10\\text{ cm}"
                ],
                [
                    "Giá trị của căn bậc hai số học $\\sqrt{196} - \\sqrt{81}$ bằng:",
                    "5"
                ],
                [
                    "Tìm số hữu tỉ $x > 0$, biết $\\left|x - \\dfrac{1}{3}\\right| = \\dfrac{5}{3}$:",
                    "x = 2"
                ],
                [
                    "Cho $\\Delta ABC, \\Delta MNP$ vuông tại $B, N$, có $BA=NM$. Cần thêm điều kiện:",
                    "BC = NP"
                ],
                [
                    "Cho $\\Delta OAB = \\Delta OCD$, biết $CD = 52\\text{ m}$. Độ dài cạnh $AB$ là:",
                    "52\\text{ m}"
                ],
                [
                    "Giá trị của biểu thức $\\left(-\\dfrac{1}{5}\\right)^2 \\cdot 25 + (-1)^{2028}$ bằng:",
                    "2"
                ],
                [
                    "Cho $EF$ cắt $GH$ tại trung điểm $K$ mỗi đoạn. Khi đó $\\Delta KEG$ bằng:",
                    "\\Delta KFH"
                ]
            ],
            "q11": {
                "a": "$\\dfrac{7}{15} + \\dfrac{2}{9} + \\dfrac{8}{15} - \\dfrac{11}{9}$",
                "b": "$\\dfrac{3}{8} \\cdot \\left(-\\dfrac{1}{6}\\right) + \\dfrac{3}{8} \\cdot \\left(-\\dfrac{5}{6}\\right) + \\dfrac{11}{8}$",
                "c": "$\\left(-\\dfrac{1}{2}\\right)^4 : \\dfrac{1}{8} + \\left(\\dfrac{2}{3}\\right)^0$",
                "d": "$\\sqrt{\\dfrac{36}{81}} - \\left|-\\dfrac{1}{9}\\right| + \\sqrt{\\dfrac{16}{81}}$",
                "e": "$\\dfrac{4}{5} - \\left[ \\dfrac{1}{2} + \\left(\\dfrac{1}{10} - \\dfrac{3}{10}\\right) \\right]$",
                "f": "$\\dfrac{27^2 \\cdot 4^4}{6^6}$"
            },
            "q12": {
                "a": "$x - \\dfrac{1}{3} = \\dfrac{5}{6}$",
                "b": "$\\dfrac{3}{5}x + \\dfrac{1}{2} = \\dfrac{11}{10}$",
                "c": "$\\left(x + \\dfrac{1}{2}\\right)^2 = \\dfrac{25}{16}$",
                "d": "$\\left|3x - \\dfrac{1}{2}\\right| = \\dfrac{5}{2}$"
            },
            "q13": {
                "de": "Cho góc nhọn $\\widehat{xAy}$. Trên tia $Ax$ lấy điểm $B$, trên tia $Ay$ lấy điểm $C$ sao cho $AB = AC$. Gọi $At$ là tia phân giác của góc $\\widehat{xAy}$. Trên tia $At$ lấy điểm $M$ ($M \\neq A$).",
                "a": "(1,0 điểm) Chứng minh rằng $\\Delta ABM = \\Delta ACM$.",
                "b": "(1,0 điểm) Gọi $D$ là giao điểm của $AM$ và $BC$. Chứng minh rằng $MB = MC$ và $AM \\perp BC$."
            },
            "q14": {
                "de": "Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 1| + |x - 6|$."
            }
        },
        "104": {
            "short": [
                [
                    "Trong $\\Delta HIK$, góc xen giữa hai cạnh $HK$ và $IK$ là:",
                    "\\widehat{K}"
                ],
                [
                    "Để $\\Delta DEF = \\Delta HKM$ (c.g.c) khi $DE=HK, EF=KM$, cần thêm:",
                    "\\widehat{E} = \\widehat{K}"
                ],
                [
                    "Cho $\\Delta ABC = \\Delta DEF$ (c.g.c), $\\widehat{D}=60^\\circ, \\widehat{E}=50^\\circ$. Khi đó $\\widehat{C}$ bằng:",
                    "70^\\circ"
                ],
                [
                    "Cho $\\Delta ABC = \\Delta HIK$ (c.g.c), biết $AC = 7\\text{ cm}$. Độ dài cạnh $HK$ là:",
                    "7\\text{ cm}"
                ],
                [
                    "Giá trị của căn bậc hai số học $\\sqrt{225} - \\sqrt{100}$ bằng:",
                    "5"
                ],
                [
                    "Tìm số hữu tỉ $x > 0$, biết $\\left|x - \\dfrac{2}{3}\\right| = \\dfrac{7}{3}$:",
                    "x = 3"
                ],
                [
                    "Cho $\\Delta DEF, \\Delta HIK$ vuông tại $E, I$, có $EF=IK$. Cần thêm điều kiện:",
                    "ED = IH"
                ],
                [
                    "Cho $\\Delta OAB = \\Delta OCD$, biết $CD = 65\\text{ m}$. Độ dài cạnh $AB$ là:",
                    "65\\text{ m}"
                ],
                [
                    "Giá trị của biểu thức $\\left(-\\dfrac{1}{2}\\right)^3 \\cdot (-8) + (-1)^{2030}$ bằng:",
                    "2"
                ],
                [
                    "Cho $AB$ cắt $CD$ tại trung điểm $O$ mỗi đoạn. Khi đó $\\Delta OAD$ bằng:",
                    "\\Delta OBC"
                ]
            ],
            "q11": {
                "a": "$\\dfrac{4}{17} + \\dfrac{3}{5} + \\dfrac{13}{17} - \\dfrac{8}{5}$",
                "b": "$\\dfrac{6}{11} \\cdot \\left(-\\dfrac{2}{7}\\right) + \\dfrac{6}{11} \\cdot \\left(-\\dfrac{5}{7}\\right) + \\dfrac{17}{11}$",
                "c": "$\\left(-\\dfrac{1}{4}\\right)^2 \\cdot 32 - \\left(\\dfrac{7}{9}\\right)^0$",
                "d": "$\\sqrt{\\dfrac{49}{64}} - \\left|-\\dfrac{3}{8}\\right| + \\sqrt{\\dfrac{4}{64}}$",
                "e": "$\\dfrac{5}{6} - \\left[ \\dfrac{1}{2} + \\left(\\dfrac{1}{12} - \\dfrac{5}{12}\right) \\right]$",
                "f": "$\\dfrac{16^2 \\cdot 25^2}{20^3}$"
            },
            "q12": {
                "a": "$x - \\dfrac{2}{5} = \\dfrac{3}{10}$",
                "b": "$\\dfrac{4}{5}x + \\dfrac{1}{3} = \\dfrac{17}{15}$",
                "c": "$\\left(x + \\dfrac{2}{3}\\right)^2 = \\dfrac{16}{9}$",
                "d": "$\\left|3x - \\dfrac{1}{4}\\right| = \\dfrac{7}{4}$"
            },
            "q13": {
                "de": "Cho góc nhọn $\\widehat{pSq}$. Trên tia $Sp$ lấy điểm $M$, trên tia $Sq$ lấy điểm $N$ sao cho $SM = SN$. Gọi $St$ là tia phân giác của góc $\\widehat{pSq}$. Trên tia $St$ lấy điểm $P$ ($P \\neq S$).",
                "a": "(1,0 điểm) Chứng minh rằng $\\Delta SMP = \\Delta SNP$.",
                "b": "(1,0 điểm) Gọi $K$ là giao điểm của $SP$ và $MN$. Chứng minh rằng $PM = PN$ và $SP \\perp MN$."
            },
            "q14": {
                "de": "Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 4| + |x - 9|$."
            }
        }
    }
}

json_path = os.path.join(CUR_DIR, "data_de.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Refined {json_path} successfully.")
