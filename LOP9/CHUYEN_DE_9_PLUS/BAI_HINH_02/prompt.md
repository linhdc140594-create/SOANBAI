# PROMPT CHUYÊN SÂU PHÂN TÍCH SUY LUẬN TOÁN 9+ - BÀI HÌNH 02
> **Nguồn trích xuất:** Đề số 02 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10  
> **Mô hình toán học:** Bổ đề Trực tâm kinh điển (Hình bình hành $BHCM$ & Điểm đối xứng của trực tâm trên đường tròn) kết hợp Cực trị hình học (BĐT Cauchy $DB \cdot DC \le \frac{BC^2}{4}$)

---

## 📌 I. NGUYÊN VĂN ĐỀ BÀI TOÁN HÌNH HỌC

```latex
Cho đường tròn (O), bán kính R (R > 0) và dây cung BC cố định. Một điểm A chuyển động trên cung lớn BC sao cho tam giác ABC có ba góc nhọn. Kẻ các đường cao AD, BE của tam giác ABC cắt nhau tại H.
a) Chứng minh rằng tứ giác DHEC nội tiếp một đường tròn.
b) Kẻ đường kính AM của đường tròn (O) và OI vuông góc với BC tại I. Chứng minh rằng I là trung điểm của HM.
c) (Phân hóa 9+): Khi BC cố định, xác định vị trí của A trên đường tròn (O) để tích DH . DA đạt giá trị lớn nhất.
```

---

## 🎯 II. NHIỆM VỤ YÊU CẦU DÀNH CHO AI (CLAUDE / OPENAI)

Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.  
Hãy phân tích sâu và giải mã bài toán hình học này theo các tiêu chuẩn cao cấp sau:

### 1. Phân tích mô hình toán học cốt lõi
- Nhận diện 2 "bổ đề vàng" trong hình học trực tâm:
  + Bổ đề 1: Tứ giác $BHCM$ là hình bình hành $\implies I$ là trung điểm chung của $BC$ và $HM$.
  + Bổ đề 2: Kéo dài $AD$ cắt $(O)$ tại $K \implies K$ đối xứng với trực tâm $H$ qua cạnh $BC$, tức $DH = DK$.
- Điểm nghẽn ở câu phân hóa c: Làm sao đánh giá tích biến thiên $DH \cdot DA$ khi cả $A, H, D$ đều thay đổi vị trí?
- Chiến lược giải: Chuyển $DH$ thành $DK$, dùng phương tích $DK \cdot DA = DB \cdot DC$, sau đó áp dụng BĐT Cauchy cho 2 đoạn thẳng có tổng không đổi $DB + DC = BC$ cố định!

### 2. Thiết lập Sơ đồ Tư duy ngược (Reverse Thinking Mindmap)
- Lập chuỗi truy ngược từ **[ĐÍCH ĐẾN CẦN CHỨNG MINH: MAX DH . DA]** ngược về **[GIẢ THIẾT GỐC]**:
  + **Đích đến:** $\max(DH \cdot DA)$ khi $BC$ cố định.
  + $\Uparrow$ Cần chặn trên bằng đại lượng không đổi liên quan tới $BC$: $DH \cdot DA \le \left(\frac{BC}{2}\right)^2$.
  + $\Uparrow$ Áp dụng BĐT Cauchy: $DB \cdot DC \le \left(\frac{DB+DC}{2}\right)^2 = \left(\frac{BC}{2}\right)^2$.
  + $\Uparrow$ Cần chuyển đổi tích đoạn thẳng: $DH \cdot DA = DB \cdot DC$.
  + $\Uparrow$ Dùng phương tích qua cát tuyến trong $(O)$: $DK \cdot DA = DB \cdot DC$.
  + $\Uparrow$ Cần: $DH = DK$ (với $K$ là giao điểm thứ hai của $AD$ với $(O)$).
  + $\Uparrow$ Chứng minh $BD$ là đường trung trực của $HK \iff \triangle HBK$ cân tại $B \iff \widehat{HBD} = \widehat{KBD}$.
  + $\Uparrow$ So sánh góc qua góc trung gian $\widehat{C}$:
    * $\widehat{HBD} = 90^\circ - \widehat{C}$
    * $\widehat{KBD} = \widehat{KAC} = 90^\circ - \widehat{C}$ (hai góc nội tiếp cùng chắn $\stackrel{\frown}{KC}$).
    $\implies \widehat{HBD} = \widehat{KBD}$ (ĐIỂM KHỞI PHÁT TỰ NHIÊN!).

### 3. Thiết lập Sơ đồ Công thức hình Cây thông (Pine-Tree Formula Tree)
- Thiết kế cây logic thuần túy công thức toán học:
  - **Đỉnh ngọn:** $\boxed{\mathbf{\max(DH \cdot DA) = \dfrac{BC^2}{4} \iff A \text{ LÀ ĐIỂM CHÍNH GIỮA CỦA CUNG LỚN } BC}}$
  - Thân cây: Các bước biến đổi:
    * Dấu bằng BĐT Cauchy: $DB = DC \iff D \equiv I \iff \triangle ABC$ cân tại $A$.
    * Cauchy: $DB \cdot DC \le \left(\frac{DB+DC}{2}\right)^2 = \frac{BC^2}{4}$.
    * Phương tích: $DH \cdot DA = DK \cdot DA = DB \cdot DC$.
  - Tách 2 nhánh:
    * Nhánh trái: $\triangle DBK \sim \triangle DAC \implies DK \cdot DA = DB \cdot DC$
    * Nhánh phải: $\triangle HBK$ cân tại $B$ $\implies DH = DK$
  - Gốc rễ: $\widehat{KBD} = \widehat{KAC} = 90^\circ - \widehat{C} = \widehat{HBD}$ (Khởi phát).

