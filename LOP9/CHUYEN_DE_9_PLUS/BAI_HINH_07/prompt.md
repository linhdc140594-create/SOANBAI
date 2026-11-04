# PROMPT CHUYÊN SÂU PHÂN TÍCH SUY LUẬN TOÁN 9+ - BÀI HÌNH 07
> **Nguồn trích xuất:** Đề số 07 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10  
> **Mô hình toán học:** Bổ đề Tam giác đồng dạng xoay $\triangle AHK \backsim \triangle ABN$ & Kỹ thuật Tam giác cân kép chứng minh đường thẳng $HK$ đi qua trung điểm của đoạn $AB$.

---

## 📌 I. NGUYÊN VĂN ĐỀ BÀI TOÁN HÌNH HỌC

```latex
Cho tam giác nhọn ABC nội tiếp trong đường tròn (O) có AB < AC. Trên cung nhỏ AC lấy điểm M khác A thỏa mãn MA < MC. Vẽ đường kính MN của đường tròn (O). Gọi H và K lần lượt là hình chiếu vuông góc của điểm A trên các đường thẳng MB và MN.
a) Chứng minh bốn điểm A, H, K, M cùng thuộc một đường tròn đường kính AM.
b) Chứng minh tam giác AHK đồng dạng với tam giác ABN và AH . AN = AK . AB.
c) (Phân hóa 9+): Chứng minh đường thẳng HK cắt đoạn thẳng AB tại đúng trung điểm của AB.
```

---

## 🎯 II. NHIỆM VỤ YÊU CẦU DÀNH CHO AI (CLAUDE / OPENAI)

Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.  
Hãy phân tích sâu và giải mã bài toán hình học này theo các tiêu chuẩn cao cấp sau:

### 1. Phân tích mô hình toán học cốt lõi
- **Nhận diện Bổ đề Đồng dạng xoay:**
  + Tứ giác $AHKM$ nội tiếp đường tròn đường kính $AM$.
  + Các góc nội tiếp chuyển giao tự nhiên: $\widehat{AHK} = \widehat{AMN} = \widehat{ABN}$ và $\widehat{AKH} = \widehat{AMB} = \widehat{ANB}$.
  $\implies \triangle AHK \backsim \triangle ABN$ (g-g) $\implies AH \cdot AN = AK \cdot AB$.
- **Kỹ thuật Đỉnh cao Tam giác cân kép:**
  + Để chứng minh $E = HK \cap AB$ là trung điểm $AB$, ta không dùng Ta-lét phức tạp mà bắc cầu qua đoạn $EH$:
    * Chứng minh $EA = EH$ ($\triangle EAH$ cân tại $E$).
    * Chứng minh $EB = EH$ ($\triangle EHB$ cân tại $E$).
  + Điểm kích hoạt then chốt: $AH \parallel BN$ (cùng vuông góc với $MB$) tạo ra cặp góc so le trong $\widehat{EAH} = \widehat{ABN}$, bằng đúng góc $\widehat{EHA} = \widehat{AHK}$!

### 2. Thiết lập Sơ đồ Tư duy ngược (Reverse Thinking Mindmap)
- Lập chuỗi truy ngược từ **[ĐÍCH ĐẾN: E LÀ TRUNG ĐIỂM CỦA AB]** ngược về **[GIẢ THIẾT GỐC]**:
  + **Đích đến:** $E = HK \cap AB$ là trung điểm của đoạn thẳng $AB \iff EA = EB$.
  + $\Uparrow$ Kỹ thuật bắc cầu qua đoạn trung gian $EH$: $EA = EH$ và $EB = EH$.
  + $\Uparrow$ Hai tam giác cân độc lập tại đỉnh $E$:
    * $\triangle EAH$ cân tại $E \iff \widehat{EHA} = \widehat{EAH}$.
    * $\triangle EHB$ cân tại $E \iff \widehat{EHB} = \widehat{EBH}$.
  + $\Uparrow$ Liên kết góc phụ trong tam giác vuông $AHB$ tại $H$:
    $\widehat{EHB} = 90^\circ - \widehat{EHA}$ và $\widehat{EBH} = 90^\circ - \widehat{EAH}$.
    $\implies$ Chỉ cần chứng minh $\widehat{EHA} = \widehat{EAH}$!
  + $\Uparrow$ Kết nối qua góc trung gian $\widehat{ABN}$:
    * $\widehat{EHA} = \widehat{AHK} = \widehat{AMN} = \widehat{ABN}$ (tứ giác nội tiếp $AHKM$ và $(O)$).
    * $\widehat{EAH} = \widehat{HAB} = \widehat{ABN}$ (hai góc so le trong do $AH \parallel BN$).
  + $\Uparrow$ Điều kiện song song: $AH \parallel BN$.
  + $\Uparrow$ **Giả thiết gốc:** $AH \perp MB$ (theo giả thiết) và $BN \perp MB$ (góc nội tiếp chắn nửa đường tròn $\widehat{MBN} = 90^\circ$ của $(O)$ đường kính $MN$)!

