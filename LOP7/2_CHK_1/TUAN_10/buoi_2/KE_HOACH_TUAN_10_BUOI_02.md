# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 10 - BUỔI 02 (TOÁN 7)
## CHỦ ĐỀ: BÀI 13 - LUYỆN TẬP C-C-C: CHỨNG MINH SONG SONG, VUÔNG GÓC & ỨNG DỤNG THỰC TẾ
### Bám sát chương trình: SGK Toán 7 - Kết nối tri thức với cuộc sống (Chương IV)
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Củng cố và nâng cao trường hợp bằng nhau thứ nhất Cạnh - Cạnh - Cạnh (c.c.c).
   - Vận dụng hai tam giác bằng nhau suy ra hai góc so le trong bằng nhau $\implies$ chứng minh hai đường thẳng song song.
   - Vận dụng hai tam giác bằng nhau suy ra hai góc kề bù bằng nhau $\implies$ mỗi góc bằng $90^\circ$ (chứng minh hai đường thẳng vuông góc).
   - Hiểu và giải thích được ứng dụng thực tế của tính cứng vững của kết cấu tam giác trong giàn giáo xây dựng, khung xe đạp, vì kèo mái nhà.
   - Củng cố Đại số: Phép tính số hữu tỉ nâng cao, lũy thừa, căn bậc hai số học, phương trình tìm $x$ và bài toán cực trị chứa giá trị tuyệt đối.

2. **Kỹ năng:**
   - Kỹ năng vẽ hình hình học chính xác bằng thước và compa.
   - Trình bày chứng minh hình học đa bước (chứng minh tam giác bằng nhau $\to$ suy ra góc tương ứng $\to$ kết luận song song / vuông góc) mạch lạc, logic.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

* **Thời gian làm bài:** 45 phút.
* **Gồm 4 mã đề tương đương:** $101, 102, 103, 104$.
* **Quy chuẩn trang:** Trọn vẹn 2 trang A4 / mã đề (Tổng file PDF: 8 trang).

| Phần / Câu | Số câu/ý | Điểm | Thời gian (phút) | Dạng câu hỏi & Quy cách trình bày |
| :--- | :---: | :---: | :---: | :--- |
| **Câu 1 $\to$ 10** | 10 câu | **2,5 đ** *(0,25 đ/câu)* | 10 | Trả lời ngắn, lệnh `\shortans`, ô kết quả `KQ: [   ]` bo góc mép phải, bố trí 2 cột Trang 1. |
| **Câu 11** | 6 ý | **3,0 đ** *(0,5 đ/ý)* | 15 | Thực hiện phép tính (hợp lý nếu có thể). Bảng $3 \times 2$, dùng **`\oBaiTap[5]`** lấp kín đáy Trang 1. |
| **Câu 12** | 4 ý | **2,0 đ** *(0,5 đ/ý)* | 10 | Tìm số hữu tỉ $x$. Bảng $2 \times 2$, dùng **`\oBaiTap[5]`** đầu Trang 2. |
| **Câu 13** | 2 ý | **2,0 đ** *(1,0 đ/ý)* | 8 | Bài toán Hình học chứng minh C-C-C $\implies$ Song song. Ghép đề + hình TikZ vào box, bài giải **`\dongkeHaiCot{11}`**. |
| **Câu 14** | 1 ý | **0,5 đ** | 2 | Vận dụng cao điểm 10: GTLN của phân thức chứa giá trị tuyệt đối. Box bài giải **`\dongkeHaiCot{7}`** chạm sát đáy Trang 2. |
| **Tổng cộng** | **23 ý** | **10,0 đ** | **45** | **Khít mép giấy cả 2 trang, không tràn, không hở.** |

---

