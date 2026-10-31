# -*- coding: utf-8 -*-
"""
Script sinh Phiếu bài tập cuối tuần Toán 5 - TUAN_15 với 7 Mã đề (501 -> 507).
Chủ đề: Luyện tập chung hình phẳng -- Ôn tập số thập phân
Bài 4 và Bài 5: Chuẩn hóa theo chương trình Học kì 1 Lớp 5 (GDPT 2018).
Mỗi mã đề đúng 2 trang A4 in 2 mặt (Tổng 14 trang/file PDF).
"""

import os
import sys
import json
from shared_template import render_tex, render_markdown_answers, compile_and_verify

WEEK_NUM = 15
WEEK_TITLE = 'Luyện tập chung hình phẳng -- Ôn tập số thập phân'

TOPICS = [
    'Đọc, viết và xác định giá trị theo hàng của số thập phân',
    'So sánh và sắp xếp các số thập phân',
    'Làm tròn số thập phân đến hàng phần mười',
    'Viết số đo diện tích dưới dạng số thập phân',
    'Kỹ năng tính toán với số thập phân',
    'Giá trị biểu thức phối hợp số thập phân',
    'Diện tích hình tam giác',
    'Diện tích hình thang',
    'Chu vi và diện tích hình tròn',
    'Tính diện tích hình phẳng hỗn hợp',
    'Bài toán thực tế lát sàn / trồng cỏ',
    'Bài toán chi phí và tiền công thực tế'
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'grade5_bai4_bai5_data.json'), 'r', encoding='utf-8') as f:
    g5_bai4_bai5 = json.load(f)[str(WEEK_NUM)]

