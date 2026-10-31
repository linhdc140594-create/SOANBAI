# -*- coding: utf-8 -*-
"""
Script sinh Phiếu bài tập cuối tuần Toán 5 - TUAN_16 với 7 Mã đề (501 -> 507).
Chủ đề: Ôn tập phép tính với số thập phân -- Hình phẳng -- Tỉ số phần trăm (Cuối HK1)
Bài 4 và Bài 5: Chuẩn hóa theo chương trình Học kì 1 Lớp 5 (GDPT 2018).
Mỗi mã đề đúng 2 trang A4 in 2 mặt (Tổng 14 trang/file PDF).
"""

import os
import sys
import json
from shared_template import render_tex, render_markdown_answers, compile_and_verify

WEEK_NUM = 16
WEEK_TITLE = 'Ôn tập phép tính với số thập phân -- Hình phẳng -- Tỉ số phần trăm'

TOPICS = [
    'Bốn phép tính với số thập phân',
    'Tính giá trị biểu thức và tính hợp lý',
    'Khái niệm tỉ số của hai số',
    'Viết tỉ số dưới dạng tỉ số phần trăm',
    'Tìm tỉ số phần trăm của hai số',
    'Tìm giá trị phần trăm của một số',
    'Tìm một số khi biết giá trị phần trăm của nó',
    'Bài toán thực tế về tiền vốn, tiền lãi',
    'Ôn tập diện tích hình tam giác và hình thang',
    'Ôn tập chu vi và diện tích hình tròn',
    'Bài toán diện tích kết hợp tỉ số phần trăm',
    'Bài toán thực tế tỉ số phần trăm trong trường học'
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'grade5_bai4_bai5_data.json'), 'r', encoding='utf-8') as f:
    g5_bai4_bai5 = json.load(f)[str(WEEK_NUM)]