### 3. Thiết lập Sơ đồ Công thức hình Cây thông (Pine-Tree Formula Tree)
- Thiết kế cây logic thuần túy công thức toán học:
  - **Đỉnh ngọn:** $\boxed{\mathbf{E = HK \cap AB \text{ LÀ TRUNG ĐIỂM CỦA } AB \iff EA = EB = \dfrac{AB}{2}}}$
  - Thân cây:
    * $\Uparrow \quad EA = EH \quad \text{và} \quad EB = EH \quad (\text{Bắc cầu qua đoạn } EH)$
    * $\Uparrow \quad \triangle EAH \text{ cân tại } E \quad \& \quad \triangle EHB \text{ cân tại } E \quad (\triangle AHB \text{ vuông tại } H)$
    * $\Uparrow \quad \widehat{EHA} = \widehat{EAH} \iff \widehat{EHB} = 90^\circ - \widehat{EHA} = 90^\circ - \widehat{EAH} = \widehat{EBH}$
    * $\Uparrow \quad \widehat{EHA} = \widehat{ABN} \quad \text{và} \quad \widehat{EAH} = \widehat{ABN}$
  - Tách hai nhánh:
    * Nhánh trái (Tứ giác nội tiếp): $\widehat{EHA} = \widehat{AHK} = \widehat{AMN} = \widehat{ABN} \quad (\text{cùng chắn } \stackrel{\frown}{AN})$
    * Nhánh phải (Cặp góc so le trong): $\widehat{EAH} = \widehat{HAB} = \widehat{ABN} \quad (AH \parallel BN)$
  - Bệ đỡ khởi phát: $AH \perp MB \text{ và } BN \perp MB \ (\widehat{MBN}=90^\circ \text{ do đường kính } MN) \implies AH \parallel BN$.

### 4. Bình luận sư phạm & Kỹ thuật Tam giác cân kép
- Phân tích: **"Tại sao lại nghĩ đến việc so sánh EA và EB thông qua EH?"**
  + Điểm $H$ là đỉnh góc vuông của $\triangle AHB$. Trong tam giác vuông, đường trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền. Do đó nếu $E$ là trung điểm $AB$ thì chắc chắn $EH = EA = EB$!
  + Việc đảo ngược tính chất đường trung tuyến thành "chứng minh hai tam giác cân $EAH$ và $EHB$" là một đòn bẩy sư phạm mẫu mực giúp học sinh giải quyết bài toán chỉ bằng các góc so le trong và góc nội tiếp cơ bản!
- Chuỗi 4 câu hỏi dẫn dắt của Giáo viên trên lớp.

### 5. Lời giải chuẩn mực & Barem điểm chi tiết
- Trình bày lời giải xuôi 3 câu a, b, c.
- Barem điểm chia nhỏ đến từng $0{,}25$đ.

---

## 📤 III. ĐỊNH DẠNG ĐẦU RA MONG MUỐN (JSON CHUẨN)

Trả về kết quả dưới định dạng JSON hợp lệ đầy đủ các khóa: `bai_toan`, `mo_hinh_cot_loi`, `so_do_tu_duy_nguoc`, `cay_thong_cong_thuc`, `binh_luan_su_pham`, `loi_giai_chi_tiet`.
