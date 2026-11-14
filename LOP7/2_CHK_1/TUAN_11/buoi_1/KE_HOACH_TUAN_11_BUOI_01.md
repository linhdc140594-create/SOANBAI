# KẾ HOẠCH BÀI KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 11 - BUỔI 01
## BÀI 14: TRƯỜNG HỢP BẰNG NHAU THỨ HAI CỦA TAM GIÁC: CẠNH - GÓC - CẠNH (C-G-C) & TAM GIÁC VUÔNG (C.G.V - C.G.V)
### Bám sát chương trình: SGK Toán 7 - Kết nối tri thức với cuộc sống (Chương IV)

---

## 🎯 I. MỤC TIÊU CẦN ĐẠT

1. **Kiến thức:**
   - Nhận biết góc xen giữa hai cạnh của một tam giác.
   - Nắm vững và phát biểu chính xác định lí trường hợp bằng nhau thứ hai của tam giác (Cạnh - Góc - Cạnh).
   - Hiểu và vận dụng trường hợp bằng nhau đặc biệt của tam giác vuông: hai cạnh góc vuông (c.g.v - c.g.v).
   - Vận dụng chứng minh hai tam giác bằng nhau theo c-g-c để suy ra: hai đoạn thẳng bằng nhau, hai góc bằng nhau, chứng minh tia phân giác, hai đường thẳng vuông góc.
2. **Kỹ năng & Năng lực:**
   - Trình bày lời giải hình học mạch lạc, lập luận chặt chẽ: đủ 3 yếu tố (cạnh - góc xen giữa - cạnh).
   - Vẽ hình chính xác theo đề bài bằng thước và compa.
   - Kỹ năng tính toán số hữu tỉ: quy đồng, phối hợp lũy thừa, căn bậc hai số học, quy tắc dấu ngoặc.
   - Năng lực giải quyết vấn đề toán học: tư duy cực trị chứa dấu giá trị tuyệt đối.

---

## 📐 II. MA TRẬN ĐỀ THI 10 ĐIỂM (45 PHÚT - 2 MẶT A4)

| STT | Dạng bài | Số câu / Ý | Điểm số | Vị trí trên phiếu | Quy chuẩn định dạng |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | Trả lời ngắn (Short Answer) | 10 câu | 2,5 đ | Trang 1 (Đầu trang) | Lệnh `\shortans`, ô bo góc `KQ: [   ]` sát mép phải. |
| **2** | Thực hiện phép tính | 6 ý ($a \to f$) | 3,0 đ | Trang 1 (Cuối trang) | Bảng $3 \times 2$, dùng `\oBaiTap[5]` lấp kín 100% lề dưới. |
| **3** | Tìm số hữu tỉ $x$ | 4 ý ($a \to d$) | 2,0 đ | Trang 2 (Đầu trang) | Bảng $2 \times 2$, dùng `\oBaiTap[5]`. |
| **4** | Hình học C-G-C | 2 ý ($a, b$) | 2,0 đ | Trang 2 (Giữa trang) | Ghép box `tabularx` có hình TikZ, bài giải `\dongkeHaiCot{11}`. |
| **5** | Vận dụng cao điểm 10 | 1 bài | 0,5 đ | Trang 2 (Cuối trang) | Ghép box `tabularx`, bài giải `\dongkeHaiCot{7}` sát lề dưới. |
| **TỔNG** | | **23 mục** | **10,0 đ** | **2 mặt A4** | **Chính xác 8 trang PDF cho 4 mã đề (101-104)** |

---

