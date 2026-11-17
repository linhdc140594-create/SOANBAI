# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 11 (TOÁN 7)
## CHIẾN DỊCH 2_CHK_1: BÀI 14 - CÁC TRƯỜNG HỢP BẰNG NHAU THỨ HAI VÀ THỨ BA CỦA TAM GIÁC (C-G-C, G-C-G) & CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC VUÔNG
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)
### Bám sát chương trình: SGK Toán 7 - Kết nối tri thức với cuộc sống (Chương IV)

---

## 🎯 I. MỤC TIÊU HỌC TẬP & NGUYÊN TẮC SƯ PHẠM (TUẦN 11)

Tuần 11 tiếp tục đào sâu và mở rộng mạch kiến thức Hình học phẳng (Chương IV: Tam giác bằng nhau), trọng tâm là làm chủ trọn vẹn **Bài 14: Trường hợp bằng nhau thứ hai và thứ ba của tam giác (C-G-C, G-C-G)** cùng hệ quả áp dụng cho **Tam giác vuông**:

### 1. Mục tiêu trọng tâm từng buổi:
* **Buổi 01 - Trường hợp bằng nhau Cạnh - Góc - Cạnh (C-G-C) & Tam giác vuông (c.g.v - c.g.v):**
  - Nhận biết góc xen giữa hai cạnh của một tam giác.
  - Nắm vững định lí trường hợp C-G-C: Nếu hai cạnh và góc xen giữa của tam giác này bằng hai cạnh và góc xen giữa của tam giác kia thì hai tam giác đó bằng nhau.
  - Vận dụng trường hợp bằng nhau đặc biệt của tam giác vuông: Hai cạnh góc vuông (c.g.v - c.g.v).
  - Trình bày lập luận chứng minh hai tam giác bằng nhau (c.g.c) $\implies$ suy ra hai cạnh tương ứng bằng nhau, hai góc tương ứng bằng nhau, chứng minh tia phân giác, hai đường thẳng vuông góc hoặc song song.
  - Vận dụng bài toán thực tế: Đo khoảng cách giữa hai vị trí bị ngăn cách bởi vật cản (ao, hồ, toà nhà).
  - Củng cố Đại số: Phép tính số hữu tỉ (nhóm phân số, lũy thừa, căn bậc hai số học), giải phương trình tìm $x$ (lũy thừa chẵn, giá trị tuyệt đối).
  - Vận dụng cao: Cực trị biểu thức chứa dấu giá trị tuyệt đối dạng $A = |x - a| + |x - b|$ áp dụng BĐT $|A| + |B| \ge |A + B|$.

* **Buổi 02 - Trường hợp bằng nhau Góc - Cạnh - Góc (G-C-G) & Các trường hợp bằng nhau của Tam giác vuông:**
  - Nhận biết cạnh kề hai góc (cạnh nằm giữa hai góc).
  - Nắm vững định lí trường hợp G-C-G: Nếu một cạnh và hai góc kề của tam giác này bằng một cạnh và hai góc kề của tam giác kia thì hai tam giác đó bằng nhau.
  - Vận dụng các trường hợp bằng nhau của tam giác vuông suy ra từ G-C-G:
    + Cạnh góc vuông và góc nhọn kề (c.g.v - g.nhọn).
    + Cạnh huyền và góc nhọn (c.huyền - g.nhọn).
  - Vận dụng bài toán thực tế: Phương pháp đo khoảng cách từ bờ tới một con tàu trên biển hoặc khoảng cách qua sông (phương pháp Thales).
  - Củng cố Đại số: Biểu thức số hữu tỉ phức hợp, phương trình tìm $x$ chứa giá trị tuyệt đối.
  - Vận dụng cao: Tìm giá trị lớn nhất của phân thức có mẫu chứa giá trị tuyệt đối dạng $B = \dfrac{k}{|x - a| + b}$ ($k, b > 0$).

---

## 📐 II. QUY CHUẨN MA TRẬN ĐỀ THI (10 ĐIỂM / 45 PHÚT / 1 TỜ A4 IN 2 MẶT)

