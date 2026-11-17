# KẾ HOẠCH BÀI KIỂM TRA ĐỊNH KỲ TOÁN 7 - TUẦN 11 - BUỔI 02
## BÀI 14 (TIẾP THEO): TRƯỜNG HỢP BẰNG NHAU THỨ BA GÓC - CẠNH - GÓC (G-C-G) & CÁC TRƯỜNG HỢP BẰNG NHAU CỦA TAM GIÁC VUÔNG
### Bám sát chương trình: SGK Toán 7 - Kết nối tri thức với cuộc sống (Chương IV)

---

## 🎯 I. MỤC TIÊU CẦN ĐẠT

1. **Kiến thức:**
   - Nhận biết cạnh kề hai góc (cạnh nằm giữa hai góc).
   - Nắm vững và phát biểu định lí trường hợp bằng nhau thứ ba của tam giác (Góc - Cạnh - Góc).
   - Nắm vững hai trường hợp bằng nhau của tam giác vuông suy ra từ G-C-G:
     + Cạnh góc vuông và góc nhọn kề (c.g.v - g.nhọn).
     + Cạnh huyền và góc nhọn (c.huyền - g.nhọn).
   - Vận dụng chứng minh hai tam giác vuông bằng nhau để suy ra: hai cạnh bằng nhau, hai góc bằng nhau, hai đường thẳng song song.
   - Vận dụng bài toán thực tế: Đo khoảng cách từ đất liền ra tàu thuyền hoặc qua sông (phương pháp Thales).
2. **Kỹ năng & Năng lực:**
   - Kỹ năng lập luận suy diễn hình học chặt chẽ, chính xác.
   - Kỹ năng vẽ hình phụ trợ, kí hiệu góc vuông, góc bằng nhau trên hình.
   - Rèn luyện kỹ năng thực hiện phép tính phân số, số thập phân, căn bậc hai, quy tắc dấu ngoặc.
   - Giải phương trình tìm $x$ chứa dấu giá trị tuyệt đối dạng $a|x - b| + c = d$.
   - Tìm giá trị lớn nhất của phân thức có mẫu là biểu thức chứa giá trị tuyệt đối.

---

## 📐 II. MA TRẬN ĐỀ THI 10 ĐIỂM (45 PHÚT - 2 MẶT A4)

| STT | Dạng bài | Số câu / Ý | Điểm số | Vị trí trên phiếu | Quy chuẩn định dạng |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | Trả lời ngắn (Short Answer) | 10 câu | 2,5 đ | Trang 1 (Đầu trang) | Lệnh `\shortans`, ô bo góc `KQ: [   ]` sát mép phải. |
| **2** | Thực hiện phép tính | 6 ý ($a \to f$) | 3,0 đ | Trang 1 (Cuối trang) | Bảng $3 \times 2$, dùng `\oBaiTap[5]` lấp kín 100% lề dưới. |
| **3** | Tìm số hữu tỉ $x$ | 4 ý ($a \to d$) | 2,0 đ | Trang 2 (Đầu trang) | Bảng $2 \times 2$, dùng `\oBaiTap[5]`. |
| **4** | Hình học G-C-G & Tam giác vuông | 2 ý ($a, b$) | 2,0 đ | Trang 2 (Giữa trang) | Ghép box `tabularx` có hình TikZ, bài giải `\dongkeHaiCot{11}`. |
| **5** | Vận dụng cao điểm 10 | 1 bài | 0,5 đ | Trang 2 (Cuối trang) | Ghép box `tabularx`, bài giải `\dongkeHaiCot{7}` sát lề dưới. |
| **TỔNG** | | **23 mục** | **10,0 đ** | **2 mặt A4** | **Chính xác 8 trang PDF cho 4 mã đề (101-104)** |

---

## 📊 III. CHI TIẾT DỮ LIỆU TOÁN HỌC 4 MÃ ĐỀ (101, 102, 103, 104)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - MỖI CÂU 0,25 ĐIỂM)

