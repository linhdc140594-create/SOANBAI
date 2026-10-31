# -*- coding: utf-8 -*-
"""
Script sinh Phiếu bài tập cuối tuần Toán 5 - TUAN_11 với 7 Mã đề (501 -> 507).
Chủ đề: Phép nhân và phép chia số thập phân
Bài 4 và Bài 5: Chuẩn hóa theo chương trình Học kì 1 Lớp 5 (GDPT 2018).
Mỗi mã đề đúng 2 trang A4 in 2 mặt (Tổng 14 trang/file PDF).
"""

import os
import sys
import json
from shared_template import render_tex, render_markdown_answers, compile_and_verify

WEEK_NUM = 11
WEEK_TITLE = 'Phép nhân và phép chia số thập phân'

TOPICS = [
    'Nhân số thập phân với số tự nhiên',
    'Nhân nhẩm số thập phân với 10, 100, 1000',
    'Nhân hai số thập phân',
    'Tính chất phân phối của phép nhân đối với phép cộng',
    'Chia số thập phân cho số tự nhiên',
    'Chia số tự nhiên cho số tự nhiên, thương là số thập phân',
    'Chia một số tự nhiên cho một số thập phân',
    'Chia hai số thập phân',
    'Tìm thành phần chưa biết (tìm thừa số, số bị chia)',
    'Tìm thành phần chưa biết (tìm số chia)',
    'Diện tích hình chữ nhật có kích thước là số thập phân',
    'Bài toán rút về đơn vị liên quan đến số thập phân'
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'grade5_bai4_bai5_data.json'), 'r', encoding='utf-8') as f:
    g5_bai4_bai5 = json.load(f)[str(WEEK_NUM)]