* **Hình thức xuất bản:** Phiếu kiểm tra in 2 mặt giấy A4, gồm **4 mã đề hoán vị tương đương ($101, 102, 103, 104$)**, biên dịch chính xác **8 trang PDF** (mỗi mã đề trọn vẹn 2 trang).
* **Phân phối điểm số chuẩn Layout Gold Standard (Lớp 7):**
  * **Câu 1 đến Câu 10 (2,5 điểm - Mặt trước - Trang 1):** 10 câu trả lời ngắn dùng lệnh `\shortans`, mỗi câu $0{,}25$ điểm. Ô vuông bo góc `KQ: [   ]` cố định sát mép phải.
  * **Câu 11 (3,0 điểm - Mặt trước - Trang 1):** Thực hiện phép tính gồm **6 ý ($a, b, c, d, e, f$)**, mỗi ý $0{,}5$ điểm (bố trí bảng $3 \times 2$, dùng `\oBaiTap[5]` lấp kín 100% sát mép đáy Trang 1).
  * **Câu 12 (2,0 điểm - Mặt sau - Trang 2):** Tìm số hữu tỉ $x$ gồm **4 ý ($a, b, c, d$)**, mỗi ý $0{,}5$ điểm (bố trí bảng $2 \times 2$, dùng `\oBaiTap[5]`).
  * **Câu 13 (2,0 điểm - Mặt sau - Trang 2):** Bài toán hình học phẳng (2 ý $a, b$, mỗi ý $1{,}0$ điểm). Ghép đề bài + hình vẽ TikZ trực tiếp vào khung box `tabularx`, khu vực bài giải chia 2 cột `\dongkeHaiCot{11}` có vách phân cách mờ ở giữa.
  * **Câu 14 (0,5 điểm - Mặt sau - Trang 2):** Bài toán vận dụng cao phân loại điểm 10. Ghép đề bài vào khung box `tabularx`, bài giải `\dongkeHaiCot{7}` chạm sát đáy mép dưới Trang 2.

---

## 🗺️ III. MA TRẬN CHI TIẾT TỪNG BUỔI HỌC

### 📌 BUỔI 01: TRƯỜNG HỢP CẠNH - GÓC - CẠNH (C-G-C) & TAM GIÁC VUÔNG (C.G.V - C.G.V)
* **Kế hoạch chi tiết:** [buoi_1/KE_HOACH_TUAN_11_BUOI_01.md](buoi_1/KE_HOACH_TUAN_11_BUOI_01.md)
* **Câu 1 $\to$ 10 (2,5 đ):** Nhận diện góc xen giữa hai cạnh; Điều kiện bổ sung c-g-c; Tìm góc tương ứng trong tam giác bằng nhau; Tính chu vi tam giác tương ứng; Căn bậc hai số học; Giá trị tuyệt đối; Trường hợp c.g.v - c.g.v của tam giác vuông; Bài toán thực tế đo khoảng cách qua ao hồ; Lũy thừa số hữu tỉ; Nhận biết tam giác bằng nhau từ hình vẽ đối xứng tâm.
* **Câu 11 (3,0 đ - Trang 1): Thực hiện phép tính (6 ý $a \to f$, mỗi ý $0{,}5$đ):**
  * $a)$ Cộng trừ nhóm phân số cùng mẫu.
  * $b)$ Tính nhanh bằng phân phối phép nhân đối với phép cộng/trừ.
  * $c)$ Lũy thừa số hữu tỉ kết hợp phép chia/nhân.
  * $d)$ Căn bậc hai số học phối hợp giá trị tuyệt đối.
  * $e)$ Thứ tự thực hiện phép tính có ngoặc tròn, ngoặc vuông $[ \dots ]$.
  * $f)$ Rút gọn biểu thức lũy thừa đưa về cùng cơ số nguyên tố.
* **Câu 12 (2,0 đ - Trang 2): Tìm số hữu tỉ $x$ (4 ý $a \to d$, mỗi ý $0{,}5$đ):**
  * $a)$ Phương trình chuyển vế đổi dấu cơ bản.
  * $b)$ Phương trình bậc nhất chứa nhân chia và phân số.
  * $c)$ Phương trình lũy thừa bậc hai $\left(x \pm \dfrac{a}{b}\right)^2 = \dfrac{c^2}{d^2}$ (2 nghiệm).
  * $d)$ Phương trình chứa giá trị tuyệt đối $|ax \pm b| = c$ (2 nghiệm).
* **Câu 13 (2,0 đ - Trang 2): Bài toán Hình học chứng minh C-G-C (Chia 2 cột `\dongkeHaiCot{11}`):**
  * Bối cảnh: Cho góc nhọn $\widehat{xOy}$. Trên tia $Ox$ lấy điểm $A$, trên tia $Oy$ lấy điểm $B$ sao cho $OA = OB$. Lấy điểm $M$ thuộc tia phân giác $Ot$ của góc $\widehat{xOy}$ ($M \neq O$).
  * $a)$ (1,0 đ): Chứng minh $\Delta OAM = \Delta OBM$ (c.g.c).
  * $b)$ (1,0 đ): Chứng minh $MA = MB$ và đường thẳng $OM$ vuông góc với đoạn thẳng $AB$.
* **Câu 14 (0,5 đ - Trang 2): Vận dụng cao điểm 10 (Chia 2 cột `\dongkeHaiCot{7}`):**
  * Tìm giá trị nhỏ nhất của biểu thức chứa giá trị tuyệt đối: $A = |x - a| + |x - b|$ ($a < b$).

---

