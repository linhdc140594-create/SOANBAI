# PROMPT CHUYÊN SÂU PHÂN TÍCH SUY LUẬN TOÁN 9+ - BÀI HÌNH 06
> **Nguồn trích xuất:** Đề số 06 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10  
> **Mô hình toán học:** Bổ đề Tiếp tuyến kép từ trung điểm đường cao (Tiếp tuyến $KE, KF$) & Ngũ giác nội tiếp đường kính $OK$ ($O, D, E, K, F$).

---

## 📌 I. NGUYÊN VĂN ĐỀ BÀI TOÁN HÌNH HỌC

```latex
Cho tam giác ABC có ba góc nhọn (AB < AC), đường tròn (O) đường kính BC cắt các cạnh AB, AC lần lượt tại E và F. Gọi H là giao điểm của BF và CE, đoạn thẳng AH cắt BC tại D.
a) Chứng minh tứ giác AEHF nội tiếp đường tròn và xác định tâm K của đường tròn đó.
b) Chứng minh KE và KF là các tiếp tuyến của đường tròn (O) đường kính BC.
c) (Phân hóa 9+): Chứng minh năm điểm O, D, E, K, F cùng thuộc một đường tròn đường kính OK, và OK là đường trung trực của đoạn thẳng EF.
```

---

## 🎯 II. NHIỆM VỤ YÊU CẦU DÀNH CHO AI (CLAUDE / OPENAI)

Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.  
Hãy phân tích sâu và giải mã bài toán hình học này theo các tiêu chuẩn cao cấp sau:

### 1. Phân tích mô hình toán học cốt lõi
- **Nhận diện Bổ đề "Cạnh huyền chung OK":**
  + Điểm $K$ là trung điểm đường cao $AH$, điểm $O$ là trung điểm cạnh đáy $BC$.
  + Đoạn nối hai tâm $OK$ đóng vai trò là cạnh huyền chung của 3 tam giác vuông:
    * $\triangle KEO$ vuông tại $E$ (tiếp tuyến $KE \perp OE$).
    * $\triangle KDO$ vuông tại $D$ (đường cao $AD \perp BC$).
    * $\triangle KFO$ vuông tại $F$ (tiếp tuyến $KF \perp OF$).
  + Cả ba đỉnh $E, D, F$ cùng nhìn đoạn $OK$ dưới góc vuông $90^\circ \implies 5$ điểm $O, D, E, K, F$ cùng thuộc đường tròn đường kính $OK$!
- **Hệ quả đối xứng:** $KE = KF$ (hai tiếp tuyến cắt nhau) và $OE = OF = R \implies OK$ là đường trung trực của dây cung chung $EF$ $\implies OK \perp EF$.

### 2. Thiết lập Sơ đồ Tư duy ngược (Reverse Thinking Mindmap)
- Lập chuỗi truy ngược từ **[ĐÍCH ĐẾN: 5 ĐIỂM O, D, E, K, F CÙNG THUỘC ĐƯỜNG TRÒN ĐƯỜNG KÍNH OK]** ngược về **[GIẢ THIẾT GỐC]**:
  + **Đích đến:** Năm điểm $O, D, E, K, F$ cùng thuộc đường tròn đường kính $OK$.
  + $\Uparrow$ Ba đỉnh $E, D, F$ cùng nhìn đoạn $OK$ dưới góc $90^\circ$: $\widehat{KEO} = \widehat{KDO} = \widehat{KFO} = 90^\circ$.
  + $\Uparrow$ Ba điều kiện vuông góc độc lập:
    * Điều kiện 1: $\widehat{KDO} = 90^\circ \iff AD \perp BC \text{ tại } D$ (do $H$ là trực tâm $\triangle ABC$).
    * Điều kiện 2: $\widehat{KEO} = 90^\circ \iff KE \perp OE$ (chứng minh tiếp tuyến $KE$).
    * Điều kiện 3: $\widehat{KFO} = 90^\circ \iff KF \perp OF$ (chứng minh tiếp tuyến $KF$).
  + $\Uparrow$ Kỹ thuật cộng góc bẹt chứng minh tiếp tuyến:
    $\widehat{KEO} = 180^\circ - (\widehat{KEA} + \widehat{OEB}) = 180^\circ - (\widehat{KAE} + \widehat{OBE}) = 180^\circ - 90^\circ = 90^\circ$.
  + $\Uparrow$ Sử dụng hai tam giác cân:
    * $\triangle KAE$ cân tại $K$ ($KE = KA = \frac{AH}{2}$ do trung tuyến tam giác vuông $\triangle AEH$).
    * $\triangle OBE$ cân tại $O$ ($OE = OB = R$).
  + $\Uparrow$ Tổng hai góc phụ nhau trong tam giác vuông $ABD$ tại $D$: $\widehat{BAD} + \widehat{ABD} = 90^\circ$.
  + $\Uparrow$ **Giả thiết gốc:** Góc nội tiếp chắn nửa đường tròn $\widehat{BEC} = \widehat{BFC} = 90^\circ$ của đường tròn $(O)$ đường kính $BC$!

