# PROMPT CHUYÊN SÂU PHÂN TÍCH SUY LUẬN TOÁN 9+ - BÀI HÌNH 01
> **Nguồn trích xuất:** Đề số 01 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10  
> **Mô hình toán học:** Mô hình Tiếp tuyến $(C; CA)$ kết hợp Tam giác vuông xoay quanh tâm & Chứng minh 3 điểm thẳng hàng qua góc bẹt $180^\circ$

---

## 📌 I. NGUYÊN VĂN ĐỀ BÀI TOÁN HÌNH HỌC

```latex
Cho tam giác ABC vuông tại A. Vẽ đường tròn tâm C, bán kính CA. Từ điểm B kẻ tiếp tuyến BM với đường tròn (C; CA) (M là tiếp điểm, M và A nằm khác phía đối với đường thẳng BC).
a) Chứng minh tứ giác ACMB nội tiếp một đường tròn.
b) Lấy điểm N thuộc đoạn thẳng AB (N khác A, N khác B). Lấy điểm P thuộc tia đối của tia MB sao cho MP = AN.
   1) Chứng minh tam giác CPN là tam giác cân tại C.
   2) (Phân hóa 9+): Chứng minh đường thẳng AM đi qua trung điểm của đoạn thẳng NP.
```

---

## 🎯 II. NHIỆM VỤ YÊU CẦU DÀNH CHO AI (CLAUDE / OPENAI)

Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.  
Hãy phân tích sâu và giải mã bài toán hình học này theo các tiêu chuẩn cao cấp sau:

### 1. Phân tích mô hình toán học cốt lõi
- Nhận diện bản chất hình học: Phép quay tâm $C$ góc $\widehat{ACM}$ biến $\triangle CAN$ thành $\triangle CMP$.
- Điểm nghẽn lớn nhất của học sinh ở câu phân hóa b2: Làm thế nào để chứng minh một đường thẳng ($AM$) đi qua trung điểm của một đoạn thẳng ($NP$)? 
- Chiến lược giải: Chuyển bài toán "đường thẳng đi qua trung điểm" về bài toán **"Chứng minh 3 điểm thẳng hàng"** bằng cách gọi trước $I$ là trung điểm của $NP$, sau đó chứng minh $A, I, M$ thẳng hàng!

### 2. Thiết lập Sơ đồ Tư duy ngược (Reverse Thinking Mindmap)
- Lập chuỗi truy ngược từ **[ĐÍCH ĐẾN CẦN CHỨNG MINH: AM ĐI QUA TRUNG ĐIỂM NP]** ngược về **[GIẢ THIẾT GỐC]**:
  + **Đích đến:** $A, I, M$ thẳng hàng (với $I$ là trung điểm $NP$).
  + $\Uparrow$ Cần: $\widehat{AIM} = 180^\circ \iff \widehat{PIA} + \widehat{MIP} = 180^\circ$.
  + $\Uparrow$ Mà $I$ thuộc $NP \implies \widehat{PIA} + \widehat{NIA} = 180^\circ$. Do đó chỉ cần chứng minh: $\widehat{NIA} = \widehat{MIP}$.
  + $\Uparrow$ Ghép vào các tứ giác nội tiếp:
    * $\triangle CPN$ cân tại $C$ có trung tuyến $CI \implies CI \perp NP \implies \widehat{CIN} = \widehat{CIP} = 90^\circ$.
    * Tứ giác $NACI$ có $\widehat{CAN} = \widehat{CIN} = 90^\circ \implies NACI$ nội tiếp $\implies \widehat{NIA} = \widehat{NCA}$.
    * Tứ giác $CIMP$ có $\widehat{CMP} = \widehat{CIP} = 90^\circ \implies CIMP$ nội tiếp $\implies \widehat{MIP} = \widehat{MCP}$.
  + $\Uparrow$ Cần: $\widehat{NCA} = \widehat{MCP}$.
  + $\Uparrow$ Bắt vào kết quả câu b1: $\triangle CAN = \triangle CMP \text{ (c-g-c)} \implies \widehat{NCA} = \widehat{MCP}$ (LUÔN ĐÚNG!).

### 3. Thiết lập Sơ đồ Công thức hình Cây thông (Pine-Tree Formula Tree)
- Thiết kế cây logic thuần túy công thức toán học (tối giản chữ nghĩa):
  - **Đỉnh ngọn:** $\boxed{\mathbf{AM \text{ ĐI QUA TRUNG ĐIỂM } NP \iff A, I, M \text{ THẲNG HÀNG}}}$
  - Thân cây: Các bước chuyển đổi góc $\widehat{AIM} = 180^\circ \iff \widehat{NIA} = \widehat{MIP}$.
  - Tách 2 nhánh:
    * Nhánh trái: Tứ giác $NACI$ nội tiếp $\implies \widehat{NIA} = \widehat{NCA}$
    * Nhánh phải: Tứ giác $CIMP$ nội tiếp $\implies \widehat{MIP} = \widehat{MCP}$
  - Gốc rễ: $\triangle CAN = \triangle CMP \text{ (c-g-c)} \implies \widehat{NCA} = \widehat{MCP}$ (Khởi phát).

### 4. Bình luận sư phạm & Kỹ thuật chuyển đổi bài toán
- Phân tích: **"Tại sao lại gọi điểm phụ I là trung điểm NP?"**
  + Nếu để $AM$ cắt $NP$ tại $I$, học sinh sẽ bị bế tắc khi đi chứng minh $IN = IP$.
  + Kỹ thuật đảo: **Gọi trước $I$ là trung điểm $NP$** $\to$ kích hoạt ngay tính chất tam giác cân $\triangle CPN \implies CI \perp NP \implies$ tạo ra 2 góc vuông $\widehat{CIN} = \widehat{CIP} = 90^\circ$ để sinh ra 2 tứ giác nội tiếp $NACI$ và $CIMP$!
