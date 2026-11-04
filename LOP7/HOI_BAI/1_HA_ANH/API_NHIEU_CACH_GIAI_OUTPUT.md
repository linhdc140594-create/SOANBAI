# GIẢI CHI TIẾT 3 BÀI TOÁN LỚP 7

---

## BÀI 1

**Đề:** $\triangle ABC = \triangle MNP$, $AB=5$ cm, $AC=7$ cm, $NP=(2x+1)$ cm, chu vi $\triangle ABC = 21$ cm. Tìm $x$.

**Phân tích:** Ký hiệu $\triangle ABC=\triangle MNP$ cho biết các đỉnh tương ứng theo thứ tự: $A\leftrightarrow M,\ B\leftrightarrow N,\ C\leftrightarrow P$. Suy ra các cạnh tương ứng:

$$AB=MN,\quad AC=MP,\quad BC=NP.$$

### Cách 1: Tìm cạnh tương ứng rồi giải phương trình (chuẩn mực)

Cạnh $BC = 21 - AB - AC = 21 - 5 - 7 = 9$ (cm).

Vì $BC=NP$ nên $2x+1=9 \Rightarrow 2x=8 \Rightarrow x=4$.

### Cách 2: Dùng chu vi hai tam giác bằng nhau

Hai tam giác bằng nhau thì có cùng chu vi, nên $P_{MNP}=P_{ABC}=21$. Ta có $MN=AB=5$, $MP=AC=7$, do đó:

$$5+7+(2x+1)=21 \iff 2x+13=21 \iff x=4.$$

### Cách 3: Số học và sơ đồ đoạn thẳng

Vẽ đoạn thẳng biểu diễn chu vi 21 cm, gồm ba đoạn nối tiếp: 5, 7 và $NP$. Phần còn lại là $21-(5+7)=9$.

Vậy $NP=9$. Ta cần tìm số $x$ sao cho $2x+1=9$. Bớt 1 được 8, chia đôi được 4.

### Cách 4: Thử lại (kiểm tra nghiệm)

Với $x=4$: $NP=2\cdot4+1=9$. Tam giác $MNP$ có các cạnh 5, 7, 9, tổng là 21 (đúng). Bất đẳng thức tam giác cũng thỏa: $5+7=12>9$.

**Đáp số:** $x=4$.

### Nhận xét sư phạm

| Cách | Ưu điểm | Nhược điểm |
|---|---|---|
| 1 | Bám sát định nghĩa hai tam giác bằng nhau, rõ ràng | Cần nhớ đúng cạnh tương ứng |
| 2 | Ngắn gọn, đưa về một phương trình | Dễ quên giải thích $MN=AB$, $MP=AC$ |
| 3 | Trực quan, phù hợp học sinh yếu | Khó mở rộng khi số liệu phức tạp |
| 4 | Rèn thói quen kiểm tra, phát hiện nghiệm vô lý | Chỉ là bước bổ trợ |

### Sai lầm phổ biến

1. Cho $NP = AC$ hoặc $NP=AB$ vì không xác định đúng thứ tự đỉnh. Phải ghép $N\leftrightarrow B$, $P\leftrightarrow C$ nên $NP=BC$.
2. Lấy $2x+1=21$ (nhầm $NP$ là chu vi).
3. Quên tính $BC$ trước, hoặc trừ sai: $21-5-7=8$.
4. Không kiểm tra điều kiện $x$ để $NP>0$ và thỏa bất đẳng thức tam giác.

### Mở rộng

- **(a)** Nếu $\triangle ABC=\triangle MNP$ và $AB=5$, $AC=7$, $NP=(2x+1)$ nhưng chu vi chưa biết, tìm $x$ để $\triangle MNP$ tồn tại. Cần $2<2x+1<12$, tức $\tfrac12<x<\tfrac{11}{2}$.
- **(b)** Tìm $x$ để $\triangle MNP$ cân. Có hai khả năng: $NP=5$ cho $x=2$, hoặc $NP=7$ cho $x=3$.
- **(c)** Nếu $AB=x+2$, $AC=2x-1$, $NP=3x$ và chu vi bằng 30, tìm $x$ và độ dài ba cạnh.

