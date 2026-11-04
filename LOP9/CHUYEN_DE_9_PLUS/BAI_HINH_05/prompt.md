# PROMPT CHUYÊN SÂU PHÂN TÍCH SUY LUẬN TOÁN 9+ - BÀI HÌNH 05
> **Nguồn trích xuất:** Đề số 05 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10  
> **Mô hình toán học:** Bổ đề Đường kính vuông góc dây cung kết hợp Trực tâm ẩn $M$ của tam giác $CDI$ và Tam giác trực tâm $HKN$.

---

## 📌 I. NGUYÊN VĂN ĐỀ BÀI TOÁN HÌNH HỌC

```latex
Cho đường tròn (O) và dây cung AB không đi qua tâm. Gọi H là trung điểm của AB, đường thẳng HO cắt đường tròn (O) tại hai điểm C và D (C thuộc cung nhỏ AB). Lấy điểm M thuộc đoạn AH (M khác A và H), tia CM cắt đường tròn (O) tại điểm thứ hai là N.
a) Chứng minh bốn điểm D, N, M, H cùng thuộc một đường tròn.
b) Gọi I là giao điểm của hai đường thẳng DN và AB, K là giao điểm của hai đường thẳng CI và DM. Chứng minh CM . CN = CK . CI.
c) (Phân hóa 9+): Chứng minh điểm M là tâm của đường tròn nội tiếp tam giác trực tâm HKN.
```

---

## 🎯 II. NHIỆM VỤ YÊU CẦU DÀNH CHO AI (CLAUDE / OPENAI)

Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.  
Hãy phân tích sâu và giải mã bài toán hình học này theo các tiêu chuẩn cao cấp sau:

### 1. Phân tích mô hình toán học cốt lõi
- **Phát hiện mô hình Trực tâm ẩn:**
  + Trong tam giác $CDI$, ta có:
    * $IH \perp CD$ tại $H$ (đường kính qua trung điểm dây cung $AB$ thì vuông góc với dây cung).
    * $CN \perp DI$ tại $N$ (góc nội tiếp chắn nửa đường tròn đường kính $CD$).
    * Hai đường cao $IH$ và $CN$ giao nhau tại điểm $M$.
    $\implies M$ chính là **trực tâm của tam giác $CDI$**!
  + Hệ quả trực tiếp: Đường thẳng qua đỉnh thứ ba $D$ và trực tâm $M$ là đường cao thứ ba: $DM \perp CI$ tại $K$.
  + Tam giác $HKN$ chính là **tam giác trực tâm (Orthic Triangle)** của $\triangle CDI$.
  + Do đó, trực tâm $M$ đồng thời là **tâm đường tròn nội tiếp của tam giác $HKN$** (Kế thừa trọn vẹn Bổ đề ở Bài 4).

### 2. Thiết lập Sơ đồ Tư duy ngược (Reverse Thinking Mindmap)
- Lập chuỗi truy ngược từ **[ĐÍCH ĐẾN: M LÀ TÂM ĐƯỜNG TRÒN NỘI TIẾP TAM GIÁC HKN]** ngược về **[GIẢ THIẾT GỐC]**:
  + **Đích đến:** $M$ là tâm đường tròn nội tiếp tam giác trực tâm $HKN$.
  + $\Uparrow$ $KM, NM, HM$ là các tia phân giác trong của tam giác $HKN$.
  + $\Uparrow$ Cần chứng minh $KM$ là phân giác trong của $\widehat{HKN} \iff \widehat{MKH} = \widehat{MKN}$.
  + $\Uparrow$ Dùng góc phụ với $90^\circ$ qua đường cao $DK \perp CI$:
    * $\widehat{MKH} = 90^\circ - \widehat{IKH}$
    * $\widehat{MKN} = 90^\circ - \widehat{CKN}$
    $\implies$ Cần chứng minh $\widehat{IKH} = \widehat{CKN}$.
  + $\Uparrow$ Chuyển góc qua hai tứ giác nội tiếp:
    * Tứ giác $HKMI$ nội tiếp (đường kính $MI$) $\implies \widehat{IKH} = \widehat{IMH}$ (cùng chắn cung $IH$).
    * Tứ giác $DKNC$ nội tiếp (đường kính $CD$) $\implies \widehat{CKN} = \widehat{CDN}$ (cùng chắn cung $CN$).
  + $\Uparrow$ Cần chứng minh $\widehat{IMH} = \widehat{CDN}$.
  + $\Uparrow$ Nhận xét: $\widehat{IMH} = \widehat{DMN}$ (hai góc đối đỉnh). Mà trong tam giác vuông $DMN$ vuông tại $N$, ta có $\widehat{DMN} = 90^\circ - \widehat{MDN} = 90^\circ - \widehat{CDN} \dots$ hoặc trong tam giác vuông $CDI$, hai góc nhọn cùng phụ một góc!
  + $\Uparrow$ **Giả thiết gốc:** $M$ là trực tâm của tam giác $CDI$ (giao điểm của $IH \perp CD$ và $CN \perp DI$).

