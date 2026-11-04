# KẾ HOẠCH NỘI DUNG & MA TRẬN ĐỀ KIỂM TRA - TUẦN 10 - BUỔI 02 (TOÁN 8)
## CHỦ ĐỀ: ĐỊNH LÍ THALÈS ĐẢO & HỆ QUẢ - ỨNG DỤNG ĐO ĐẠC THỰC TẾ
### Bám sát chương trình: SGK Toán 8 - Kết nối tri thức với cuộc sống (Chương IV) & Cánh diều
### Đơn vị biên soạn: Lớp Toán Thầy Lĩnh (loptoanthaylinh.vn)

---

## 🎯 I. MỤC TIÊU VÀ YÊU CẦU CẦN ĐẠT

1. **Kiến thức:**
   - Nắm vững định lí Thalès đảo trong tam giác: Nếu một đường thẳng cắt hai cạnh của tam giác và định ra trên hai cạnh này những đoạn thẳng tương ứng tỉ lệ thì đường thẳng đó song song với cạnh còn lại của tam giác.
   - Vận dụng định lí Thalès đảo để chứng minh quan hệ song song ($MN \parallel BC$).
   - Nắm vững hệ quả của định lí Thalès: Nếu một đường thẳng cắt hai cạnh của một tam giác và song song với cạnh còn lại thì nó tạo thành một tam giác mới có ba cạnh tương ứng tỉ lệ với ba cạnh của tam giác đã cho.
   - Vận dụng tỉ lệ thức hệ quả Thalès $\dfrac{MN}{BC} = \dfrac{AM}{AB}$ để tính độ dài cạnh song song $MN$.
   - Ứng dụng đo khoảng cách thực địa: đo khoảng cách giữa hai điểm ngăn cách bởi bờ sông hoặc hồ nước.
   - Củng cố Đại số: Rút gọn biểu thức tổng hai bình phương đối xứng $(ax - b)^2 + (ax + b)^2$, phân tích đa thức thành nhân tử thành thạo (đặt nhân tử chung, dùng hằng đẳng thức, nhóm hạng tử, tách hạng tử tam thức bậc hai).
   - Tìm $x$: Phương trình tích, hiệu hai bình phương, bình phương một nhị thức.
   - Nâng cao: Tìm giá trị lớn nhất (GTLN) của tam thức bậc hai mang dấu âm $P = -x^2 + 2ax + c$.

2. **Kỹ năng:**
   - Kỹ năng vẽ hình hình học chính xác với TikZ, ký hiệu rõ ràng trung điểm và tỉ số.
   - Trình bày bài toán tự luận hình học 2 cột khoa học (`\dongkeHaiCot{11}`).
   - Rèn luyện kỹ năng biến đổi đại số chuẩn xác, lập luận chặt chẽ khi tìm cực trị.

---

## 📐 II. CẤU TRÚC MA TRẬN ĐỀ THI 10 ĐIỂM (CHUẨN 2 TRANG A4)

* **Thời gian làm bài:** 45 phút.
* **Gồm 4 mã đề tương đương:** $101, 102, 103, 104$.
* **Quy chuẩn trang:** Trọn vẹn 2 trang A4 / mã đề (Tổng file PDF: 8 trang).

| Phần / Câu | Số câu/ý | Điểm | Thời gian (phút) | Dạng câu hỏi & Quy cách trình bày |
| :--- | :---: | :---: | :---: | :--- |
| **Câu 1 $\to$ 10** | 10 câu | **2,5 đ** *(0,25 đ/câu)* | 10 | Trả lời ngắn, lệnh `\shortans`, ô kết quả `KQ: [   ]` bo góc mép phải, bố trí 2 cột Trang 1. |
| **Câu 11** | 6 ý | **3,0 đ** *(0,5 đ/ý)* | 15 | Thực hiện phép tính & Phân tích nhân tử. Bảng $3 \times 2$, dùng **`\oBaiTap[5]`** lấp kín đáy Trang 1. |
| **Câu 12** | 4 ý | **2,0 đ** *(0,5 đ/ý)* | 10 | Tìm $x$. Bảng $2 \times 2$, dùng **`\oBaiTap[5]`** đầu Trang 2. |
| **Câu 13** | 2 ý | **2,0 đ** *(1,0 đ/ý)* | 8 | Bài toán Hình học Định lí Thalès đảo & Hệ quả. Box `tabularx` kèm hình vẽ TikZ, bài giải **`\dongkeHaiCot{11}`**. |
| **Câu 14** | 1 ý | **0,5 đ** | 2 | Vận dụng cao điểm 10: Tìm GTLN của tam thức bậc hai âm $-x^2 + 2ax + c$. Box bài giải **`\dongkeHaiCot{7}`** chạm sát đáy Trang 2. |
| **Tổng cộng** | **23 ý** | **10,0 đ** | **45** | **Khít mép giấy cả 2 trang, không tràn, không hở.** |

