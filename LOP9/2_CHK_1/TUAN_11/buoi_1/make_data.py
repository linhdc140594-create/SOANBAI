import json
import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

data = {
    "title_p1": "PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 11 - BUỔI 01",
    "title_p2": "TOÁN 9 - TUẦN 11 - BUỔI 01",
    "base_filename": "Phieu_Kiem_Tra_Tuan_11_Buoi_01",
    "codes": {
        "101": {
            "short": [
                ("Cho $(O; 6\\text{ cm})$, cung tròn có số đo $60^\\circ$. Độ dài cung là:", "2\\pi\\text{ cm}"),
                ("Đường tròn có chu vi $C = 16\\pi\\text{ cm}$. Bán kính $R$ bằng:", "8\\text{ cm}"),
                ("Cho $(O; 12\\text{ cm})$ có cung độ dài $3\\pi\\text{ cm}$. Số đo cung là:", "45^\\circ"),
                ("Căn bậc hai số học của $144$ là:", "12"),
                ("Điều kiện xác định của biểu thức $\\sqrt{2x - 8}$ là:", "x \\ge 4"),
                ("Tính giá trị của biểu thức $\\sqrt{50} - \\sqrt{18} + \\sqrt{8} = $", "4\\sqrt{2}"),
                ("Hệ phương trình $\\begin{cases} 3x - y = 7 \\\\ x + y = 5 \\end{cases}$ có nghiệm $(x; y)$ là:", "(3; 2)"),
                ("Tam giác vuông có hai cạnh góc vuông $6\\text{ cm}, 8\\text{ cm}$. Đường cao là:", "4{,}8\\text{ cm}"),
                ("Tiếp tuyến của $(O)$ vuông góc với bán kính đi qua điểm nào:", "\\text{tiếp điểm}"),
                ("Bánh xe có đường kính $60\\text{ cm}$, khi lăn $10$ vòng đi được:", "6\\pi\\text{ m}")
            ],
            "c11": [
                ["a) (1,25 điểm)", "Giải hệ phương trình:\\par $\\begin{cases} 2x - 3y = 1 \\\\ 3x + 2y = 8 \\end{cases}$"],
                ["b) (1,25 điểm)", "Cho biểu thức $P = \\left(\\dfrac{\\sqrt{x}}{\\sqrt{x} + 2} + \\dfrac{4\\sqrt{x}}{x - 4}\\right) : \\dfrac{\\sqrt{x} + 2}{x - 4}$ với $x \\ge 0, x \\ne 4$.\\par Rút gọn $P$ và tính giá trị của $P$ tại $x = 9$."]
            ],
            "c12": "Hai tổ công nhân cùng làm chung một công việc thì hoàn thành trong $12$ giờ. Nếu tổ I làm trong $4$ giờ rồi nghỉ, tổ II làm tiếp trong $9$ giờ thì cả hai tổ hoàn thành được $\\dfrac{7}{12}$ công việc. Hỏi nếu làm riêng thì mỗi tổ hoàn thành công việc đó trong bao lâu?",
            "c13": {
                "gt": "Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.",
                "a": "\\textbf{a) (1,25 điểm)} Chứng minh $OA \\perp BC$ tại $H$. Cho $R = 6\\text{ cm}$ và $\\widehat{BOC} = 120^\\circ$, hãy tính độ dài cung nhỏ $\\wideparen{BC}$ của $(O)$.",
                "b": "\\textbf{b) (1,25 điểm)} Kẻ đường kính $BD$ của đường tròn $(O)$. Chứng minh $CD \\parallel OA$."
            }
        },
        "102": {
            "short": [
                ("Cho $(O; 9\\text{ cm})$, cung tròn có số đo $40^\\circ$. Độ dài cung là:", "2\\pi\\text{ cm}"),
                ("Đường tròn có chu vi $C = 18\\pi\\text{ cm}$. Bán kính $R$ bằng:", "9\\text{ cm}"),
                ("Cho $(O; 10\\text{ cm})$ có cung độ dài $5\\pi\\text{ cm}$. Số đo cung là:", "90^\\circ"),
                ("Căn bậc hai số học của $169$ là:", "13"),
                ("Điều kiện xác định của biểu thức $\\sqrt{3x - 12}$ là:", "x \\ge 4"),
                ("Tính giá trị của biểu thức $\\sqrt{75} - \\sqrt{27} + \\sqrt{12} = $", "4\\sqrt{3}"),
                ("Hệ phương trình $\\begin{cases} 2x - y = 5 \\\\ x + y = 4 \\end{cases}$ có nghiệm $(x; y)$ là:", "(3; 1)"),
                ("Tam giác vuông có hai cạnh góc vuông $9\\text{ cm}, 12\\text{ cm}$. Đường cao là:", "7{,}2\\text{ cm}"),
                ("Đường thẳng vuông góc bán kính tại điểm trên đường tròn là:", "\\text{tiếp tuyến}"),
                ("Bánh xe có đường kính $70\\text{ cm}$, khi lăn $10$ vòng đi được:", "7\\pi\\text{ m}")
            ],
            "c11": [
                ["a) (1,25 điểm)", "Giải hệ phương trình:\\par $\\begin{cases} 3x + 2y = 7 \\\\ 2x - 3y = -4 \\end{cases}$"],
                ["b) (1,25 điểm)", "Cho biểu thức $P = \\left(\\dfrac{\\sqrt{x}}{\\sqrt{x} + 3} + \\dfrac{6\\sqrt{x}}{x - 9}\\right) : \\dfrac{\\sqrt{x} + 3}{x - 9}$ với $x \\ge 0, x \\ne 9$.\\par Rút gọn $P$ và tính giá trị của $P$ tại $x = 16$."]
            ],
            "c12": "Hai đội công nhân cùng sửa một đoạn đường thì hoàn thành trong $12$ ngày. Nếu đội I làm trong $3$ ngày rồi nghỉ, đội II làm tiếp trong $8$ ngày thì cả hai đội sửa được $\\dfrac{1}{2}$ đoạn đường. Hỏi nếu làm riêng thì mỗi đội sửa xong đoạn đường trong bao lâu?",
            "c13": {
                "gt": "Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.",
                "a": "\\textbf{a) (1,25 điểm)} Chứng minh $OA \\perp BC$ tại $H$. Cho $R = 9\\text{ cm}$ và $\\widehat{BOC} = 80^\\circ$, hãy tính độ dài cung nhỏ $\\wideparen{BC}$ của $(O)$.",
                "b": "\\textbf{b) (1,25 điểm)} Kẻ đường kính $BD$ của đường tròn $(O)$. Chứng minh $CD \\parallel OA$."
            }
        },
        "103": {
            "short": [
                ("Cho $(O; 4\\text{ cm})$, cung tròn có số đo $90^\\circ$. Độ dài cung là:", "2\\pi\\text{ cm}"),
                ("Đường tròn có chu vi $C = 20\\pi\\text{ cm}$. Bán kính $R$ bằng:", "10\\text{ cm}"),
                ("Cho $(O; 18\\text{ cm})$ có cung độ dài $6\\pi\\text{ cm}$. Số đo cung là:", "60^\\circ"),
                ("Căn bậc hai số học của $196$ là:", "14"),
                ("Điều kiện xác định của biểu thức $\\sqrt{5x - 15}$ là:", "x \\ge 3"),
                ("Tính giá trị của biểu thức $\\sqrt{48} - \\sqrt{12} + \\sqrt{27} = $", "5\\sqrt{3}"),
                ("Hệ phương trình $\\begin{cases} 3x + y = 10 \\\\ x - y = 2 \\end{cases}$ có nghiệm $(x; y)$ là:", "(3; 1)"),
                ("Tam giác vuông có hai cạnh góc vuông $3\\text{ cm}, 4\\text{ cm}$. Đường cao là:", "2{,}4\\text{ cm}"),
                ("Số tiếp tuyến kẻ từ điểm ngoài đường tròn tới $(O)$ là:", "2"),
                ("Bánh xe có đường kính $50\\text{ cm}$, khi lăn $10$ vòng đi được:", "5\\pi\\text{ m}")
            ],
            "c11": [
                ["a) (1,25 điểm)", "Giải hệ phương trình:\\par $\\begin{cases} 3x - 2y = 4 \\\\ 2x + 3y = 7 \\end{cases}$"],
                ["b) (1,25 điểm)", "Cho biểu thức $P = \\left(\\dfrac{\\sqrt{x}}{\\sqrt{x} + 1} + \\dfrac{2\\sqrt{x}}{x - 1}\\right) : \\dfrac{\\sqrt{x} + 1}{x - 1}$ với $x \\ge 0, x \\ne 1$.\\par Rút gọn $P$ và tính giá trị của $P$ tại $x = 25$."]
            ],
            "c12": "Hai vòi nước cùng chảy vào một bể cạn thì đầy bể sau $6$ giờ. Nếu mở vòi I chảy trong $2$ giờ rồi khóa lại và mở vòi II chảy tiếp trong $5$ giờ thì cả hai vòi chảy được $\\dfrac{8}{15}$ bể nước. Hỏi nếu chảy riêng thì mỗi vòi chảy đầy bể trong bao lâu?",
            "c13": {
                "gt": "Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.",
                "a": "\\textbf{a) (1,25 điểm)} Chứng minh $OA \\perp BC$ tại $H$. Cho $R = 8\\text{ cm}$ và $\\widehat{BOC} = 90^\\circ$, hãy tính độ dài cung nhỏ $\\wideparen{BC}$ của $(O)$.",
                "b": "\\textbf{b) (1,25 điểm)} Kẻ đường kính $BD$ của đường tròn $(O)$. Chứng minh $CD \\parallel OA$."
            }
        },
        "104": {
            "short": [
                ("Cho $(O; 10\\text{ cm})$, cung tròn có số đo $36^\\circ$. Độ dài cung là:", "2\\pi\\text{ cm}"),
                ("Đường tròn có chu vi $C = 12\\pi\\text{ cm}$. Bán kính $R$ bằng:", "6\\text{ cm}"),
                ("Cho $(O; 15\\text{ cm})$ có cung độ dài $2{,}5\\pi\\text{ cm}$. Số đo cung là:", "30^\\circ"),
                ("Căn bậc hai số học của $225$ là:", "15"),
                ("Điều kiện xác định của biểu thức $\\sqrt{4x - 20}$ là:", "x \\ge 5"),
                ("Tính giá trị của biểu thức $\\sqrt{32} - \\sqrt{8} + \\sqrt{18} = $", "5\\sqrt{2}"),
                ("Hệ phương trình $\\begin{cases} 2x + y = 8 \\\\ x - y = 1 \\end{cases}$ có nghiệm $(x; y)$ là:", "(3; 2)"),
                ("Tam giác vuông có hai cạnh góc vuông $12\\text{ cm}, 16\\text{ cm}$. Đường cao là:", "9{,}6\\text{ cm}"),
                ("Khoảng cách từ tâm tới tiếp tuyến của $(O; R)$ là:", "R"),
                ("Bánh xe có đường kính $80\\text{ cm}$, khi lăn $10$ vòng đi được:", "8\\pi\\text{ m}")
            ],
            "c11": [
                ["a) (1,25 điểm)", "Giải hệ phương trình:\\par $\\begin{cases} 2x + 3y = 8 \\\\ 3x - 2y = -1 \\end{cases}$"],
                ["b) (1,25 điểm)", "Cho biểu thức $P = \\left(\\dfrac{\\sqrt{x}}{\\sqrt{x} + 4} + \\dfrac{8\\sqrt{x}}{x - 16}\\right) : \\dfrac{\\sqrt{x} + 4}{x - 16}$ với $x \\ge 0, x \\ne 16$.\\par Rút gọn $P$ và tính giá trị của $P$ tại $x = 4$."]
            ],
            "c12": "Hai vòi nước cùng chảy vào một bể cạn thì đầy bể sau $4$ giờ. Nếu mở vòi I chảy trong $3$ giờ rồi khóa lại và mở vòi II chảy tiếp trong $2$ giờ thì cả hai vòi chảy được $\\dfrac{2}{3}$ bể nước. Hỏi nếu chảy riêng thì mỗi vòi chảy đầy bể trong bao lâu?",
            "c13": {
                "gt": "Cho đường tròn $(O; R)$ và điểm $A$ nằm bên ngoài đường tròn. Từ $A$ kẻ hai tiếp tuyến $AB, AC$ với $(O)$ ($B, C$ là các tiếp điểm). Gọi $H$ là giao điểm của $OA$ và $BC$.",
                "a": "\\textbf{a) (1,25 điểm)} Chứng minh $OA \\perp BC$ tại $H$. Cho $R = 12\\text{ cm}$ và $\\widehat{BOC} = 60^\\circ$, hãy tính độ dài cung nhỏ $\\wideparen{BC}$ của $(O)$.",
                "b": "\\textbf{b) (1,25 điểm)} Kẻ đường kính $BD$ của đường tròn $(O)$. Chứng minh $CD \\parallel OA$."
            }
        }
    }
}

with open(os.path.join(CUR_DIR, 'data_de.json'), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Created data_de.json for LOP9 TUAN 11 BUOI 01 successfully!")