MA_DE_CONFIGS = [
    {
        'code': '501',
        'c1': ('Kết quả của phép tính $12{,}5 \\times 6$ là:', '$75$', '$7{,}5$', '$750$', '$72{,}5$', 'A'),
        'c2': ('Kết quả tính nhẩm $3{,}45 \\times 100$ là:', '$34{,}5$', '$345$', '$3\\,450$', '$0{,}345$', 'B'),
        'c3': ('Kết quả của phép tính $2{,}5 \\times 1{,}4$ là:', '$3{,}05$', '$35$', '$3{,}5$', '$0{,}35$', 'C'),
        'c4': ('Biểu thức $a \\times (b + c) = a \\times b + a \\times c$ là:', 'Nhân một số với một tổng', 'Nhân một số với một hiệu', 'Tính chất giao hoán', 'Tính chất kết hợp', 'A'),
        'c5': ('Kết quả của phép tính $28{,}5 : 5$ là:', '$5{,}5$', '$5{,}7$', '$5{,}9$', '$6{,}7$', 'B'),
        'c6': ('Thương của phép chia $27 : 4$ viết dưới dạng số thập phân là:', '$6{,}5$', '$6{,}25$', '$6{,}75$', '$7{,}25$', 'C'),
        'c7': ('Kết quả của phép tính $45 : 2{,}5$ là:', '$18$', '$1{,}8$', '$180$', '$16$', 'A'),
        'c8': ('Kết quả của phép tính $17{,}5 : 3{,}5$ là:', '$4$', '$5$', '$6$', '$5{,}5$', 'B'),
        'c9': ('Tìm $x$, biết: $x \\times 3{,}5 = 14$. Giá trị của $x$ là:', '$3$', '$5$', '$4$', '$4{,}5$', 'C'),
        'c10': ('Tìm $x$, biết: $24 : x = 4{,}8$. Giá trị của $x$ là:', '$5$', '$4$', '$6$', '$5{,}2$', 'A'),
        'c11': (r'Một mảnh vườn hình chữ nhật có chiều dài $15{,}5\,\text{m}$, chiều rộng $8\,\text{m}$. Diện tích mảnh vườn đó là:', r'$120\,\text{m}^2$', r'$124\,\text{m}^2$', r'$128\,\text{m}^2$', r'$114\,\text{m}^2$', 'B'),
        'c12': (r'Mua $5\,\text{kg}$ gạo hết $110\,000$ đồng. Mua $8{,}5\,\text{kg}$ gạo cùng loại hết số tiền là:', r'$187\,000$ đồng', r'$176\,000$ đồng', r'$198\,000$ đồng', r'$180\,000$ đồng', 'A'),
        'b1': ('$24{,}5 \\times 3{,}6$', '$15{,}8 \\times 4{,}5$', '$75{,}6 : 6$', '$91{,}8 : 3{,}4$'),
        'b1_ans': ('88{,}2', '71{,}1', '12{,}6', '27'),
        'b2': [('x \\times 3{,}5 = 29{,}75', 'x = 29{,}75 : 3{,}5', 'x = 8{,}5'),
               ('x : 4{,}2 = 6{,}5', 'x = 6{,}5 \\times 4{,}2', 'x = 27{,}3'),
               ('84 : x = 17{,}5', 'x = 84 : 17{,}5', 'x = 4{,}8'),
               ('x \\times 2{,}5 = 15{,}5 + 4{,}5', 'x \\times 2{,}5 = 20', 'x = 8')],
        'b3': [(r'4{,}5 \times 10', r'\dots', '45'),
               (r'0{,}38 \times 100', r'\dots', '38'),
               (r'72{,}5 : 10', r'\dots', '7{,}25'),
               (r'450 : 100', r'\dots', '4{,}5')]
    },
    {
        'code': '502',
        'c1': ('Kết quả của phép tính $14{,}5 \\times 4$ là:', '$58$', '$5{,}8$', '$580$', '$56$', 'A'),
        'c2': ('Kết quả tính nhẩm $5{,}68 \\times 100$ là:', '$56{,}8$', '$568$', '$5\\,680$', '$0{,}568$', 'B'),
        'c3': ('Kết quả của phép tính $3{,}5 \\times 1{,}6$ là:', '$5{,}06$', '$56$', '$5{,}6$', '$0{,}56$', 'C'),
        'c4': ('Biểu thức $a \\times (b - c) = a \\times b - a \\times c$ là:', 'Nhân một số với một hiệu', 'Nhân một số với một tổng', 'Tính chất giao hoán', 'Tính chất kết hợp', 'A'),
        'c5': ('Kết quả của phép tính $34{,}8 : 6$ là:', '$5{,}6$', '$5{,}8$', '$6{,}2$', '$5{,}7$', 'B'),
        'c6': ('Thương của phép chia $39 : 4$ viết dưới dạng số thập phân là:', '$9{,}5$', '$9{,}25$', '$9{,}75$', '$8{,}75$', 'C'),
        'c7': ('Kết quả của phép tính $54 : 3{,}6$ là:', '$15$', '$1{,}5$', '$150$', '$12$', 'A'),
        'c8': ('Kết quả của phép tính $21{,}6 : 2{,}4$ là:', '$8$', '$9$', '$10$', '$9{,}5$', 'B'),
        'c9': ('Tìm $x$, biết: $x \\times 4{,}5 = 27$. Giá trị của $x$ là:', '$5$', '$7$', '$6$', '$6{,}5$', 'C'),
        'c10': ('Tìm $x$, biết: $36 : x = 4{,}5$. Giá trị của $x$ là:', '$8$', '$7$', '$9$', '$8{,}5$', 'A'),
        'c11': (r'Một mảnh đất hình chữ nhật có chiều dài $18{,}5\,\text{m}$, chiều rộng $6\,\text{m}$. Diện tích mảnh đất đó là:', r'$110\,\text{m}^2$', r'$111\,\text{m}^2$', r'$112\,\text{m}^2$', r'$108\,\text{m}^2$', 'B'),
        'c12': (r'Mua $4\,\text{m}$ vải hết $140\,000$ đồng. Mua $6{,}5\,\text{m}$ vải cùng loại hết số tiền là:', r'$227\,500$ đồng', r'$210\,000$ đồng', r'$245\,000$ đồng', r'$220\,000$ đồng', 'A'),
        'b1': ('$26{,}4 \\times 2{,}8$', '$18{,}5 \\times 3{,}4$', '$84{,}8 : 8$', '$86{,}4 : 2{,}7$'),
        'b1_ans': ('73{,}92', '62{,}9', '10{,}6', '32'),
        'b2': [('x \\times 4{,}2 = 35{,}7', 'x = 35{,}7 : 4{,}2', 'x = 8{,}5'),
               ('x : 3{,}5 = 7{,}2', 'x = 7{,}2 \\times 3{,}5', 'x = 25{,}2'),
               ('96 : x = 12{,}5', 'x = 96 : 12{,}5', 'x = 7{,}68'),
               ('x \\times 3{,}5 = 18{,}5 + 9{,}5', 'x \\times 3{,}5 = 28', 'x = 8')],
        'b3': [(r'6{,}8 \times 10', r'\dots', '68'),
               (r'0{,}45 \times 100', r'\dots', '45'),
               (r'84{,}6 : 10', r'\dots', '8{,}46'),
               (r'560 : 100', r'\dots', '5{,}6')]
    },
    {
        'code': '503',
        'c1': ('Kết quả của phép tính $16{,}5 \\times 5$ là:', '$82{,}5$', '$8{,}25$', '$825$', '$80{,}5$', 'A'),
        'c2': ('Kết quả tính nhẩm $7{,}25 \\times 100$ là:', '$72{,}5$', '$725$', '$7\\,250$', '$0{,}725$', 'B'),
        'c3': ('Kết quả của phép tính $4{,}5 \\times 1{,}8$ là:', '$8{,}01$', '$81$', '$8{,}1$', '$0{,}81$', 'C'),
        'c4': ('Muốn nhân hai số thập phân, ta đếm phần thập phân của cả hai thừa số có bao nhiêu chữ số rồi:', 'Đặt dấu phẩy kể từ phải sang trái bấy nhiêu chữ số', 'Đặt dấu phẩy tùy ý', 'Không cần đặt dấu phẩy', 'Đặt dấu phẩy ở giữa', 'A'),
        'c5': ('Kết quả của phép tính $42{,}7 : 7$ là:', '$6{,}01$', '$6{,}1$', '$6{,}2$', '$5{,}9$', 'B'),
        'c6': ('Thương của phép chia $31 : 5$ viết dưới dạng số thập phân là:', '$6{,}1$', '$6{,}02$', '$6{,}2$', '$6{,}25$', 'C'),
        'c7': ('Kết quả của phép tính $63 : 4{,}2$ là:', '$15$', '$1{,}5$', '$150$', '$14$', 'A'),
        'c8': ('Kết quả của phép tính $25{,}2 : 3{,}6$ là:', '$6$', '$7$', '$8$', '$7{,}5$', 'B'),
        'c9': ('Tìm $x$, biết: $x \\times 5{,}5 = 33$. Giá trị của $x$ là:', '$5$', '$7$', '$6$', '$6{,}5$', 'C'),
        'c10': ('Tìm $x$, biết: $45 : x = 7{,}5$. Giá trị của $x$ là:', '$6$', '$5$', '$7$', '$6{,}5$', 'A'),
        'c11': (r'Một hình chữ nhật có chiều dài $22{,}5\,\text{m}$, chiều rộng $7\,\text{m}$. Diện tích hình chữ nhật đó là:', r'$155{,}5\,\text{m}^2$', r'$157{,}5\,\text{m}^2$', r'$159{,}5\,\text{m}^2$', r'$154\,\text{m}^2$', 'B'),
        'c12': (r'Mua $6\,\text{hộp}$ sữa hết $150\,000$ đồng. Mua $9{,}5\,\text{hộp}$ sữa như thế (tính theo dung tích) hết số tiền là:', r'$237\,500$ đồng', r'$225\,000$ đồng', r'$250\,000$ đồng', r'$230\,000$ đồng', 'A'),
        'b1': ('$32{,}5 \\times 2{,}4$', '$16{,}4 \\times 5{,}5$', '$96{,}6 : 7$', '$78{,}2 : 3{,}4$'),
        'b1_ans': ('78', '90{,}2', '13{,}8', '23'),
        'b2': [('x \\times 5{,}2 = 44{,}2', 'x = 44{,}2 : 5{,}2', 'x = 8{,}5'),
               ('x : 2{,}8 = 6{,}5', 'x = 6{,}5 \\times 2{,}8', 'x = 18{,}2'),
               ('105 : x = 14', 'x = 105 : 14', 'x = 7{,}5'),
               ('x \\times 4{,}5 = 23{,}5 + 12{,}5', 'x \\times 4{,}5 = 36', 'x = 8')],
        'b3': [(r'8{,}2 \times 10', r'\dots', '82'),
               (r'0{,}64 \times 100', r'\dots', '64'),
               (r'93{,}5 : 10', r'\dots', '9{,}35'),
               (r'780 : 100', r'\dots', '7{,}8')]
    },
    {
        'code': '504',
        'c1': ('Kết quả của phép tính $18{,}5 \\times 6$ là:', '$111$', '$11{,}1$', '$1\\,110$', '$108$', 'A'),
        'c2': ('Kết quả tính nhẩm $8{,}42 \\times 100$ là:', '$84{,}2$', '$842$', '$8\\,420$', '$0{,}842$', 'B'),
        'c3': ('Kết quả của phép tính $5{,}5 \\times 1{,}4$ là:', '$7{,}07$', '$77$', '$7{,}7$', '$0{,}77$', 'C'),
        'c4': ('Khi nhân một số thập phân với $10;\\; 100;\\; 1000;\\; \\dots$ ta chỉ việc chuyển dấu phẩy sang bên phải:', 'Lần lượt $1;\\; 2;\\; 3;\\; \\dots$ chữ số', 'Lần lượt sang bên trái', 'Không cần chuyển', 'Chỉ thêm chữ số 0', 'A'),
        'c5': ('Kết quả của phép tính $51{,}2 : 8$ là:', '$6{,}2$', '$6{,}4$', '$6{,}6$', '$5{,}8$', 'B'),
        'c6': ('Thương của phép chia $43 : 4$ viết dưới dạng số thập phân là:', '$10{,}5$', '$10{,}25$', '$10{,}75$', '$11{,}25$', 'C'),
        'c7': ('Kết quả của phép tính $72 : 4{,}5$ là:', '$16$', '$1{,}6$', '$160$', '$14$', 'A'),
        'c8': ('Kết quả của phép tính $29{,}4 : 4{,}2$ là:', '$6$', '$7$', '$8$', '$7{,}5$', 'B'),
        'c9': ('Tìm $x$, biết: $x \\times 6{,}5 = 52$. Giá trị của $x$ là:', '$7$', '$9$', '$8$', '$8{,}5$', 'C'),
        'c10': ('Tìm $x$, biết: $56 : x = 8{,}75$. Giá trị của $x$ là:', '$6{,}4$', '$5{,}4$', '$7{,}4$', '$6{,}8$', 'A'),
        'c11': (r'Một thửa ruộng hình chữ nhật có chiều dài $24{,}5\,\text{m}$, chiều rộng $8\,\text{m}$. Diện tích thửa ruộng đó là:', r'$194\,\text{m}^2$', r'$196\,\text{m}^2$', r'$198\,\text{m}^2$', r'$192\,\text{m}^2$', 'B'),
        'c12': (r'Mua $8\,\text{lít}$ dầu ăn hết $240\,000$ đồng. Mua $12{,}5\,\text{lít}$ dầu ăn cùng loại hết số tiền là:', r'$375\,000$ đồng', r'$360\,000$ đồng', r'$390\,000$ đồng', r'$350\,000$ đồng', 'A'),
        'b1': ('$28{,}6 \\times 3{,}5$', '$14{,}8 \\times 6{,}5$', '$89{,}6 : 4$', '$98{,}8 : 2{,}6$'),
        'b1_ans': ('100{,}1', '96{,}2', '22{,}4', '38'),
        'b2': [('x \\times 6{,}4 = 54{,}4', 'x = 54{,}4 : 6{,}4', 'x = 8{,}5'),
               ('x : 3{,}6 = 8{,}5', 'x = 8{,}5 \\times 3{,}6', 'x = 30{,}6'),
               ('120 : x = 16', 'x = 120 : 16', 'x = 7{,}5'),
               ('x \\times 5{,}5 = 31{,}8 + 17{,}7', 'x \\times 5{,}5 = 49{,}5', 'x = 9')],
        'b3': [(r'9{,}4 \times 10', r'\dots', '94'),
               (r'0{,}75 \times 100', r'\dots', '75'),
               (r'125{,}6 : 10', r'\dots', '12{,}56'),
               (r'890 : 100', r'\dots', '8{,}9')]
    },
    {
        'code': '505',
        'c1': ('Kết quả của phép tính $22{,}5 \\times 4$ là:', '$90$', '$9{,}0$', '$900$', '$88$', 'A'),
        'c2': ('Kết quả tính nhẩm $9{,}36 \\times 100$ là:', '$93{,}6$', '$936$', '$9\\,360$', '$0{,}936$', 'B'),
        'c3': ('Kết quả của phép tính $6{,}5 \\times 1{,}6$ là:', '$10{,}04$', '$104$', '$10{,}4$', '$1{,}04$', 'C'),
        'c4': ('Khi nhân một số với $0{,}1;\\; 0{,}01;\\; 0{,}001$ ta chỉ việc chuyển dấu phẩy sang bên trái:', 'Lần lượt $1;\\; 2;\\; 3;\\; \\dots$ chữ số', 'Lần lượt sang bên phải', 'Không thay đổi', 'Chỉ thêm chữ số 0', 'A'),
        'c5': ('Kết quả của phép tính $58{,}5 : 9$ là:', '$6{,}3$', '$6{,}5$', '$6{,}7$', '$5{,}9$', 'B'),
        'c6': ('Thương của phép chia $53 : 4$ viết dưới dạng số thập phân là:', '$13{,}5$', '$13{,}2$', '$13{,}25$', '$13{,}75$', 'C'),
        'c7': ('Kết quả của phép tính $81 : 5{,}4$ là:', '$15$', '$1{,}5$', '$150$', '$16$', 'A'),
        'c8': ('Kết quả của phép tính $33{,}6 : 4{,}8$ là:', '$6$', '$7$', '$8$', '$7{,}5$', 'B'),
        'c9': ('Tìm $x$, biết: $x \\times 7{,}5 = 60$. Giá trị của $x$ là:', '$7$', '$9$', '$8$', '$8{,}5$', 'C'),
        'c10': ('Tìm $x$, biết: $63 : x = 8{,}4$. Giá trị của $x$ là:', '$7{,}5$', '$6{,}5$', '$8{,}5$', '$7{,}2$', 'A'),
        'c11': (r'Một mảnh đất hình chữ nhật có chiều dài $26{,}5\,\text{m}$, chiều rộng $8\,\text{m}$. Diện tích mảnh đất đó là:', r'$210\,\text{m}^2$', r'$212\,\text{m}^2$', r'$214\,\text{m}^2$', r'$208\,\text{m}^2$', 'B'),
        'c12': (r'Mua $6\,\text{kg}$ cam hết $168\,000$ đồng. Mua $9{,}5\,\text{kg}$ cam cùng loại hết số tiền là:', r'$266\,000$ đồng', r'$252\,000$ đồng', r'$280\,000$ đồng', r'$260\,000$ đồng', 'A'),
        'b1': ('$35{,}4 \\times 2{,}5$', '$19{,}6 \\times 4{,}5$', '$79{,}2 : 6$', '$88{,}4 : 3{,}4$'),
        'b1_ans': ('88{,}5', '88{,}2', '13{,}2', '26'),
        'b2': [('x \\times 7{,}2 = 61{,}2', 'x = 61{,}2 : 7{,}2', 'x = 8{,}5'),
               ('x : 4{,}5 = 7{,}6', 'x = 7{,}6 \\times 4{,}5', 'x = 34{,}2'),
               ('135 : x = 18', 'x = 135 : 18', 'x = 7{,}5'),
               ('x \\times 6{,}5 = 38{,}6 + 26{,}4', 'x \\times 6{,}5 = 65', 'x = 10')],
        'b3': [(r'12{,}5 \times 10', r'\dots', '125'),
               (r'0{,}82 \times 100', r'\dots', '82'),
               (r'145{,}8 : 10', r'\dots', '14{,}58'),
               (r'920 : 100', r'\dots', '9{,}2')]
    },
    {
        'code': '506',
        'c1': ('Kết quả của phép tính $25{,}5 \\times 4$ là:', '$102$', '$10{,}2$', '$1\\,020$', '$100$', 'A'),
        'c2': ('Kết quả tính nhẩm $12{,}48 \\times 100$ là:', '$124{,}8$', '$1\\,248$', '$12\\,480$', '$1{,}248$', 'B'),
        'c3': ('Kết quả của phép tính $7{,}5 \\times 1{,}6$ là:', '$12{,}05$', '$120$', '$12$', '$1{,}2$', 'C'),
        'c4': ('Biểu thức $a \\times b = b \\times a$ thể hiện tính chất nào:', 'Tính chất giao hoán', 'Tính chất kết hợp', 'Tính chất phân phối', 'Nhân với số 1', 'A'),
        'c5': ('Kết quả của phép tính $67{,}2 : 8$ là:', '$8{,}2$', '$8{,}4$', '$8{,}6$', '$7{,}8$', 'B'),
        'c6': ('Thương của phép chia $57 : 4$ viết dưới dạng số thập phân là:', '$14{,}5$', '$14{,}2$', '$14{,}25$', '$14{,}75$', 'C'),
        'c7': ('Kết quả của phép tính $90 : 7{,}5$ là:', '$12$', '$1{,}2$', '$120$', '$15$', 'A'),
        'c8': ('Kết quả của phép tính $39{,}2 : 5{,}6$ là:', '$6$', '$7$', '$8$', '$7{,}5$', 'B'),
        'c9': ('Tìm $x$, biết: $x \\times 8{,}5 = 68$. Giá trị của $x$ là:', '$7$', '$9$', '$8$', '$8{,}5$', 'C'),
        'c10': ('Tìm $x$, biết: $72 : x = 9{,}6$. Giá trị của $x$ là:', '$7{,}5$', '$6{,}5$', '$8{,}5$', '$7{,}2$', 'A'),
        'c11': (r'Một thửa ruộng hình chữ nhật có chiều dài $28{,}5\,\text{m}$, chiều rộng $8\,\text{m}$. Diện tích thửa ruộng đó là:', r'$226\,\text{m}^2$', r'$228\,\text{m}^2$', r'$230\,\text{m}^2$', r'$224\,\text{m}^2$', 'B'),
        'c12': (r'Mua $7\,\text{kg}$ táo hết $224\,000$ đồng. Mua $10{,}5\,\text{kg}$ táo cùng loại hết số tiền là:', r'$336\,000$ đồng', r'$320\,000$ đồng', r'$350\,000$ đồng', r'$330\,000$ đồng', 'A'),
        'b1': ('$42{,}5 \\times 1{,}8$', '$17{,}5 \\times 4{,}6$', '$94{,}5 : 5$', '$79{,}8 : 2{,}8$'),
        'b1_ans': ('76{,}5', '80{,}5', '18{,}9', '28{,}5'),
        'b2': [('x \\times 8{,}4 = 71{,}4', 'x = 71{,}4 : 8{,}4', 'x = 8{,}5'),
               ('x : 5{,}2 = 6{,}5', 'x = 6{,}5 \\times 5{,}2', 'x = 33{,}8'),
               ('156 : x = 20{,}8', 'x = 156 : 20{,}8', 'x = 7{,}5'),
               ('x \\times 7{,}5 = 46{,}8 + 28{,}2', 'x \\times 7{,}5 = 75', 'x = 10')],
        'b3': [(r'15{,}6 \times 10', r'\dots', '156'),
               (r'0{,}95 \times 100', r'\dots', '95'),
               (r'168{,}4 : 10', r'\dots', '16{,}84'),
               (r'1\\,250 : 100', r'\dots', '12{,}5')]
    },
    {
        'code': '507',
        'c1': ('Kết quả của phép tính $28{,}5 \\times 4$ là:', '$114$', '$11{,}4$', '$1\\,140$', '$112$', 'A'),
        'c2': ('Kết quả tính nhẩm $15{,}72 \\times 100$ là:', '$157{,}2$', '$1\\,572$', '$15\\,720$', '$1{,}572$', 'B'),
        'c3': ('Kết quả của phép tính $8{,}5 \\times 1{,}4$ là:', '$11{,}09$', '$119$', '$11{,}9$', '$1{,}19$', 'C'),
        'c4': ('Biểu thức $(a \\times b) \\times c = a \\times (b \\times c)$ thể hiện tính chất nào:', 'Tính chất kết hợp', 'Tính chất giao hoán', 'Tính chất phân phối', 'Nhân với số 1', 'A'),
        'c5': ('Kết quả của phép tính $76{,}8 : 8$ là:', '$9{,}4$', '$9{,}6$', '$9{,}8$', '$8{,}6$', 'B'),
        'c6': ('Thương của phép chia $69 : 4$ viết dưới dạng số thập phân là:', '$17{,}5$', '$17{,}2$', '$17{,}25$', '$17{,}75$', 'C'),
        'c7': ('Kết quả của phép tính $96 : 6{,}4$ là:', '$15$', '$1{,}5$', '$150$', '$16$', 'A'),
        'c8': ('Kết quả của phép tính $46{,}8 : 5{,}2$ là:', '$8$', '$9$', '$10$', '$9{,}5$', 'B'),
        'c9': ('Tìm $x$, biết: $x \\times 9{,}5 = 76$. Giá trị của $x$ là:', '$7$', '$9$', '$8$', '$8{,}5$', 'C'),
        'c10': ('Tìm $x$, biết: $84 : x = 11{,}2$. Giá trị của $x$ là:', '$7{,}5$', '$6{,}5$', '$8{,}5$', '$7{,}2$', 'A'),
        'c11': (r'Một mảnh đất hình chữ nhật có chiều dài $32{,}5\,\text{m}$, chiều rộng $8\,\text{m}$. Diện tích mảnh đất đó là:', r'$258\,\text{m}^2$', r'$260\,\text{m}^2$', r'$262\,\text{m}^2$', r'$256\,\text{m}^2$', 'B'),
        'c12': (r'Mua $8\,\text{kg}$ nho hết $280\,000$ đồng. Mua $11{,}5\,\text{kg}$ nho cùng loại hết số tiền là:', r'$402\,500$ đồng', r'$385\,000$ đồng', r'$420\,000$ đồng', r'$395\,000$ đồng', 'A'),
        'b1': ('$38{,}5 \\times 2{,}6$', '$15{,}6 \\times 5{,}5$', '$93{,}6 : 8$', '$94{,}3 : 4{,}1$'),
        'b1_ans': ('100{,}1', '85{,}8', '11{,}7', '23'),
        'b2': [('x \\times 9{,}2 = 78{,}2', 'x = 78{,}2 : 9{,}2', 'x = 8{,}5'),
               ('x : 6{,}5 = 7{,}2', 'x = 7{,}2 \\times 6{,}5', 'x = 46{,}8'),
               ('168 : x = 22{,}4', 'x = 168 : 22{,}4', 'x = 7{,}5'),
               ('x \\times 8{,}5 = 54{,}8 + 30{,}2', 'x \\times 8{,}5 = 85', 'x = 10')],
        'b3': [(r'18{,}4 \times 10', r'\dots', '184'),
               (r'0{,}98 \times 100', r'\dots', '98'),
               (r'215{,}6 : 10', r'\dots', '21{,}56'),
               (r'1\\,450 : 100', r'\dots', '14{,}5')]
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