### 4. Bình luận sư phạm & Kỹ thuật kẻ đường phụ
- Phân tích: **"Tại sao lại kéo dài AD cắt (O) tại K?"**
  + Đoạn $DH$ nằm lơ lửng bên trong tam giác, không thuộc bất kỳ đường tròn nào.
  + Kéo dài $AD$ cắt $(O)$ tại $K$ đưa điểm $H$ thành điểm $K$ nằm trên đường tròn $(O)$, lập tức kích hoạt định lý phương tích cát tuyến $DK \cdot DA = DB \cdot DC$!
- Chuỗi 4 câu hỏi dẫn dắt của Giáo viên trên lớp.

### 5. Lời giải chuẩn mực & Barem điểm chi tiết
- Trình bày lời giải xuôi hoàn chỉnh chuẩn mực.
- Barem điểm chia nhỏ đến từng $0{,}25$đ.

---

## 📤 III. ĐỊNH DẠNG ĐẦU RA MONG MUỐN (JSON CHUẨN)

Trả về kết quả dưới định dạng JSON hợp lệ:
```json
{
  "bai_toan": {
    "ma_bai": "BAI_HINH_02",
    "nguon": "Đề 02 - Tuyển tập 55 Đề Thi Vào Lớp 10",
    "mo_hinh": "Trực tâm tam giác nhọn, hình bình hành BHCM, điểm đối xứng trên đường tròn và cực trị Cauchy",
    "de_bai": "Cho đường tròn (O), bán kính R và dây cung BC cố định..."
  },
  "so_do_tu_duy_nguoc": [
    {
      "tang": 1,
      "dich_den": "max(DH . DA) khi BC cố định",
      "cau_hoi_truy_nguoc": "DH và DA đều thay đổi, làm sao quy về đại lượng cố định?",
      "muc_tieu_con": "Biến đổi tích DH . DA thành tích DB . DC để áp dụng BĐT Cauchy với DB + DC = BC không đổi"
    },
    {
      "tang": 2,
      "dich_den": "DH . DA = DB . DC",
      "cau_hoi_truy_nguoc": "Làm sao gắn DH và DA vào đường tròn (O)?",
      "vu_khi_duong_phu": "Kéo dài AD cắt (O) tại K. Chứng minh DH = DK và DK . DA = DB . DC"
    },
    {
      "tang": 3,
      "dich_den": "DH = DK",
      "suy_luan": "Tam giác HBK cân tại B có BD là đường cao đồng thời là phân giác do góc HBD = góc KBD = 90 độ - góc C"
    },
    {
      "tang": 4,
      "dich_den": "DK . DA = DB . DC",
      "suy_luan": "Tam giác DBK đồng dạng tam giác DAC (g-g) do góc BDK = ADC = 90 độ và góc BKD = ACD (cùng chắn cung AB)"
    },
    {
      "tang": 5,
      "dich_den": "Kết luận cực trị",
      "suy_luan": "DH . DA = DB . DC <= ((DB+DC)/2)^2 = BC^2 / 4. Dấu bằng khi DB = DC <=> A là điểm chính giữa cung lớn BC"
    }
  ],
  "so_do_cong_thuc_hinh_thong": [
    "[ĐÍCH ĐẾN]: max(DH . DA) = BC^2 / 4 <=> A LÀ ĐIỂM CHÍNH GIỮA CUNG LỚN BC",
    "<= Dấu '=' BĐT Cauchy: DB = DC <=> D trùng I <=> Tam giác ABC cân tại A",
    "<= BĐT Cauchy: DB . DC <= ((DB+DC)/2)^2 = (BC/2)^2 = BC^2 / 4",
    "<= DH . DA = DB . DC",
    "<= { DH = DK ; DK . DA = DB . DC }",
    "<= { Tam giác HBK cân tại B <=> góc HBD = góc KBD ; Tam giác DBK ∼ Tam giác DAC (g-g) }",
    "<= góc HBD = góc KBD = góc KAC = 90° - góc C [GIẢ THIẾT KHỞI PHÁT TỰ NHIÊN]"
  ],
  "barem_diem": [
    {"muc": "Câu a", "diem": 0.75, "noi_dung": "Chứng minh tứ giác DHEC nội tiếp đường tròn đường kính HC"},
    {"muc": "Câu b", "diem": 0.75, "noi_dung": "Chứng minh BHCM là hình bình hành suy ra I là trung điểm HM"},
    {"muc": "Câu c - Ý 1", "diem": 0.25, "noi_dung": "Kéo dài AD cắt (O) tại K, chứng minh tam giác HBK cân suy ra DH = DK"},
    {"muc": "Câu c - Ý 2", "diem": 0.25, "noi_dung": "Chứng minh tam giác DBK đồng dạng DAC suy ra DK . DA = DB . DC"},
    {"muc": "Câu c - Ý 3", "diem": 0.25, "noi_dung": "Áp dụng BĐT Cauchy suy ra DH . DA <= BC^2 / 4"},
    {"muc": "Câu c - Ý 4", "diem": 0.25, "noi_dung": "Chỉ ra dấu bằng và kết luận A là điểm chính giữa cung lớn BC"}
  ]
}
```
"""
    with open(os.path.join("LOP9/CHUYEN_DE_9_PLUS/BAI_HINH_02", "prompt.md"), "w", encoding="utf-8") as f:
        f.write(prompt_content)
    print("Updated prompt.md for BAI_HINH_02 successfully.")