---

## BÀI 2

**Đề:** Thùng 120 lít. Lần 1 dùng $\dfrac14$ lượng nước trong thùng. Lần 2 dùng $\dfrac25$ lượng nước **còn lại** sau lần 1. Hỏi còn bao nhiêu lít?

### Cách 1: Tính từng bước (số học)

- Lần 1 dùng: $120\cdot\dfrac14=30$ (lít). Còn lại: $120-30=90$ (lít).
- Lần 2 dùng: $90\cdot\dfrac25=36$ (lít). Còn lại: $90-36=54$ (lít).

### Cách 2: Tìm "phần còn lại" bằng phân số (nhân liên tiếp)

Sau lần 1 còn $1-\dfrac14=\dfrac34$ lượng nước. Sau lần 2 còn $1-\dfrac25=\dfrac35$ của lượng đó.

$$120\cdot\frac34\cdot\frac35=120\cdot\frac{9}{20}=54 \text{ (lít)}.$$

### Cách 3: Sơ đồ đoạn thẳng (quy về đơn vị)

Chia 120 lít thành 20 phần bằng nhau (BCNN của 4 và 5), mỗi phần là $120:20=6$ lít.

- Lần 1 dùng $\frac14$ nên dùng 5 phần, còn $20-5=15$ phần.
- Lần 2 dùng $\frac25$ của 15 phần, tức 6 phần, còn $15-6=9$ phần.

Vậy còn $9\cdot6=54$ lít.

### Cách 4: Phần trăm và tổng lượng đã dùng

- Lần 1 dùng $25\%$ lượng ban đầu, còn $75\%$.
- Lần 2 dùng $40\%$ của $75\%$, tức $30\%$ lượng ban đầu.
- Tổng đã dùng: $25\%+30\%=55\%$, tức $120\cdot0{,}55=66$ lít.
- Còn lại: $120-66=54$ lít.

### Cách 5: Đại số (đặt ẩn)

Gọi $y$ là lượng nước còn lại sau lần 1: $y=120-\dfrac14\cdot120=90$. Gọi $z$ là lượng nước còn lại sau hai lần: $z=y-\dfrac25y=\dfrac35y=54$.

**Đáp số:** 54 lít.

### Nhận xét sư phạm

- Cách 1 là cách cơ bản nhất, nên khuyến khích cho mọi học sinh.
- Cách 2 là cách "tinh gọn", giúp hiểu bản chất "nhân phân số liên tiếp", nhưng dễ nhầm nếu chưa nắm khái niệm "phần còn lại".
- Cách 3 trực quan và phù hợp khi bài toán có nhiều phân số, và là bước đệm sang bài toán ngược.
- Cách 4 liên hệ với phần trăm, rất hữu ích trong thực tế.
- Cách 5 giúp làm quen với tư duy đại số.

### Sai lầm phổ biến

1. **Lấy $\dfrac25$ của 120 thay vì của 90** (lượng ban đầu thay vì lượng còn lại): $\dfrac25\cdot120=48$, cho ra $120-30-48=42$ lít. Đây là kết quả sai.
2. Cộng thẳng $\dfrac14+\dfrac25=\dfrac{13}{20}$ rồi tính $120\cdot\dfrac{13}{20}=78$, còn $42$ lít. Sai vì hai phân số có "đơn vị tổng thể" khác nhau.
3. Nhầm giữa "lượng đã dùng" và "lượng còn lại" (trả lời 36 lít hoặc 66 lít thay vì 54 lít).
4. Quy đồng sai, hoặc không ghi đơn vị.

### Mở rộng

- **(a) Bài toán ngược:** Sau hai lần dùng như trên, thùng còn 54 lít. Hỏi ban đầu có bao nhiêu lít? ($54:\frac35:\frac34=120$).
- **(b)** Lần 3 dùng $\dfrac13$ lượng còn lại sau lần 2. Hỏi cuối cùng còn bao nhiêu lít? ($54\cdot\frac23=36$).
- **(c)** Nếu lần 1 dùng $\frac14$ và lần 2 dùng $\frac25$ của lượng *ban đầu*, còn bao nhiêu? So sánh với đề gốc. ($120\cdot(1-\frac14-\frac25)=42$).
- **(d)** Tổng quát: ban đầu có $a$ lít, lần $k$ dùng $\frac{p_k}{q_k}$ lượng còn lại, thì lượng còn lại là $a\prod\left(1-\frac{p_k}{q_k}\right)$.