MA_DE_CONFIGS = [
    {
        'code': '501',
        'c1': ('Kết quả của phép tính $24{,}5 \\times 0{,}4$ là:', '$9{,}8$', '$98$', '$0{,}98$', '$9{,}08$', 'A'),
        'c2': ('Giá trị của biểu thức $15{,}6 + 4{,}4 \\times 2$ là:', '$40$', '$24{,}4$', '$25{,}4$', '$38{,}8$', 'B'),
        'c3': ('Tỉ số của hai số $3$ và $5$ viết dưới dạng phân số là:', '$\\dfrac{5}{3}$', '$3{,}5$', '$\\dfrac{3}{5}$', '$0{,}35$', 'C'),
        'c4': (r'Phân số $\dfrac{3}{4}$ viết dưới dạng tỉ số phần trăm là:', '$75\%$', '$60\%$', '$80\%$', '$70\%$', 'A'),
        'c5': ('Tỉ số phần trăm của $15$ và $60$ là:', '$20\%$', '$25\%$', '$30\%$', '$15\%$', 'B'),
        'c6': (r'$35\%$ của $120\,\text{kg}$ là:', r'$42\,\text{kg}$', r'$40\,\text{kg}$', r'$45\,\text{kg}$', r'$35\,\text{kg}$', 'A'),
        'c7': ('Biết $25\%$ của một số là $40$. Số đó là:', '$10$', '$80$', '$160$', '$100$', 'C'),
        'c8': ('Một cửa hàng nhập áo giá $200\,000$ đồng, bán lãi $20\%$. Số tiền lãi là:', '$40\,000$ đồng', '$50\,000$ đồng', '$30\,000$ đồng', '$20\,000$ đồng', 'A'),
        'c9': (r'Một hình thang có hai đáy $18\,\text{cm}$ và $12\,\text{cm}$, chiều cao $9\,\text{cm}$. Diện tích hình thang là:', r'$270\,\text{cm}^2$', r'$135\,\text{cm}^2$', r'$145\,\text{cm}^2$', r'$150\,\text{cm}^2$', 'B'),
        'c10': (r'Một hình tròn có đường kính $10\,\text{cm}$. Diện tích hình tròn đó là:', r'$314\,\text{cm}^2$', r'$157\,\text{cm}^2$', r'$78{,}5\,\text{cm}^2$', r'$31{,}4\,\text{cm}^2$', 'C'),
        'c11': (r'Mảnh đất $500\,\text{m}^2$, dành $40\%$ diện tích làm nhà, phần còn lại trồng cây. Diện tích đất trồng cây là:', r'$300\,\text{m}^2$', r'$200\,\text{m}^2$', r'$250\,\text{m}^2$', r'$350\,\text{m}^2$', 'A'),
        'c12': ('Lớp 5A có $40$ học sinh, trong đó có $24$ bạn nữ. Tỉ số phần trăm của số bạn nữ so với cả lớp là:', '$55\%$', '$60\%$', '$65\%$', '$50\%$', 'B'),
        'b1': ('$48{,}75 + 36{,}8$', '$95{,}2 - 47{,}85$', '$34{,}5 \\times 2{,}6$', '$117{,}6 : 4{,}2$'),
        'b1_ans': ('85{,}55', '47{,}35', '89{,}7', '28'),
        'b2': [('x \\times 4{,}5 + 12{,}5 = 39{,}5', 'x \\times 4{,}5 = 27', 'x = 6'),
               ('x : 3{,}6 - 4{,}5 = 8{,}5', 'x : 3{,}6 = 13', 'x = 46{,}8'),
               ('65 - x \\times 3{,}2 = 45{,}8', 'x \\times 3{,}2 = 19{,}2', 'x = 6'),
               ('(x + 15{,}5) : 4{,}5 = 8', 'x + 15{,}5 = 36', 'x = 20{,}5')],
        'b3': [(r'15 : 50', r'\%', '30'),
               (r'25\% \text{ của } 240\,\text{kg}', r'\text{kg}', '60'),
               (r'S_{\text{thang}} = (25 + 15) \times 10 : 2', r'\text{m}^2', '200'),
               (r'S_{\text{tròn}} = 5 \times 5 \times 3{,}14', r'\text{cm}^2', '78{,}5')]
    },
    {
        'code': '502',
        'c1': ('Kết quả của phép tính $32{,}5 \\times 0{,}4$ là:', '$13$', '$130$', '$1{,}3$', '$13{,}5$', 'A'),
        'c2': ('Giá trị của biểu thức $18{,}4 + 5{,}6 \\times 3$ là:', '$72$', '$35{,}2$', '$36{,}2$', '$34{,}2$', 'B'),
        'c3': ('Tỉ số của hai số $4$ và $7$ viết dưới dạng phân số là:', '$\\dfrac{7}{4}$', '$4{,}7$', '$\\dfrac{4}{7}$', '$0{,}47$', 'C'),
        'c4': (r'Phân số $\dfrac{4}{5}$ viết dưới dạng tỉ số phần trăm là:', '$80\%$', '$75\%$', '$85\%$', '$70\%$', 'A'),
        'c5': ('Tỉ số phần trăm của $18$ và $72$ là:', '$20\%$', '$25\%$', '$30\%$', '$15\%$', 'B'),
        'c6': (r'$45\%$ của $160\,\text{kg}$ là:', r'$72\,\text{kg}$', r'$70\,\text{kg}$', r'$75\,\text{kg}$', r'$68\,\text{kg}$', 'A'),
        'c7': ('Biết $30\%$ của một số là $45$. Số đó là:', '$15$', '$135$', '$150$', '$120$', 'C'),
        'c8': ('Một chiếc xe đạp giá $1\,500\,000$ đồng, được giảm giá $10\%$. Số tiền được giảm là:', '$150\,000$ đồng', '$100\,000$ đồng', '$200\,000$ đồng', '$120\,000$ đồng', 'A'),
        'c9': (r'Một hình thang có hai đáy $22\,\text{cm}$ và $14\,\text{cm}$, chiều cao $10\,\text{cm}$. Diện tích hình thang là:', r'$360\,\text{cm}^2$', r'$180\,\text{cm}^2$', r'$190\,\text{cm}^2$', r'$200\,\text{cm}^2$', 'B'),
        'c10': (r'Một hình tròn có đường kính $12\,\text{cm}$. Diện tích hình tròn đó là:', r'$452{,}16\,\text{cm}^2$', r'$226{,}08\,\text{cm}^2$', r'$113{,}04\,\text{cm}^2$', r'$37{,}68\,\text{cm}^2$', 'C'),
        'c11': (r'Mảnh đất $600\,\text{m}^2$, dành $35\%$ diện tích làm nhà, phần còn lại trồng hoa. Diện tích đất trồng hoa là:', r'$390\,\text{m}^2$', r'$210\,\text{m}^2$', r'$350\,\text{m}^2$', r'$400\,\text{m}^2$', 'A'),
        'c12': ('Lớp 5B có $35$ học sinh, trong đó có $21$ bạn đạt điểm tốt. Tỉ số phần trăm của bạn đạt điểm tốt là:', '$55\%$', '$60\%$', '$65\%$', '$50\%$', 'B'),
        'b1': ('$56{,}48 + 42{,}7$', '$104{,}5 - 58{,}75$', '$38{,}5 \\times 3{,}4$', '$136{,}8 : 3{,}6$'),
        'b1_ans': ('99{,}18', '45{,}75', '130{,}9', '38'),
        'b2': [('x \\times 5{,}2 + 15{,}6 = 57{,}2', 'x \\times 5{,}2 = 41{,}6', 'x = 8'),
               ('x : 4{,}5 - 6{,}2 = 9{,}8', 'x : 4{,}5 = 16', 'x = 72'),
               ('78 - x \\times 4{,}5 = 46{,}5', 'x \\times 4{,}5 = 31{,}5', 'x = 7'),
               ('(x + 18{,}5) : 5{,}2 = 7', 'x + 18{,}5 = 36{,}4', 'x = 17{,}9')],
        'b3': [(r'24 : 80', r'\%', '30'),
               (r'35\% \text{ của } 200\,\text{kg}', r'\text{kg}', '70'),
               (r'S_{\text{thang}} = (28 + 16) \times 12 : 2', r'\text{m}^2', '264'),
               (r'S_{\text{tròn}} = 6 \times 6 \times 3{,}14', r'\text{cm}^2', '113{,}04')]
    },
    {
        'code': '503',
        'c1': ('Kết quả của phép tính $45{,}5 \\times 0{,}4$ là:', '$18{,}2$', '$182$', '$1{,}82$', '$18{,}02$', 'A'),
        'c2': ('Giá trị của biểu thức $24{,}5 + 6{,}5 \\times 4$ là:', '$124$', '$50{,}5$', '$51{,}5$', '$49{,}5$', 'B'),
        'c3': ('Tỉ số của hai số $5$ và $8$ viết dưới dạng phân số là:', '$\\dfrac{8}{5}$', '$5{,}8$', '$\\dfrac{5}{8}$', '$0{,}58$', 'C'),
        'c4': (r'Phân số $\dfrac{1}{4}$ viết dưới dạng tỉ số phần trăm là:', '$25\%$', '$20\%$', '$30\%$', '$15\%$', 'A'),
        'c5': ('Tỉ số phần trăm của $24$ và $80$ là:', '$25\%$', '$30\%$', '$35\%$', '$20\%$', 'B'),
        'c6': (r'$55\%$ của $200\,\text{kg}$ là:', r'$110\,\text{kg}$', r'$100\,\text{kg}$', r'$115\,\text{kg}$', r'$105\,\text{kg}$', 'A'),
        'c7': ('Biết $40\%$ của một số là $60$. Số đó là:', '$24$', '$120$', '$150$', '$100$', 'C'),
        'c8': ('Gửi tiết kiệm $10\,000\,000$ đồng với lãi suất $0{,}5\%$/tháng. Tiền lãi một tháng là:', '$50\,000$ đồng', '$500\,000$ đồng', '$5\,000$ đồng', '$20\,000$ đồng', 'A'),
        'c9': (r'Một hình thang có hai đáy $24\,\text{cm}$ và $16\,\text{cm}$, chiều cao $12\,\text{cm}$. Diện tích hình thang là:', r'$480\,\text{cm}^2$', r'$240\,\text{cm}^2$', r'$250\,\text{cm}^2$', r'$260\,\text{cm}^2$', 'B'),
        'c10': (r'Một hình tròn có đường kính $14\,\text{cm}$. Diện tích hình tròn đó là:', r'$615{,}44\,\text{cm}^2$', r'$307{,}72\,\text{cm}^2$', r'$153{,}86\,\text{cm}^2$', r'$43{,}96\,\text{cm}^2$', 'C'),
        'c11': (r'Mảnh đất $750\,\text{m}^2$, dành $30\%$ diện tích làm nhà, phần còn lại đào ao. Diện tích ao là:', r'$525\,\text{m}^2$', r'$225\,\text{m}^2$', r'$500\,\text{m}^2$', r'$550\,\text{m}^2$', 'A'),
        'c12': ('Một đàn gà có $80$ con, trong đó có $52$ con gà mái. Tỉ số phần trăm của gà mái trong đàn là:', '$60\%$', '$65\%$', '$70\%$', '$55\%$', 'B'),
        'b1': ('$65{,}35 + 48{,}9$', '$118{,}4 - 69{,}75$', '$42{,}5 \\times 2{,}8$', '$159{,}8 : 4{,}7$'),
        'b1_ans': ('114{,}25', '48{,}65', '119', '34'),
        'b2': [('x \\times 6{,}4 + 18{,}2 = 69{,}4', 'x \\times 6{,}4 = 51{,}2', 'x = 8'),
               ('x : 5{,}2 - 7{,}5 = 10{,}5', 'x : 5{,}2 = 18', 'x = 93{,}6'),
               ('86 - x \\times 5{,}4 = 48{,}2', 'x \\times 5{,}4 = 37{,}8', 'x = 7'),
               ('(x + 22{,}5) : 6{,}4 = 6', 'x + 22{,}5 = 38{,}4', 'x = 15{,}9')],
        'b3': [(r'32 : 80', r'\%', '40'),
               (r'45\% \text{ của } 300\,\text{kg}', r'\text{kg}', '135'),
               (r'S_{\text{thang}} = (30 + 20) \times 14 : 2', r'\text{m}^2', '350'),
               (r'S_{\text{tròn}} = 7 \times 7 \times 3{,}14', r'\text{cm}^2', '153{,}86')]
    },
    {
        'code': '504',
        'c1': ('Kết quả của phép tính $52{,}5 \\times 0{,}4$ là:', '$21$', '$210$', '$2{,}1$', '$21{,}5$', 'A'),
        'c2': ('Giá trị của biểu thức $32{,}8 + 7{,}2 \\times 3$ là:', '$120$', '$54{,}4$', '$55{,}4$', '$53{,}4$', 'B'),
        'c3': ('Tỉ số của hai số $6$ và $11$ viết dưới dạng phân số là:', '$\\dfrac{11}{6}$', '$6{,}11$', '$\\dfrac{6}{11}$', '$0{,}611$', 'C'),
        'c4': (r'Phân số $\dfrac{1}{2}$ viết dưới dạng tỉ số phần trăm là:', '$50\%$', '$20\%$', '$40\%$', '$25\%$', 'A'),
        'c5': ('Tỉ số phần trăm của $28$ và $70$ là:', '$35\%$', '$40\%$', '$45\%$', '$30\%$', 'B'),
        'c6': (r'$65\%$ của $240\,\text{kg}$ là:', r'$156\,\text{kg}$', r'$150\,\text{kg}$', r'$160\,\text{kg}$', r'$152\,\text{kg}$', 'A'),
        'c7': ('Biết $50\%$ của một số là $75$. Số đó là:', '$37{,}5$', '$125$', '$150$', '$100$', 'C'),
        'c8': ('Một chiếc tivi giá $8\,000\,000$ đồng, được giảm giá $15\%$. Số tiền được giảm là:', '$1\,200\,000$ đồng', '$1\,000\,000$ đồng', '$1\,500\,000$ đồng', '$800\,000$ đồng', 'A'),
        'c9': (r'Một hình thang có hai đáy $26\,\text{cm}$ và $18\,\text{cm}$, chiều cao $14\,\text{cm}$. Diện tích hình thang là:', r'$616\,\text{cm}^2$', r'$308\,\text{cm}^2$', r'$320\,\text{cm}^2$', r'$330\,\text{cm}^2$', 'B'),
        'c10': (r'Một hình tròn có đường kính $16\,\text{cm}$. Diện tích hình tròn đó là:', r'$803{,}84\,\text{cm}^2$', r'$401{,}92\,\text{cm}^2$', r'$200{,}96\,\text{cm}^2$', r'$50{,}24\,\text{cm}^2$', 'C'),
        'c11': (r'Mảnh đất $800\,\text{m}^2$, dành $45\%$ diện tích làm nhà, phần còn lại làm sân vườn. Diện tích sân vườn là:', r'$440\,\text{m}^2$', r'$360\,\text{m}^2$', r'$450\,\text{m}^2$', r'$420\,\text{m}^2$', 'A'),
        'c12': ('Một trang trại nuôi $120$ con lợn, đã tiêm phòng cho $84$ con. Tỉ số phần trăm số lợn đã tiêm là:', '$65\%$', '$70\%$', '$75\%$', '$60\%$', 'B'),
        'b1': ('$74{,}65 + 53{,}8$', '$126{,}2 - 78{,}45$', '$48{,}5 \\times 3{,}2$', '$187{,}2 : 5{,}2$'),
        'b1_ans': ('128{,}45', '47{,}75', '155{,}2', '36'),
        'b2': [('x \\times 7{,}2 + 24{,}6 = 89{,}4', 'x \\times 7{,}2 = 64{,}8', 'x = 9'),
               ('x : 6{,}4 - 8{,}5 = 11{,}5', 'x : 6{,}4 = 20', 'x = 128'),
               ('95 - x \\times 6{,}2 = 51{,}6', 'x \\times 6{,}2 = 43{,}4', 'x = 7'),
               ('(x + 25{,}5) : 7{,}2 = 5', 'x + 25{,}5 = 36', 'x = 10{,}5')],
        'b3': [(r'35 : 70', r'\%', '50'),
               (r'60\% \text{ của } 250\,\text{kg}', r'\text{kg}', '150'),
               (r'S_{\text{thang}} = (34 + 22) \times 15 : 2', r'\text{m}^2', '420'),
               (r'S_{\text{tròn}} = 8 \times 8 \times 3{,}14', r'\text{cm}^2', '200{,}96')]
    },
    {
        'code': '505',
        'c1': ('Kết quả của phép tính $64{,}5 \\times 0{,}4$ là:', '$25{,}8$', '$258$', '$2{,}58$', '$25{,}08$', 'A'),
        'c2': ('Giá trị của biểu thức $41{,}5 + 8{,}5 \\times 3$ là:', '$150$', '$67$', '$68$', '$66$', 'B'),
        'c3': ('Tỉ số của hai số $7$ và $12$ viết dưới dạng phân số là:', '$\\dfrac{12}{7}$', '$7{,}12$', '$\\dfrac{7}{12}$', '$0{,}712$', 'C'),
        'c4': (r'Phân số $\dfrac{3}{5}$ viết dưới dạng tỉ số phần trăm là:', '$60\%$', '$50\%$', '$70\%$', '$55\%$', 'A'),
        'c5': ('Tỉ số phần trăm của $36$ và $90$ là:', '$35\%$', '$40\%$', '$45\%$', '$30\%$', 'B'),
        'c6': (r'$75\%$ của $280\,\text{kg}$ là:', r'$210\,\text{kg}$', r'$200\,\text{kg}$', r'$220\,\text{kg}$', r'$205\,\text{kg}$', 'A'),
        'c7': ('Biết $60\%$ của một số là $90$. Số đó là:', '$54$', '$120$', '$150$', '$100$', 'C'),
        'c8': ('Một cửa hàng nhập quạt máy giá $400\,000$ đồng, bán lãi $15\%$. Số tiền lãi là:', '$60\,000$ đồng', '$50\,000$ đồng', '$70\,000$ đồng', '$45\,000$ đồng', 'A'),
        'c9': (r'Một hình thang có hai đáy $28\,\text{cm}$ và $20\,\text{cm}$, chiều cao $15\,\text{cm}$. Diện tích hình thang là:', r'$720\,\text{cm}^2$', r'$360\,\text{cm}^2$', r'$380\,\text{cm}^2$', r'$390\,\text{cm}^2$', 'B'),
        'c10': (r'Một hình tròn có đường kính $18\,\text{cm}$. Diện tích hình tròn đó là:', r'$1\\,017{,}36\,\text{cm}^2$', r'$508{,}68\,\text{cm}^2$', r'$254{,}34\,\text{cm}^2$', r'$56{,}52\,\text{cm}^2$', 'C'),
        'c11': (r'Mảnh đất $900\,\text{m}^2$, dành $35\%$ diện tích làm nhà, phần còn lại trồng cây ăn quả. Diện tích trồng cây là:', r'$585\,\text{m}^2$', r'$315\,\text{m}^2$', r'$600\,\text{m}^2$', r'$550\,\text{m}^2$', 'A'),
        'c12': ('Khối 5 có $150$ học sinh, trong đó có $105$ bạn tham gia câu lạc bộ. Tỉ số phần trăm tham gia là:', '$65\%$', '$70\%$', '$75\%$', '$60\%$', 'B'),
        'b1': ('$82{,}75 + 61{,}6$', '$135{,}4 - 86{,}75$', '$52{,}5 \\times 2{,}8$', '$204 : 4{,}8$'),
        'b1_ans': ('144{,}35', '48{,}65', '147', '42{,}5'),
        'b2': [('x \\times 8{,}2 + 28{,}4 = 94', 'x \\times 8{,}2 = 65{,}6', 'x = 8'),
               ('x : 7{,}5 - 9{,}2 = 12{,}8', 'x : 7{,}5 = 22', 'x = 165'),
               ('108 - x \\times 7{,}5 = 55{,}5', 'x \\times 7{,}5 = 52{,}5', 'x = 7'),
               ('(x + 28{,}5) : 8{,}2 = 5', 'x + 28{,}5 = 41', 'x = 12{,}5')],
        'b3': [(r'45 : 90', r'\%', '50'),
               (r'75\% \text{ của } 320\,\text{kg}', r'\text{kg}', '240'),
               (r'S_{\text{thang}} = (36 + 24) \times 16 : 2', r'\text{m}^2', '480'),
               (r'S_{\text{tròn}} = 9 \times 9 \times 3{,}14', r'\text{cm}^2', '254{,}34')]
    },
    {
        'code': '506',
        'c1': ('Kết quả của phép tính $72{,}5 \\times 0{,}4$ là:', '$29$', '$290$', '$2{,}9$', '$29{,}5$', 'A'),
        'c2': ('Giá trị của biểu thức $48{,}6 + 9{,}4 \\times 3$ là:', '$174$', '$76{,}8$', '$77{,}8$', '$75{,}8$', 'B'),
        'c3': ('Tỉ số của hai số $8$ và $15$ viết dưới dạng phân số là:', '$\\dfrac{15}{8}$', '$8{,}15$', '$\\dfrac{8}{15}$', '$0{,}815$', 'C'),
        'c4': (r'Phân số $\dfrac{7}{10}$ viết dưới dạng tỉ số phần trăm là:', '$70\%$', '$60\%$', '$75\%$', '$80\%$', 'A'),
        'c5': ('Tỉ số phần trăm của $45$ và $150$ là:', '$25\%$', '$30\%$', '$35\%$', '$20\%$', 'B'),
        'c6': (r'$80\%$ của $350\,\text{kg}$ là:', r'$280\,\text{kg}$', r'$270\,\text{kg}$', r'$290\,\text{kg}$', r'$275\,\text{kg}$', 'A'),
        'c7': ('Biết $75\%$ của một số là $120$. Số đó là:', '$90$', '$150$', '$160$', '$140$', 'C'),
        'c8': ('Một đôi giày giá $600\,000$ đồng, được giảm giá $20\%$. Số tiền được giảm là:', '$120\,000$ đồng', '$100\,000$ đồng', '$150\,000$ đồng', '$80\,000$ đồng', 'A'),
        'c9': (r'Một hình thang có hai đáy $32\,\text{cm}$ và $22\,\text{cm}$, chiều cao $16\,\text{cm}$. Diện tích hình thang là:', r'$864\,\text{cm}^2$', r'$432\,\text{cm}^2$', r'$440\,\text{cm}^2$', r'$450\,\text{cm}^2$', 'B'),
        'c10': (r'Một hình tròn có đường kính $20\,\text{cm}$. Diện tích hình tròn đó là:', r'$1\\,256\,\text{cm}^2$', r'$628\,\text{cm}^2$', r'$314\,\text{cm}^2$', r'$62{,}8\,\text{cm}^2$', 'C'),
        'c11': (r'Mảnh đất $1\\,000\,\text{m}^2$, dành $30\%$ diện tích làm nhà, phần còn lại làm sân bóng mini. Diện tích sân bóng là:', r'$700\,\text{m}^2$', r'$300\,\text{m}^2$', r'$650\,\text{m}^2$', r'$750\,\text{m}^2$', 'A'),
        'c12': ('Một công ty có $200$ nhân viên, trong đó có $130$ nhân viên nam. Tỉ số phần trăm nhân viên nam là:', '$60\%$', '$65\%$', '$70\%$', '$55\%$', 'B'),
        'b1': ('$91{,}65 + 68{,}8$', '$146{,}5 - 94{,}75$', '$58{,}5 \\times 3{,}2$', '$228 : 4{,}8$'),
        'b1_ans': ('160{,}45', '51{,}75', '187{,}2', '47{,}5'),
        'b2': [('x \\times 9{,}2 + 31{,}6 = 105{,}2', 'x \\times 9{,}2 = 73{,}6', 'x = 8'),
               ('x : 8{,}4 - 10{,}5 = 14{,}5', 'x : 8{,}4 = 25', 'x = 210'),
               ('125 - x \\times 8{,}5 = 65{,}5', 'x \\times 8{,}5 = 59{,}5', 'x = 7'),
               ('(x + 32{,}5) : 9{,}2 = 5', 'x + 32{,}5 = 46', 'x = 13{,}5')],
        'b3': [(r'56 : 140', r'\%', '40'),
               (r'80\% \text{ của } 400\,\text{kg}', r'\text{kg}', '320'),
               (r'S_{\text{thang}} = (40 + 26) \times 18 : 2', r'\text{m}^2', '594'),
               (r'S_{\text{tròn}} = 10 \times 10 \times 3{,}14', r'\text{cm}^2', '314')]
    },
    {
        'code': '507',
        'c1': ('Kết quả của phép tính $84{,}5 \\times 0{,}4$ là:', '$33{,}8$', '$338$', '$3{,}38$', '$33{,}08$', 'A'),
        'c2': ('Giá trị của biểu thức $54{,}8 + 11{,}2 \\times 3$ là:', '$198$', '$88{,}4$', '$89{,}4$', '$87{,}4$', 'B'),
        'c3': ('Tỉ số của hai số $9$ và $16$ viết dưới dạng phân số là:', '$\\dfrac{16}{9}$', '$9{,}16$', '$\\dfrac{9}{16}$', '$0{,}916$', 'C'),
        'c4': (r'Phân số $\dfrac{9}{10}$ viết dưới dạng tỉ số phần trăm là:', '$90\%$', '$80\%$', '$85\%$', '$95\%$', 'A'),
        'c5': ('Tỉ số phần trăm của $54$ và $180$ là:', '$25\%$', '$30\%$', '$35\%$', '$20\%$', 'B'),
        'c6': (r'$85\%$ của $400\,\text{kg}$ là:', r'$340\,\text{kg}$', r'$330\,\text{kg}$', r'$350\,\text{kg}$', r'$335\,\text{kg}$', 'A'),
        'c7': ('Biết $80\%$ của một số là $160$. Số đó là:', '$128$', '$180$', '$200$', '$190$', 'C'),
        'c8': ('Một người bán hàng lãi $12\%$ trên vốn $5\,000\,000$ đồng. Số tiền lãi là:', '$600\,000$ đồng', '$500\,000$ đồng', '$700\,000$ đồng', '$550\,000$ đồng', 'A'),
        'c9': (r'Một hình thang có hai đáy $36\,\text{cm}$ và $24\,\text{cm}$, chiều cao $18\,\text{cm}$. Diện tích hình thang là:', r'$1\\,080\,\text{cm}^2$', r'$540\,\text{cm}^2$', r'$550\,\text{cm}^2$', r'$560\,\text{cm}^2$', 'B'),
        'c10': (r'Một hình tròn có đường kính $24\,\text{cm}$. Diện tích hình tròn đó là:', r'$1\\,808{,}64\,\text{cm}^2$', r'$904{,}32\,\text{cm}^2$', r'$452{,}16\,\text{cm}^2$', r'$75{,}36\,\text{cm}^2$', 'C'),
        'c11': (r'Mảnh đất $1\\,200\,\text{m}^2$, dành $25\%$ diện tích làm nhà, phần còn lại trồng cây cảnh. Diện tích trồng cây cảnh là:', r'$900\,\text{m}^2$', r'$300\,\text{m}^2$', r'$850\,\text{m}^2$', r'$950\,\text{m}^2$', 'A'),
        'c12': ('Một cửa hàng nhập $250$ chiếc bút, đã bán được $175$ chiếc. Tỉ số phần trăm số bút đã bán là:', '$65\%$', '$70\%$', '$75\%$', '$60\%$', 'B'),
        'b1': ('$98{,}75 + 74{,}6$', '$158{,}2 - 96{,}85$', '$64{,}5 \\times 3{,}4$', '$255 : 5{,}1$'),
        'b1_ans': ('173{,}35', '61{,}35', '219{,}3', '50'),
        'b2': [('x \\times 9{,}5 + 35{,}8 = 121{,}3', 'x \\times 9{,}5 = 85{,}5', 'x = 9'),
               ('x : 9{,}2 - 12{,}5 = 17{,}5', 'x : 9{,}2 = 30', 'x = 276'),
               ('140 - x \\times 9{,}2 = 75{,}6', 'x \\times 9{,}2 = 64{,}4', 'x = 7'),
               ('(x + 36{,}5) : 9{,}5 = 5', 'x + 36{,}5 = 47{,}5', 'x = 11')],
        'b3': [(r'72 : 180', r'\%', '40'),
               (r'85\% \text{ của } 500\,\text{kg}', r'\text{kg}', '425'),
               (r'S_{\text{thang}} = (45 + 30) \times 20 : 2', r'\text{m}^2', '750'),
               (r'S_{\text{tròn}} = 12 \times 12 \times 3{,}14', r'\text{cm}^2', '452{,}16')]
    }
]

