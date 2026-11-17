import json
import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

data = {
    "base_filename": "Phieu_Kiem_Tra_Tuan_11_Buoi_01",
    "title_p1": "PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 8 - TUẦN 11 - BUỔI 01",
    "title_p2": "TOÁN 8 - TUẦN 11 - BUỔI 01",
    "codes": {
        "101": {
            "short": [
                ("Cho $\\Delta ABC$ có $M, N$ là trung điểm $AB, AC$. Đoạn thẳng $MN$ là:", "Đường trung bình"),
                ("Cho $\\Delta ABC$ có đường trung bình $MN = 6\\text{ cm}$. Độ dài cạnh đáy $BC$ là:", "12\\text{ cm}"),
                ("Cho $\\Delta ABC$ có chu vi $24\\text{ cm}$. Tam giác nối ba trung điểm có chu vi là:", "12\\text{ cm}"),
                ("Phân tích đa thức $3x^2 - 6x$ thành nhân tử, ta được kết quả là:", "3x(x - 2)"),
                ("Tính nhanh giá trị của biểu thức $65^2 - 35^2$, ta được kết quả là:", "3\\,000"),
                ("Cho hằng đẳng thức $(x + 3)^2 = x^2 + ax + 9$. Giá trị của hệ số $a$ là:", "6"),
                ("Bậc của đa thức $P = 4x^3 y^2 - 5x^2 y^4 + 7$ sau khi thu gọn là:", "6"),
                ("Cho $x + y = 5$. Giá trị của biểu thức $A = x(x + y) + y(x + y)$ là:", "25"),
                ("Đo khoảng cách $AB$ qua hồ có ĐTB $MN = 45\\text{ m}$. Khi đó $AB$ bằng:", "90\\text{ m}"),
                ("Tứ giác có hai cặp cạnh đối song song là hình gì?", "Hình bình hành")
            ],
            "q11": {
                "a": "$3x^2 - 6x$",
                "b": "$x^2 - 16$",
                "c": "$x^2 - 6x + 9$",
                "d": "$xy + 2y + 3x + 6$",
                "e": "$x^2 - 2xy + y^2 - 16$",
                "f": "$x^2 - 5x + 6$"
            },
            "q12": {
                "a": "$x^2 - 4x = 0$",
                "b": "$x^2 - 36 = 0$",
                "c": "$x^2 - 8x + 16 = 0$",
                "d": "$(x - 2)(x + 3) - 2(x + 3) = 0$"
            },
            "q13": {
                "de": "Cho tam giác $ABC$ nhọn ($AB < AC$). Gọi $D, E$ lần lượt là trung điểm của $AB$ và $AC$.",
                "a": "(1,0 điểm) Chứng minh $DE$ là đường trung bình của tam giác $ABC$. Biết $BC = 12\\text{ cm}$, tính độ dài đoạn thẳng $DE$.",
                "b": "(1,0 điểm) Trên tia đối của tia $ED$ lấy điểm $F$ sao cho $EF = ED$. Chứng minh tứ giác $ADCF$ là hình bình hành."
            },
            "q14": {
                "de": "Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 6x + 14$."
            }
        },
        "102": {
            "short": [
                ("Cho $\\Delta MNP$ có $E, F$ là trung điểm $MN, MP$. Đoạn thẳng $EF$ là:", "Đường trung bình"),
                ("Cho $\\Delta MNP$ có đường trung bình $EF = 7\\text{ cm}$. Độ dài cạnh đáy $NP$ là:", "14\\text{ cm}"),
                ("Cho $\\Delta ABC$ có chu vi $30\\text{ cm}$. Tam giác nối ba trung điểm có chu vi là:", "15\\text{ cm}"),
                ("Phân tích đa thức $4x^2 - 8x$ thành nhân tử, ta được kết quả là:", "4x(x - 2)"),
                ("Tính nhanh giá trị của biểu thức $75^2 - 25^2$, ta được kết quả là:", "5\\,000"),
                ("Cho hằng đẳng thức $(x - 4)^2 = x^2 - bx + 16$. Giá trị của hệ số $b$ là:", "8"),
                ("Bậc của đa thức $Q = 5x^2 y^4 - 3x^3 y^2 + 2$ sau khi thu gọn là:", "6"),
                ("Cho $x + y = 6$. Giá trị của biểu thức $A = x(x + y) + y(x + y)$ là:", "36"),
                ("Đo khoảng cách $AB$ qua hồ có ĐTB $MN = 55\\text{ m}$. Khi đó $AB$ bằng:", "110\\text{ m}"),
                ("Hình bình hành có một góc vuông là hình gì?", "Hình chữ nhật")
            ],
            "q11": {
                "a": "$4x^2 - 8x$",
                "b": "$x^2 - 25$",
                "c": "$x^2 + 8x + 16$",
                "d": "$xy + 3y + 2x + 6$",
                "e": "$x^2 - 2xy + y^2 - 25$",
                "f": "$x^2 - 7x + 12$"
            },
            "q12": {
                "a": "$x^2 - 5x = 0$",
                "b": "$x^2 - 49 = 0$",
                "c": "$x^2 - 10x + 25 = 0$",
                "d": "$(x - 1)(x + 4) - 3(x + 4) = 0$"
            },
            "q13": {
                "de": "Cho tam giác $MNP$ nhọn ($MN < MP$). Gọi $D, E$ lần lượt là trung điểm của $MN$ và $MP$.",
                "a": "(1,0 điểm) Chứng minh $DE$ là đường trung bình của tam giác $MNP$. Biết $NP = 14\\text{ cm}$, tính độ dài đoạn thẳng $DE$.",
                "b": "(1,0 điểm) Trên tia đối của tia $ED$ lấy điểm $F$ sao cho $EF = ED$. Chứng minh tứ giác $MDFP$ là hình bình hành."
            },
            "q14": {
                "de": "Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 8x + 21$."
            }
        },
        "103": {
            "short": [
                ("Cho $\\Delta DEF$ có $I, K$ là trung điểm $DE, DF$. Đoạn thẳng $IK$ là:", "Đường trung bình"),
                ("Cho $\\Delta DEF$ có đường trung bình $IK = 8\\text{ cm}$. Độ dài cạnh đáy $EF$ là:", "16\\text{ cm}"),
                ("Cho $\\Delta DEF$ có chu vi $28\\text{ cm}$. Tam giác nối ba trung điểm có chu vi là:", "14\\text{ cm}"),
                ("Phân tích đa thức $5x^2 - 10x$ thành nhân tử, ta được kết quả là:", "5x(x - 2)"),
                ("Tính nhanh giá trị của biểu thức $85^2 - 15^2$, ta được kết quả là:", "7\\,000"),
                ("Cho hằng đẳng thức $(2x + 1)^2 = 4x^2 + cx + 1$. Giá trị của hệ số $c$ là:", "4"),
                ("Bậc của đa thức $R = 2x^5 y - 6x^2 y^3 + 9$ sau khi thu gọn là:", "6"),
                ("Cho $x + y = 7$. Giá trị của biểu thức $A = x(x + y) + y(x + y)$ là:", "49"),
                ("Đo khoảng cách $AB$ qua hồ có ĐTB $MN = 38\\text{ m}$. Khi đó $AB$ bằng:", "76\\text{ m}"),
                ("Hình bình hành có hai cạnh kề bằng nhau là hình gì?", "Hình thoi")
            ],
            "q11": {
                "a": "$5x^2 - 15x$",
                "b": "$4x^2 - 9$",
                "c": "$x^2 - 10x + 25$",
                "d": "$xy + 4y + 2x + 8$",
                "e": "$x^2 + 2xy + y^2 - 9$",
                "f": "$x^2 + 5x + 6$"
            },
            "q12": {
                "a": "$x^2 + 3x = 0$",
                "b": "$x^2 - 81 = 0$",
                "c": "$x^2 + 6x + 9 = 0$",
                "d": "$(x - 3)(x + 2) - 2(x + 2) = 0$"
            },
            "q13": {
                "de": "Cho tam giác $ABC$ nhọn ($AB < AC$). Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$.",
                "a": "(1,0 điểm) Chứng minh $MN$ là đường trung bình của tam giác $ABC$. Biết $BC = 16\\text{ cm}$, tính độ dài đoạn thẳng $MN$.",
                "b": "(1,0 điểm) Trên tia đối của tia $NM$ lấy điểm $P$ sao cho $NP = NM$. Chứng minh tứ giác $AMCP$ là hình bình hành."
            },
            "q14": {
                "de": "Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 4x + 11$."
            }
        },
        "104": {
            "short": [
                ("Cho $\\Delta ABC$ có $D, E$ là trung điểm $AB, BC$. Đoạn thẳng $DE$ là:", "Đường trung bình"),
                ("Cho $\\Delta MNP$ có đường trung bình $EF = 9\\text{ cm}$. Độ dài cạnh đáy $NP$ là:", "18\\text{ cm}"),
                ("Cho $\\Delta MNP$ có chu vi $36\\text{ cm}$. Tam giác nối ba trung điểm có chu vi là:", "18\\text{ cm}"),
                ("Phân tích đa thức $2x^2 - 6x$ thành nhân tử, ta được kết quả là:", "2x(x - 3)"),
                ("Tính nhanh giá trị của biểu thức $95^2 - 5^2$, ta được kết quả là:", "9\\,000"),
                ("Cho hằng đẳng thức $(x + 5)^2 = x^2 + dx + 25$. Giá trị của hệ số $d$ là:", "10"),
                ("Bậc của đa thức $T = 7xy^5 - 4x^3 y^2 + 5$ sau khi thu gọn là:", "6"),
                ("Cho $x + y = 8$. Giá trị của biểu thức $A = x(x + y) + y(x + y)$ là:", "64"),
                ("Đo khoảng cách $AB$ qua hồ có ĐTB $MN = 62\\text{ m}$. Khi đó $AB$ bằng:", "124\\text{ m}"),
                ("Hình chữ nhật có hai cạnh kề bằng nhau là hình gì?", "Hình vuông")
            ],
            "q11": {
                "a": "$2x^2 - 8x$",
                "b": "$9x^2 - 16$",
                "c": "$x^2 + 12x + 36$",
                "d": "$xy + 5y + 3x + 15$",
                "e": "$x^2 + 2xy + y^2 - 49$",
                "f": "$x^2 - 8x + 15$"
            },
            "q12": {
                "a": "$x^2 + 6x = 0$",
                "b": "$x^2 - 64 = 0$",
                "c": "$x^2 + 10x + 25 = 0$",
                "d": "$(x - 2)(x + 5) - 3(x + 5) = 0$"
            },
            "q13": {
                "de": "Cho tam giác $DEF$ nhọn ($DE < DF$). Gọi $M, N$ lần lượt là trung điểm của $DE$ và $DF$.",
                "a": "(1,0 điểm) Chứng minh $MN$ là đường trung bình của tam giác $DEF$. Biết $EF = 18\\text{ cm}$, tính độ dài đoạn thẳng $MN$.",
                "b": "(1,0 điểm) Trên tia đối của tia $NM$ lấy điểm $P$ sao cho $NP = NM$. Chứng minh tứ giác $DMFP$ là hình bình hành."
            },
            "q14": {
                "de": "Tìm giá trị nhỏ nhất của biểu thức: $A = x^2 - 10x + 31$."
            }
        }
    }
}

with open(os.path.join(CUR_DIR, 'data_de.json'), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated data_de.json successfully!")