---

## BÀI 3

**Đề:** $\triangle ABC$; trên nửa mặt phẳng bờ $AC$ không chứa $B$ lấy $D$ sao cho $AD=BC$, $CD=AB$.

### Hình vẽ (mô tả)

```
        D ________ C
         /       / 
        /       /  
       /_______/    
      A        B     (minh hoạ: B và D nằm khác phía đối với AC)
```

Cách vẽ chuẩn:
1. Vẽ $\triangle ABC$.
2. Vẽ cung tròn tâm $A$ bán kính $BC$ và cung tròn tâm $C$ bán kính $AB$ về phía không chứa $B$ (đối với đường thẳng $AC$). Giao điểm của hai cung là $D$.
3. Nối $AD$, $CD$.

Kết quả là tứ giác $ABCD$ có các cặp cạnh đối bằng nhau ($AB=CD$, $BC=AD$), với $AC$ là một đường chéo.

### Giả thiết – Kết luận

$$\textbf{GT}:\quad \begin{cases}\triangle ABC\\ D\ \text{và}\ B\ \text{khác phía đối với}\ AC\\ AD=BC,\ CD=AB\\ \widehat{BAC}=50^\circ,\ \widehat{ABC}=60^\circ\ \text{(cho câu c)}\end{cases}$$

$$\textbf{KL}:\quad \begin{cases}\text{a) }\triangle ABC=\triangle CDA\\ \text{b) }AB\parallel CD\\ \text{c) }\widehat{ACB}=?\end{cases}$$

---

### Câu a) Chứng minh $\triangle ABC=\triangle CDA$

**Cách 1 (c.c.c, cách duy nhất cần thiết):**

Xét $\triangle ABC$ và $\triangle CDA$ có:
- $AB=CD$ (giả thiết)
- $BC=DA$ (giả thiết)
- $AC$ là cạnh chung

$\Rightarrow \triangle ABC=\triangle CDA$ (c.c.c).

Thứ tự đỉnh tương ứng: $A\leftrightarrow C$, $B\leftrightarrow D$, $C\leftrightarrow A$. Từ đó có các cặp góc tương ứng:

$$\widehat{BAC}=\widehat{DCA},\quad \widehat{ABC}=\widehat{CDA},\quad \widehat{ACB}=\widehat{CAD}.$$

*(Câu a chỉ có một hướng chứng minh hợp lý vì giả thiết cho đúng ba cặp cạnh bằng nhau. Đây là điểm cần nhấn mạnh với học sinh: giả thiết nào thì trường hợp bằng nhau đó.)*

---

### Câu b) Chứng minh $AB\parallel CD$

**Cách 1 (từ tam giác bằng nhau, hai góc so le trong):**

Từ câu a, $\widehat{BAC}=\widehat{DCA}$ (hai góc tương ứng).

Hai góc này nằm ở vị trí so le trong tạo bởi cát tuyến $AC$ với hai đường thẳng $AB$ và $CD$ (vì $B$, $D$ nằm khác phía đối với $AC$).

$\Rightarrow AB\parallel CD$ (dấu hiệu nhận biết hai đường thẳng song song).

**Cách 2 (dùng tam giác khác, qua đường chéo $BD$):**

Nối $BD$. Xét $\triangle ABD$ và $\triangle CDB$:
- $AB=CD$ (gt), $AD=CB$ (gt), $BD$ chung

$\Rightarrow \triangle ABD=\triangle CDB$ (c.c.c) $\Rightarrow \widehat{ABD}=\widehat{CDB}$.

Hai góc này so le trong với cát tuyến $BD$, nên $AB\parallel CD$.

*(Cách này cần chú ý: phải lập luận $A$, $C$ nằm khác phía đối với $BD$. Với tứ giác lồi $ABCD$ thì điều này hiển nhiên.)*

