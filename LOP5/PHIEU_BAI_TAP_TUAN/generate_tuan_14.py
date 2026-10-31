# -*- coding: utf-8 -*-
"""
Script sinh Phiếu bài tập cuối tuần Toán 5 - TUAN_14 với 7 Mã đề (501 -> 507).
Chủ đề: Đường tròn -- Chu vi và diện tích hình tròn -- Thực hành hình phẳng
Bài 4 và Bài 5: Chuẩn hóa theo chương trình Học kì 1 Lớp 5 (GDPT 2018).
Mỗi mã đề đúng 2 trang A4 in 2 mặt (Tổng 14 trang/file PDF).
"""

import os
import sys
import json
from shared_template import render_tex, render_markdown_answers, compile_and_verify

WEEK_NUM = 14
WEEK_TITLE = 'Đường tròn -- Chu vi và diện tích hình tròn -- Thực hành hình phẳng'

TOPICS = [
    'Nhận biết tâm, bán kính, đường kính của hình tròn',
    'Công thức tính chu vi hình tròn',
    'Tính chu vi hình tròn khi biết bán kính',
    'Tính chu vi hình tròn khi biết đường kính',
    'Tìm bán kính hoặc đường kính khi biết chu vi',
    'Công thức tính diện tích hình tròn',
    'Tính diện tích hình tròn khi biết bán kính',
    'Tính diện tích hình tròn khi biết đường kính',
    'Bài toán bánh xe lăn: Tính quãng đường sau N vòng',
    'Bài toán bánh xe lăn: Tính số vòng trên quãng đường',
    'Diện tích hình vành khuyên (giữa hai hình tròn)',
    'Diện tích phần tô đậm ghép giữa hình vuông và hình tròn'
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'grade5_bai4_bai5_data.json'), 'r', encoding='utf-8') as f:
    g5_bai4_bai5 = json.load(f)[str(WEEK_NUM)]

