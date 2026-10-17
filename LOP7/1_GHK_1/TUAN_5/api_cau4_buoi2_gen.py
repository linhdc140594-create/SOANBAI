import os
import sys

# Ensure root SACH directory is in path to import ai_client
sach_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if sach_dir not in sys.path:
    sys.path.insert(0, sach_dir)

import ai_client

prompt_cau4 = """
Bạn là một chuyên gia sư phạm Toán THCS hàng đầu, chuyên gia biên soạn đề thi theo chương trình GDPT 2018 (SGK Kết nối tri thức với cuộc sống).
Hãy biên soạn CÂU 4 (2,5 ĐIỂM) - HÌNH HỌC TÍNH GÓC GÃY KHÚC CHO CẢ 4 MÃ ĐỀ (101, 102, 103, 104) cho Phiếu kiểm tra Toán 7 - Tuần 5 - Buổi 02.

NỘI DUNG VÀ YÊU CẦU SƯ PHẠM:
1. Đề bài:
   Cho hình vẽ, biết hai tia Ax và By cùng hướng và song song với nhau (Ax // By). Lấy điểm O nằm giữa hai đường thẳng sao cho tạo thành góc AOB (đường gấp khúc A-O-B).
   Biết số đo góc xAO và góc yBO:
   - Mã 101: \widehat{xAO} = 40^\circ, \widehat{yBO} = 50^\circ
   - Mã 102: \widehat{xAO} = 35^\circ, \widehat{yBO} = 55^\circ
   - Mã 103: \widehat{xAO} = 45^\circ, \widehat{yBO} = 65^\circ
   - Mã 104: \widehat{xAO} = 50^\circ, \widehat{yBO} = 60^\circ

2. Yêu cầu câu hỏi (cho mỗi mã đề):
   a) (1,25 điểm): Kẻ qua O tia Oz song song với tia Ax (tia Oz nằm trong góc AOB, cùng hướng với tia Ax). Chứng minh rằng tia Oz cũng song song với tia By.
   b) (1,25 điểm): Chỉ ra các cặp góc so le trong tạo bởi tia Oz với các tia Ax và By. Từ đó tính số đo của góc \widehat{AOB}.

3. Barem chấm điểm chi tiết (chia nhỏ đến 0,25đ và 0,625đ):
   - Ý a (1,25đ):
     + Nêu lập luận kẻ Oz // Ax (0,25đ)
     + Lý luận tính chất: Ax // By và Oz // Ax => Oz // By (hai đường thẳng cùng song song với đường thẳng thứ ba thì song song với nhau) (1,0đ)
   - Ý b (1,25đ):
     + Vì Ax // Oz => góc AOz = góc xAO (so le trong) => tính số đo (0,625đ)
     + Vì By // Oz => góc BOz = góc yBO (so le trong) => tính số đo (0,375đ)
     + Vì tia Oz nằm trong góc AOB => góc AOB = góc AOz + góc BOz => tính kết quả (0,25đ)

4. MÃ TIKZ VẼ HÌNH CHUẨN XÁC CHO CẢ 4 MÃ ĐỀ:
   - Vẽ sẵn hình với 2 tia Ax, By nằm ngang song song cùng hướng sang phải.
   - Điểm O ở giữa, nối đoạn AO và BO.
   - KHÔNG vẽ tia Oz (để học sinh tự vẽ).
   - Đánh dấu cung góc \widehat{xAO} và \widehat{yBO} kèm số đo rõ ràng.
   - Kích thước TikZ gọn gàng (scale ~ 0.8), vừa vặn ô bảng chiều rộng 5.2cm - 5.5cm, chiều cao ~ 3.5cm.

Hãy xuất kết quả đầy đủ gồm:
- PHẦN 1: Nội dung đề bài Câu 4 cho 4 mã đề.
- PHẦN 2: Đáp án & Barem chấm điểm chi tiết cho 4 mã đề.
- PHẦN 3: Mã TikZ độc lập chuẩn đẹp cho 4 mã đề.
"""

print("Đang gọi API gemini-3.1-pro-preview để tạo Câu 4 Buổi 02...")
output = ai_client.ask_ai(prompt_cau4, system_prompt="Bạn là chuyên gia sư phạm Toán THCS và lập trình LaTeX TikZ chuẩn mực.")

out_file = os.path.join(os.path.dirname(__file__), "api_cau4_buoi2_output.txt")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Đã lưu kết quả API vào: {out_file}")