| Câu | Chủ đề / Dạng toán | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Cạnh kề hai góc trong tam giác | $\Delta ABC$: cạnh kề $\widehat{B}, \widehat{C}$ $\to BC$ | $\Delta MNP$: cạnh kề $\widehat{M}, \widehat{P}$ $\to MP$ | $\Delta DEF$: cạnh kề $\widehat{D}, \widehat{E}$ $\to DE$ | $\Delta HIK$: cạnh kề $\widehat{I}, \widehat{K}$ $\to IK$ |
| **2** | Điều kiện bổ sung g.c.g | $\widehat{B}=\widehat{E}, BC=EF \implies \widehat{C}=\widehat{F}$ | $\widehat{M}=\widehat{Q}, MN=QR \implies \widehat{N}=\widehat{R}$ | $\widehat{A}=\widehat{M}, AC=MP \implies \widehat{C}=\widehat{P}$ | $\widehat{E}=\widehat{I}, EF=IK \implies \widehat{F}=\widehat{K}$ |
| **3** | Cạnh huyền - góc nhọn | $\Delta ABC, \Delta DEF$ vuông, $BC=EF \to \widehat{B}=\widehat{E}$ | $\Delta MNP, \Delta GHK$ vuông, $NP=HK \to \widehat{N}=\widehat{H}$ | $\Delta ABC, \Delta MNP$ vuông, $AC=MP \to \widehat{A}=\widehat{M}$ | $\Delta DEF, \Delta HIK$ vuông, $DF=HK \to \widehat{D}=\widehat{H}$ |
| **4** | C.g.v - góc nhọn kề | $\Delta ABC, \Delta A'B'$ vuông, $AB=A'B' \to \widehat{B}=\widehat{B'}$ | $\Delta MNP, \Delta DEF$ vuông, $MP=DF \to \widehat{P}=\widehat{F}$ | $\Delta ABC, \Delta MNP$ vuông, $BC=NP \to \widehat{C}=\widehat{P}$ | $\Delta DEF, \Delta HIK$ vuông, $DE=HI \to \widehat{D}=\widehat{H}$ |
| **5** | Tính góc thứ ba từ $\Delta = \Delta$ | $\widehat{A}=70^\circ, \widehat{B}=45^\circ \to \widehat{F}=65^\circ$ | $\widehat{A}=65^\circ, \widehat{B}=55^\circ \to \widehat{P}=60^\circ$ | $\widehat{D}=50^\circ, \widehat{E}=80^\circ \to \widehat{K}=50^\circ$ | $\widehat{A}=75^\circ, \widehat{B}=35^\circ \to \widehat{F}=70^\circ$ |
| **6** | Tính cạnh tương ứng qua chu vi | $AB=6, BC=8, C=24 \to MP=10\text{ cm}$ | $MN=5, NP=9, C=22 \to AC=8\text{ cm}$ | $DE=7, EF=10, C=25 \to DF=8\text{ cm}$ | $HI=6, IK=7, C=21 \to AC=8\text{ cm}$ |
| **7** | Căn bậc hai số học | $3\sqrt{16} - 2\sqrt{25} = 2$ | $2\sqrt{49} - 3\sqrt{16} = 2$ | $4\sqrt{25} - 2\sqrt{81} = 2$ | $5\sqrt{9} - 2\sqrt{36} = 3$ |
| **8** | Giá trị tuyệt đối ($x < 0$) | $|x + 1| = 3 \to x = -4$ | $|x + 2| = 5 \to x = -7$ | $|x + 3| = 4 \to x = -7$ | $|x + 1| = 5 \to x = -6$ |
| **9** | Thực tế: đo khoảng cách ra tàu | $AD = 62\text{ m} \to AC = 62\text{ m}$ | $AD = 75\text{ m} \to AC = 75\text{ m}$ | $AD = 84\text{ m} \to AC = 84\text{ m}$ | $AD = 96\text{ m} \to AC = 96\text{ m}$ |
| **10** | Tam giác vuông: 2 góc nhọn phụ | Góc nhọn $35^\circ \to 55^\circ$ | Góc nhọn $40^\circ \to 50^\circ$ | Góc nhọn $25^\circ \to 65^\circ$ | Góc nhọn $48^\circ \to 42^\circ$ |

---

### 2. CÂU 11 (3,0 ĐIỂM - THỰC HIỆN PHÉP TÍNH - 6 Ý $A \to F$)

* **Mã đề 101:**
  - $a)$ $\dfrac{4}{15} - \dfrac{5}{12} + \dfrac{11}{15} - \dfrac{7}{12} = 0$
  - $b)$ $\dfrac{3}{5} \cdot \dfrac{7}{11} + \dfrac{3}{5} \cdot \dfrac{4}{11} + \dfrac{2}{5} = 1$
  - $c)$ $\left(-\dfrac{2}{3}\right)^2 : \dfrac{8}{9} + \left(-\dfrac{1}{2}\right)^3 \cdot 4 = 0$
  - $d)$ $\sqrt{\dfrac{49}{100}} - \left|-\dfrac{3}{10}\right| + \sqrt{0{,}36} = 1$
  - $e)$ $\dfrac{2}{3} - \left[ \dfrac{1}{6} - \left(\dfrac{3}{4} - \dfrac{1}{2}\right) \right] = \dfrac{3}{4}$
  - $f)$ $\dfrac{9^3 \cdot 2^6}{6^5} = 6$

