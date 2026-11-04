# PROMPT CHUYÊN SÂU PHÂN TÍCH SUY LUẬN TOÁN 9+ - BÀI HÌNH 03
> **Nguồn trích xuất:** Đề số 03 - Tuyển tập 55 Đề Thi Tuyển Sinh Vào Lớp 10  
> **Mô hình toán học:** Mô hình Đường tròn đường kính cạnh đối diện kết hợp Trực tâm tam giác & Bổ đề tiếp tuyến từ trung điểm đường cao (Tiếp tuyến $IE$ của $(O)$)

---

## 📌 I. NGUYÊN VĂN ĐỀ BÀI TOÁN HÌNH HỌC

```latex
Cho tam giác ABC có ba góc nhọn (AB < AC). Vẽ đường tròn (O) đường kính BC. Đường tròn (O) cắt các cạnh AB, AC lần lượt tại D và E (D khác B, E khác C). Gọi H là giao điểm của BE và CD.
a) Chứng minh bốn điểm A, D, H, E cùng nằm trên một đường tròn. Xác định vị trí tâm I của đường tròn đó.
b) Chứng minh AE . AC = AB . AD và tam giác ADE đồng dạng với tam giác ACB.
c) (Phân hóa 9+): Gọi I là trung điểm của AH. Chứng minh IE là tiếp tuyến của đường tròn (O) đường kính BC.
```

---

## 🎯 II. NHIỆM VỤ YÊU CẦU DÀNH CHO AI (CLAUDE / OPENAI)

Bạn là chuyên gia hàng đầu về bồi dưỡng học sinh giỏi Toán 9 và luyện thi vào lớp 10 chuyên Toán.  
Hãy phân tích sâu và giải mã bài toán hình học này theo các tiêu chuẩn cao cấp sau:

### 1. Phân tích mô hình toán học cốt lõi
- Nhận diện 2 "bổ đề vàng" trong mô hình trực tâm nội tiếp đường tròn đường kính $BC$:
  + **Bổ đề 1 (Trực tâm tam giác):** Góc nội tiếp chắn nửa đường tròn $\widehat{BDC} = \widehat{BEC} = 90^\circ \implies CD \perp AB$ và $BE \perp AC$. Do đó $H$ chính là trực tâm của $\triangle ABC$, dẫn tới $AH \perp BC$.
  + **Bổ đề 2 (Tiếp tuyến từ trung điểm cạnh huyền / trục đẳng phương):** Trong tam giác vuông $AEH$ vuông tại $E$, trung tuyến ứng với cạnh huyền $IE = \frac{1}{2}AH \implies \triangle IEH$ cân tại $I$. Tương tự $\triangle OEC$ cân tại $O$. Sự kết hợp của hai tam giác cân này qua hai góc đối đỉnh $\widehat{IHE} = \widehat{BHD}$ tạo nên tổng hai góc bằng $90^\circ$, chứng minh $IE \perp OE$.
- Điểm nghẽn ở câu phân hóa c: Học sinh thường lúng túng khi muốn chứng minh tiếp tuyến mà chưa nhận ra kỹ thuật "phân rã góc bẹt/phân rã góc $\widehat{IEO}$ thành tổng hai góc cân".

### 2. Thiết lập Sơ đồ Tư duy ngược (Reverse Thinking Mindmap)
- Lập chuỗi truy ngược từ **[ĐÍCH ĐẾN CẦN CHỨNG MINH: IE LÀ TIẾP TUYẾN CỦA (O)]** ngược về **[GIẢ THIẾT GỐC]**:
  + **Đích đến:** $IE$ là tiếp tuyến của đường tròn $(O)$ tại điểm $E \in (O)$.
  + $\Uparrow$ Cần chứng minh bán kính vuông góc tiếp tuyến: $IE \perp OE \iff \widehat{IEO} = 90^\circ$.
  + $\Uparrow$ Phân tích góc $\widehat{IEO}$ thành hai góc kề nhau: $\widehat{IEO} = \widehat{IEH} + \widehat{HEO} = 90^\circ$.
  + $\Uparrow$ Chuyển đổi hai góc thành các góc tương đương nhờ tính chất tam giác cân:
    * $\widehat{IEH} = \widehat{IHE}$ (do $\triangle IEH$ cân tại $I$ vì $IE = IH = \frac{1}{2}AH$).
    * $\widehat{HEO} = \widehat{OCE}$ (do $\triangle OEC$ cân tại $O$ vì $OE = OC = R$).
  + $\Uparrow$ Cần chứng minh tổng hai góc đáy bằng $90^\circ$: $\widehat{IHE} + \widehat{OCE} = 90^\circ$.
  + $\Uparrow$ Đổi góc đỉnh $H$: $\widehat{IHE} = \widehat{BHD}$ (hai góc đối đỉnh) $\implies$ Cần $\widehat{BHD} + \widehat{HCD} = 90^\circ$.
  + $\Uparrow$ Quan sát tam giác vuông $\triangle BDH$: Tam giác $BDH$ vuông tại $D \implies \widehat{BHD} + \widehat{HBD} = 90^\circ$.
  + $\Uparrow$ Cần $\widehat{HBD} = \widehat{HCD}$ (hoặc nhận thấy ngay $\widehat{BDC} = 90^\circ \implies \triangle BDH$ vuông tại $D \implies \widehat{BHD} + \widehat{HBD} = 90^\circ$, mà $\widehat{HBD} = 90^\circ - \widehat{C}$ và $\widehat{HCD} = 90^\circ - \widehat{B}$, tổng hai góc phụ nhau lập tức thỏa mãn).
  + $\Uparrow$ **Giả thiết gốc:** Góc $\widehat{BDC} = 90^\circ$ và $\widehat{BEC} = 90^\circ$ là hai góc nội tiếp chắn nửa đường tròn $(O)$ đường kính $BC$!