---

## 🔢 III. BẢNG DỮ LIỆU SỐ HỌC 4 MÃ ĐỀ (HOÀN TOÀN TƯƠNG ĐƯƠNG)

### 1. PHẦN TRẢ LỜI NGẮN (CÂU 1 ĐẾN CÂU 10 - 2,5 ĐIỂM)

| Câu | Nội dung kiến thức | Mã đề 101 | Mã đề 102 | Mã đề 103 | Mã đề 104 |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | Định lí Thalès đảo | $\dfrac{AM}{MB} = \dfrac{AN}{NC} = \dfrac{2}{3} \implies MN \dots BC$: **$\parallel$** | $\dfrac{AM}{AB} = \dfrac{AN}{AC} = \dfrac{1}{3} \implies MN \dots BC$: **$\parallel$** | $\dfrac{MB}{AB} = \dfrac{NC}{AC} = \dfrac{3}{5} \implies MN \dots BC$: **$\parallel$** | $\dfrac{AM}{MB} = \dfrac{AN}{NC} = \dfrac{1}{2} \implies MN \dots BC$: **$\parallel$** |
| **2** | Hệ quả định lí Thalès | $\Delta ABC, MN \parallel BC$. $AM=2, AB=6, BC=9 \implies MN =$ **$3\text{ cm}$** | $\Delta ABC, MN \parallel BC$. $AM=3, AB=9, BC=12 \implies MN =$ **$4\text{ cm}$** | $\Delta ABC, MN \parallel BC$. $AM=4, AB=10, BC=15 \implies MN =$ **$6\text{ cm}$** | $\Delta ABC, MN \parallel BC$. $AM=2, AB=8, BC=16 \implies MN =$ **$4\text{ cm}$** |
| **3** | Tỉ số đoạn thẳng Thalès | $DE \parallel BC, AD=3, DB=2 \implies \dfrac{DE}{BC} =$ **$\dfrac{3}{5}$** | $DE \parallel BC, AD=4, DB=3 \implies \dfrac{DE}{BC} =$ **$\dfrac{4}{7}$** | $DE \parallel BC, AD=2, DB=3 \implies \dfrac{DE}{BC} =$ **$\dfrac{2}{5}$** | $DE \parallel BC, AD=5, DB=2 \implies \dfrac{DE}{BC} =$ **$\dfrac{5}{7}$** |
| **4** | Phân tích đặt nhân tử chung | Phân tích $3x^2 - 6x$ thành nhân tử: **$3x(x - 2)$** | Phân tích $4x^2 - 8x$ thành nhân tử: **$4x(x - 2)$** | Phân tích $5x^2 - 10x$ thành nhân tử: **$5x(x - 2)$** | Phân tích $2x^2 - 6x$ thành nhân tử: **$2x(x - 3)$** |
| **5** | Phân tích hiệu hai bình phương | Phân tích $x^2 - 25$ thành nhân tử: **$(x-5)(x+5)$** | Phân tích $x^2 - 36$ thành nhân tử: **$(x-6)(x+6)$** | Phân tích $x^2 - 49$ thành nhân tử: **$(x-7)(x+7)$** | Phân tích $x^2 - 64$ thành nhân tử: **$(x-8)(x+8)$** |
| **6** | Thu gọn thành bình phương | Thu gọn $x^2 + 6x + 9$ thành: **$(x + 3)^2$** | Thu gọn $x^2 - 8x + 16$ thành: **$(x - 4)^2$** | Thu gọn $x^2 + 10x + 25$ thành: **$(x + 5)^2$** | Thu gọn $x^2 - 12x + 36$ thành: **$(x - 6)^2$** |
| **7** | Bậc của đa thức | Bậc của $P = 4x^3 y^2 - 5x^2 y^3 + 2xy - 1$ là: **$5$** | Bậc của $Q = 6x^4 y - 2x^2 y^3 + 3x^3 y^2 - 9$ là: **$5$** | Bậc của $R = 3x^5 y - 4x^3 y^3 + x^2 y - 7$ là: **$6$** | Bậc của $S = 2x^4 y^2 - 5x^3 y^3 + 4xy^4 + 1$ là: **$6$** |
| **8** | Chia đơn thức cho đơn thức | $(18x^5 y^4) : (6x^3 y^2) =$ **$3x^2 y^2$** | $(24x^6 y^5) : (8x^4 y^3) =$ **$3x^2 y^2$** | $(20x^5 y^3) : (5x^3 y) =$ **$4x^2 y^2$** | $(35x^7 y^4) : (7x^5 y^2) =$ **$5x^2 y^2$** |
| **9** | Lý thuyết định lí Thalès đảo | Định lí Thalès đảo dùng để chứng minh hai đường thẳng: **Song song** | Định lí Thalès thuận dùng để tính: **Độ dài đoạn thẳng** | Hệ quả Thalès tạo thành tam giác có ba cạnh: **Tương ứng tỉ lệ** | Đường thẳng song song một cạnh tam giác tạo ra các đoạn thẳng: **Tương ứng tỉ lệ** |
| **10** | Toán thực tế đo bờ sông | $OM=4\text{ m}, MA=8\text{ m}, MN=6\text{ m} \implies AB =$ **$18\text{ m}$** | $OM=5\text{ m}, MA=10\text{ m}, MN=7\text{ m} \implies AB =$ **$21\text{ m}$** | $OM=3\text{ m}, MA=9\text{ m}, MN=5\text{ m} \implies AB =$ **$20\text{ m}$** | $OM=4\text{ m}, MA=12\text{ m}, MN=6\text{ m} \implies AB =$ **$24\text{ m}$** |