* **Mã đề 102:**
  - $a)$ $\dfrac{5}{18} - \dfrac{7}{16} + \dfrac{13}{18} - \dfrac{9}{16} = 0$
  - $b)$ $\dfrac{4}{7} \cdot \dfrac{5}{13} + \dfrac{4}{7} \cdot \dfrac{8}{13} + \dfrac{3}{7} = 1$
  - $c)$ $\left(-\dfrac{3}{4}\right)^2 : \dfrac{9}{8} + \left(-\dfrac{1}{3}\right)^2 \cdot (-9) = -\dfrac{1}{2}$
  - $d)$ $\sqrt{\dfrac{81}{100}} - \left|-\dfrac{4}{10}\right| + \sqrt{0{,}25} = 1$
  - $e)$ $\dfrac{3}{4} - \left[ \dfrac{1}{4} - \left(\dfrac{5}{6} - \dfrac{1}{3}\right) \right] = 1$
  - $f)$ $\dfrac{8^3 \cdot 3^8}{6^7} = 12$

* **Mã đề 103:**
  - $a)$ $\dfrac{3}{14} - \dfrac{5}{9} + \dfrac{11}{14} - \dfrac{4}{9} = 0$
  - $b)$ $\dfrac{5}{8} \cdot \dfrac{4}{9} + \dfrac{5}{8} \cdot \dfrac{5}{9} + \dfrac{3}{8} = 1$
  - $c)$ $\left(-\dfrac{1}{2}\right)^3 : \dfrac{1}{8} + \left(-\dfrac{2}{5}\right)^0 = 0$
  - $d)$ $\sqrt{\dfrac{64}{100}} - \left|-\dfrac{1}{10}\right| + \sqrt{0{,}09} = 1$
  - $e)$ $\dfrac{5}{6} - \left[ \dfrac{1}{3} - \left(\dfrac{3}{4} - \dfrac{1}{4}\right) \right] = 1$
  - $f)$ $\dfrac{25^2 \cdot 2^5}{10^4} = 2$

* **Mã đề 104:**
  - $a)$ $\dfrac{6}{19} - \dfrac{3}{8} + \dfrac{13}{19} - \dfrac{5}{8} = 0$
  - $b)$ $\dfrac{2}{9} \cdot \dfrac{7}{15} + \dfrac{2}{9} \cdot \dfrac{8}{15} + \dfrac{7}{9} = 1$
  - $c)$ $\left(-\dfrac{1}{3}\right)^3 \cdot 27 + \left(\dfrac{4}{9}\right)^0 = 0$
  - $d)$ $\sqrt{\dfrac{121}{100}} - \left|-\dfrac{5}{10}\right| + \sqrt{0{,}16} = 1$
  - $e)$ $\dfrac{4}{5} - \left[ \dfrac{1}{5} - \left(\dfrac{7}{10} - \dfrac{3}{10}\right) \right] = 1$
  - $f)$ $\dfrac{27^3 \cdot 2^8}{6^8} = 3$

---

### 3. CÂU 12 (2,0 ĐIỂM - TÌM SỐ HỮU TỈ $x$ - 4 Ý $A \to D$)

| Ý | Dạng phương trình | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **a** | Chuyển vế cơ bản | $x - \dfrac{3}{4} = \dfrac{1}{8} \to x = \dfrac{7}{8}$ | $x - \dfrac{2}{3} = \dfrac{1}{6} \to x = \dfrac{5}{6}$ | $x + \dfrac{1}{4} = \dfrac{5}{8} \to x = \dfrac{3}{8}$ | $x + \dfrac{2}{5} = \dfrac{9}{10} \to x = \dfrac{1}{2}$ |
| **b** | Nhân chia phân số | $\dfrac{3}{4}x + \dfrac{1}{3} = \dfrac{5}{6} \to x = \dfrac{2}{3}$ | $\dfrac{2}{5}x + \dfrac{1}{2} = \dfrac{9}{10} \to x = 1$ | $\dfrac{4}{5}x - \dfrac{1}{2} = \dfrac{3}{10} \to x = 1$ | $\dfrac{5}{6}x - \dfrac{1}{4} = \dfrac{7}{12} \to x = 1$ |
| **c** | Lũy thừa bậc hai | $\left(2x - \dfrac{1}{2}\right)^2 = \dfrac{9}{4} \to x \in \left\{1; -\dfrac{1}{2}\right\}$ | $\left(2x - \dfrac{1}{3}\right)^2 = \dfrac{25}{9} \to x \in \left\{1; -\dfrac{2}{3}\right\}$ | $\left(3x - \dfrac{1}{2}\right)^2 = \dfrac{25}{4} \to x \in \left\{1; -\dfrac{2}{3}\right\}$ | $\left(2x + \dfrac{1}{4}\right)^2 = \dfrac{49}{16} \to x \in \left\{\dfrac{3}{4}; -1\right\}$ |
| **d** | Giá trị tuyệt đối | $3\left\|x - \dfrac{1}{2}\right\| - \dfrac{1}{4} = \dfrac{5}{4} \to x \in \{1; 0\}$ | $2\left\|x - \dfrac{2}{3}\right\| - \dfrac{1}{3} = \dfrac{5}{3} \to x \in \left\{\dfrac{5}{3}; -\dfrac{1}{3}\right\}$ | $4\left\|x - \dfrac{1}{3}\right\| - \dfrac{2}{3} = \dfrac{10}{3} \to x \in \left\{\dfrac{4}{3}; -\dfrac{2}{3}\right\}$ | $2\left\|x - \dfrac{3}{4}\right\| - \dfrac{1}{2} = \dfrac{3}{2} \to x \in \left\{\dfrac{7}{4}; -\dfrac{1}{4}\right\}$ |

