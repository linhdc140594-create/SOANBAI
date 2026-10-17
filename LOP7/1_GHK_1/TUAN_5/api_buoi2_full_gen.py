import os
import sys

sach_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if sach_dir not in sys.path:
    sys.path.insert(0, sach_dir)

import ai_client

prompt_buoi2 = """
Bạn là một chuyên gia sư phạm Toán THCS hàng đầu, chuyên gia biên soạn đề thi Toán 7 theo chuẩn chương trình GDPT 2018 (SGK Kết nối tri thức với cuộc sống).
Hãy biên soạn NỘI DUNG ĐỀ THI VÀ ĐÁP ÁN BAREM cho PHẦN I (Trắc nghiệm), CÂU 2 (Phép tính & làm tròn), CÂU 3 (Tìm số thực x) cho 4 MÃ ĐỀ (101, 102, 103, 104) của PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 5 - BUỔI 02.
Chủ đề: Ôn tập Chương 2: Số thực và Làm tròn số.

YÊU CẦU MA TRẬN CHO TỪNG MÃ ĐỀ:
1. PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (2,5 điểm - 5 câu, mỗi câu 4 phương án A, B, C, D có 1 đáp án đúng):
   - Câu 1: Lý thuyết quy tắc làm tròn số (chữ số đầu tiên bỏ đi nhỏ hơn 5 hoặc lớn hơn hay bằng 5).
   - Câu 2: Làm tròn số thập phân (số pi = 3,14159... hoặc căn bậc hai) đến hàng phần trăm / phần mười / phần nghìn.
   - Câu 3: Làm tròn số với độ chính xác d cho trước (ví dụ d = 50 thì làm tròn đến hàng trăm; d = 0,05 thì làm tròn đến hàng phần mười; d = 500 thì làm tròn đến hàng nghìn).
   - Câu 4: Nhận biết quan hệ hai đường thẳng song song (hai góc so le trong, đồng vị, trong cùng phía).
   - Câu 5: Dấu hiệu nhận biết hai đường thẳng song song (hai góc so le trong bằng nhau...).
   * Yêu cầu: 4 mã đề hoán vị số liệu và đáp án rõ ràng (ghi rõ bảng đáp án 5 câu cho từng mã đề).

2. CÂU 2 (2,5 điểm). Tự luận: Thực hiện phép tính và làm tròn số (mỗi ý 0,625đ, gồm 4 ý a, b, c, d):
   - a) Tính giá trị và làm tròn đến hàng đơn vị (chứa căn bậc hai, ví dụ sqrt{37} + 4.28 hoặc tương tự).
   - b) Tính giá trị và làm tròn đến hàng phần mười (chứa phân số và số thập phân).
   - c) Tính biểu thức tích/thương và làm tròn với độ chính xác d = 0,05 hoặc d = 0,005.
   - d) Phối hợp căn bậc hai, giá trị tuyệt đối và làm tròn kết quả đến chữ số thập phân thứ hai (hàng phần trăm).
   * Yêu cầu: Số liệu đẹp, chuẩn xác, không quá rườm rà, phù hợp thời gian 10-12 phút.

3. CÂU 3 (2,5 điểm). Tự luận: Tìm số thực x, biết (mỗi ý 0,625đ, gồm 4 ý a, b, c, d):
   - a) Phương trình căn bậc hai cơ bản: sqrt{x} = a (với a > 0).
   - b) Phương trình chứa căn thức: sqrt{x - m} = n (với n > 0).
   - c) Phương trình chứa giá trị tuyệt đối: |ax + b| = c (chia 2 trường hợp ra số hữu tỉ đẹp).
   - d) Dạng nâng cao phân loại tìm x, y: |x - x0| + |y - y0| = 0 hoặc |x - x0| + (y - y0)^2 = 0.
   * Yêu cầu: Lời giải chi tiết và đáp án cho từng mã đề.

Hãy xuất định dạng rõ ràng:
- PHẦN 1: Đề bài chi tiết 4 mã đề (101, 102, 103, 104) với cú pháp LaTeX chuẩn (macro \cauTN{...}{...}{...}{...}{...}, bảng \oBaiTap[6]{...}{...}).
- PHẦN 2: Đáp án & Barem chấm điểm chi tiết (0,25đ và 0,625đ).
"""

print("Đang gọi API gemini-3.1-pro-preview để tạo toàn bộ đề & barem Buổi 02...")
output = ai_client.ask_ai(prompt_buoi2, system_prompt="Bạn là chuyên gia sư phạm Toán THCS và biên soạn đề kiểm tra chuẩn GDPT 2018.")

out_file = os.path.join(os.path.dirname(__file__), "api_buoi2_full_output.txt")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Đã lưu kết quả API vào: {out_file}")