- Chuỗi 4 câu hỏi dẫn dắt của Giáo viên trên lớp để học sinh tự phản xạ.

### 5. Lời giải chuẩn mực & Barem điểm chi tiết
- Trình bày lời giải xuôi hoàn chỉnh chuẩn mực.
- Barem điểm chia nhỏ đến từng $0{,}25$đ.

---

## 📤 III. ĐỊNH DẠNG ĐẦU RA MONG MUỐN (JSON CHUẨN)

Trả về kết quả dưới định dạng JSON hợp lệ:
```json
{
  "bai_toan": {
    "ma_bai": "BAI_HINH_01",
    "nguon": "Đề 01 - Tuyển tập 55 Đề Thi Vào Lớp 10",
    "mo_hinh": "Tiếp tuyến đường tròn tâm C, tam giác vuông xoay quanh tâm C và chứng minh thẳng hàng qua góc bù 180 độ",
    "de_bai": "Cho tam giác ABC vuông tại A. Vẽ đường tròn tâm C, bán kính CA. Từ B kẻ tiếp tuyến BM với (C; CA)..."
  },
  "so_do_tu_duy_nguoc": [
    {
      "tang": 1,
      "dich_den": "AM đi qua trung điểm của NP",
      "chuyen_doi_chien_luoc": "Gọi I là trung điểm của NP, quy về chứng minh A, I, M thẳng hàng",
      "cau_hoi_truy_nguoc": "Làm sao chứng minh A, I, M thẳng hàng khi đã có I nằm giữa N và P?",
      "muc_tieu_con": "Chứng minh góc AIM = 180 độ <=> góc NIA = góc MIP"
    },
    {
      "tang": 2,
      "dich_den": "góc NIA = góc MIP",
      "cau_hoi_truy_nguoc": "Góc NIA và MIP liên hệ thế nào với các đỉnh của hình?",
      "suy_luan": "Tam giác CPN cân tại C có trung tuyến CI => CI vuông góc NP tại I. Sinh ra hai góc vuông CIN = CIP = 90 độ."
    },
    {
      "tang": 3,
      "dich_den": "Khai thác tứ giác nội tiếp sinh ra bởi góc vuông tại I",
      "suy_luan": "Tứ giác NACI nội tiếp => góc NIA = góc NCA; Tứ giác CIMP nội tiếp => góc MIP = góc MCP."
    },
    {
      "tang": 4,
      "dich_den": "góc NCA = góc MCP (ĐIỂM KHỞI PHÁT)",
      "suy_luan": "Do tam giác CAN = tam giác CMP (c-g-c) đã chứng minh ở câu b1. Dữ kiện hoàn tất!"
    }
  ],
  "so_do_cong_thuc_hinh_thong": [
    "[ĐÍCH ĐẾN]: AM ĐI QUA TRUNG ĐIỂM NP <=> A, I, M THẲNG HÀNG",
    "<= góc AIM = 180 độ <=> góc PIA + góc MIP = 180 độ",
    "<= góc MIP = góc NIA (do góc PIA + góc NIA = 180 độ vì N, I, P thẳng hàng)",
    "<= { góc NIA = góc NCA (tứ giác NACI nội tiếp) ; góc MIP = góc MCP (tứ giác CIMP nội tiếp) }",
    "<= góc NCA = góc MCP",
    "<= ΔCAN = ΔCMP (c-g-c) [GIẢ THIẾT KHỞI PHÁT TỰ NHIÊN]"
  ],
  "phan_tich_su_pham": {
    "ky_thuat_vang": "Chuyển bài toán 'chứng minh trung điểm' sang 'chứng minh 3 điểm thẳng hàng' bằng cách gọi trước I là trung điểm NP để khai thác tính chất tam giác cân CI vuông góc NP.",
    "chuoi_cau_hoi": [
      "Câu 1: Câu b1 đã chứng minh tam giác CPN cân tại C, tính chất đường trung tuyến ứng với đỉnh C là gì?",
      "Câu 2: Nếu gọi I là trung điểm của NP, ta có ngay CI vuông góc NP, điều này tạo ra những góc vuông nào?",
      "Câu 3: Kết hợp góc vuông CIN = 90 độ với góc CAN = 90 độ, ta phát hiện tứ giác nào nội tiếp?",
      "Câu 4: Ba điểm N, I, P đã thẳng hàng (góc NIP = 180 độ), làm sao để kéo A, I, M thẳng hàng theo?"
    ]
  },
  "barem_diem": [
    {"muc": "Câu a", "diem": 0.75, "noi_dung": "Chứng minh tứ giác ACMB nội tiếp đường tròn đường kính BC"},
    {"muc": "Câu b1", "diem": 0.75, "noi_dung": "Chứng minh tam giác CAN = tam giác CMP (c-g-c) suy ra tam giác CPN cân tại C"},
    {"muc": "Câu b2", "diem": 1.00, "noi_dung": "Gọi I là trung điểm NP, chứng minh tứ giác NACI, CIMP nội tiếp và kết luận A, I, M thẳng hàng"}
  ]
}
```
"""
    with open(prompt_file, 'w', encoding='utf-8') as f:
        f.write(prompt_content)

print("Updated prompt.md successfully for BAI_HINH_01!")