## 📊 III. CHI TIẾT DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Chủ đề / Dạng toán | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Xác định góc xen giữa hai cạnh | $\Delta ABC$: góc xen giữa $AB, BC$ $\to \widehat{B}$ | $\Delta MNP$: góc xen giữa $MN, MP$ $\to \widehat{M}$ | $\Delta DEF$: góc xen giữa $DE, EF$ $\to \widehat{E}$ | $\Delta HIK$: góc xen giữa $HK, IK$ $\to \widehat{K}$ |
| **2** | Điều kiện bổ sung c.g.c | $AB=DE, AC=DF$ $\implies \widehat{A} = \widehat{D}$ | $MN=QR, NP=RS$ $\implies \widehat{N} = \widehat{R}$ | $BC=NP, AC=MP$ $\implies \widehat{C} = \widehat{P}$ | $DE=HK, EF=KM$ $\implies \widehat{E} = \widehat{K}$ |
| **3** | Tính góc tương ứng từ $\Delta = \Delta$ | $\widehat{A}=55^\circ, \widehat{B}=65^\circ \to \widehat{P} = 60^\circ$ | $\widehat{M}=50^\circ, \widehat{N}=70^\circ \to \widehat{C} = 60^\circ$ | $\widehat{D}=45^\circ, \widehat{E}=75^\circ \to \widehat{K} = 60^\circ$ | $\widehat{D}=60^\circ, \widehat{E}=50^\circ \to \widehat{C} = 70^\circ$ |
| **4** | Tính cạnh tương ứng qua chu vi | $AB=5, AC=6, C=18 \to BC = 7\text{ cm}$ | $MN=4, NP=7, C=17 \to AC = 6\text{ cm}$ | $DE=6, DF=8, C=24 \to EF = 10\text{ cm}$ | $HI=5, IK=8, C=20 \to AC = 7\text{ cm}$ |
| **5** | Căn bậc hai số học | $\sqrt{144} - \sqrt{49} = 5$ | $\sqrt{169} - \sqrt{64} = 5$ | $\sqrt{196} - \sqrt{81} = 5$ | $\sqrt{225} - \sqrt{100} = 5$ |
| **6** | Giá trị tuyệt đối ($x > 0$) | $|x - 1/2| = 3/2 \to x = 2$ | $|x - 3/2| = 5/2 \to x = 4$ | $|x - 1/3| = 5/3 \to x = 2$ | $|x - 2/3| = 7/3 \to x = 3$ |
| **7** | Tam giác vuông: c.g.v - c.g.v | $\Delta ABC, \Delta A'B'$ vuông, $AB=A'B' \to AC=A'C'$ | $\Delta MNP, \Delta DEF$ vuông, $MN=DE \to MP=DF$ | $\Delta ABC, \Delta MNP$ vuông, $BA=NM \to BC=NP$ | $\Delta DEF, \Delta HIK$ vuông, $EF=IK \to ED=IH$ |
| **8** | Thực tế: đo khoảng cách ao hồ | $CD = 38\text{ m} \to AB = 38\text{ m}$ | $CD = 45\text{ m} \to AB = 45\text{ m}$ | $CD = 52\text{ m} \to AB = 52\text{ m}$ | $CD = 65\text{ m} \to AB = 65\text{ m}$ |
| **9** | Lũy thừa số hữu tỉ | $(-1/3)^2 \cdot 9 + (-1)^{2026} = 2$ | $(-1/4)^2 \cdot 16 + (-1)^{2024} = 2$ | $(-1/5)^2 \cdot 25 + (-1)^{2028} = 2$ | $(-1/2)^3 \cdot (-8) + (-1)^{2030} = 2$ |
| **10** | Đối xứng tâm $\Delta = \Delta$ | $AB \cap CD = \{O\} \to \Delta OAC = \Delta OBD$ | $MN \cap PQ = \{I\} \to \Delta IMP = \Delta INQ$ | $EF \cap GH = \{K\} \to \Delta KEG = \Delta KFH$ | $AB \cap CD = \{O\} \to \Delta OAD = \Delta OBC$ |

---

### 2. CÂU 11 (3,0 ĐIỂM - THỰC HIỆN PHÉP TÍNH - 6 Ý $A \to F$)

* **Mã đề 101:**
  - $a)$ $\dfrac{5}{13} + \dfrac{4}{7} + \dfrac{8}{13} - \dfrac{11}{7} = 0$
  - $b)$ $\dfrac{4}{7} \cdot \left(-\dfrac{2}{5}\right) + \dfrac{4}{7} \cdot \left(-\dfrac{3}{5}\right) + \dfrac{11}{7} = 1$
  - $c)$ $\left(-\dfrac{1}{2}\right)^3 : \dfrac{1}{4} + \left(\dfrac{3}{4}\right)^0 = \dfrac{1}{2}$
  - $d)$ $\sqrt{\dfrac{16}{25}} - \left|-\dfrac{2}{5}\right| + \sqrt{\dfrac{4}{25}} = \dfrac{4}{5}$
  - $e)$ $\dfrac{3}{4} - \left[ \dfrac{1}{2} + \left(\dfrac{3}{8} - \dfrac{5}{8}\right) \right] = \dfrac{1}{2}$
  - $f)$ $\dfrac{4^3 \cdot 9^2}{6^4} = 4$

* **Mã đề 102:**
  - $a)$ $\dfrac{3}{11} + \dfrac{5}{8} + \dfrac{8}{11} - \dfrac{13}{8} = 0$
  - $b)$ $\dfrac{5}{9} \cdot \left(-\dfrac{3}{7}\right) + \dfrac{5}{9} \cdot \left(-\dfrac{4}{7}\right) + \dfrac{14}{9} = 1$
  - $c)$ $\left(-\dfrac{1}{3}\right)^2 \cdot 18 - \left(\dfrac{5}{7}\right)^0 = 1$
  - $d)$ $\sqrt{\dfrac{25}{49}} - \left|-\dfrac{3}{7}\right| + \sqrt{\dfrac{9}{49}} = \dfrac{5}{7}$
  - $e)$ $\dfrac{5}{6} - \left[ \dfrac{2}{3} + \left(\dfrac{1}{4} - \dfrac{3}{4}\right) \right] = \dfrac{2}{3}$
  - $f)$ $\dfrac{8^2 \cdot 9^3}{6^5} = 6$