---

### 2. PHẦN TỰ LUẬN - TRANG 1 & TRANG 2

#### CÂU 11 (3,0 ĐIỂM): THỰC HIỆN PHÉP TÍNH & PHÂN TÍCH NHÂN TỬ

* **Mã đề 101:**
  - $a) 3x(2x^2 - 5x + 3) = 6x^3 - 15x^2 + 9x$
  - $b) (x - 1)(x + 4) - (x^2 - 4) = x^2 + 3x - 4 - x^2 + 4 = 3x$
  - $c) (2x - 3)^2 + (2x + 3)^2 = 2[(2x)^2 + 3^2] = 2(4x^2 + 9) = 8x^2 + 18$
  - $d)$ Phân tích nhân tử: $xy - 3x + 2y - 6 = x(y - 3) + 2(y - 3) = (x + 2)(y - 3)$
  - $e)$ Phân tích nhân tử: $x^2 - y^2 + 4x + 4 = (x^2 + 4x + 4) - y^2 = (x + 2)^2 - y^2 = (x + 2 - y)(x + 2 + y)$
  - $f)$ Phân tích tam thức bậc hai: $x^2 - 7x + 12 = x^2 - 3x - 4x + 12 = x(x - 3) - 4(x - 3) = (x - 3)(x - 4)$

* **Mã đề 102:**
  - $a) 4x(2x^2 - 3x + 4) = 8x^3 - 12x^2 + 16x$
  - $b) (x - 2)(x + 5) - (x^2 - 10) = x^2 + 3x - 10 - x^2 + 10 = 3x$
  - $c) (3x - 2)^2 + (3x + 2)^2 = 2[(3x)^2 + 2^2] = 2(9x^2 + 4) = 18x^2 + 8$
  - $d)$ Phân tích nhân tử: $xy - 4x + 3y - 12 = x(y - 4) + 3(y - 4) = (x + 3)(y - 4)$
  - $e)$ Phân tích nhân tử: $x^2 - y^2 + 6x + 9 = (x^2 + 6x + 9) - y^2 = (x + 3)^2 - y^2 = (x + 3 - y)(x + 3 + y)$
  - $f)$ Phân tích tam thức bậc hai: $x^2 - 8x + 15 = x^2 - 3x - 5x + 15 = x(x - 3) - 5(x - 3) = (x - 3)(x - 5)$