## 🔢 III. BẢNG DỮ LIỆU SỐ HỌC 4 MÃ ĐỀ (HOÀN TOÀN TƯƠNG ĐƯƠNG)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - 2,5 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Số đối của số hữu tỉ | Số đối của $\dfrac{4}{9}$ là: **$-\dfrac{4}{9}$** | Số đối của $\dfrac{5}{7}$ là: **$-\dfrac{5}{7}$** | Số đối của $\dfrac{3}{11}$ là: **$-\dfrac{3}{11}$** | Số đối của $\dfrac{6}{13}$ là: **$-\dfrac{6}{13}$** |
| **2** | Căn bậc hai số học | $\sqrt{144} =$ **$12$** | $\sqrt{169} =$ **$13$** | $\sqrt{196} =$ **$14$** | $\sqrt{225} =$ **$15$** |
| **3** | Giá trị tuyệt đối | $\left\|-7{,}82\right\| =$ **$7{,}82$** | $\left\|-4{,}95\right\| =$ **$4{,}95$** | $\left\|-6{,}38\right\| =$ **$6{,}38$** | $\left\|-9{,}15\right\| =$ **$9{,}15$** |
| **4** | Định lí trường hợp c.c.c | Ba cạnh tam giác này bằng ba cạnh tam giác kia thì: **Hai tam giác bằng nhau** | Ba cạnh tam giác này bằng ba cạnh tam giác kia thì: **Hai tam giác bằng nhau** | Ba cạnh tam giác này bằng ba cạnh tam giác kia thì: **Hai tam giác bằng nhau** | Ba cạnh tam giác này bằng ba cạnh tam giác kia thì: **Hai tam giác bằng nhau** |
| **5** | Góc tương ứng từ $\Delta = \Delta$ | Cho $\Delta ABC = \Delta CDA, \widehat{BAC}=35^\circ \implies \widehat{DCA}=$ **$35^\circ$** | Cho $\Delta ABC = \Delta CDA, \widehat{BCA}=42^\circ \implies \widehat{DAC}=$ **$42^\circ$** | Cho $\Delta MNP = \Delta QPN, \widehat{MNP}=48^\circ \implies \widehat{QPN}=$ **$48^\circ$** | Cho $\Delta MNP = \Delta QPN, \widehat{MPN}=38^\circ \implies \widehat{QNP}=$ **$38^\circ$** |
| **6** | Suy ra song song | Có $\widehat{BAC} = \widehat{DCA}$ so le trong suy ra: **$AB \parallel CD$** | Có $\widehat{BCA} = \widehat{DAC}$ so le trong suy ra: **$AD \parallel BC$** | Có $\widehat{MNP} = \widehat{QPN}$ so le trong suy ra: **$MN \parallel PQ$** | Có $\widehat{MPN} = \widehat{QNP}$ so le trong suy ra: **$MQ \parallel NP$** |
| **7** | Nhận biết góc vuông ($90^\circ$) | Cho $\Delta ABM = \Delta ACM$, $\widehat{AMB}$ và $\widehat{AMC}$ kề bù $\implies \widehat{AMB}=$ **$90^\circ$** | Cho $\Delta HIK = \Delta HIN$, $\widehat{HIK}$ và $\widehat{HIN}$ kề bù $\implies \widehat{HIK}=$ **$90^\circ$** | Cho $\Delta DEF = \Delta DEG$, $\widehat{DEF}$ và $\widehat{DEG}$ kề bù $\implies \widehat{DEF}=$ **$90^\circ$** | Cho $\Delta PQR = \Delta PQS$, $\widehat{PQR}$ và $\widehat{PQS}$ kề bù $\implies \widehat{PQR}=$ **$90^\circ$** |
| **8** | Cạnh chung của 2 tam giác | Tứ giác $ABCD$ có $AB=CD, BC=DA$. Cạnh chung $\Delta ABC, \Delta CDA$ là: **Cạnh $AC$** | Tứ giác $MNPQ$ có $MN=PQ, NP=QM$. Cạnh chung $\Delta MNP, \Delta PQM$ là: **Cạnh $MP$** | Tứ giác $ABCD$ có $AB=AD, CB=CD$. Cạnh chung $\Delta ABC, \Delta ADC$ là: **Cạnh $AC$** | Tứ giác $EFGH$ có $EF=EH, GF=GH$. Cạnh chung $\Delta EFG, \Delta EHG$ là: **Cạnh $EG$** |
| **9** | Ứng dụng vẽ tia phân giác | Dùng compa vẽ 2 cung tròn cắt nhau tại $C$, tia $OC$ là: **Tia phân giác** | Vẽ tam giác biết độ dài 3 cạnh dựa trên trường hợp bằng nhau: **Cạnh - Cạnh - Cạnh** | Để kiểm tra 2 tam giác bằng gỗ có bằng nhau, chỉ cần đo: **Độ dài 3 cạnh** | Biết độ dài 3 cạnh thì vẽ được duy nhất mấy hình tam giác? **$1$ hình tam giác** |
| **10** | Toán thực tế kết cấu tam giác | Cánh cổng sắt có thanh giằng chéo không bị xệ nhờ tính: **Không biến dạng của tam giác** | Tháp truyền hình được cấu tạo bởi các thanh kim loại ghép thành: **Các hình tam giác** | Khung xe đạp thể thao cấu tạo gồm các hình tam giác giúp xe: **Cứng vững** | Khung giá chữ A treo tranh vẽ đứng vững trên mặt sàn nhờ cấu trúc: **Hình tam giác** |