### 3. Thiết lập Sơ đồ Công thức hình Cây thông (Pine-Tree Formula Tree)
- Thiết kế cây logic thuần túy công thức toán học:
  - **Đỉnh ngọn:** $\boxed{\mathbf{M \text{ LÀ TÂM ĐƯỜNG TRÒN NỘI TIẾP } \triangle HKN}}$
  - Thân cây:
    * $\Uparrow \quad KM, NM, HM \text{ là các đường phân giác trong của } \triangle HKN$
    * $\Uparrow \quad \widehat{MKH} = \widehat{MKN} \iff 90^\circ - \widehat{IKH} = 90^\circ - \widehat{CKN} \quad (DK \perp CI)$
    * $\Uparrow \quad \widehat{IKH} = \widehat{CKN}$
    * $\Uparrow \quad \widehat{IMH} = \widehat{CDN} \quad (\triangle IMH \backsim \triangle CDN)$
  - Hai nhánh gốc rễ:
    * Nhánh trái: Tứ giác $HKMI$ nội tiếp (đường kính $MI$) $\implies \widehat{IKH} = \widehat{IMH}$
    * Nhánh phải: Tứ giác $DKNC$ nội tiếp (đường kính $CD$) $\implies \widehat{CKN} = \widehat{CDN}$
  - Bệ đỡ khởi phát: $IH \perp CD \text{ tại } H \text{ và } CN \perp DI \text{ tại } N \implies M \text{ là trực tâm của } \triangle CDI \implies DK \perp CI \text{ tại } K$.

### 4. Bình luận sư phạm & Kỹ thuật nhận diện Trực tâm ẩn
- Phân tích: **"Làm sao phát hiện ra tam giác lớn CDI và trực tâm M?"**
  + Đoạn thẳng $AB$ vuông góc với đường kính $CD$ tại $H$ chính là một đường cao.
  + Điểm $N$ thuộc đường tròn đường kính $CD$ sinh ra góc vuông thứ hai $CN \perp DI$.
  + Sự giao cắt của hai đường cao này tại $M$ lập tức chỉ ra $M$ là trực tâm của $\triangle CDI$!
- Chuỗi 4 câu hỏi dẫn dắt của Giáo viên trên lớp.

### 5. Lời giải chuẩn mực & Barem điểm chi tiết
- Trình bày lời giải xuôi 3 câu a, b, c.
- Barem điểm chia nhỏ đến từng $0{,}25$đ.

---

## 📤 III. ĐỊNH DẠNG ĐẦU RA MONG MUỐN (JSON CHUẨN)

Trả về kết quả dưới định dạng JSON hợp lệ đầy đủ các khóa: `bai_toan`, `mo_hinh_cot_loi`, `so_do_tu_duy_nguoc`, `cay_thong_cong_thuc`, `binh_luan_su_pham`, `loi_giai_chi_tiet`.