* **Mã đề 103:**
  - $a) 2x(3x^2 - 4x + 5) = 6x^3 - 8x^2 + 10x$
  - $b) (x - 3)(x + 7) - (x^2 - 21) = x^2 + 4x - 21 - x^2 + 21 = 4x$
  - $c) (2x - 1)^2 + (2x + 1)^2 = 2[(2x)^2 + 1^2] = 2(4x^2 + 1) = 8x^2 + 2$
  - $d)$ Phân tích nhân tử: $xy - 5x + 2y - 10 = x(y - 5) + 2(y - 5) = (x + 2)(y - 5)$
  - $e)$ Phân tích nhân tử: $x^2 - y^2 + 8x + 16 = (x^2 + 8x + 16) - y^2 = (x + 4)^2 - y^2 = (x + 4 - y)(x + 4 + y)$
  - $f)$ Phân tích tam thức bậc hai: $x^2 - 9x + 20 = x^2 - 4x - 5x + 20 = x(x - 4) - 5(x - 4) = (x - 4)(x - 5)$

* **Mã đề 104:**
  - $a) 3x(3x^2 - 2x + 4) = 9x^3 - 6x^2 + 12x$
  - $b) (x - 2)(x + 6) - (x^2 - 12) = x^2 + 4x - 12 - x^2 + 12 = 4x$
  - $c) (3x - 1)^2 + (3x + 1)^2 = 2[(3x)^2 + 1^2] = 2(9x^2 + 1) = 18x^2 + 2$
  - $d)$ Phân tích nhân tử: $xy - 2x + 4y - 8 = x(y - 2) + 4(y - 2) = (x + 4)(y - 2)$
  - $e)$ Phân tích nhân tử: $x^2 - y^2 + 10x + 25 = (x^2 + 10x + 25) - y^2 = (x + 5)^2 - y^2 = (x + 5 - y)(x + 5 + y)$
  - $f)$ Phân tích tam thức bậc hai: $x^2 - 7x + 10 = x^2 - 2x - 5x + 10 = x(x - 2) - 5(x - 2) = (x - 2)(x - 5)$

---

#### CÂU 12 (2,0 ĐIỂM): TÌM $x$

* **Mã đề 101:**
  - $a) 2x(x - 4) - 2x^2 = 16 \iff 2x^2 - 8x - 2x^2 = 16 \iff -8x = 16 \iff x = -2$.
  - $b) x(x - 3) - 5(x - 3) = 0 \iff (x - 3)(x - 5) = 0 \iff x = 3$ hoặc $x = 5$.
  - $c) (x - 2)^2 - 16 = 0 \iff (x - 2 - 4)(x - 2 + 4) = 0 \iff (x - 6)(x + 2) = 0 \iff x = 6$ hoặc $x = -2$.
  - $d) (2x + 3)^2 = 49 \iff 2x + 3 = 7$ hoặc $2x + 3 = -7 \iff 2x = 4$ hoặc $2x = -10 \iff x = 2$ hoặc $x = -5$.

* **Mã đề 102:**
  - $a) 3x(x - 3) - 3x^2 = 18 \iff 3x^2 - 9x - 3x^2 = 18 \iff -9x = 18 \iff x = -2$.
  - $b) x(x - 4) - 6(x - 4) = 0 \iff (x - 4)(x - 6) = 0 \iff x = 4$ hoặc $x = 6$.
  - $c) (x - 3)^2 - 25 = 0 \iff (x - 3 - 5)(x - 3 + 5) = 0 \iff (x - 8)(x + 2) = 0 \iff x = 8$ hoặc $x = -2$.
  - $d) (2x - 1)^2 = 49 \iff 2x - 1 = 7$ hoặc $2x - 1 = -7 \iff 2x = 8$ hoặc $2x = -6 \iff x = 4$ hoặc $x = -3$.