### 📌 BUỔI 02: TRƯỜNG HỢP GÓC - CẠNH - GÓC (G-C-G) & CÁC TRƯỜNG HỢP CỦA TAM GIÁC VUÔNG
* **Kế hoạch chi tiết:** [buoi_2/KE_HOACH_TUAN_11_BUOI_02.md](buoi_2/KE_HOACH_TUAN_11_BUOI_02.md)
* **Câu 1 $\to$ 10 (2,5 đ):** Nhận diện cạnh kề hai góc; Điều kiện bổ sung g-c-g; Trường hợp cạnh huyền - góc nhọn; Trường hợp c.g.v - góc nhọn kề; Tính số đo góc thứ ba trong tam giác bằng nhau; Tính độ dài cạnh tương ứng; Căn bậc hai số học và lũy thừa; Phân số và số thập phân; Bài toán thực tế đo khoảng cách từ bờ ra tàu trên biển (phương pháp Thales); Khẳng định đúng sai về tam giác vuông.
* **Câu 11 (3,0 đ - Trang 1): Thực hiện phép tính (6 ý $a \to f$, mỗi ý $0{,}5$đ):**
  * Phép tính số hữu tỉ kết hợp phân số, số thập phân, lũy thừa, căn bậc hai số học và thứ tự ngoặc lồng nhau.
* **Câu 12 (2,0 đ - Trang 2): Tìm số hữu tỉ $x$ (4 ý $a \to d$, mỗi ý $0{,}5$đ):**
  * 4 dạng toán tìm $x$ chuẩn mực: chuyển vế, nhân chia, lũy thừa bậc hai, giá trị tuyệt đối dạng $a|x - b| + c = d$.
* **Câu 13 (2,0 đ - Trang 2): Bài toán Hình học chứng minh Tam giác vuông bằng nhau (Chia 2 cột `\dongkeHaiCot{11}`):**
  * Bối cảnh: Cho đoạn thẳng $AB$ và trung điểm $I$ của $AB$. Qua $I$ kẻ đường thẳng $xy$ (không vuông góc với $AB$). Kẻ $AH \perp xy$ tại $H$ và $BK \perp xy$ tại $K$.
  * $a)$ (1,0 đ): Chứng minh $\Delta AHI = \Delta BKI$ (cạnh huyền - góc nhọn).
  * $b)$ (1,0 đ): Chứng minh $AH = BK$ và $AH \parallel BK$.
* **Câu 14 (0,5 đ - Trang 2): Vận dụng cao điểm 10 (Chia 2 cột `\dongkeHaiCot{7}`):**
  * Tìm giá trị lớn nhất của phân thức có mẫu chứa giá trị tuyệt đối: $B = \dfrac{k}{|x - a| + b}$ ($k, b > 0$).

---

## 📐 IV. BẢNG THAM CHIẾU QUY CHUẨN KỸ THUẬT IN ẤN (LAYOUT GOLD STANDARD)

| Vị trí | Quy cách kỹ thuật tối ưu mới | Tác dụng thẩm mỹ & Sư phạm |
| :--- | :--- | :--- |
| **Header Trang 1** | Bảng 1 dòng duy nhất: `PHIẾU KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 11 - BUỔI <Y>` \| `Mã đề: <MÃ> - Trang 1/2` | Tiết kiệm diện tích, bỏ hoàn toàn khung họ tên rườm rà. |
| **Khung Điểm số** | Bảng Điểm & Nhận xét cao cố định `\rule{0pt}{1.8cm}` | Rộng rãi, trang trọng, thuận tiện ghi lời phê. |
| **10 Câu ngắn** | Dùng lệnh `\shortans{...}` với cấu hình `\SAOPTN{widthSA=2.6,heightSA=0.62}` | Bỏ bảng trắc nghiệm A, B, C, D; sinh ô `KQ: [   ]` bo góc tinh tế mép phải. |
| **Câu 11 (Trang 1)** | Bảng $3 \times 2$ gồm **6 ý ($a \to f$)** với **`\oBaiTap[5]`** (5 dòng kẻ mờ/ô) | Auto-fill lấp kín 100% sát đáy Trang 1 (3,0 điểm). |
| **Header Trang 2** | Khung rút gọn: `TOÁN 7 - TUẦN 11 - BUỔI <Y> \| Mã đề: <MÃ> - Trang 2/2` | Đồng bộ nhận diện đề thi mặt sau. |
| **Câu 12 (Trang 2)** | Bảng $2 \times 2$ gồm **4 ý ($a \to d$)** với **`\oBaiTap[5]`** | Trình bày 4 phương trình tìm $x$ rõ ràng, mạch lạc (2,0 điểm). |
| **Câu 13 (Trang 2)** | Ghép đề bài + hình TikZ vào box `tabularx`, bài giải **`\dongkeHaiCot{11}`** | Chia đôi cột làm bài, nhân đôi không gian trình bày hình học (2,0 điểm). |
| **Câu 14 (Trang 2)** | Ghép đề bài vào box `tabularx`, bài giải **`\dongkeHaiCot{7}`** | Chạm sát mép lề dưới Trang 2, tuyệt đối không tràn (0,5 điểm). |

