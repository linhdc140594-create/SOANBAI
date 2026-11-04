# PROMPT CHUYÊN SÂU PHÂN TÍCH SUY LUẬN TOÁN 9+ - BÀI HÌNH 04
> **Nguồn trích xuất:** Đề số 04 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10  
> **Mô hình toán học:** Bổ đề Tam giác trực tâm kinh điển (Orthic Triangle) & Trực tâm $H$ là Tâm đường tròn nội tiếp của tam giác tạo bởi ba chân đường cao.

---

## 📌 I. NGUYÊN VĂN ĐỀ BÀI TOÁN HÌNH HỌC

```latex
Cho tam giác ABC có ba góc nhọn (AB < AC). Ba đường cao AI, BK, CL cắt nhau tại trực tâm H.
a) Chứng minh các tứ giác BIHL và CIHK nội tiếp đường tròn.
b) Chứng minh góc AKL = góc IKC và suy ra KB là tia phân giác của góc LKI.
c) (Phân hóa 9+): Chứng minh trực tâm H là tâm của đường tròn nội tiếp tam giác trực tâm IKL.
```

---

## 🎯 II. NHIỆM VỤ YÊU CẦU DÀNH CHO AI (CLAUDE / OPENAI)

Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.  
Hãy phân tích sâu và giải mã bài toán hình học này theo các tiêu chuẩn cao cấp sau:

### 1. Phân tích mô hình toán học cốt lõi
- Nhận diện hệ thống 6 tứ giác nội tiếp xoay quanh trực tâm $H$:
  + Ba tứ giác nội tiếp đường kính các đoạn $AH, BH, CH$: $AKHL$ (đường kính $AH$), $BIHL$ (đường kính $BH$), $CIHK$ (đường kính $CH$).
  + Ba tứ giác nội tiếp đường kính các cạnh $BC, CA, AB$: $BCLK$ (đường kính $BC$), $ACKI$ (đường kính $AC$), $ABIK$ (đường kính $AB$).
- Điểm nghẽn học sinh thường gặp:
  + Không kết nối được mối liên hệ giữa các góc nội tiếp cùng chắn một cung với cặp góc đối đỉnh $\widehat{AHL} = \widehat{IHC}$.
  + Lúng túng khi chứng minh một điểm là tâm nội tiếp vì nghĩ rằng phải tính bán kính hoặc khoảng cách, thay vì chứng minh giao điểm của hai đường phân giác trong.

### 2. Thiết lập Sơ đồ Tư duy ngược (Reverse Thinking Mindmap)
- Lập chuỗi truy ngược từ **[ĐÍCH ĐẾN: H LÀ TÂM ĐƯỜNG TRÒN NỘI TIẾP TAM GIÁC IKL]** ngược về **[GIẢ THIẾT GỐC]**:
  + **Đích đến:** $H$ là tâm đường tròn nội tiếp $\triangle IKL$.
  + $\Uparrow$ $H$ là giao điểm của các đường phân giác trong của $\triangle IKL$ ($KH$ và $IH$).
  + $\Uparrow$ Cần chứng minh $KH$ là tia phân giác của $\widehat{LKI} \iff \widehat{LKH} = \widehat{IKH}$.
  + $\Uparrow$ Dùng góc phụ với $90^\circ$ của đường cao $BK \perp AC$:
    * $\widehat{LKH} = 90^\circ - \widehat{AKL}$
    * $\widehat{IKH} = 90^\circ - \widehat{IKC}$
    $\implies$ Cần chứng minh $\widehat{AKL} = \widehat{IKC}$.
  + $\Uparrow$ Chuyển góc qua 2 tứ giác nội tiếp đường kính chứa trực tâm $H$:
    * $\widehat{AKL} = \widehat{AHL}$ (do tứ giác $AKHL$ nội tiếp đường tròn đường kính $AH$).
    * $\widehat{IKC} = \widehat{IHC}$ (do tứ giác $CIHK$ nội tiếp đường tròn đường kính $CH$).
  + $\Uparrow$ Cần chứng minh $\widehat{AHL} = \widehat{IHC}$.
  + $\Uparrow$ **Giả thiết gốc:** Hai góc $\widehat{AHL}$ và $\widehat{IHC}$ là hai góc đối đỉnh (vì ba điểm $A, H, I$ thẳng hàng và $C, H, L$ thẳng hàng theo định nghĩa trực tâm)!

### 3. Thiết lập Sơ đồ Công thức hình Cây thông (Pine-Tree Formula Tree)
- Thiết kế cây logic thuần túy công thức toán học:
  - **Đỉnh ngọn:** $\boxed{\mathbf{H \text{ LÀ TÂM NỘI TIẾP TAM GIÁC TRỰC TÂM } IKL}}$
  - Thân cây:
    * $\Uparrow \quad KH \text{ và } IH \text{ là hai đường phân giác trong của } \triangle IKL$
    * $\Uparrow \quad \widehat{LKH} = \widehat{IKH} \iff 90^\circ - \widehat{AKL} = 90^\circ - \widehat{IKC}$
    * $\Uparrow \quad \widehat{AKL} = \widehat{IKC}$
    * $\Uparrow \quad \widehat{AHL} = \widehat{IHC}$
  - Hai nhánh gốc rễ:
    * Nhánh trái: Tứ giác $AKHL$ nội tiếp $(\text{đường kính } AH) \implies \widehat{AKL} = \widehat{AHL}$
    * Nhánh phải: Tứ giác $CIHK$ nội tiếp $(\text{đường kính } CH) \implies \widehat{IKC} = \widehat{IHC}$
  - Bệ đỡ khởi phát: $A, H, I \text{ thẳng hàng và } C, H, L \text{ thẳng hàng} \implies \widehat{AHL} = \widehat{IHC} \text{ (Hai góc đối đỉnh)}$.

### 4. Bình luận sư phạm & Kỹ thuật tư duy
- Phân tích: **"Tại sao các đường cao của tam giác ban đầu lại trở thành các đường phân giác của tam giác trực tâm?"**
  + Bản chất đối xứng quang học (Định lý Fagnano): Ánh sáng phản xạ trên ba cạnh tam giác sẽ đi theo chu vi của tam giác trực tâm $IKL$ vì góc tới bằng góc phản xạ ($\widehat{AKL} = \widehat{IKC}$).
  + Nhận thức sâu sắc về sự chuyển hóa vai trò: Đường cao $\longrightarrow$ Đường phân giác.
- Chuỗi 4 câu hỏi dẫn dắt của Giáo viên trên lớp.

### 5. Lời giải chuẩn mực & Barem điểm chi tiết
- Trình bày lời giải xuôi 3 câu a, b, c.
- Barem điểm chia nhỏ đến từng $0{,}25$đ.

---

## 📤 III. ĐỊNH DẠNG ĐẦU RA MONG MUỐN (JSON CHUẨN)

Trả về kết quả dưới định dạng JSON hợp lệ:
```json
{
  "bai_toan": {
    "ma_bai": "BAI_HINH_04",
    "nguon": "Đề 04 - Tuyển tập 55 Đề Thi Vào Lớp 10",
    "mo_hinh": "Tam giác trực tâm IKL và trực tâm H là tâm đường tròn nội tiếp",
    "de_bai": "Cho tam giác ABC có ba góc nhọn..."
  },
  "so_do_tu_duy_nguoc": [
    ...
  ],
  "cay_thong_cong_thuc": {
    ...
  },
  "binh_luan_su_pham": {
    ...
  },
  "loi_giai_chi_tiet": [
    ...
  ]
}
```