* **Mã đề 103:**
  - $a) 4x(x - 3) - 4x^2 = 24 \iff 4x^2 - 12x - 4x^2 = 24 \iff -12x = 24 \iff x = -2$.
  - $b) x(x - 2) - 7(x - 2) = 0 \iff (x - 2)(x - 7) = 0 \iff x = 2$ hoặc $x = 7$.
  - $c) (x - 4)^2 - 9 = 0 \iff (x - 4 - 3)(x - 4 + 3) = 0 \iff (x - 7)(x - 1) = 0 \iff x = 7$ hoặc $x = 1$.
  - $d) (3x + 2)^2 = 64 \iff 3x + 2 = 8$ hoặc $3x + 2 = -8 \iff 3x = 6$ hoặc $3x = -10 \iff x = 2$ hoặc $x = -\dfrac{10}{3}$.

* **Mã đề 104:**
  - $a) 5x(x - 3) - 5x^2 = 30 \iff 5x^2 - 15x - 5x^2 = 30 \iff -15x = 30 \iff x = -2$.
  - $b) x(x - 5) - 4(x - 5) = 0 \iff (x - 5)(x - 4) = 0 \iff x = 5$ hoặc $x = 4$.
  - $c) (x - 5)^2 - 16 = 0 \iff (x - 5 - 4)(x - 5 + 4) = 0 \iff (x - 9)(x - 1) = 0 \iff x = 9$ hoặc $x = 1$.
  - $d) (3x - 2)^2 = 64 \iff 3x - 2 = 8$ hoặc $3x - 2 = -8 \iff 3x = 10$ hoặc $3x = -6 \iff x = \dfrac{10}{3}$ hoặc $x = -2$.

---

#### CÂU 13 (2,0 ĐIỂM): BÀI TOÁN HÌNH HỌC ĐỊNH LÍ THALÈS ĐẢO & HỆ QUẢ

Cho tam giác $ABC$. Trên cạnh $AB$ lấy điểm $M$, trên cạnh $AC$ lấy điểm $N$.
* **Mã đề 101:** Cho $AM = 4\text{ cm}, MB = 6\text{ cm}, AN = 6\text{ cm}, NC = 9\text{ cm}$. Cạnh $BC = 15\text{ cm}$.
  - $a)$ (1,0 điểm): Chứng minh $MN \parallel BC$.
    * Ta có tỉ số: $\dfrac{AM}{MB} = \dfrac{4}{6} = \dfrac{2}{3}$ ($0{,}25$đ).
    * Và: $\dfrac{AN}{NC} = \dfrac{6}{9} = \dfrac{2}{3}$ ($0{,}25$đ).
    * Suy ra: $\dfrac{AM}{MB} = \dfrac{AN}{NC} = \dfrac{2}{3}$ ($0{,}25$đ).
    * Do đó, theo định lí Thalès đảo trong tam giác $ABC$, ta có $MN \parallel BC$ (đpcm) ($0{,}25$đ).
  - $b)$ (1,0 điểm): Tính độ dài đoạn thẳng $MN$.
    * Độ dài cạnh $AB = AM + MB = 4 + 6 = 10\text{ cm}$ ($0{,}25$đ).
    * Vì $MN \parallel BC$, theo hệ quả của định lí Thalès ta có: $\dfrac{MN}{BC} = \dfrac{AM}{AB}$ ($0{,}25$đ).
    * Thay số: $\dfrac{MN}{15} = \dfrac{4}{10} = \dfrac{2}{5}$ ($0{,}25$đ).
    * Suy ra: $MN = \dfrac{15 \cdot 2}{5} = 6\text{ cm}$ ($0{,}25$đ).

* **Mã đề 102:** Cho $AM = 6\text{ cm}, MB = 9\text{ cm}, AN = 8\text{ cm}, NC = 12\text{ cm}$. Cạnh $BC = 20\text{ cm}$.
  - $a)$ $\dfrac{AM}{MB} = \dfrac{6}{9} = \dfrac{2}{3}$; $\dfrac{AN}{NC} = \dfrac{8}{12} = \dfrac{2}{3} \implies \dfrac{AM}{MB} = \dfrac{AN}{NC} \implies MN \parallel BC$ (định lí Thalès đảo).
  - $b)$ $AB = 6 + 9 = 15\text{ cm}$. Theo hệ quả Thalès: $\dfrac{MN}{BC} = \dfrac{AM}{AB} \iff \dfrac{MN}{20} = \dfrac{6}{15} \implies MN = \dfrac{20 \cdot 6}{15} = 8\text{ cm}$.