### 3. Thiết lập Sơ đồ Công thức hình Cây thông (Pine-Tree Formula Tree)
- Thiết kế cây logic thuần túy công thức toán học:
  - **Đỉnh ngọn:** $\boxed{\mathbf{5 \text{ ĐIỂM } O, D, E, K, F \text{ CÙNG THUỘC ĐƯỜNG TRÒN ĐƯỜNG KÍNH } OK}}$
  - Thân cây:
    * $\Uparrow \quad \widehat{KEO} = \widehat{KDO} = \widehat{KFO} = 90^\circ \quad (\text{Cùng nhìn đoạn } OK \text{ dưới góc } 90^\circ)$
  - Tách 3 nhánh cân xứng:
    * Nhánh trái: $KE \perp OE \iff \widehat{KEO} = 180^\circ - (\widehat{KAE} + \widehat{OBE}) = 90^\circ$
    * Nhánh giữa: $AD \perp BC \text{ tại } D \implies \widehat{KDO} = 90^\circ \quad (H \text{ là trực tâm } \triangle ABC)$
    * Nhánh phải: $KF \perp OF \iff \widehat{KFO} = 180^\circ - (\widehat{KAF} + \widehat{OCF}) = 90^\circ$
  - Bệ đỡ khởi phát: $E, F \in (O) \text{ đường kính } BC \implies CE \perp AB, \ BF \perp AC \implies H \text{ là trực tâm và } K \text{ là trung điểm } AH$.

### 4. Bình luận sư phạm & Kỹ thuật chứng minh 5 điểm nội tiếp
- Phân tích: **"Tại sao lại nhắm vào đoạn OK làm đường kính?"**
  + Đoạn $OK$ nối hai tâm của hai đường tròn $(K, AH/2)$ và $(O, BC/2)$.
  + Điểm $D$ là chân đường cao chung. Hai điểm $E, F$ là hai tiếp điểm của các tiếp tuyến kẻ từ $K$ đến $(O)$.
  + Đây là mô hình kinh điển: Tâm $K$ và tâm $O$ tạo thành cạnh huyền của tất cả các góc vuông sinh ra từ tiếp tuyến và chân đường vuông góc!
- Chuỗi 4 câu hỏi dẫn dắt của Giáo viên trên lớp.

### 5. Lời giải chuẩn mực & Barem điểm chi tiết
- Trình bày lời giải xuôi 3 câu a, b, c.
- Barem điểm chia nhỏ đến từng $0{,}25$đ.

---

## 📤 III. ĐỊNH DẠNG ĐẦU RA MONG MUỐN (JSON CHUẨN)

Trả về kết quả dưới định dạng JSON hợp lệ đầy đủ các khóa: `bai_toan`, `mo_hinh_cot_loi`, `so_do_tu_duy_nguoc`, `cay_thong_cong_thuc`, `binh_luan_su_pham`, `loi_giai_chi_tiet`.