---

### 2. PHẦN TỰ LUẬN - TRANG 1 & TRANG 2

#### CÂU 11 (3,0 ĐIỂM): THỰC HIỆN PHÉP TÍNH (HỢP LÝ NẾU CÓ THỂ)

* **Mã đề 101:**
  - $a) \dfrac{7}{10} + \dfrac{11}{20} - \dfrac{1}{4} = \dfrac{14 + 11 - 5}{20} = \dfrac{20}{20} = 1$
  - $b) \dfrac{7}{15} \cdot \left(-\dfrac{5}{8}\right) + \dfrac{7}{15} \cdot \left(-\dfrac{3}{8}\right) = \dfrac{7}{15} \cdot (-1) = -\dfrac{7}{15}$
  - $c) \left(-\dfrac{1}{3}\right)^3 \cdot 27 + \dfrac{4}{9} : \dfrac{2}{9} = -\dfrac{1}{27} \cdot 27 + 2 = -1 + 2 = 1$
  - $d) \sqrt{\dfrac{100}{49}} - \left|-\dfrac{4}{7}\right| + \dfrac{1}{7} = \dfrac{10}{7} - \dfrac{4}{7} + \dfrac{1}{7} = \dfrac{7}{7} = 1$
  - $e) \dfrac{10}{3} - \left[\dfrac{4}{3} + \left(\dfrac{1}{2}\right)^3 \cdot 8\right] = \dfrac{10}{3} - \left[\dfrac{4}{3} + 1\right] = \dfrac{10}{3} - \dfrac{7}{3} = 1$
  - $f) \dfrac{3^{10} \cdot 8^3}{2^8 \cdot 9^4} = \dfrac{3^{10} \cdot 2^9}{2^8 \cdot 3^8} = 3^2 \cdot 2 = 18$

* **Mã đề 102:**
  - $a) \dfrac{5}{8} + \dfrac{11}{16} - \dfrac{5}{16} = \dfrac{10 + 11 - 5}{16} = \dfrac{16}{16} = 1$
  - $b) \dfrac{8}{17} \cdot \left(-\dfrac{7}{12}\right) + \dfrac{8}{17} \cdot \left(-\dfrac{5}{12}\right) = \dfrac{8}{17} \cdot (-1) = -\dfrac{8}{17}$
  - $c) \left(-\dfrac{1}{2}\right)^4 \cdot 16 + \dfrac{5}{8} : \dfrac{5}{16} = \dfrac{1}{16} \cdot 16 + 2 = 1 + 2 = 3$
  - $d) \sqrt{\dfrac{121}{64}} - \left|-\dfrac{5}{8}\right| + \dfrac{2}{8} = \dfrac{11}{8} - \dfrac{5}{8} + \dfrac{2}{8} = \dfrac{8}{8} = 1$
  - $e) \dfrac{11}{3} - \left[\dfrac{5}{3} + \left(\dfrac{1}{3}\right)^2 \cdot 9\right] = \dfrac{11}{3} - \left[\dfrac{5}{3} + 1\right] = \dfrac{11}{3} - \dfrac{8}{3} = 1$
  - $f) \dfrac{2^{11} \cdot 27^3}{3^8 \cdot 4^5} = \dfrac{2^{11} \cdot 3^9}{3^8 \cdot 2^{10}} = 2 \cdot 3 = 6$