### 3. Thiết lập Sơ đồ Công thức hình Cây thông (Pine-Tree Formula Tree)
- Thiết kế cây logic thuần túy công thức toán học (tối giản chữ nghĩa):
  - **Đỉnh ngọn:** $\boxed{\mathbf{IE \text{ LÀ TIẾP TUYẾN CỦA } (O) \text{ TẠI } E}}$
  - Thân cây:
    * $\Uparrow \quad IE \perp OE \iff \widehat{IEO} = 90^\circ$
    * $\Uparrow \quad \widehat{IEO} = \widehat{IEH} + \widehat{HEO} = 90^\circ$
    * $\Uparrow \quad \widehat{IHE} + \widehat{OCE} = 90^\circ$
    * $\Uparrow \quad \widehat{BHD} + \widehat{HCD} = 90^\circ$
  - Hai nhánh gốc rễ:
    * Nhánh trái (Tính chất tâm $I$): $I \text{ là trung điểm } AH \implies IE = IH = \frac{AH}{2} \implies \triangle IEH \text{ cân tại } I \implies \widehat{IEH} = \widehat{IHE} = \widehat{BHD}$.
    * Nhánh phải (Tính chất tâm $O$): $O \text{ là trung điểm } BC \implies OE = OC = R \implies \triangle OEC \text{ cân tại } O \implies \widehat{HEO} = \widehat{OCE} = \widehat{HCD}$.
  - Bệ đỡ khởi phát: $\triangle BDH \text{ vuông tại } D \ (\widehat{BDC} = 90^\circ \text{ do góc nội tiếp chắn nửa đường tròn } (O))$.

### 4. Bình luận sư phạm & Kỹ thuật tư duy tiếp tuyến
- Phân tích: **"Tại sao lại nghĩ đến việc cộng hai góc $\widehat{IEH}$ và $\widehat{HEO}$?"**
  + Điểm $E$ là giao điểm chung của hai đường tròn $(I)$ và $(O)$. Bán kính của $(O)$ là $OE$, đường nối tâm là $OI$, đoạn thẳng cần chứng minh tiếp tuyến là $IE$.
  + Đoạn $EH$ là "dây cung chung / đường nối các tam giác vuông". Nhờ có $EH$, góc bẹt tại $E$ được chẻ đôi tự nhiên thành hai góc thuộc về hai tam giác cân riêng biệt có đỉnh là tâm $I$ và tâm $O$!
- Chuỗi 4 câu hỏi dẫn dắt của Giáo viên trên lớp để học sinh tự mở khóa bài toán.

### 5. Lời giải chuẩn mực & Barem điểm chi tiết
- Trình bày lời giải xuôi câu a, b, c.
- Barem điểm chia nhỏ đến từng $0{,}25$đ.

---

## 📤 III. ĐỊNH DẠNG ĐẦU RA MONG MUỐN (JSON CHUẨN)