MA_DE_LIST = []
for idx, cfg in enumerate(MA_DE_CONFIGS):
    item = {
        'ma_de': cfg['code'],
        'tn': [
            cfg['c1'], cfg['c2'], cfg['c3'], cfg['c4'],
            cfg['c5'], cfg['c6'], cfg['c7'], cfg['c8'],
            cfg['c9'], cfg['c10'], cfg['c11'], cfg['c12']
        ],
        'bai1': cfg['b1'],
        'bai1_ans': cfg['b1_ans'],
        'bai2': cfg['b2'],
        'bai3': cfg['b3'],
        'bai4': g5_bai4_bai5[idx]['bai4'],
        'bai5': g5_bai4_bai5[idx]['bai5']
    }
    MA_DE_LIST.append(item)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base_dir, f'TUAN_{WEEK_NUM:02d}')
    os.makedirs(out_dir, exist_ok=True)

    tex_content = render_tex(WEEK_NUM, WEEK_TITLE, MA_DE_LIST, grade=5)
    tex_path = os.path.join(out_dir, f'Phieu_Bai_Tap_Tuan_{WEEK_NUM:02d}_Toan5.tex')
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print('Wrote:', tex_path)

    md_content = render_markdown_answers(WEEK_NUM, WEEK_TITLE, TOPICS, MA_DE_LIST, grade=5)
    md_path = os.path.join(out_dir, 'DAP_AN_VA_THANG_DIEM.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print('Wrote:', md_path)

    compile_and_verify(WEEK_NUM, base_dir)

if __name__ == '__main__':
    main()