* **Mã đề 103:**
  - $a) \dfrac{4}{9} + \dfrac{13}{18} - \dfrac{1}{6} = \dfrac{8 + 13 - 3}{18} = \dfrac{18}{18} = 1$
  - $b) \dfrac{9}{19} \cdot \left(-\dfrac{8}{13}\right) + \dfrac{9}{19} \cdot \left(-\dfrac{5}{13}\right) = \dfrac{9}{19} \cdot (-1) = -\dfrac{9}{19}$
  - $c) \left(-\dfrac{1}{5}\right)^2 \cdot 25 + \dfrac{6}{7} : \dfrac{3}{7} = \dfrac{1}{25} \cdot 25 + 2 = 1 + 2 = 3$
  - $d) \sqrt{\dfrac{144}{81}} - \left|-\dfrac{5}{9}\right| + \dfrac{2}{9} = \dfrac{12}{9} - \dfrac{5}{9} + \dfrac{2}{9} = \dfrac{9}{9} = 1$
  - $e) \dfrac{13}{4} - \left[\dfrac{5}{4} + \left(\dfrac{1}{2}\right)^2 \cdot 4\right] = \dfrac{13}{4} - \left[\dfrac{5}{4} + 1\right] = \dfrac{13}{4} - \dfrac{9}{4} = 1$
  - $f) \dfrac{5^{10} \cdot 6^4}{15^4 \cdot 25^2} = \dfrac{5^{10} \cdot 2^4 \cdot 3^4}{3^4 \cdot 5^4 \cdot 5^4} = 5^2 \cdot 2^4 = 25 \cdot 16 = 400$

* **Mã đề 104:**
  - $a) \dfrac{5}{12} + \dfrac{17}{24} - \dfrac{1}{8} = \dfrac{10 + 17 - 3}{24} = \dfrac{24}{24} = 1$
  - $b) \dfrac{11}{21} \cdot \left(-\dfrac{9}{14}\right) + \dfrac{11}{21} \cdot \left(-\dfrac{5}{14}\right) = \dfrac{11}{21} \cdot (-1) = -\dfrac{11}{21}$
  - $c) \left(-\dfrac{1}{2}\right)^5 \cdot 32 + \dfrac{8}{9} : \dfrac{4}{9} = -\dfrac{1}{32} \cdot 32 + 2 = -1 + 2 = 1$
  - $d) \sqrt{\dfrac{169}{100}} - \left|-\dfrac{7}{10}\right| + \dfrac{4}{10} = \dfrac{13}{10} - \dfrac{7}{10} + \dfrac{4}{10} = \dfrac{10}{10} = 1$
  - $e) \dfrac{15}{4} - \left[\dfrac{7}{4} + \left(\dfrac{1}{4}\right) \cdot 4\right] = \dfrac{15}{4} - \left[\dfrac{7}{4} + 1\right] = \dfrac{15}{4} - \dfrac{11}{4} = 1$
  - $f) \dfrac{2^9 \cdot 125^3}{10^7 \cdot 5} = \dfrac{2^9 \cdot 5^9}{2^7 \cdot 5^7 \cdot 5} = 2^2 \cdot 5 = 20$

---

#### CÂU 12 (2,0 ĐIỂM): TÌM SỐ HỮU TỈ $x$, BIẾT

* **Mã đề 101:**
  - $a) x + \dfrac{3}{7} = \dfrac{11}{14} \iff x = \dfrac{11}{14} - \dfrac{6}{14} = \dfrac{5}{14}$
  - $b) \dfrac{5}{6} - \dfrac{2}{3}x = \dfrac{1}{2} \iff \dfrac{2}{3}x = \dfrac{5}{6} - \dfrac{3}{6} = \dfrac{1}{3} \iff x = \dfrac{1}{2}$
  - $c) \left(2x - \dfrac{1}{3}\right)^2 = \dfrac{25}{9} \iff 2x - \dfrac{1}{3} = \pm \dfrac{5}{3} \iff x \in \left\{1; -\dfrac{2}{3}\right\}$
  - $d) \left|3x + \dfrac{1}{2}\right| = \dfrac{7}{2} \iff 3x + \dfrac{1}{2} = \pm \dfrac{7}{2} \iff x \in \left\{1; -\dfrac{4}{3}\right\}$

* **Mã đề 102:**
  - $a) x + \dfrac{2}{5} = \dfrac{9}{10} \iff x = \dfrac{9}{10} - \dfrac{4}{10} = \dfrac{5}{10} = \dfrac{1}{2}$
  - $b) \dfrac{7}{8} - \dfrac{3}{4}x = \dfrac{1}{8} \iff \dfrac{3}{4}x = \dfrac{6}{8} = \dfrac{3}{4} \iff x = 1$
  - $c) \left(2x - \dfrac{1}{2}\right)^2 = \dfrac{9}{4} \iff 2x - \dfrac{1}{2} = \pm \dfrac{3}{2} \iff x \in \left\{1; -\dfrac{1}{2}\right\}$
  - $d) \left|2x + \dfrac{1}{3}\right| = \dfrac{7}{3} \iff 2x + \dfrac{1}{3} = \pm \dfrac{7}{3} \iff x \in \left\{1; -\dfrac{4}{3}\right\}$