* **Mã đề 103:** Cho $AM = 3\text{ cm}, MB = 6\text{ cm}, AN = 4\text{ cm}, NC = 8\text{ cm}$. Cạnh $BC = 18\text{ cm}$.
  - $a)$ $\dfrac{AM}{MB} = \dfrac{3}{6} = \dfrac{1}{2}$; $\dfrac{AN}{NC} = \dfrac{4}{8} = \dfrac{1}{2} \implies \dfrac{AM}{MB} = \dfrac{AN}{NC} \implies MN \parallel BC$.
  - $b)$ $AB = 3 + 6 = 9\text{ cm}$. Theo hệ quả Thalès: $\dfrac{MN}{BC} = \dfrac{AM}{AB} \iff \dfrac{MN}{18} = \dfrac{3}{9} \implies MN = \dfrac{18 \cdot 3}{9} = 6\text{ cm}$.

* **Mã đề 104:** Cho $AM = 5\text{ cm}, MB = 10\text{ cm}, AN = 6\text{ cm}, NC = 12\text{ cm}$. Cạnh $BC = 24\text{ cm}$.
  - $a)$ $\dfrac{AM}{MB} = \dfrac{5}{10} = \dfrac{1}{2}$; $\dfrac{AN}{NC} = \dfrac{6}{12} = \dfrac{1}{2} \implies \dfrac{AM}{MB} = \dfrac{AN}{NC} \implies MN \parallel BC$.
  - $b)$ $AB = 5 + 10 = 15\text{ cm}$. Theo hệ quả Thalès: $\dfrac{MN}{BC} = \dfrac{AM}{AB} \iff \dfrac{MN}{24} = \dfrac{5}{15} \implies MN = \dfrac{24 \cdot 5}{15} = 8\text{ cm}$.

---

#### CÂU 14 (0,5 ĐIỂM): VẬN DỤNG CAO - GIÁ TRỊ LỚN NHẤT CỦA TAM THỨC BẬC HAI

* **Mã đề 101:** Tìm giá trị lớn nhất của biểu thức $P = -x^2 + 6x + 2020$.
  - Biến đổi: $P = -(x^2 - 6x + 9) + 2029 = -(x - 3)^2 + 2029$ ($0{,}25$đ).
  - Lập luận: Vì $-(x - 3)^2 \le 0$ với mọi $x \in \mathbb{R}$, nên $P \le 2029$ với mọi $x$.
  - Dấu đẳng thức xảy ra khi $x - 3 = 0 \iff x = 3$.
  - Kết luận: Giá trị lớn nhất của biểu thức $P$ bằng $2029$, đạt được khi $x = 3$ ($0{,}25$đ).

* **Mã đề 102:** Tìm giá trị lớn nhất của biểu thức $Q = -x^2 + 8x + 2010$.
  - $Q = -(x^2 - 8x + 16) + 2026 = -(x - 4)^2 + 2026 \le 2026$.
  - Dấu "$=$" xảy ra khi $x = 4$. Vậy $\max Q = 2026$ khi $x = 4$.

* **Mã đề 103:** Tìm giá trị lớn nhất của biểu thức $R = -x^2 + 10x + 2002$.
  - $R = -(x^2 - 10x + 25) + 2027 = -(x - 5)^2 + 2027 \le 2027$.
  - Dấu "$=$" xảy ra khi $x = 5$. Vậy $\max R = 2027$ khi $x = 5$.

* **Mã đề 104:** Tìm giá trị lớn nhất của biểu thức $S = -x^2 + 4x + 2024$.
  - $S = -(x^2 - 4x + 4) + 2028 = -(x - 2)^2 + 2028 \le 2028$.
  - Dấu "$=$" xảy ra khi $x = 2$. Vậy $\max S = 2028$ khi $x = 2$.

