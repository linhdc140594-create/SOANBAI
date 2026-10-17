import os
import sys
import json
import re
import subprocess

# Add project root to sys.path to import ai_client
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import ai_client

SYSTEM_PROMPT = """Bạn là chuyên gia sư phạm Toán THCS và biên soạn tài liệu LaTeX chuyên nghiệp.
Nhiệm vụ của bạn là biên soạn nội dung 4 mã đề (101, 102, 103, 104) cho PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 05 - BUỔI 01 bám sát tuyệt đối kế hoạch học tập.

Yêu cầu chất lượng toán học:
1. Độ khó tương đương giữa 4 mã đề.
2. Số liệu đẹp, chuẩn xác, nghiệm của hệ phương trình và phương trình bậc hai là số nguyên hoặc phân số tối giản gọn gàng.
3. Đáp án đúng trắc nghiệm phải được hoán vị ngẫu nhiên giữa A, B, C, D qua các mã đề.
4. Cú pháp LaTeX chuẩn, tương thích với gói ex_test và tabularx.
"""

USER_PROMPT = """Hãy tạo nội dung chi tiết cho 4 mã đề (101, 102, 103, 104) của PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 9 - TUẦN 05 - BUỔI 01.

Chủ đề: HỆ PHƯƠNG TRÌNH & RÚT GỌN PHÂN THỨC CHỨA CĂN BẬC HAI (ẨN x)
Thời gian: 45 phút.

Ma trận chi tiết cho mỗi mã đề:
1. PHẦN I. TRẮC NGHIỆM KHÁCH QUAN (2,5 điểm - 5 câu, mỗi câu 0,5đ):
- Câu 1 (Nhận biết): Căn bậc hai số học của một số chính phương (ví dụ 49, 64, 81, 36,...).
- Câu 2 (Nhận biết): Điều kiện xác định (có nghĩa) của biểu thức chứa căn dạng $\\sqrt{ax+b}$ hoặc $\\sqrt{b-ax}$.
- Câu 3 (Thông hiểu): Rút gọn biểu thức $\\sqrt{(a - \\sqrt{b})^2}$ với $a < \\sqrt{b}$.
- Câu 4 (Thông hiểu): So sánh hai số (so sánh số nguyên với căn số học, hoặc $a\\sqrt{b}$ với $c\\sqrt{d}$).
- Câu 5 (Kỹ năng tính): Kiểm tra cặp nghiệm của một hệ phương trình bậc nhất hai ẩn.

2. PHẦN II. TỰ LUẬN (7,5 điểm):
- Câu 1 (2,5 điểm): Giải các hệ phương trình sau:
  a) (1,25đ) Hệ phương trình bậc nhất hai ẩn cơ bản (dùng cộng đại số hoặc thế, nghiệm nguyên đẹp).
  b) (1,25đ) Hệ phương trình đặt ẩn phụ chứa $1/x$ và $1/y$ (ĐKXĐ $x \\ne 0, y \\ne 0$, nghiệm nguyên đẹp).
- Câu 2 (2,5 điểm): Rút gọn biểu thức phân thức chứa căn bậc hai có ẩn $x$ (Trích DETHI2010):
  a) (1,25đ) Biểu thức dạng $\\dfrac{a\\sqrt{x}+b}{x-c^2} - \\dfrac{d}{c-\\sqrt{x}}$ với $x \\ge 0, x \\ne c^2$.
  b) (1,25đ) Biểu thức dạng $\\dfrac{a}{\\sqrt{x}+c} + \\dfrac{a}{\\sqrt{x}-c} + \\dfrac{\\sqrt{x}-k}{x-c^2}$ với $x \\ge 0, x \\ne c^2$.
- Câu 3 (2,5 điểm): Bài toán thực tế hình học khu vườn (Trích Đề 25 - DETHI2010):
  Một khu vườn hình chữ nhật có chiều dài lớn hơn chiều rộng $d$ mét và diện tích bằng $S$ m$^2$.
  a) (1,5đ) Tìm chiều dài và chiều rộng ban đầu của khu vườn.
  b) (1,0đ) Người ta muốn xây tường rào bao quanh khu vườn và chừa một cổng đi rộng $w$ mét. Hỏi chiều dài bờ tường cần xây là bao nhiêu mét?

Hãy trả về dưới định dạng JSON duy nhất với cấu trúc:
{
  "codes": {
    "101": {
      "mcq": [
        {"q": "...", "A": "...", "B": "...", "C": "...", "D": "...", "ans": "A/B/C/D"}
      ],
      "c1": {
        "a": "...",
        "b": "..."
      },
      "c2": {
        "a": "...",
        "b": "..."
      },
      "c3": {
        "text": "...",
        "sub_a": "...",
        "sub_b": "..."
      }
    },
    "102": { ... },
    "103": { ... },
    "104": { ... }
  },
  "solutions_markdown": "... (Toàn bộ nội dung Barem đáp án và thang điểm chi tiết bằng Markdown cho cả 4 mã đề) ..."
}
Chỉ trả về JSON hợp lệ, không bọc thêm bất kỳ văn bản mở đầu hay kết thúc nào ngoài khối JSON.
"""

def main():
    print("=== Đang gọi AI API (gemini-3.1-pro-preview qua ai_client) ===")
    response_text = ai_client.ask_ai(
        prompt=USER_PROMPT,
        system_prompt=SYSTEM_PROMPT,
        model="gemini-3.1-pro-preview",
        temperature=0.3
    )
    
    # Save raw response for reference
    with open("ai_raw_response.json", "w", encoding="utf-8") as f:
        f.write(response_text)
    print("Đã nhận phản hồi từ AI API, độ dài:", len(response_text))

if __name__ == "__main__":
    main()