* **Mã đề 103:**
  - $a) x + \dfrac{3}{8} = \dfrac{11}{16} \iff x = \dfrac{11}{16} - \dfrac{6}{16} = \dfrac{5}{16}$
  - $b) \dfrac{4}{5} - \dfrac{3}{5}x = \dfrac{1}{5} \iff \dfrac{3}{5}x = \dfrac{3}{5} \iff x = 1$
  - $c) \left(3x - \dfrac{1}{2}\right)^2 = \dfrac{25}{4} \iff 3x - \dfrac{1}{2} = \pm \dfrac{5}{2} \iff x \in \left\{1; -\dfrac{2}{3}\right\}$
  - $d) \left|4x + \dfrac{1}{2}\right| = \dfrac{9}{2} \iff 4x + \dfrac{1}{2} = \pm \dfrac{9}{2} \iff x \in \left\{1; -\dfrac{5}{4}\right\}$

* **Mã đề 104:**
  - $a) x + \dfrac{4}{9} = \dfrac{13}{18} \iff x = \dfrac{13}{18} - \dfrac{8}{18} = \dfrac{5}{18}$
  - $b) \dfrac{5}{6} - \dfrac{1}{2}x = \dfrac{1}{3} \iff \dfrac{1}{2}x = \dfrac{5}{6} - \dfrac{2}{6} = \dfrac{1}{2} \iff x = 1$
  - $c) \left(3x - \dfrac{1}{3}\right)^2 = \dfrac{16}{9} \iff 3x - \dfrac{1}{3} = \pm \dfrac{4}{3} \iff x \in \left\{\dfrac{5}{9}; -\dfrac{1}{3}\right\}$
  - $d) \left|2x + \dfrac{3}{4}\right| = \dfrac{7}{4} \iff 2x + \dfrac{3}{4} = \pm \dfrac{7}{4} \iff x \in \left\{\dfrac{1}{2}; -\dfrac{5}{4}\right\}$

---

#### CÂU 13 (2,0 ĐIỂM): BÀI TOÁN HÌNH HỌC CHỨNG MINH C-C-C $\implies$ SONG SONG

* **Mã đề 101:**
  - **Đề bài:** Cho tứ giác $ABCD$ có $AB = CD$ và $BC = DA$. Nối hai đỉnh $A$ và $C$.\par
    a) (1,0 điểm) Chứng minh rằng $\Delta ABC = \Delta CDA$.\par
    b) (1,0 điểm) Chứng minh rằng $AB \parallel CD$ và $AD \parallel BC$. Biết $\widehat{B} = 110^\circ, \widehat{BAC} = 30^\circ$, tính số đo các góc $\widehat{D}$ và $\widehat{DCA}$.
  - **Lời giải:**
    * a) Xét $\Delta ABC$ và $\Delta CDA$, có:
      - $AB = CD$ (theo giả thiết)
      - $BC = DA$ (theo giả thiết)
      - $AC$ là cạnh chung
      $\implies \Delta ABC = \Delta CDA$ (c.c.c).
    * b) Do $\Delta ABC = \Delta CDA \implies \widehat{BAC} = \widehat{DCA}$ (hai góc tương ứng).
      Mà hai góc này ở vị trí so le trong, nên $AB \parallel CD$.
      Tương tự, $\widehat{BCA} = \widehat{DAC}$ (hai góc tương ứng), mà hai góc này ở vị trí so le trong nên $AD \parallel BC$.
      Do $\Delta ABC = \Delta CDA \implies \widehat{D} = \widehat{B} = 110^\circ$ và $\widehat{DCA} = \widehat{BAC} = 30^\circ$.