* **Mã đề 103:**
  - $a)$ $\dfrac{7}{15} + \dfrac{2}{9} + \dfrac{8}{15} - \dfrac{11}{9} = 0$
  - $b)$ $\dfrac{3}{8} \cdot \left(-\dfrac{1}{6}\right) + \dfrac{3}{8} \cdot \left(-\dfrac{5}{6}\right) + \dfrac{11}{8} = 1$
  - $c)$ $\left(-\dfrac{1}{2}\right)^4 : \dfrac{1}{8} + \left(\dfrac{2}{3}\right)^0 = \dfrac{3}{2}$
  - $d)$ $\sqrt{\dfrac{36}{81}} - \left|-\dfrac{1}{9}\right| + \sqrt{\dfrac{16}{81}} = 1$
  - $e)$ $\dfrac{4}{5} - \left[ \dfrac{1}{2} + \left(\dfrac{1}{10} - \dfrac{3}{10}\right) \right] = \dfrac{1}{2}$
  - $f)$ $\dfrac{27^2 \cdot 4^4}{6^6} = 4$

* **Mã đề 104:**
  - $a)$ $\dfrac{4}{17} + \dfrac{3}{5} + \dfrac{13}{17} - \dfrac{8}{5} = 0$
  - $b)$ $\dfrac{6}{11} \cdot \left(-\dfrac{2}{7}\right) + \dfrac{6}{11} \cdot \left(-\dfrac{5}{7}\right) + \dfrac{17}{11} = 1$
  - $c)$ $\left(-\dfrac{1}{4}\right)^2 \cdot 32 - \left(\dfrac{7}{9}\right)^0 = 1$
  - $d)$ $\sqrt{\dfrac{49}{64}} - \left|-\dfrac{3}{8}\right| + \sqrt{\dfrac{4}{64}} = \dfrac{3}{4}$
  - $e)$ $\dfrac{5}{6} - \left[ \dfrac{1}{2} + \left(\dfrac{1}{12} - \dfrac{5}{12}\right) \right] = \dfrac{2}{3}$
  - $f)$ $\dfrac{16^2 \cdot 25^2}{20^3} = 20$

---

### 3. CÂU 12 (2,0 ĐIỂM - TÌM SỐ HỮU TỈ $x$ - 4 Ý $A \to D$)

| Ý | Dạng phương trình | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **a** | Chuyển vế cơ bản | $x + \dfrac{2}{5} = \dfrac{7}{10} \to x = \dfrac{3}{10}$ | $x + \dfrac{3}{4} = \dfrac{7}{8} \to x = \dfrac{1}{8}$ | $x - \dfrac{1}{3} = \dfrac{5}{6} \to x = \dfrac{7}{6}$ | $x - \dfrac{2}{5} = \dfrac{3}{10} \to x = \dfrac{7}{10}$ |
| **b** | Nhân chia phân số | $\dfrac{2}{3}x - \dfrac{1}{2} = \dfrac{5}{6} \to x = 2$ | $\dfrac{3}{4}x - \dfrac{2}{3} = \dfrac{5}{6} \to x = 2$ | $\dfrac{3}{5}x + \dfrac{1}{2} = \dfrac{11}{10} \to x = 1$ | $\dfrac{4}{5}x + \dfrac{1}{3} = \dfrac{17}{15} \to x = 1$ |
| **c** | Lũy thừa bậc hai | $\left(x - \dfrac{1}{2}\right)^2 = \dfrac{9}{16} \to x \in \left\{\dfrac{5}{4}; -\dfrac{1}{4}\right\}$ | $\left(x - \dfrac{1}{3}\right)^2 = \dfrac{4}{9} \to x \in \left\{1; -\dfrac{1}{3}\right\}$ | $\left(x + \dfrac{1}{2}\right)^2 = \dfrac{25}{16} \to x \in \left\{\dfrac{3}{4}; -\dfrac{7}{4}\right\}$ | $\left(x + \dfrac{2}{3}\right)^2 = \dfrac{16}{9} \to x \in \left\{\dfrac{2}{3}; -2\right\}$ |
| **d** | Giá trị tuyệt đối | $\left\|2x - \dfrac{1}{3}\right\| = \dfrac{5}{3} \to x \in \left\{1; -\dfrac{2}{3}\right\}$ | $\left\|2x - \dfrac{1}{2}\right\| = \dfrac{3}{2} \to x \in \left\{1; -\dfrac{1}{2}\right\}$ | $\left\|3x - \dfrac{1}{2}\right\| = \dfrac{5}{2} \to x \in \left\{1; -\dfrac{2}{3}\right\}$ | $\left\|3x - \dfrac{1}{4}\right\| = \dfrac{7}{4} \to x \in \left\{\dfrac{2}{3}; -\dfrac{1}{2}\right\}$ |