Trả về kết quả dưới định dạng JSON hợp lệ:
```json
{
  "bai_toan": {
    "ma_bai": "BAI_HINH_03",
    "nguon": "Đề 03 - Tuyển tập 55 Đề Thi Vào Lớp 10",
    "mo_hinh": "Đường tròn đường kính BC, trực tâm tam giác nhọn và tiếp tuyến từ trung điểm AH",
    "de_bai": "Cho tam giác ABC có ba góc nhọn (AB < AC). Vẽ đường tròn (O) đường kính BC..."
  },
  "so_do_tu_duy_nguoc": [
    {
      "tang": 1,
      "tieu_de": "TẦNG 1: XÁC ĐỊNH ĐÍCH ĐẾN",
      "muc_tieu": "Chứng minh IE là tiếp tuyến của (O) tại E",
      "cong_thuc": "IE \\perp OE \\iff \\widehat{IEO} = 90^\\circ \\quad (E \\in (O))",
      "cau_hoi_truy_van": "Để chứng minh một đường thẳng là tiếp tuyến của (O) tại điểm E đã thuộc (O), ta cần chứng minh điều gì?",
      "phan_tich_logic": "Điểm E đã nằm trên đường tròn (O). Do đó, theo định nghĩa và dấu hiệu nhận biết tiếp tuyến, ta chỉ cần chứng minh IE vuông góc với bán kính OE tại E, tức là chứng minh góc IEO = 90 độ.",
      "huong_suy_luan_nguoc": "Làm thế nào để tính hoặc chứng minh góc IEO = 90 độ khi góc này nằm lơ lửng giữa tam giác?"
    }
  ],
  "cay_thong_cong_thuc": {
    "dinh_ngon": "\\boxed{\\mathbf{IE \\text{ LÀ TIẾP TUYẾN CỦA } (O) \\text{ TẠI } E}}",
    "than_cay": [
      "\\Updownarrow",
      "IE \\perp OE \\iff \\widehat{IEO} = 90^\\circ \\quad (E \\in (O))",
      "\\Uparrow",
      "\\widehat{IEO} = \\widehat{IEH} + \\widehat{HEO} = 90^\\circ",
      "\\Uparrow",
      "\\widehat{IHE} + \\widehat{OCE} = 90^\\circ \\iff \\widehat{BHD} + \\widehat{HCD} = 90^\\circ",
      "\\Uparrow",
      "\\triangle BDH \\text{ vuông tại } D \\implies \\widehat{BHD} + \\widehat{HBD} = 90^\\circ"
    ],
    "hai_nhanh": {
      "nhanh_trai": "\\triangle IEH \\text{ cân tại } I \\ (IE=IH=\\frac{AH}{2}) \\implies \\widehat{IEH} = \\widehat{IHE} = \\widehat{BHD}",
      "nhanh_phai": "\\triangle OEC \\text{ cân tại } O \\ (OE=OC=R) \\implies \\widehat{HEO} = \\widehat{OCE} = \\widehat{HCD}"
    },
    "goc_re": "\\widehat{BDC} = \\widehat{BEC} = 90^\\circ \\quad (\\text{Góc nội tiếp chắn nửa đường tròn } (O) \\text{ đường kính } BC)"
  },
  "binh_luan_su_pham": {
    "tai_sao_nghi_ra": "Phân tích vì sao lại chẻ góc IEO thành tổng hai góc IEH và HEO...",
    "cau_hoi_goi_mo": [
      "Câu 1: Điểm E đã thuộc đường tròn (O) chưa? Vậy muốn chứng minh IE là tiếp tuyến cần chỉ ra điều gì?",
      "Câu 2: Đoạn thẳng EH chia góc IEO thành hai góc nào?",
      "Câu 3: Tam giác AEH vuông tại E có I là trung điểm cạnh huyền AH, vậy tam giác IEH có tính chất gì đặc biệt?",
      "Câu 4: Bán kính OE và OC có mối quan hệ gì? Tổng hai góc đáy của hai tam giác cân đó liên hệ như thế nào với tam giác vuông BDH?"
    ],
    "sai_lam_thuong_gap": "Học sinh thường quên không chỉ ra điểm E thuộc (O) trước khi kết luận tiếp tuyến, hoặc nhầm lẫn khi chuyển góc đối đỉnh.",
    "bai_tap_tuong_tu": [
      "Bài 1: Chứng minh ID cũng là tiếp tuyến của đường tròn (O) và IO vuông góc với DE.",
      "Bài 2: Cho tứ giác BCDE nội tiếp (O). Kẻ tiếp tuyến tại D và E cắt nhau tại I. Chứng minh I, H, A thẳng hàng."
    ]
  },
  "loi_giai_chi_tiet": [
    {
      "buoc": "Bước 1: Chứng minh bốn điểm A, D, H, E cùng thuộc đường tròn (I) đường kính AH",
      "noi_dung": "Do D, E thuộc (O) đường kính BC nên BDC = BEC = 90 độ...",
      "diem": "0.75đ"
    },
    {
      "buoc": "Bước 2: Chứng minh AE . AC = AB . AD và tam giác ADE đồng dạng tam giác ACB",
      "noi_dung": "Xét tam giác vuông AEB và ADC có góc A chung...",
      "diem": "0.75đ"
    },
    {
      "buoc": "Bước 3: Thiết lập hai tam giác cân từ trung điểm I và tâm O",
      "noi_dung": "Trong tam giác vuông AEH vuông tại E, trung tuyến EI = AH/2 = IH nên tam giác IEH cân tại I...",
      "diem": "0.5đ"
    },
    {
      "buoc": "Bước 4: Chứng minh IE vuông góc OE và kết luận tiếp tuyến",
      "noi_dung": "IEO = IEH + HEO = BHD + HCD = 90 độ do tam giác BDH vuông tại D...",
      "diem": "0.5đ"
    }
  ]
}
```