MA_DE_CONFIGS = [
    {
        'code': '501',
        'c1': ('Trong một hình tròn, độ dài đường kính gấp mấy lần bán kính:', '$2$ lần', '$3$ lần', '$4$ lần', 'Bằng bán kính', 'A'),
        'c2': ('Công thức tính chu vi hình tròn có bán kính $r$ là:', '$C = r \\times 3{,}14$', '$C = r \\times 2 \\times 3{,}14$', '$C = r \\times r \\times 3{,}14$', '$C = r \\times 4 \\times 3{,}14$', 'B'),
        'c3': (r'Chu vi hình tròn có bán kính $5\,\text{cm}$ là:', r'$15{,}7\,\text{cm}$', r'$62{,}8\,\text{cm}$', r'$31{,}4\,\text{cm}$', r'$78{,}5\,\text{cm}$', 'C'),
        'c4': (r'Chu vi hình tròn có đường kính $6\,\text{dm}$ là:', r'$18{,}84\,\text{dm}$', r'$37{,}68\,\text{dm}$', r'$28{,}26\,\text{dm}$', r'$113{,}04\,\text{dm}$', 'A'),
        'c5': (r'Một hình tròn có chu vi $12{,}56\,\text{m}$. Bán kính của hình tròn đó là:', r'$4\,\text{m}$', r'$2\,\text{m}$', r'$1\,\text{m}$', r'$3\,\text{m}$', 'B'),
        'c6': ('Công thức tính diện tích hình tròn có bán kính $r$ là:', '$S = r \\times r \\times 3{,}14$', '$S = r \\times 2 \\times 3{,}14$', '$S = d \\times 3{,}14$', '$S = r \\times 3{,}14$', 'A'),
        'c7': (r'Diện tích hình tròn có bán kính $4\,\text{cm}$ là:', r'$25{,}12\,\text{cm}^2$', r'$50{,}24\,\text{cm}^2$', r'$12{,}56\,\text{cm}^2$', r'$100{,}48\,\text{cm}^2$', 'B'),
        'c8': (r'Diện tích hình tròn có đường kính $10\,\text{dm}$ là:', r'$314\,\text{dm}^2$', r'$157\,\text{dm}^2$', r'$78{,}5\,\text{dm}^2$', r'$31{,}4\,\text{dm}^2$', 'C'),
        'c9': (r'Một bánh xe đạp có đường kính $0{,}65\,\text{m}$. Khi bánh xe lăn $100\,\text{vòng}$ thì đi được quãng đường là:', r'$204{,}1\,\text{m}$', r'$130\,\text{m}$', r'$408{,}2\,\text{m}$', r'$200\,\text{m}$', 'A'),
        'c10': (r'Một bánh xe có chu vi $2\,\text{m}$. Bánh xe đó phải lăn bao nhiêu vòng để đi hết quãng đường $500\,\text{m}$:', r'$200\,\text{vòng}$', r'$250\,\text{vòng}$', r'$300\,\text{vòng}$', r'$150\,\text{vòng}$', 'B'),
        'c11': (r'Một bồn hoa hình tròn bán kính $3\,\text{m}$. Người ta làm đường đi rộng $1\,\text{m}$ bao quanh. Diện tích con đường đó là:', r'$21{,}98\,\text{m}^2$', r'$28{,}26\,\text{m}^2$', r'$50{,}24\,\text{m}^2$', r'$18{,}84\,\text{m}^2$', 'A'),
        'c12': (r'Một hình vuông cạnh $10\,\text{cm}$, bên trong vẽ hình tròn nội tiếp đường kính $10\,\text{cm}$. Diện tích phần ngoài hình tròn là:', r'$20\,\text{cm}^2$', r'$21{,}5\,\text{cm}^2$', r'$25\,\text{cm}^2$', r'$18{,}5\,\text{cm}^2$', 'B'),
        'b1': ('$35{,}6 \\times 3{,}14$', '$18{,}84 : 3{,}14$', '$50{,}24 : 3{,}14$', '$78{,}5 - 28{,}26$'),
        'b1_ans': ('111{,}784', '6', '16', '50{,}24'),
        'b2': [('x \\times 3{,}14 = 31{,}4', 'x = 31{,}4 : 3{,}14', 'x = 10'),
               ('x : 3{,}14 = 8', 'x = 8 \\times 3{,}14', 'x = 25{,}12'),
               ('x \\times 6{,}28 = 37{,}68', 'x = 37{,}68 : 6{,}28', 'x = 6'),
               ('(x + 4{,}5) \\times 3{,}14 = 31{,}4', 'x + 4{,}5 = 10', 'x = 5{,}5')],
        'b3': [(r'C = 2 \times 6 \times 3{,}14', r'\text{cm}', '37{,}68'),
               (r'C = 12 \times 3{,}14', r'\text{dm}', '37{,}68'),
               (r'S = 6 \times 6 \times 3{,}14', r'\text{cm}^2', '113{,}04'),
               (r'S = 10 \times 10 \times 3{,}14', r'\text{m}^2', '314')]
    },
    {
        'code': '502',
        'c1': ('Nếu bán kính hình tròn là $r$ thì đường kính $d$ bằng:', '$d = 2 \\times r$', '$d = r : 2$', '$d = r \\times r$', '$d = r + 2$', 'A'),
        'c2': ('Chu vi hình tròn có đường kính $d$ tính bằng công thức:', '$C = d \\times 2 \\times 3{,}14$', '$C = d \\times 3{,}14$', '$C = d \\times d \\times 3{,}14$', '$C = d : 3{,}14$', 'B'),
        'c3': (r'Chu vi hình tròn có bán kính $4\,\text{cm}$ là:', r'$12{,}56\,\text{cm}$', r'$50{,}24\,\text{cm}$', r'$25{,}12\,\text{cm}$', r'$37{,}68\,\text{cm}$', 'C'),
        'c4': (r'Chu vi hình tròn có đường kính $8\,\text{dm}$ là:', r'$25{,}12\,\text{dm}$', r'$50{,}24\,\text{dm}$', r'$16{,}28\,\text{dm}$', r'$75{,}36\,\text{dm}$', 'A'),
        'c5': (r'Một hình tròn có chu vi $18{,}84\,\text{m}$. Bán kính của hình tròn đó là:', r'$6\,\text{m}$', r'$3\,\text{m}$', r'$2\,\text{m}$', r'$4\,\text{m}$', 'B'),
        'c6': ('Nếu bán kính hình tròn gấp lên 2 lần thì diện tích hình tròn:', 'Gấp lên 4 lần', 'Gấp lên 2 lần', 'Gấp lên 8 lần', 'Không đổi', 'A'),
        'c7': (r'Diện tích hình tròn có bán kính $5\,\text{cm}$ là:', r'$31{,}4\,\text{cm}^2$', r'$78{,}5\,\text{cm}^2$', r'$157\,\text{cm}^2$', r'$25\,\text{cm}^2$', 'B'),
        'c8': (r'Diện tích hình tròn có đường kính $8\,\text{dm}$ là:', r'$200{,}96\,\text{dm}^2$', r'$100{,}48\,\text{dm}^2$', r'$50{,}24\,\text{dm}^2$', r'$25{,}12\,\text{dm}^2$', 'C'),
        'c9': (r'Một bánh xe đạp có đường kính $0{,}6\,\text{m}$. Khi bánh xe lăn $200\,\text{vòng}$ thì đi được quãng đường là:', r'$376{,}8\,\text{m}$', r'$188{,}4\,\text{m}$', r'$753{,}6\,\text{m}$', r'$360\,\text{m}$', 'A'),
        'c10': (r'Một bánh xe có chu vi $1{,}5\,\text{m}$. Bánh xe đó phải lăn bao nhiêu vòng để đi hết quãng đường $450\,\text{m}$:', r'$250\,\text{vòng}$', r'$300\,\text{vòng}$', r'$350\,\text{vòng}$', r'$200\,\text{vòng}$', 'B'),
        'c11': (r'Một cái giếng hình tròn có bán kính $0{,}7\,\text{m}$. Người ta xây thành giếng rộng $0{,}3\,\text{m}$. Diện tích thành giếng là:', r'$1{,}6014\,\text{m}^2$', r'$3{,}14\,\text{m}^2$', r'$1{,}5386\,\text{m}^2$', r'$2{,}12\,\text{m}^2$', 'A'),
        'c12': (r'Một hình vuông cạnh $8\,\text{cm}$, bên trong vẽ hình tròn nội tiếp đường kính $8\,\text{cm}$. Diện tích phần ngoài hình tròn là:', r'$12\,\text{cm}^2$', r'$13{,}76\,\text{cm}^2$', r'$15\,\text{cm}^2$', r'$14{,}5\,\text{cm}^2$', 'B'),
        'b1': ('$42{,}8 \\times 3{,}14$', '$25{,}12 : 3{,}14$', '$78{,}5 : 3{,}14$', '$113{,}04 - 50{,}24$'),
        'b1_ans': ('134{,}392', '8', '25', '62{,}8'),
        'b2': [('x \\times 3{,}14 = 47{,}1', 'x = 47{,}1 : 3{,}14', 'x = 15'),
               ('x : 3{,}14 = 10', 'x = 10 \\times 3{,}14', 'x = 31{,}4'),
               ('x \\times 6{,}28 = 50{,}24', 'x = 50{,}24 : 6{,}28', 'x = 8'),
               ('(x + 6{,}5) \\times 3{,}14 = 47{,}1', 'x + 6{,}5 = 15', 'x = 8{,}5')],
        'b3': [(r'C = 2 \times 8 \times 3{,}14', r'\text{cm}', '50{,}24'),
               (r'C = 14 \times 3{,}14', r'\text{dm}', '43{,}96'),
               (r'S = 7 \times 7 \times 3{,}14', r'\text{cm}^2', '153{,}86'),
               (r'S = 12 \times 12 \times 3{,}14', r'\text{m}^2', '452{,}16')]
    },
    {
        'code': '503',
        'c1': ('Tất cả các bán kính của một hình tròn đều:', 'Bằng nhau', 'Khác nhau', 'Vuông góc với nhau', 'Song song với nhau', 'A'),
        'c2': ('Số $3{,}14$ thường được dùng trong công thức tính chu vi và diện tích hình tròn là giá trị gần đúng của số:', 'Phi ($\\phi$)', 'Pi ($\\pi$)', 'Alpha ($\\alpha$)', 'Beta ($\\beta$)', 'B'),
        'c3': (r'Chu vi hình tròn có bán kính $6\,\text{cm}$ là:', r'$18{,}84\,\text{cm}$', r'$75{,}36\,\text{cm}$', r'$37{,}68\,\text{cm}$', r'$113{,}04\,\text{cm}$', 'C'),
        'c4': (r'Chu vi hình tròn có đường kính $10\,\text{dm}$ là:', r'$31{,}4\,\text{dm}$', r'$62{,}8\,\text{dm}$', r'$78{,}5\,\text{dm}$', r'$314\,\text{dm}$', 'A'),
        'c5': (r'Một hình tròn có chu vi $25{,}12\,\text{m}$. Bán kính của hình tròn đó là:', r'$8\,\text{m}$', r'$4\,\text{m}$', r'$2\,\text{m}$', r'$6\,\text{m}$', 'B'),
        'c6': ('Nếu bán kính hình tròn tăng gấp 3 lần thì diện tích hình tròn:', 'Tăng gấp 9 lần', 'Tăng gấp 3 lần', 'Tăng gấp 6 lần', 'Không đổi', 'A'),
        'c7': (r'Diện tích hình tròn có bán kính $6\,\text{cm}$ là:', r'$37{,}68\,\text{cm}^2$', r'$113{,}04\,\text{cm}^2$', r'$226{,}08\,\text{cm}^2$', r'$36\,\text{cm}^2$', 'B'),
        'c8': (r'Diện tích hình tròn có đường kính $12\,\text{dm}$ là:', r'$452{,}16\,\text{dm}^2$', r'$226{,}08\,\text{dm}^2$', r'$113{,}04\,\text{dm}^2$', r'$37{,}68\,\text{dm}^2$', 'C'),
        'c9': (r'Một bánh xe đạp có đường kính $0{,}7\,\text{m}$. Khi bánh xe lăn $150\,\text{vòng}$ thì đi được quãng đường là:', r'$329{,}7\,\text{m}$', r'$164{,}85\,\text{m}$', r'$659{,}4\,\text{m}$', r'$300\,\text{m}$', 'A'),
        'c10': (r'Một bánh xe có đường kính $0{,}5\,\text{m}$. Bánh xe đó phải lăn bao nhiêu vòng để đi hết quãng đường $314\,\text{m}$:', r'$150\,\text{vòng}$', r'$200\,\text{vòng}$', r'$250\,\text{vòng}$', r'$100\,\text{vòng}$', 'B'),
        'c11': (r'Một hồ nước hình tròn có bán kính $5\,\text{m}$. Người ta đắp một con đường rộng $2\,\text{m}$ bao quanh. Diện tích con đường đó là:', r'$75{,}36\,\text{m}^2$', r'$87{,}92\,\text{m}^2$', r'$100\,\text{m}^2$', r'$62{,}8\,\text{m}^2$', 'A'),
        'c12': (r'Một hình vuông cạnh $12\,\text{cm}$, bên trong vẽ hình tròn nội tiếp đường kính $12\,\text{cm}$. Diện tích phần ngoài hình tròn là:', r'$30\,\text{cm}^2$', r'$30{,}96\,\text{cm}^2$', r'$32\,\text{cm}^2$', r'$28{,}5\,\text{cm}^2$', 'B'),
        'b1': ('$53{,}4 \\times 3{,}14$', '$31{,}4 : 3{,}14$', '$113{,}04 : 3{,}14$', '$153{,}86 - 78{,}5$'),
        'b1_ans': ('167{,}676', '10', '36', '75{,}36'),
        'b2': [('x \\times 3{,}14 = 62{,}8', 'x = 62{,}8 : 3{,}14', 'x = 20'),
               ('x : 3{,}14 = 12', 'x = 12 \\times 3{,}14', 'x = 37{,}68'),
               ('x \\times 6{,}28 = 62{,}8', 'x = 62{,}8 : 6{,}28', 'x = 10'),
               ('(x + 8{,}5) \\times 3{,}14 = 62{,}8', 'x + 8{,}5 = 20', 'x = 11{,}5')],
        'b3': [(r'C = 2 \times 9 \times 3{,}14', r'\text{cm}', '56{,}52'),
               (r'C = 16 \times 3{,}14', r'\text{dm}', '50{,}24'),
               (r'S = 8 \times 8 \times 3{,}14', r'\text{cm}^2', '200{,}96'),
               (r'S = 14 \times 14 \times 3{,}14', r'\text{m}^2', '615{,}44')]
    },
    {
        'code': '504',
        'c1': ('Đoạn thẳng nối hai điểm bất kì trên đường tròn và đi qua tâm gọi là:', 'Đường kính', 'Bán kính', 'Dây cung', 'Tiếp tuyến', 'A'),
        'c2': ('Độ dài của đường tròn được gọi là:', 'Diện tích hình tròn', 'Chu vi hình tròn', 'Đường kính', 'Bán kính', 'B'),
        'c3': (r'Chu vi hình tròn có bán kính $7\,\text{cm}$ là:', r'$21{,}98\,\text{cm}$', r'$87{,}92\,\text{cm}$', r'$43{,}96\,\text{cm}$', r'$153{,}86\,\text{cm}$', 'C'),
        'c4': (r'Chu vi hình tròn có đường kính $12\,\text{dm}$ là:', r'$37{,}68\,\text{dm}$', r'$75{,}36\,\text{dm}$', r'$113{,}04\,\text{dm}$', r'$452{,}16\,\text{dm}$', 'A'),
        'c5': (r'Một hình tròn có chu vi $31{,}4\,\text{m}$. Bán kính của hình tròn đó là:', r'$10\,\text{m}$', r'$5\,\text{m}$', r'$2{,}5\,\text{m}$', r'$6\,\text{m}$', 'B'),
        'c6': ('Nếu đường kính hình tròn gấp lên 2 lần thì diện tích hình tròn:', 'Gấp lên 4 lần', 'Gấp lên 2 lần', 'Gấp lên 8 lần', 'Không đổi', 'A'),
        'c7': (r'Diện tích hình tròn có bán kính $7\,\text{cm}$ là:', r'$43{,}96\,\text{cm}^2$', r'$153{,}86\,\text{cm}^2$', r'$307{,}72\,\text{cm}^2$', r'$49\,\text{cm}^2$', 'B'),
        'c8': (r'Diện tích hình tròn có đường kính $14\,\text{dm}$ là:', r'$615{,}44\,\text{dm}^2$', r'$307{,}72\,\text{dm}^2$', r'$153{,}86\,\text{dm}^2$', r'$43{,}96\,\text{dm}^2$', 'C'),
        'c9': (r'Một bánh xe đạp có đường kính $0{,}65\,\text{m}$. Khi bánh xe lăn $250\,\text{vòng}$ thì đi được quãng đường là:', r'$510{,}25\,\text{m}$', r'$255{,}12\,\text{m}$', r'$1\\,020{,}5\,\text{m}$', r'$500\,\text{m}$', 'A'),
        'c10': (r'Một bánh xe có bán kính $0{,}25\,\text{m}$. Bánh xe đó lăn bao nhiêu vòng để đi hết quãng đường $314\,\text{m}$:', r'$150\,\text{vòng}$', r'$200\,\text{vòng}$', r'$250\,\text{vòng}$', r'$100\,\text{vòng}$', 'B'),
        'c11': (r'Một bồn cỏ hình tròn có bán kính $4\,\text{m}$. Người ta lát gạch viền xung quanh rộng $1\,\text{m}$. Diện tích phần lát gạch là:', r'$28{,}26\,\text{m}^2$', r'$31{,}4\,\text{m}^2$', r'$50{,}24\,\text{m}^2$', r'$25{,}12\,\text{m}^2$', 'A'),
        'c12': (r'Một hình vuông cạnh $14\,\text{cm}$, bên trong vẽ hình tròn nội tiếp đường kính $14\,\text{cm}$. Diện tích phần ngoài hình tròn là:', r'$40\,\text{cm}^2$', r'$42{,}14\,\text{cm}^2$', r'$45\,\text{cm}^2$', r'$39{,}5\,\text{cm}^2$', 'B'),
        'b1': ('$62{,}5 \\times 3{,}14$', '$37{,}68 : 3{,}14$', '$153{,}86 : 3{,}14$', '$200{,}96 - 113{,}04$'),
        'b1_ans': ('196{,}25', '12', '49', '87{,}92'),
        'b2': [('x \\times 3{,}14 = 78{,}5', 'x = 78{,}5 : 3{,}14', 'x = 25'),
               ('x : 3{,}14 = 15', 'x = 15 \\times 3{,}14', 'x = 47{,}1'),
               ('x \\times 6{,}28 = 75{,}36', 'x = 75{,}36 : 6{,}28', 'x = 12'),
               ('(x + 10{,}5) \\times 3{,}14 = 78{,}5', 'x + 10{,}5 = 25', 'x = 14{,}5')],
        'b3': [(r'C = 2 \times 10 \times 3{,}14', r'\text{cm}', '62{,}8'),
               (r'C = 18 \times 3{,}14', r'\text{dm}', '56{,}52'),
               (r'S = 9 \times 9 \times 3{,}14', r'\text{cm}^2', '254{,}34'),
               (r'S = 15 \times 15 \times 3{,}14', r'\text{m}^2', '706{,}5')]
    },
    {
        'code': '505',
        'c1': ('Nếu đường kính hình tròn là $d$ thì bán kính $r$ bằng:', '$r = d : 2$', '$r = d \\times 2$', '$r = d \\times d$', '$r = d - 2$', 'A'),
        'c2': ('Bán kính hình tròn là đoạn thẳng nối từ tâm đến:', 'Một điểm bất kì ngoài hình tròn', 'Một điểm bất kì trên đường tròn', 'Tâm của hình tròn khác', 'Trung điểm đường kính', 'B'),
        'c3': (r'Chu vi hình tròn có bán kính $8\,\text{cm}$ là:', r'$25{,}12\,\text{cm}$', r'$100{,}48\,\text{cm}$', r'$50{,}24\,\text{cm}$', r'$200{,}96\,\text{cm}$', 'C'),
        'c4': (r'Chu vi hình tròn có đường kính $14\,\text{dm}$ là:', r'$43{,}96\,\text{dm}$', r'$87{,}92\,\text{dm}$', r'$153{,}86\,\text{dm}$', r'$615{,}44\,\text{dm}$', 'A'),
        'c5': (r'Một hình tròn có chu vi $37{,}68\,\text{m}$. Bán kính của hình tròn đó là:', r'$12\,\text{m}$', r'$6\,\text{m}$', r'$3\,\text{m}$', r'$8\,\text{m}$', 'B'),
        'c6': ('Nếu bán kính hình tròn giảm đi một nửa thì diện tích hình tròn:', 'Giảm đi 4 lần', 'Giảm đi 2 lần', 'Không đổi', 'Giảm đi 8 lần', 'A'),
        'c7': (r'Diện tích hình tròn có bán kính $8\,\text{cm}$ là:', r'$50{,}24\,\text{cm}^2$', r'$200{,}96\,\text{cm}^2$', r'$401{,}92\,\text{cm}^2$', r'$64\,\text{cm}^2$', 'B'),
        'c8': (r'Diện tích hình tròn có đường kính $16\,\text{dm}$ là:', r'$803{,}84\,\text{dm}^2$', r'$401{,}92\,\text{dm}^2$', r'$200{,}96\,\text{dm}^2$', r'$50{,}24\,\text{dm}^2$', 'C'),
        'c9': (r'Một bánh xe đạp có đường kính $0{,}6\,\text{m}$. Khi bánh xe lăn $300\,\text{vòng}$ thì đi được quãng đường là:', r'$565{,}2\,\text{m}$', r'$282{,}6\,\text{m}$', r'$1\\,130{,}4\,\text{m}$', r'$540\,\text{m}$', 'A'),
        'c10': (r'Một bánh xe có chu vi $2{,}5\,\text{m}$. Bánh xe đó phải lăn bao nhiêu vòng để đi hết quãng đường $750\,\text{m}$:', r'$250\,\text{vòng}$', r'$300\,\text{vòng}$', r'$350\,\text{vòng}$', r'$200\,\text{vòng}$', 'B'),
        'c11': (r'Một bồn hoa hình tròn bán kính $5\,\text{m}$. Người ta lát gạch làm lối đi rộng $1\,\text{m}$ bao quanh. Diện tích lối đi là:', r'$34{,}54\,\text{m}^2$', r'$31{,}4\,\text{m}^2$', r'$62{,}8\,\text{m}^2$', r'$40\,\text{m}^2$', 'A'),
        'c12': (r'Một hình vuông cạnh $16\,\text{cm}$, bên trong vẽ hình tròn nội tiếp đường kính $16\,\text{cm}$. Diện tích phần ngoài hình tròn là:', r'$50\,\text{cm}^2$', r'$55{,}04\,\text{cm}^2$', r'$60\,\text{cm}^2$', r'$52{,}5\,\text{cm}^2$', 'B'),
        'b1': ('$74{,}2 \\times 3{,}14$', '$43{,}96 : 3{,}14$', '$200{,}96 : 3{,}14$', '$254{,}34 - 153{,}86$'),
        'b1_ans': ('232{,}988', '14', '64', '100{,}48'),
        'b2': [('x \\times 3{,}14 = 94{,}2', 'x = 94{,}2 : 3{,}14', 'x = 30'),
               ('x : 3{,}14 = 18', 'x = 18 \\times 3{,}14', 'x = 56{,}52'),
               ('x \\times 6{,}28 = 87{,}92', 'x = 87{,}92 : 6{,}28', 'x = 14'),
               ('(x + 12{,}5) \\times 3{,}14 = 94{,}2', 'x + 12{,}5 = 30', 'x = 17{,}5')],
        'b3': [(r'C = 2 \times 12 \times 3{,}14', r'\text{cm}', '75{,}36'),
               (r'C = 20 \times 3{,}14', r'\text{dm}', '62{,}8'),
               (r'S = 10 \times 10 \times 3{,}14', r'\text{cm}^2', '314'),
               (r'S = 16 \times 16 \times 3{,}14', r'\text{m}^2', '803{,}84')]
    },
    {
        'code': '506',
        'c1': ('Tâm của hình tròn là:', 'Trung điểm của mọi đường kính', 'Điểm nằm ngoài hình tròn', 'Điểm nằm trên đường tròn', 'Giao điểm của hai dây cung bất kì', 'A'),
        'c2': ('Chu vi của nửa hình tròn bán kính $r$ (kể cả đường kính) tính bởi:', '$r \\times 3{,}14$', '$r \\times 3{,}14 + 2 \\times r$', '$2 \\times r \\times 3{,}14$', '$r \\times r \\times 3{,}14 : 2$', 'B'),
        'c3': (r'Chu vi hình tròn có bán kính $9\,\text{cm}$ là:', r'$28{,}26\,\text{cm}$', r'$113{,}04\,\text{cm}$', r'$56{,}52\,\text{cm}$', r'$254{,}34\,\text{cm}$', 'C'),
        'c4': (r'Chu vi hình tròn có đường kính $16\,\text{dm}$ là:', r'$50{,}24\,\text{dm}$', r'$100{,}48\,\text{dm}$', r'$200{,}96\,\text{dm}$', r'$803{,}84\,\text{dm}$', 'A'),
        'c5': (r'Một hình tròn có chu vi $43{,}96\,\text{m}$. Bán kính của hình tròn đó là:', r'$14\,\text{m}$', r'$7\,\text{m}$', r'$3{,}5\,\text{m}$', r'$10\,\text{m}$', 'B'),
        'c6': ('Hai hình tròn có bán kính gấp nhau 2 lần thì chu vi của chúng gấp nhau:', '2 lần', '4 lần', '8 lần', 'Không đổi', 'A'),
        'c7': (r'Diện tích hình tròn có bán kính $9\,\text{cm}$ là:', r'$56{,}52\,\text{cm}^2$', r'$254{,}34\,\text{cm}^2$', r'$508{,}68\,\text{cm}^2$', r'$81\,\text{cm}^2$', 'B'),
        'c8': (r'Diện tích hình tròn có đường kính $18\,\text{dm}$ là:', r'$1\\,017{,}36\,\text{dm}^2$', r'$508{,}68\,\text{dm}^2$', r'$254{,}34\,\text{dm}^2$', r'$56{,}52\,\text{dm}^2$', 'C'),
        'c9': (r'Một bánh xe đạp có đường kính $0{,}7\,\text{m}$. Khi bánh xe lăn $200\,\text{vòng}$ thì đi được quãng đường là:', r'$439{,}6\,\text{m}$', r'$219{,}8\,\text{m}$', r'$879{,}2\,\text{m}$', r'$400\,\text{m}$', 'A'),
        'c10': (r'Một bánh xe có đường kính $0{,}8\,\text{m}$. Bánh xe đó phải lăn bao nhiêu vòng để đi hết quãng đường $502{,}4\,\text{m}$:', r'$150\,\text{vòng}$', r'$200\,\text{vòng}$', r'$250\,\text{vòng}$', r'$100\,\text{vòng}$', 'B'),
        'c11': (r'Một bồn hoa hình tròn có bán kính $6\,\text{m}$. Người ta đắp lối đi rộng $1\,\text{m}$ bao quanh. Diện tích lối đi là:', r'$40{,}82\,\text{m}^2$', r'$37{,}68\,\text{m}^2$', r'$50{,}24\,\text{m}^2$', r'$45\,\text{m}^2$', 'A'),
        'c12': (r'Một hình vuông cạnh $18\,\text{cm}$, bên trong vẽ hình tròn nội tiếp đường kính $18\,\text{cm}$. Diện tích phần ngoài hình tròn là:', r'$65\,\text{cm}^2$', r'$69{,}66\,\text{cm}^2$', r'$72\,\text{cm}^2$', r'$68\,\text{cm}^2$', 'B'),
        'b1': ('$81{,}5 \\times 3{,}14$', '$50{,}24 : 3{,}14$', '$254{,}34 : 3{,}14$', '$314 - 200{,}96$'),
        'b1_ans': ('254{,}91', '16', '81', '113{,}04'),
        'b2': [('x \\times 3{,}14 = 109{,}9', 'x = 109{,}9 : 3{,}14', 'x = 35'),
               ('x : 3{,}14 = 20', 'x = 20 \\times 3{,}14', 'x = 62{,}8'),
               ('x \\times 6{,}28 = 100{,}48', 'x = 100{,}48 : 6{,}28', 'x = 16'),
               ('(x + 14{,}5) \\times 3{,}14 = 109{,}9', 'x + 14{,}5 = 35', 'x = 20{,}5')],
        'b3': [(r'C = 2 \times 14 \times 3{,}14', r'\text{cm}', '87{,}92'),
               (r'C = 24 \times 3{,}14', r'\text{dm}', '75{,}36'),
               (r'S = 11 \times 11 \times 3{,}14', r'\text{cm}^2', '379{,}94'),
               (r'S = 18 \times 18 \times 3{,}14', r'\text{m}^2', '1\\,017{,}36')]
    },
    {
        'code': '507',
        'c1': ('Đường kính của hình tròn chia hình tròn thành:', 'Hai nửa hình tròn bằng nhau', 'Ba phần bằng nhau', 'Bốn phần bằng nhau', 'Hai phần không bằng nhau', 'A'),
        'c2': ('Nếu đường kính của hình tròn tăng gấp 3 lần thì chu vi của nó:', 'Không đổi', 'Tăng gấp 3 lần', 'Tăng gấp 9 lần', 'Tăng gấp 6 lần', 'B'),
        'c3': (r'Chu vi hình tròn có bán kính $10\,\text{cm}$ là:', r'$31{,}4\,\text{cm}$', r'$125{,}6\,\text{cm}$', r'$62{,}8\,\text{cm}$', r'$314\,\text{cm}$', 'C'),
        'c4': (r'Chu vi hình tròn có đường kính $18\,\text{dm}$ là:', r'$56{,}52\,\text{dm}$', r'$113{,}04\,\text{dm}$', r'$254{,}34\,\text{dm}$', r'$1\\,017{,}36\,\text{dm}$', 'A'),
        'c5': (r'Một hình tròn có chu vi $50{,}24\,\text{m}$. Bán kính của hình tròn đó là:', r'$16\,\text{m}$', r'$8\,\text{m}$', r'$4\,\text{m}$', r'$12\,\text{m}$', 'B'),
        'c6': ('Hai hình tròn có chu vi gấp nhau 3 lần thì diện tích của chúng gấp nhau:', '9 lần', '3 lần', '6 lần', 'Không đổi', 'A'),
        'c7': (r'Diện tích hình tròn có bán kính $10\,\text{cm}$ là:', r'$62{,}8\,\text{cm}^2$', r'$314\,\text{cm}^2$', r'$628\,\text{cm}^2$', r'$100\,\text{cm}^2$', 'B'),
        'c8': (r'Diện tích hình tròn có đường kính $20\,\text{dm}$ là:', r'$1\\,256\,\text{dm}^2$', r'$628\,\text{dm}^2$', r'$314\,\text{dm}^2$', r'$62{,}8\,\text{dm}^2$', 'C'),
        'c9': (r'Một bánh xe đạp có đường kính $0{,}75\,\text{m}$. Khi bánh xe lăn $200\,\text{vòng}$ thì đi được quãng đường là:', r'$471\,\text{m}$', r'$235{,}5\,\text{m}$', r'$942\,\text{m}$', r'$450\,\text{m}$', 'A'),
        'c10': (r'Một bánh xe có đường kính $0{,}6\,\text{m}$. Bánh xe đó phải lăn bao nhiêu vòng để đi hết quãng đường $565{,}2\,\text{m}$:', r'$250\,\text{vòng}$', r'$300\,\text{vòng}$', r'$350\,\text{vòng}$', r'$200\,\text{vòng}$', 'B'),
        'c11': (r'Một hồ nước hình tròn bán kính $7\,\text{m}$. Người ta đắp lối đi rộng $1\,\text{m}$ bao quanh. Diện tích lối đi là:', r'$47{,}1\,\text{m}^2$', r'$43{,}96\,\text{m}^2$', r'$50{,}24\,\text{m}^2$', r'$45\,\text{m}^2$', 'A'),
        'c12': (r'Một hình vuông cạnh $20\,\text{cm}$, bên trong vẽ hình tròn nội tiếp đường kính $20\,\text{cm}$. Diện tích phần ngoài hình tròn là:', r'$80\,\text{cm}^2$', r'$86\,\text{cm}^2$', r'$90\,\text{cm}^2$', r'$84\,\text{cm}^2$', 'B'),
        'b1': ('$92{,}5 \\times 3{,}14$', '$56{,}52 : 3{,}14$', '$314 : 3{,}14$', '$452{,}16 - 254{,}34$'),
        'b1_ans': ('290{,}45', '18', '100', '197{,}82'),
        'b2': [('x \\times 3{,}14 = 125{,}6', 'x = 125{,}6 : 3{,}14', 'x = 40'),
               ('x : 3{,}14 = 25', 'x = 25 \\times 3{,}14', 'x = 78{,}5'),
               ('x \\times 6{,}28 = 125{,}6', 'x = 125{,}6 : 6{,}28', 'x = 20'),
               ('(x + 18{,}5) \\times 3{,}14 = 125{,}6', 'x + 18{,}5 = 40', 'x = 21{,}5')],
        'b3': [(r'C = 2 \times 15 \times 3{,}14', r'\text{cm}', '94{,}2'),
               (r'C = 30 \times 3{,}14', r'\text{dm}', '94{,}2'),
               (r'S = 12 \times 12 \times 3{,}14', r'\text{cm}^2', '452{,}16'),
               (r'S = 20 \times 20 \times 3{,}14', r'\text{m}^2', '1\\,256')]
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