---

### 4. CÂU 13 (2,0 ĐIỂM - HÌNH HỌC CHỨNG MINH C-G-C - 2 Ý $A, B$)

* **Mã đề 101:** Cho góc nhọn $\widehat{xOy}$. Trên tia $Ox$ lấy điểm $A$, trên tia $Oy$ lấy điểm $B$ sao cho $OA = OB$. Gọi $Ot$ là tia phân giác của góc $\widehat{xOy}$. Trên tia $Ot$ lấy điểm $M$ ($M \neq O$).
  - $a)$ (1,0 điểm): Chứng minh rằng $\Delta OAM = \Delta OBM$.
  - $b)$ (1,0 điểm): Gọi $H$ là giao điểm của $OM$ và $AB$. Chứng minh rằng $MA = MB$ và $OM \perp AB$.
* **Mã đề 102:** Cho góc nhọn $\widehat{mIn}$. Trên tia $Im$ lấy điểm $E$, trên tia $In$ lấy điểm $F$ sao cho $IE = IF$. Gọi $It$ là tia phân giác của góc $\widehat{mIn}$. Trên tia $It$ lấy điểm $K$ ($K \neq I$).
  - $a)$ (1,0 điểm): Chứng minh rằng $\Delta IEK = \Delta IFK$.
  - $b)$ (1,0 điểm): Gọi $H$ là giao điểm của $IK$ và $EF$. Chứng minh rằng $KE = KF$ và $IK \perp EF$.
* **Mã đề 103:** Cho góc nhọn $\widehat{xAy}$. Trên tia $Ax$ lấy điểm $B$, trên tia $Ay$ lấy điểm $C$ sao cho $AB = AC$. Gọi $At$ là tia phân giác của góc $\widehat{xAy}$. Trên tia $At$ lấy điểm $M$ ($M \neq A$).
  - $a)$ (1,0 điểm): Chứng minh rằng $\Delta ABM = \Delta ACM$.
  - $b)$ (1,0 điểm): Gọi $D$ là giao điểm của $AM$ và $BC$. Chứng minh rằng $MB = MC$ và $AM \perp BC$.
* **Mã đề 104:** Cho góc nhọn $\widehat{pSq}$. Trên tia $Sp$ lấy điểm $M$, trên tia $Sq$ lấy điểm $N$ sao cho $SM = SN$. Gọi $St$ là tia phân giác của góc $\widehat{pSq}$. Trên tia $St$ lấy điểm $P$ ($P \neq S$).
  - $a)$ (1,0 điểm): Chứng minh rằng $\Delta SMP = \Delta SNP$.
  - $b)$ (1,0 điểm): Gọi $K$ là giao điểm của $SP$ và $MN$. Chứng minh rằng $PM = PN$ và $SP \perp MN$.

---

### 5. CÂU 14 (0,5 ĐIỂM - VẬN DỤNG CAO ĐIỂM 10)

* **Mã đề 101:** Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 2| + |x - 7|$.
  - *Lời giải:* Ta có $A = |x - 2| + |7 - x| \ge |x - 2 + 7 - x| = |5| = 5$. Dấu "$=$" xảy ra $\iff (x - 2)(7 - x) \ge 0 \iff 2 \le x \le 7$. Vậy $\min A = 5$ khi $2 \le x \le 7$.
* **Mã đề 102:** Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 3| + |x - 8|$.
  - *Lời giải:* $A = |x - 3| + |8 - x| \ge |x - 3 + 8 - x| = 5$. Dấu "$=$" xảy ra khi $3 \le x \le 8$. Vậy $\min A = 5$ khi $3 \le x \le 8$.
* **Mã đề 103:** Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 1| + |x - 6|$.
  - *Lời giải:* $A = |x - 1| + |6 - x| \ge |x - 1 + 6 - x| = 5$. Dấu "$=$" xảy ra khi $1 \le x \le 6$. Vậy $\min A = 5$ khi $1 \le x \le 6$.
* **Mã đề 104:** Tìm giá trị nhỏ nhất của biểu thức: $A = |x - 4| + |x - 9|$.
  - *Lời giải:* $A = |x - 4| + |9 - x| \ge |x - 4 + 9 - x| = 5$. Dấu "$=$" xảy ra khi $4 \le x \le 9$. Vậy $\min A = 5$ khi $4 \le x \le 9$.