---

### 4. CÂU 13 (2,0 ĐIỂM - HÌNH HỌC CHỨNG MINH G-C-G & TAM GIÁC VUÔNG - 2 Ý $A, B$)

* **Mã đề 101:** Cho đoạn thẳng $AB$ có trung điểm là $I$. Qua $I$ kẻ đường thẳng $xy$ (đường thẳng $xy$ không vuông góc với $AB$). Từ $A$ kẻ $AH \perp xy$ tại $H$, từ $B$ kẻ $BK \perp xy$ tại $K$.
  - $a)$ (1,0 điểm): Chứng minh rằng $\Delta AHI = \Delta BKI$ (cạnh huyền - góc nhọn).
  - $b)$ (1,0 điểm): Chứng minh rằng $AH = BK$ và $AH \parallel BK$.
* **Mã đề 102:** Cho đoạn thẳng $CD$ có trung điểm là $O$. Qua $O$ kẻ đường thẳng $mn$ (đường thẳng $mn$ không vuông góc với $CD$). Từ $C$ kẻ $CE \perp mn$ tại $E$, từ $D$ kẻ $DF \perp mn$ tại $F$.
  - $a)$ (1,0 điểm): Chứng minh rằng $\Delta CEO = \Delta DFO$.
  - $b)$ (1,0 điểm): Chứng minh rằng $CE = DF$ và $CE \parallel DF$.
* **Mã đề 103:** Cho đoạn thẳng $MN$ có trung điểm là $E$. Qua $E$ kẻ đường thẳng $pq$ (đường thẳng $pq$ không vuông góc với $MN$). Từ $M$ kẻ $MP \perp pq$ tại $P$, từ $N$ kẻ $NQ \perp pq$ tại $Q$.
  - $a)$ (1,0 điểm): Chứng minh rằng $\Delta MPE = \Delta NQE$.
  - $b)$ (1,0 điểm): Chứng minh rằng $MP = NQ$ và $MP \parallel NQ$.
* **Mã đề 104:** Cho đoạn thẳng $EF$ có trung điểm là $K$. Qua $K$ kẻ đường thẳng $uv$ (đường thẳng $uv$ không vuông góc với $EF$). Từ $E$ kẻ $EG \perp uv$ tại $G$, từ $F$ kẻ $FH \perp uv$ tại $H$.
  - $a)$ (1,0 điểm): Chứng minh rằng $\Delta EGK = \Delta FHK$.
  - $b)$ (1,0 điểm): Chứng minh rằng $EG = FH$ và $EG \parallel FH$.

---

### 5. CÂU 14 (0,5 ĐIỂM - VẬN DỤNG CAO ĐIỂM 10)

* **Mã đề 101:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{12}{|x - 3| + 4}$.
  - *Lời giải:* Với mọi $x \in \mathbb{Q}$, ta luôn có $|x - 3| \ge 0 \implies |x - 3| + 4 \ge 4 \implies B = \dfrac{12}{|x - 3| + 4} \le \dfrac{12}{4} = 3$. Dấu "$=$" xảy ra khi $x - 3 = 0 \iff x = 3$. Vậy $\max B = 3$ khi $x = 3$.
* **Mã đề 102:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{15}{|x - 2| + 5}$.
  - *Lời giải:* Ta có $|x - 2| + 5 \ge 5 \implies B \le \dfrac{15}{5} = 3$. Dấu "$=$" xảy ra khi $x = 2$. Vậy $\max B = 3$ khi $x = 2$.
* **Mã đề 103:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{18}{|x - 5| + 6}$.
  - *Lời giải:* Ta có $|x - 5| + 6 \ge 6 \implies B \le \dfrac{18}{6} = 3$. Dấu "$=$" xảy ra khi $x = 5$. Vậy $\max B = 3$ khi $x = 5$.
* **Mã đề 104:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{20}{|x - 1| + 4}$.
  - *Lời giải:* Ta có $|x - 1| + 4 \ge 4 \implies B \le \dfrac{20}{4} = 5$. Dấu "$=$" xảy ra khi $x = 1$. Vậy $\max B = 5$ khi $x = 1$.