**Cách 3 (phản chứng, mang tính tư duy logic):**

Giả sử $AB\not\parallel CD$. Khi đó đường thẳng $AB$ và $CD$ cắt nhau tại $O$. Vì $\widehat{BAC}=\widehat{DCA}$ (đã chứng minh) và đây là hai góc so le trong, nên trong tam giác $OAC$ có hai góc ở đáy $A$ và $C$ bằng nhau theo một cách "ngược chiều" (một góc nằm trong tam giác, góc kia nằm ngoài), dẫn đến tổng hai góc của tam giác $OAC$ vượt quá $180^\circ$, mâu thuẫn. Vậy $AB\parallel CD$.

*(Cách 3 chỉ mang tính giới thiệu phương pháp. Thực chất đây là chứng minh lại chính dấu hiệu nhận biết nên không cần thiết ở lớp 7.)*

---

### Câu c) Tính $\widehat{ACB}$ khi $\widehat{BAC}=50^\circ$, $\widehat{ABC}=60^\circ$

**Cách 1 (tổng ba góc của tam giác):**

Trong $\triangle ABC$:

$$\widehat{ACB}=180^\circ-\widehat{BAC}-\widehat{ABC}=180^\circ-50^\circ-60^\circ=70^\circ.$$

**Cách 2 (góc ngoài của tam giác):**

Trên tia đối của tia $CB$ lấy điểm $E$. Góc $\widehat{ACE}$ là góc ngoài tại đỉnh $C$ của $\triangle ABC$:

$$\widehat{ACE}=\widehat{BAC}+\widehat{ABC}=50^\circ+60^\circ=110^\circ.$$

$\widehat{ACB}$ kề bù với $\widehat{ACE}$, nên $\widehat{ACB}=180^\circ-110^\circ=70^\circ$.

**Cách 3 (qua tam giác bằng nhau $\triangle CDA$):**

Từ $\triangle ABC=\triangle CDA$: $\widehat{DCA}=50^\circ$, $\widehat{CDA}=60^\circ$. Trong $\triangle CDA$:

$$\widehat{CAD}=180^\circ-50^\circ-60^\circ=70^\circ.$$

Mà $\widehat{ACB}=\widehat{CAD}$ (hai góc tương ứng), nên $\widehat{ACB}=70^\circ$.

**Cách 4 (hai đường thẳng song song, hai góc trong cùng phía):**

Tương tự câu b, chứng minh được $AD\parallel BC$ (từ $\widehat{ACB}=\widehat{CAD}$, so le trong). Khi đó $AB\parallel CD$ với cát tuyến $BC$:

$$\widehat{ABC}+\widehat{BCD}=180^\circ\Rightarrow\widehat{BCD}=120^\circ.$$

Vì $AC$ nằm trong góc $BCD$ (do $ABCD$ là hình bình hành lồi nên đường chéo $AC$ nằm trong góc $C$):

$$\widehat{BCD}=\widehat{ACB}+\widehat{ACD}\Rightarrow\widehat{ACB}=120^\circ-50^\circ=70^\circ.$$

**Đáp số:** $\widehat{ACB}=70^\circ$.

### Nhận xét sư phạm

| Câu | Cách | Ưu điểm | Nhược điểm |
|---|---|---|---|
| a | c.c.c | Duy nhất, bám giả thiết | Dễ viết sai thứ tự đỉnh |
| b | 1 | Ngắn, đúng trọng tâm | Phải chỉ rõ cặp góc nào so le trong |
| b | 2 | Rèn cách vẽ thêm đường phụ | Dài hơn, cần lập luận về vị trí điểm |
| b | 3 | Phát triển tư duy phản chứng | Không cần thiết ở mức lớp 7 |
| c | 1 | Nhanh nhất, ít sai sót | Không tận dụng cấu hình bài toán |
| c | 2 | Củng cố tính chất góc ngoài | Cần vẽ thêm điểm $E$ |
| c | 3 | Khai thác tam giác bằng nhau | Vòng vo hơn so với cách 1 |
| 