MA_DE_CONFIGS = [
    {
        'code': '501',
        'c1': ('Số thập phân $24{,}075$ đọc là:', 'Hai mươi bốn phẩy không trăm bảy mươi lăm', 'Hai mươi bốn phẩy bảy mươi lăm', 'Hai trăm bốn mươi phẩy bảy mươi lăm', 'Hai bốn phẩy không bảy lăm', 'A'),
        'c2': (r'Sắp xếp các số $5{,}42;\; 5{,}24;\; 5{,}402;\; 5{,}204$ từ bé đến lớn là:', '$5{,}24 < 5{,}204 < 5{,}42 < 5{,}402$', '$5{,}204 < 5{,}24 < 5{,}402 < 5{,}42$', '$5{,}42 < 5{,}402 < 5{,}24 < 5{,}204$', '$5{,}204 < 5{,}402 < 5{,}24 < 5{,}42$', 'B'),
        'c3': ('Làm tròn số $38{,}46$ đến hàng phần mười ta được số:', '$38{,}5$', '$38{,}4$', '$38{,}0$', '$39$', 'A'),
        'c4': (r'$4\,\text{m}^2\,8\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$4{,}8$', '$48$', '$4{,}08$', '$40{,}8$', 'C'),
        'c5': ('Kết quả của phép tính $45{,}6 + 18{,}75$ là:', '$63{,}35$', '$64{,}35$', '$64{,}25$', '$63{,}45$', 'B'),
        'c6': ('Giá trị của biểu thức $12{,}5 \\times 4 - 8{,}6 : 2$ là:', '$45{,}7$', '$46{,}7$', '$44{,}7$', '$45{,}5$', 'A'),
        'c7': (r'Một tam giác có đáy $16\,\text{cm}$, chiều cao $12\,\text{cm}$. Diện tích tam giác đó là:', r'$192\,\text{cm}^2$', r'$96\,\text{cm}^2$', r'$48\,\text{cm}^2$', r'$84\,\text{cm}^2$', 'B'),
        'c8': (r'Một hình thang có đáy lớn $24\,\text{cm}$, đáy bé $16\,\text{cm}$, chiều cao $10\,\text{cm}$. Diện tích hình thang đó là:', r'$400\,\text{cm}^2$', r'$160\,\text{cm}^2$', r'$200\,\text{cm}^2$', r'$240\,\text{cm}^2$', 'C'),
        'c9': (r'Một hình tròn có bán kính $5\,\text{cm}$. Diện tích của hình tròn đó là:', r'$78{,}5\,\text{cm}^2$', r'$31{,}4\,\text{cm}^2$', r'$157\,\text{cm}^2$', r'$25\,\text{cm}^2$', 'A'),
        'c10': (r'Một mảnh đất gồm hình chữ nhật $10\,\text{m} \times 6\,\text{m}$ ghép với một tam giác đáy $10\,\text{m}$, chiều cao $4\,\text{m}$. Diện tích mảnh đất là:', r'$70\,\text{m}^2$', r'$80\,\text{m}^2$', r'$90\,\text{m}^2$', r'$85\,\text{m}^2$', 'B'),
        'c11': (r'Một căn phòng dài $8\,\text{m}$, rộng $6\,\text{m}$. Lát bằng gạch vuông cạnh $40\,\text{cm}$ thì cần số viên gạch là:', r'$300\,\text{viên}$', r'$250\,\text{viên}$', r'$350\,\text{viên}$', r'$400\,\text{viên}$', 'A'),
        'c12': (r'Trồng cỏ trên mảnh đất hình thang diện tích $150\,\text{m}^2$ với đơn giá $45\,000$ đồng$/\text{m}^2$. Tổng số tiền công là:', r'$6\,500\,000$ đồng', r'$6\,750\,000$ đồng', r'$7\,000\,000$ đồng', r'$6\,250\,000$ đồng', 'B'),
        'b1': ('$56{,}38 + 27{,}85$', '$94{,}2 - 48{,}76$', '$28{,}5 \\times 3{,}4$', '$89{,}6 : 3{,}2$'),
        'b1_ans': ('84{,}23', '45{,}44', '96{,}9', '28'),
        'b2': [('x + 34{,}8 = 82{,}5', 'x = 82{,}5 - 34{,}8', 'x = 47{,}7'),
               ('x - 28{,}6 = 45{,}7', 'x = 45{,}7 + 28{,}6', 'x = 74{,}3'),
               ('x \\times 4{,}8 = 40{,}8', 'x = 40{,}8 : 4{,}8', 'x = 8{,}5'),
               ('x : 3{,}5 = 16', 'x = 16 \\times 3{,}5', 'x = 56')],
        'b3': [(r'S_{\Delta} = (15 \times 8) : 2', r'\text{cm}^2', '60'),
               (r'S_{\text{thang}} = (20 + 15) \times 8 : 2', r'\text{cm}^2', '140'),
               (r'C_{\text{tròn}} = 2 \times 5 \times 3{,}14', r'\text{cm}', '31{,}4'),
               (r'S_{\text{tròn}} = 4 \times 4 \times 3{,}14', r'\text{dm}^2', '50{,}24')]
    },
    {
        'code': '502',
        'c1': ('Số thập phân $45{,}082$ đọc là:', 'Bốn mươi lăm phẩy không trăm tám mươi hai', 'Bốn mươi lăm phẩy tám mươi hai', 'Bốn trăm năm mươi phẩy tám mươi hai', 'Bốn lăm phẩy không tám hai', 'A'),
        'c2': (r'Sắp xếp các số $6{,}53;\; 6{,}35;\; 6{,}503;\; 6{,}305$ từ bé đến lớn là:', '$6{,}35 < 6{,}305 < 6{,}53 < 6{,}503$', '$6{,}305 < 6{,}35 < 6{,}503 < 6{,}53$', '$6{,}53 < 6{,}503 < 6{,}35 < 6{,}305$', '$6{,}305 < 6{,}503 < 6{,}35 < 6{,}53$', 'B'),
        'c3': ('Làm tròn số $52{,}74$ đến hàng phần mười ta được số:', '$52{,}7$', '$52{,}8$', '$52{,}0$', '$53$', 'A'),
        'c4': (r'$6\,\text{m}^2\,5\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$6{,}5$', '$65$', '$6{,}05$', '$60{,}5$', 'C'),
        'c5': ('Kết quả của phép tính $54{,}8 + 26{,}45$ là:', '$80{,}25$', '$81{,}25$', '$81{,}15$', '$80{,}35$', 'B'),
        'c6': ('Giá trị của biểu thức $15{,}5 \\times 4 - 9{,}4 : 2$ là:', '$57{,}3$', '$58{,}3$', '$56{,}3$', '$57{,}5$', 'A'),
        'c7': (r'Một tam giác có đáy $18\,\text{cm}$, chiều cao $10\,\text{cm}$. Diện tích tam giác đó là:', r'$180\,\text{cm}^2$', r'$90\,\text{cm}^2$', r'$45\,\text{cm}^2$', r'$80\,\text{cm}^2$', 'B'),
        'c8': (r'Một hình thang có đáy lớn $28\,\text{cm}$, đáy bé $18\,\text{cm}$, chiều cao $12\,\text{cm}$. Diện tích hình thang đó là:', r'$552\,\text{cm}^2$', r'$250\,\text{cm}^2$', r'$276\,\text{cm}^2$', r'$280\,\text{cm}^2$', 'C'),
        'c9': (r'Một hình tròn có bán kính $6\,\text{cm}$. Diện tích của hình tròn đó là:', r'$113{,}04\,\text{cm}^2$', r'$37{,}68\,\text{cm}^2$', r'$226{,}08\,\text{cm}^2$', r'$36\,\text{cm}^2$', 'A'),
        'c10': (r'Một mảnh đất gồm hình chữ nhật $12\,\text{m} \times 8\,\text{m}$ ghép với một tam giác đáy $12\,\text{m}$, chiều cao $5\,\text{m}$. Diện tích mảnh đất là:', r'$116\,\text{m}^2$', r'$126\,\text{m}^2$', r'$136\,\text{m}^2$', r'$120\,\text{m}^2$', 'B'),
        'c11': (r'Một căn phòng dài $9\,\text{m}$, rộng $5\,\text{m}$. Lát bằng gạch vuông cạnh $50\,\text{cm}$ thì cần số viên gạch là:', r'$180\,\text{viên}$', r'$150\,\text{viên}$', r'$200\,\text{viên}$', r'$160\,\text{viên}$', 'A'),
        'c12': (r'Trồng cỏ trên mảnh đất hình tam giác diện tích $120\,\text{m}^2$ với đơn giá $50\,000$ đồng$/\text{m}^2$. Tổng số tiền công là:', r'$5\,800\,000$ đồng', r'$6\,000\,000$ đồng', r'$6\,200\,000$ đồng', r'$5\,500\,000$ đồng', 'B'),
        'b1': ('$64{,}45 + 32{,}68$', '$88{,}5 - 39{,}84$', '$32{,}5 \\times 2{,}8$', '$98{,}8 : 2{,}6$'),
        'b1_ans': ('97{,}13', '48{,}66', '91', '38'),
        'b2': [('x + 28{,}6 = 75{,}4', 'x = 75{,}4 - 28{,}6', 'x = 46{,}8'),
               ('x - 35{,}7 = 52{,}8', 'x = 52{,}8 + 35{,}7', 'x = 88{,}5'),
               ('x \\times 5{,}4 = 45{,}9', 'x = 45{,}9 : 5{,}4', 'x = 8{,}5'),
               ('x : 4{,}2 = 18', 'x = 18 \\times 4{,}2', 'x = 75{,}6')],
        'b3': [(r'S_{\Delta} = (18 \times 10) : 2', r'\text{cm}^2', '90'),
               (r'S_{\text{thang}} = (24 + 18) \times 10 : 2', r'\text{cm}^2', '210'),
               (r'C_{\text{tròn}} = 2 \times 6 \times 3{,}14', r'\text{cm}', '37{,}68'),
               (r'S_{\text{tròn}} = 5 \times 5 \times 3{,}14', r'\text{dm}^2', '78{,}5')]
    },
    {
        'code': '503',
        'c1': ('Số thập phân $68{,}045$ đọc là:', 'Sáu mươi tám phẩy không trăm bốn mươi lăm', 'Sáu mươi tám phẩy bốn mươi lăm', 'Sáu trăm tám mươi phẩy bốn mươi lăm', 'Sáu tám phẩy không bốn lăm', 'A'),
        'c2': (r'Sắp xếp các số $7{,}64;\; 7{,}46;\; 7{,}604;\; 7{,}406$ từ bé đến lớn là:', '$7{,}46 < 7{,}406 < 7{,}64 < 7{,}604$', '$7{,}406 < 7{,}46 < 7{,}604 < 7{,}64$', '$7{,}64 < 7{,}604 < 7{,}46 < 7{,}406$', '$7{,}406 < 7{,}604 < 7{,}46 < 7{,}64$', 'B'),
        'c3': ('Làm tròn số $64{,}85$ đến hàng phần mười ta được số:', '$64{,}9$', '$64{,}8$', '$64{,}0$', '$65$', 'A'),
        'c4': (r'$5\,\text{m}^2\,6\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$5{,}6$', '$56$', '$5{,}06$', '$50{,}6$', 'C'),
        'c5': ('Kết quả của phép tính $63{,}5 + 24{,}85$ là:', '$87{,}35$', '$88{,}35$', '$88{,}25$', '$87{,}45$', 'B'),
        'c6': ('Giá trị của biểu thức $18{,}5 \\times 4 - 11{,}2 : 2$ là:', '$68{,}4$', '$69{,}4$', '$67{,}4$', '$68{,}5$', 'A'),
        'c7': (r'Một tam giác có đáy $20\,\text{cm}$, chiều cao $14\,\text{cm}$. Diện tích tam giác đó là:', r'$280\,\text{cm}^2$', r'$140\,\text{cm}^2$', r'$70\,\text{cm}^2$', r'$120\,\text{cm}^2$', 'B'),
        'c8': (r'Một hình thang có đáy lớn $30\,\text{cm}$, đáy bé $20\,\text{cm}$, chiều cao $14\,\text{cm}$. Diện tích hình thang đó là:', r'$700\,\text{cm}^2$', r'$320\,\text{cm}^2$', r'$350\,\text{cm}^2$', r'$360\,\text{cm}^2$', 'C'),
        'c9': (r'Một hình tròn có bán kính $7\,\text{cm}$. Diện tích của hình tròn đó là:', r'$153{,}86\,\text{cm}^2$', r'$43{,}96\,\text{cm}^2$', r'$307{,}72\,\text{cm}^2$', r'$49\,\text{cm}^2$', 'A'),
        'c10': (r'Một mảnh đất gồm hình chữ nhật $14\,\text{m} \times 8\,\text{m}$ ghép với một tam giác đáy $14\,\text{m}$, chiều cao $6\,\text{m}$. Diện tích mảnh đất là:', r'$144\,\text{m}^2$', r'$154\,\text{m}^2$', r'$164\,\text{m}^2$', r'$150\,\text{m}^2$', 'B'),
        'c11': (r'Một căn phòng dài $10\,\text{m}$, rộng $6\,\text{m}$. Lát bằng gạch vuông cạnh $50\,\text{cm}$ thì cần số viên gạch là:', r'$240\,\text{viên}$', r'$200\,\text{viên}$', r'$260\,\text{viên}$', r'$220\,\text{viên}$', 'A'),
        'c12': (r'Trồng cỏ trên mảnh đất hình thang diện tích $180\,\text{m}^2$ với đơn giá $55\,000$ đồng$/\text{m}^2$. Tổng số tiền công là:', r'$9\,500\,000$ đồng', r'$9\,900\,000$ đồng', r'$10\,200\,000$ đồng', r'$9\,700\,000$ đồng', 'B'),
        'b1': ('$72{,}56 + 35{,}84$', '$95{,}4 - 46{,}78$', '$36{,}5 \\times 3{,}2$', '$108 : 3{,}6$'),
        'b1_ans': ('108{,}4', '48{,}62', '116{,}8', '30'),
        'b2': [('x + 36{,}5 = 94{,}2', 'x = 94{,}2 - 36{,}5', 'x = 57{,}7'),
               ('x - 42{,}8 = 56{,}5', 'x = 56{,}5 + 42{,}8', 'x = 99{,}3'),
               ('x \\times 6{,}2 = 52{,}7', 'x = 52{,}7 : 6{,}2', 'x = 8{,}5'),
               ('x : 5{,}4 = 15', 'x = 15 \\times 5{,}4', 'x = 81')],
        'b3': [(r'S_{\Delta} = (20 \times 12) : 2', r'\text{cm}^2', '120'),
               (r'S_{\text{thang}} = (26 + 20) \times 12 : 2', r'\text{cm}^2', '276'),
               (r'C_{\text{tròn}} = 2 \times 7 \times 3{,}14', r'\text{cm}', '43{,}96'),
               (r'S_{\text{tròn}} = 6 \times 6 \times 3{,}14', r'\text{dm}^2', '113{,}04')]
    },
    {
        'code': '504',
        'c1': ('Số thập phân $82{,}036$ đọc là:', 'Tám mươi hai phẩy không trăm ba mươi sáu', 'Tám mươi hai phẩy ba mươi sáu', 'Tám trăm hai mươi phẩy ba mươi sáu', 'Tám hai phẩy không ba sáu', 'A'),
        'c2': (r'Sắp xếp các số $8{,}75;\; 8{,}57;\; 8{,}705;\; 8{,}507$ từ bé đến lớn là:', '$8{,}57 < 8{,}507 < 8{,}75 < 8{,}705$', '$8{,}507 < 8{,}57 < 8{,}705 < 8{,}75$', '$8{,}75 < 8{,}705 < 8{,}57 < 8{,}507$', '$8{,}507 < 8{,}705 < 8{,}57 < 8{,}75$', 'B'),
        'c3': ('Làm tròn số $73{,}68$ đến hàng phần mười ta được số:', '$73{,}7$', '$73{,}6$', '$73{,}0$', '$74$', 'A'),
        'c4': (r'$7\,\text{m}^2\,4\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$7{,}4$', '$74$', '$7{,}04$', '$70{,}4$', 'C'),
        'c5': ('Kết quả của phép tính $72{,}6 + 28{,}75$ là:', '$100{,}35$', '$101{,}35$', '$101{,}25$', '$100{,}45$', 'B'),
        'c6': ('Giá trị của biểu thức $21{,}5 \\times 4 - 13{,}4 : 2$ là:', '$79{,}3$', '$80{,}3$', '$78{,}3$', '$79{,}5$', 'A'),
        'c7': (r'Một tam giác có đáy $22\,\text{cm}$, chiều cao $15\,\text{cm}$. Diện tích tam giác đó là:', r'$330\,\text{cm}^2$', r'$165\,\text{cm}^2$', r'$82{,}5\,\text{cm}^2$', r'$150\,\text{cm}^2$', 'B'),
        'c8': (r'Một hình thang có đáy lớn $32\,\text{cm}$, đáy bé $22\,\text{cm}$, chiều cao $15\,\text{cm}$. Diện tích hình thang đó là:', r'$810\,\text{cm}^2$', r'$380\,\text{cm}^2$', r'$405\,\text{cm}^2$', r'$420\,\text{cm}^2$', 'C'),
        'c9': (r'Một hình tròn có bán kính $8\,\text{cm}$. Diện tích của hình tròn đó là:', r'$200{,}96\,\text{cm}^2$', r'$50{,}24\,\text{cm}^2$', r'$401{,}92\,\text{cm}^2$', r'$64\,\text{cm}^2$', 'A'),
        'c10': (r'Một mảnh đất gồm hình chữ nhật $15\,\text{m} \times 8\,\text{m}$ ghép với một tam giác đáy $15\,\text{m}$, chiều cao $6\,\text{m}$. Diện tích mảnh đất là:', r'$155\,\text{m}^2$', r'$165\,\text{m}^2$', r'$175\,\text{m}^2$', r'$160\,\text{m}^2$', 'B'),
        'c11': (r'Một căn phòng dài $12\,\text{m}$, rộng $6\,\text{m}$. Lát bằng gạch vuông cạnh $60\,\text{cm}$ thì cần số viên gạch là:', r'$200\,\text{viên}$', r'$180\,\text{viên}$', r'$220\,\text{viên}$', r'$190\,\text{viên}$', 'A'),
        'c12': (r'Trồng cỏ trên mảnh đất hình thang diện tích $200\,\text{m}^2$ với đơn giá $60\,000$ đồng$/\text{m}^2$. Tổng số tiền công là:', r'$11\,500\,000$ đồng', r'$12\,000\,000$ đồng', r'$12\,500\,000$ đồng', r'$11\,800\,000$ đồng', 'B'),
        'b1': ('$78{,}48 + 36{,}75$', '$102{,}5 - 54{,}86$', '$42{,}5 \\times 2{,}6$', '$124{,}8 : 3{,}9$'),
        'b1_ans': ('115{,}23', '47{,}64', '110{,}5', '32'),
        'b2': [('x + 42{,}5 = 106{,}2', 'x = 106{,}2 - 42{,}5', 'x = 63{,}7'),
               ('x - 48{,}7 = 64{,}6', 'x = 64{,}6 + 48{,}7', 'x = 113{,}3'),
               ('x \\times 7{,}4 = 62{,}9', 'x = 62{,}9 : 7{,}4', 'x = 8{,}5'),
               ('x : 6{,}2 = 18', 'x = 18 \\times 6{,}2', 'x = 111{,}6')],
        'b3': [(r'S_{\Delta} = (22 \times 14) : 2', r'\text{cm}^2', '154'),
               (r'S_{\text{thang}} = (28 + 22) \times 14 : 2', r'\text{cm}^2', '350'),
               (r'C_{\text{tròn}} = 2 \times 8 \times 3{,}14', r'\text{cm}', '50{,}24'),
               (r'S_{\text{tròn}} = 7 \times 7 \times 3{,}14', r'\text{dm}^2', '153{,}86')]
    },
    {
        'code': '505',
        'c1': ('Số thập phân $94{,}062$ đọc là:', 'Chín mươi tư phẩy không trăm sáu mươi hai', 'Chín mươi tư phẩy sáu mươi hai', 'Chín trăm bốn mươi phẩy sáu mươi hai', 'Chín tư phẩy không sáu hai', 'A'),
        'c2': (r'Sắp xếp các số $9{,}83;\; 9{,}38;\; 9{,}803;\; 9{,}308$ từ bé đến lớn là:', '$9{,}38 < 9{,}308 < 9{,}83 < 9{,}803$', '$9{,}308 < 9{,}38 < 9{,}803 < 9{,}83$', '$9{,}83 < 9{,}803 < 9{,}38 < 9{,}308$', '$9{,}308 < 9{,}803 < 9{,}38 < 9{,}83$', 'B'),
        'c3': ('Làm tròn số $85{,}54$ đến hàng phần mười ta được số:', '$85{,}5$', '$85{,}6$', '$85{,}0$', '$86$', 'A'),
        'c4': (r'$8\,\text{m}^2\,3\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$8{,}3$', '$83$', '$8{,}03$', '$80{,}3$', 'C'),
        'c5': ('Kết quả của phép tính $81{,}5 + 34{,}68$ là:', '$115{,}18$', '$116{,}18$', '$116{,}08$', '$115{,}28$', 'B'),
        'c6': ('Giá trị của biểu thức $24{,}5 \\times 4 - 15{,}6 : 2$ là:', '$90{,}2$', '$91{,}2$', '$89{,}2$', '$90{,}5$', 'A'),
        'c7': (r'Một tam giác có đáy $24\,\text{cm}$, chiều cao $16\,\text{cm}$. Diện tích tam giác đó là:', r'$384\,\text{cm}^2$', r'$192\,\text{cm}^2$', r'$96\,\text{cm}^2$', r'$180\,\text{cm}^2$', 'B'),
        'c8': (r'Một hình thang có đáy lớn $35\,\text{cm}$, đáy bé $25\,\text{cm}$, chiều cao $16\,\text{cm}$. Diện tích hình thang đó là:', r'$960\,\text{cm}^2$', r'$450\,\text{cm}^2$', r'$480\,\text{cm}^2$', r'$500\,\text{cm}^2$', 'C'),
        'c9': (r'Một hình tròn có bán kính $9\,\text{cm}$. Diện tích của hình tròn đó là:', r'$254{,}34\,\text{cm}^2$', r'$56{,}52\,\text{cm}^2$', r'$508{,}68\,\text{cm}^2$', r'$81\,\text{cm}^2$', 'A'),
        'c10': (r'Một mảnh đất gồm hình chữ nhật $16\,\text{m} \times 10\,\text{m}$ ghép với một tam giác đáy $16\,\text{m}$, chiều cao $6\,\text{m}$. Diện tích mảnh đất là:', r'$198\,\text{m}^2$', r'$208\,\text{m}^2$', r'$218\,\text{m}^2$', r'$200\,\text{m}^2$', 'B'),
        'c11': (r'Một căn phòng dài $12\,\text{m}$, rộng $8\,\text{m}$. Lát bằng gạch vuông cạnh $40\,\text{cm}$ thì cần số viên gạch là:', r'$600\,\text{viên}$', r'$500\,\text{viên}$', r'$650\,\text{viên}$', r'$550\,\text{viên}$', 'A'),
        'c12': (r'Trồng cỏ trên mảnh đất hình thang diện tích $250\,\text{m}^2$ với đơn giá $50\,000$ đồng$/\text{m}^2$. Tổng số tiền công là:', r'$12\,000\,000$ đồng', r'$12\,500\,000$ đồng', r'$13\,000\,000$ đồng', r'$12\,250\,000$ đồng', 'B'),
        'b1': ('$84{,}65 + 43{,}86$', '$115{,}4 - 63{,}75$', '$48{,}5 \\times 2{,}4$', '$135 : 4{,}5$'),
        'b1_ans': ('128{,}51', '51{,}65', '116{,}4', '30'),
        'b2': [('x + 48{,}6 = 118{,}4', 'x = 118{,}4 - 48{,}6', 'x = 69{,}8'),
               ('x - 54{,}8 = 72{,}5', 'x = 72{,}5 + 54{,}8', 'x = 127{,}3'),
               ('x \\times 8{,}2 = 69{,}7', 'x = 69{,}7 : 8{,}2', 'x = 8{,}5'),
               ('x : 7{,}5 = 20', 'x = 20 \\times 7{,}5', 'x = 150')],
        'b3': [(r'S_{\Delta} = (24 \times 16) : 2', r'\text{cm}^2', '192'),
               (r'S_{\text{thang}} = (32 + 24) \times 15 : 2', r'\text{cm}^2', '420'),
               (r'C_{\text{tròn}} = 2 \times 9 \times 3{,}14', r'\text{cm}', '56{,}52'),
               (r'S_{\text{tròn}} = 8 \times 8 \times 3{,}14', r'\text{dm}^2', '200{,}96')]
    },
    {
        'code': '506',
        'c1': ('Số thập phân $105{,}048$ đọc là:', 'Một trăm linh năm phẩy không trăm bốn mươi tám', 'Một trăm năm phẩy bốn mươi tám', 'Mười lăm phẩy không trăm bốn mươi tám', 'Một trăm linh năm phẩy bốn mươi tám', 'A'),
        'c2': (r'Sắp xếp các số $10{,}72;\; 10{,}27;\; 10{,}702;\; 10{,}207$ từ bé đến lớn là:', '$10{,}27 < 10{,}207 < 10{,}72 < 10{,}702$', '$10{,}207 < 10{,}27 < 10{,}702 < 10{,}72$', '$10{,}72 < 10{,}702 < 10{,}27 < 10{,}207$', '$10{,}207 < 10{,}702 < 10{,}27 < 10{,}72$', 'B'),
        'c3': ('Làm tròn số $96{,}76$ đến hàng phần mười ta được số:', '$96{,}8$', '$96{,}7$', '$96{,}0$', '$97$', 'A'),
        'c4': (r'$9\,\text{m}^2\,2\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$9{,}2$', '$92$', '$9{,}02$', '$90{,}2$', 'C'),
        'c5': ('Kết quả của phép tính $88{,}7 + 36{,}58$ là:', '$124{,}28$', '$125{,}28$', '$125{,}18$', '$124{,}38$', 'B'),
        'c6': ('Giá trị của biểu thức $28{,}5 \\times 4 - 17{,}4 : 2$ là:', '$105{,}3$', '$106{,}3$', '$104{,}3$', '$105{,}5$', 'A'),
        'c7': (r'Một tam giác có đáy $26\,\text{cm}$, chiều cao $18\,\text{cm}$. Diện tích tam giác đó là:', r'$468\,\text{cm}^2$', r'$234\,\text{cm}^2$', r'$117\,\text{cm}^2$', r'$220\,\text{cm}^2$', 'B'),
        'c8': (r'Một hình thang có đáy lớn $40\,\text{cm}$, đáy bé $30\,\text{cm}$, chiều cao $18\,\text{cm}$. Diện tích hình thang đó là:', r'$1\\,260\,\text{cm}^2$', r'$600\,\text{cm}^2$', r'$630\,\text{cm}^2$', r'$650\,\text{cm}^2$', 'C'),
        'c9': (r'Một hình tròn có bán kính $10\,\text{cm}$. Diện tích của hình tròn đó là:', r'$314\,\text{cm}^2$', r'$62{,}8\,\text{cm}^2$', r'$628\,\text{cm}^2$', r'$100\,\text{cm}^2$', 'A'),
        'c10': (r'Một mảnh đất gồm hình chữ nhật $18\,\text{m} \times 10\,\text{m}$ ghép với một tam giác đáy $18\,\text{m}$, chiều cao $8\,\text{m}$. Diện tích mảnh đất là:', r'$242\,\text{m}^2$', r'$252\,\text{m}^2$', r'$262\,\text{m}^2$', r'$250\,\text{m}^2$', 'B'),
        'c11': (r'Một căn phòng dài $14\,\text{m}$, rộng $8\,\text{m}$. Lát bằng gạch vuông cạnh $40\,\text{cm}$ thì cần số viên gạch là:', r'$700\,\text{viên}$', r'$650\,\text{viên}$', r'$750\,\text{viên}$', r'$600\,\text{viên}$', 'A'),
        'c12': (r'Trồng cỏ trên mảnh đất hình thang diện tích $300\,\text{m}^2$ với đơn giá $48\,000$ đồng$/\text{m}^2$. Tổng số tiền công là:', r'$14\,000\,000$ đồng', r'$14\,400\,000$ đồng', r'$14\,800\,000$ đồng', r'$14\,200\,000$ đồng', 'B'),
        'b1': ('$92{,}58 + 48{,}76$', '$124{,}6 - 75{,}84$', '$54{,}5 \\times 2{,}8$', '$153{,}6 : 4{,}8$'),
        'b1_ans': ('141{,}34', '48{,}76', '152{,}6', '32'),
        'b2': [('x + 54{,}8 = 132{,}6', 'x = 132{,}6 - 54{,}8', 'x = 77{,}8'),
               ('x - 62{,}5 = 81{,}7', 'x = 81{,}7 + 62{,}5', 'x = 144{,}2'),
               ('x \\times 9{,}4 = 89{,}3', 'x = 89{,}3 : 9{,}4', 'x = 9{,}5'),
               ('x : 8{,}4 = 22', 'x = 22 \\times 8{,}4', 'x = 184{,}8')],
        'b3': [(r'S_{\Delta} = (28 \times 18) : 2', r'\text{cm}^2', '252'),
               (r'S_{\text{thang}} = (36 + 28) \times 16 : 2', r'\text{cm}^2', '512'),
               (r'C_{\text{tròn}} = 2 \times 10 \times 3{,}14', r'\text{cm}', '62{,}8'),
               (r'S_{\text{tròn}} = 9 \times 9 \times 3{,}14', r'\text{dm}^2', '254{,}34')]
    },
    {
        'code': '507',
        'c1': ('Số thập phân $128{,}075$ đọc là:', 'Một trăm hai mươi tám phẩy không trăm bảy mươi lăm', 'Một trăm hai tám phẩy bảy mươi lăm', 'Mười hai phẩy không trăm bảy mươi lăm', 'Một trăm hai mươi tám phẩy bảy mươi lăm', 'A'),
        'c2': (r'Sắp xếp các số $12{,}64;\; 12{,}46;\; 12{,}604;\; 12{,}406$ từ bé đến lớn là:', '$12{,}46 < 12{,}406 < 12{,}64 < 12{,}604$', '$12{,}406 < 12{,}46 < 12{,}604 < 12{,}64$', '$12{,}64 < 12{,}604 < 12{,}46 < 12{,}406$', '$12{,}406 < 12{,}604 < 12{,}46 < 12{,}64$', 'B'),
        'c3': ('Làm tròn số $104{,}86$ đến hàng phần mười ta được số:', '$104{,}9$', '$104{,}8$', '$104{,}0$', '$105$', 'A'),
        'c4': (r'$12\,\text{m}^2\,5\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$12{,}5$', '$125$', '$12{,}05$', '$120{,}5$', 'C'),
        'c5': ('Kết quả của phép tính $96{,}8 + 45{,}75$ là:', '$141{,}55$', '$142{,}55$', '$142{,}45$', '$141{,}65$', 'B'),
        'c6': ('Giá trị của biểu thức $32{,}5 \\times 4 - 19{,}6 : 2$ là:', '$120{,}2$', '$121{,}2$', '$119{,}2$', '$120{,}5$', 'A'),
        'c7': (r'Một tam giác có đáy $28\,\text{cm}$, chiều cao $20\,\text{cm}$. Diện tích tam giác đó là:', r'$560\,\text{cm}^2$', r'$280\,\text{cm}^2$', r'$140\,\text{cm}^2$', r'$260\,\text{cm}^2$', 'B'),
        'c8': (r'Một hình thang có đáy lớn $45\,\text{cm}$, đáy bé $35\,\text{cm}$, chiều cao $20\,\text{cm}$. Diện tích hình thang đó là:', r'$1\\,600\,\text{cm}^2$', r'$750\,\text{cm}^2$', r'$800\,\text{cm}^2$', r'$850\,\text{cm}^2$', 'C'),
        'c9': (r'Một hình tròn có bán kính $12\,\text{cm}$. Diện tích của hình tròn đó là:', r'$452{,}16\,\text{cm}^2$', r'$75{,}36\,\text{cm}^2$', r'$904{,}32\,\text{cm}^2$', r'$144\,\text{cm}^2$', 'A'),
        'c10': (r'Một mảnh đất gồm hình chữ nhật $20\,\text{m} \times 12\,\text{m}$ ghép với một tam giác đáy $20\,\text{m}$, chiều cao $8\,\text{m}$. Diện tích mảnh đất là:', r'$310\,\text{m}^2$', r'$320\,\text{m}^2$', r'$330\,\text{m}^2$', r'$300\,\text{m}^2$', 'B'),
        'c11': (r'Một căn phòng dài $15\,\text{m}$, rộng $8\,\text{m}$. Lát bằng gạch vuông cạnh $50\,\text{cm}$ thì cần số viên gạch là:', r'$480\,\text{viên}$', r'$450\,\text{viên}$', r'$500\,\text{viên}$', r'$460\,\text{viên}$', 'A'),
        'c12': (r'Trồng cỏ trên mảnh đất hình thang diện tích $350\,\text{m}^2$ với đơn giá $52\,000$ đồng$/\text{m}^2$. Tổng số tiền công là:', r'$17\,800\,000$ đồng', r'$18\,200\,000$ đồng', r'$18\,500\,000$ đồng', r'$18\,000\,000$ đồng', 'B'),
        'b1': ('$104{,}65 + 56{,}88$', '$138{,}2 - 84{,}65$', '$62{,}5 \\times 3{,}2$', '$184 : 4{,}6$'),
        'b1_ans': ('161{,}53', '53{,}55', '200', '40'),
        'b2': [('x + 62{,}4 = 148{,}6', 'x = 148{,}6 - 62{,}4', 'x = 86{,}2'),
               ('x - 71{,}6 = 94{,}8', 'x = 94{,}8 + 71{,}6', 'x = 166{,}4'),
               ('x \\times 9{,}8 = 102{,}9', 'x = 102{,}9 : 9{,}8', 'x = 10{,}5'),
               ('x : 9{,}5 = 25', 'x = 25 \\times 9{,}5', 'x = 237{,}5')],
        'b3': [(r'S_{\Delta} = (30 \times 20) : 2', r'\text{cm}^2', '300'),
               (r'S_{\text{thang}} = (42 + 30) \times 18 : 2', r'\text{cm}^2', '648'),
               (r'C_{\text{tròn}} = 2 \times 12 \times 3{,}14', r'\text{cm}', '75{,}36'),
               (r'S_{\text{tròn}} = 10 \times 10 \times 3{,}14', r'\text{dm}^2', '314')]
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