* **Mã đề 102:**
  - **Đề bài:** Cho tứ giác $ABCD$ có $AB = CD$ và $BC = DA$. Nối hai đỉnh $A$ và $C$.\par
    a) (1,0 điểm) Chứng minh rằng $\Delta ABC = \Delta CDA$.\par
    b) (1,0 điểm) Chứng minh rằng $AB \parallel CD$ và $AD \parallel BC$. Biết $\widehat{B} = 115^\circ, \widehat{BAC} = 25^\circ$, tính số đo các góc $\widehat{D}$ và $\widehat{DCA}$.
  - **Lời giải:**
    * a) $\Delta ABC = \Delta CDA$ (c.c.c) do $AB=CD, BC=DA$, cạnh chung $AC$.
    * b) $\widehat{BAC} = \widehat{DCA}$ (so le trong) $\implies AB \parallel CD$; $\widehat{BCA} = \widehat{DAC}$ (so le trong) $\implies AD \parallel BC$.
      $\widehat{D} = \widehat{B} = 115^\circ; \widehat{DCA} = \widehat{BAC} = 25^\circ$.

* **Mã đề 103:**
  - **Đề bài:** Cho tứ giác $ABCD$ có $AB = CD$ và $BC = DA$. Nối hai đỉnh $A$ và $C$.\par
    a) (1,0 điểm) Chứng minh rằng $\Delta ABC = \Delta CDA$.\par
    b) (1,0 điểm) Chứng minh rằng $AB \parallel CD$ và $AD \parallel BC$. Biết $\widehat{B} = 105^\circ, \widehat{BAC} = 35^\circ$, tính số đo các góc $\widehat{D}$ và $\widehat{DCA}$.
  - **Lời giải:**
    * a) $\Delta ABC = \Delta CDA$ (c.c.c).
    * b) $AB \parallel CD$ và $AD \parallel BC$.
      $\widehat{D} = \widehat{B} = 105^\circ; \widehat{DCA} = \widehat{BAC} = 35^\circ$.

* **Mã đề 104:**
  - **Đề bài:** Cho tứ giác $ABCD$ có $AB = CD$ và $BC = DA$. Nối hai đỉnh $A$ và $C$.\par
    a) (1,0 điểm) Chứng minh rằng $\Delta ABC = \Delta CDA$.\par
    b) (1,0 điểm) Chứng minh rằng $AB \parallel CD$ và $AD \parallel BC$. Biết $\widehat{B} = 120^\circ, \widehat{BAC} = 20^\circ$, tính số đo các góc $\widehat{D}$ và $\widehat{DCA}$.
  - **Lời giải:**
    * a) $\Delta ABC = \Delta CDA$ (c.c.c).
    * b) $AB \parallel CD$ và $AD \parallel BC$.
      $\widehat{D} = \widehat{B} = 120^\circ; \widehat{DCA} = \widehat{BAC} = 20^\circ$.

---

#### CÂU 14 (0,5 ĐIỂM): VẬN DỤNG CAO ĐIỂM 10 (GTLN PHÂN THỨC CHỨA GIÁ TRỊ TUYỆT ĐỐI)

* **Mã đề 101:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{12}{|x - 2026| + 3}$.
  - *Lời giải:* Với mọi số thực $x$, ta có: $|x - 2026| \ge 0 \implies |x - 2026| + 3 \ge 3$.
    Do đó $B = \dfrac{12}{|x - 2026| + 3} \le \dfrac{12}{3} = 4$.
    Dấu "$=$" xảy ra khi $|x - 2026| = 0 \iff x = 2026$.
    Kết luận: Giá trị lớn nhất của $B$ là $4$ khi $x = 2026$.

* **Mã đề 102:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{15}{|x - 2025| + 5}$.
  - *Lời giải:* Vì $|x - 2025| + 5 \ge 5 \implies B \le \dfrac{15}{5} = 3$.
    Dấu "$=$" xảy ra khi $x = 2025$.
    Kết luận: $\max B = 3$ khi $x = 2025$.

* **Mã đề 103:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{18}{|x - 2024| + 6}$.
  - *Lời giải:* Vì $|x - 2024| + 6 \ge 6 \implies B \le \dfrac{18}{6} = 3$.
    Dấu "$=$" xảy ra khi $x = 2024$.
    Kết luận: $\max B = 3$ khi $x = 2024$.

* **Mã đề 104:** Tìm giá trị lớn nhất của biểu thức: $B = \dfrac{20}{|x - 2023| + 4}$.
  - *Lời giải:* Vì $|x - 2023| + 4 \ge 4 \implies B \le \dfrac{20}{4} = 5$.
    Dấu "$=$" xảy ra khi $x = 2023$.
    Kết luận: $\max B = 5$ khi $x = 2023$.

