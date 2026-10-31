# -*- coding: utf-8 -*-
"""
Script sinh Phiếu bài tập cuối tuần Toán 5 - TUAN_09 với 7 Mã đề (501 -> 507).
Chủ đề: Ki-lô-mét vuông -- Héc-ta -- Các đơn vị đo diện tích -- Số thập phân
Bài 4 và Bài 5: Chuẩn hóa theo chương trình Học kì 1 Lớp 5 (GDPT 2018).
Mỗi mã đề đúng 2 trang A4 in 2 mặt (Tổng 14 trang/file PDF).
"""

import os
import sys
import json
from shared_template import render_tex, render_markdown_answers, compile_and_verify

WEEK_NUM = 9
WEEK_TITLE = 'Ki-lô-mét vuông -- Héc-ta -- Các đơn vị đo diện tích -- Số thập phân'

TOPICS = [
    'Hàng và giá trị của chữ số trong số thập phân',
    'Viết phân số thập phân thành số thập phân',
    'Viết hỗn số thành số thập phân',
    'So sánh hai số thập phân',
    'Sắp xếp các số thập phân theo thứ tự',
    'Làm tròn số thập phân đến hàng đơn vị',
    'Đổi đơn vị diện tích: Héc-ta sang mét vuông (ha -> m2)',
    'Đổi đơn vị diện tích: Ki-lô-mét vuông sang héc-ta (km2 -> ha)',
    'Đổi đơn vị diện tích phức hợp (m2, dm2)',
    'Viết số đo độ dài, khối lượng dưới dạng số thập phân',
    'Bài toán thực tế về héc-ta và diện tích',
    'Tìm số tự nhiên thỏa mãn bất đẳng thức kép'
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'grade5_bai4_bai5_data.json'), 'r', encoding='utf-8') as f:
    g5_bai4_bai5 = json.load(f)[str(WEEK_NUM)]

MA_DE_CONFIGS = [
    {
        'code': '501',
        'c1': ('Chữ số $7$ trong số $45{,}72$ có giá trị là:', r'$\dfrac{7}{10}$', r'$\dfrac{7}{100}$', '$7$', '$70$', 'A'),
        'c2': (r'Phân số thập phân $\dfrac{35}{100}$ viết dưới dạng số thập phân là:', '$3{,}5$', '$0{,}35$', '$0{,}035$', '$35{,}0$', 'B'),
        'c3': (r'Hỗn số $4\dfrac{6}{10}$ viết dưới dạng số thập phân là:', '$4{,}06$', '$46{,}0$', '$4{,}6$', '$0{,}46$', 'C'),
        'c4': (r'Điền dấu thích hợp vào chỗ chấm: $7{,}82 \dots 7{,}819$:', '$>$', '$<$', '$=$', 'Không so sánh được', 'A'),
        'c5': (r'Số bé nhất trong các số $3{,}45;\; 3{,}54;\; 3{,}405;\; 3{,}504$ là:', '$3{,}45$', '$3{,}54$', '$3{,}405$', '$3{,}504$', 'C'),
        'c6': ('Làm tròn số $18{,}6$ đến hàng đơn vị ta được số:', '$18$', '$19$', '$20$', '$18{,}0$', 'B'),
        'c7': (r'$3\,\text{ha} = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$300$', r'$3\,000$', r'$300\,000$', r'$30\,000$', 'D'),
        'c8': (r'$2{,}5\,\text{km}^2 = \dots\,\text{ha}$. Số thích hợp điền vào chỗ chấm là:', '$250$', '$25$', r'$2\,500$', r'$25\,000$', 'A'),
        'c9': (r'$4\,\text{m}^2\,25\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$4{,}25$', '$4{,}025$', '$42{,}5$', '$425$', 'A'),
        'c10': (r'$6\,\text{tấn}\,450\,\text{kg} = \dots\,\text{tấn}$. Số thích hợp điền vào chỗ chấm là:', '$64{,}5$', '$6{,}45$', '$6{,}045$', '$645$', 'B'),
        'c11': (r'Một khu rừng hình chữ nhật có chiều dài $500\,\text{m}$, chiều rộng $200\,\text{m}$. Diện tích khu rừng đó là:', r'$1\,\text{ha}$', r'$10\,\text{ha}$', r'$100\,\text{ha}$', r'$1\,000\,\text{ha}$', 'B'),
        'c12': ('Số tự nhiên $x$ thỏa mãn $4{,}8 < x < 5{,}9$ là:', '$5$', '$4$', '$6$', '$5{,}5$', 'A'),
        'b1': ('$34{,}5 + 28{,}7$', '$72{,}6 - 38{,}4$', '$14{,}2 \\times 4$', '$48{,}6 : 3$'),
        'b1_ans': ('63{,}2', '34{,}2', '56{,}8', '16{,}2'),
        'b2': [('x - 14{,}5 = 32{,}8', 'x = 32{,}8 + 14{,}5', 'x = 47{,}3'),
               ('58{,}4 - x = 24{,}1', 'x = 58{,}4 - 24{,}1', 'x = 34{,}3'),
               ('x \\times 4 = 48{,}8', 'x = 48{,}8 : 4', 'x = 12{,}2'),
               ('x : 5 = 12{,}3', 'x = 12{,}3 \\times 5', 'x = 61{,}5')],
        'b3': [(r'3{,}5\,\text{ha}', r'\text{m}^2', r'35\,000'),
               (r'4\,\text{km}^2\,25\,\text{ha}', r'\text{ha}', '425'),
               (r'5\,\text{m}^2\,45\,\text{dm}^2', r'\text{m}^2', '5{,}45'),
               (r'2\,\text{tấn}\,350\,\text{kg}', r'\text{tấn}', '2{,}35')]
    },
    {
        'code': '502',
        'c1': ('Chữ số $5$ trong số $38{,}452$ có giá trị là:', r'$\dfrac{5}{10}$', r'$\dfrac{5}{100}$', r'$\dfrac{5}{1000}$', '$5$', 'B'),
        'c2': (r'Phân số thập phân $\dfrac{48}{100}$ viết dưới dạng số thập phân là:', '$0{,}048$', '$4{,}8$', '$0{,}48$', '$48{,}0$', 'C'),
        'c3': (r'Hỗn số $7\dfrac{3}{10}$ viết dưới dạng số thập phân là:', '$7{,}3$', '$7{,}03$', '$73{,}0$', '$0{,}73$', 'A'),
        'c4': (r'Điền dấu thích hợp vào chỗ chấm: $9{,}604 \dots 9{,}64$:', '$>$', '$<$', '$=$', 'Không so sánh được', 'B'),
        'c5': (r'Số lớn nhất trong các số $5{,}67;\; 5{,}76;\; 5{,}607;\; 5{,}706$ là:', '$5{,}67$', '$5{,}76$', '$5{,}607$', '$5{,}706$', 'B'),
        'c6': ('Làm tròn số $24{,}3$ đến hàng đơn vị ta được số:', '$24$', '$25$', '$24{,}0$', '$23$', 'A'),
        'c7': (r'$5\,\text{ha} = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$500$', r'$5\,000$', r'$50\,000$', r'$500\,000$', 'C'),
        'c8': (r'$3{,}8\,\text{km}^2 = \dots\,\text{ha}$. Số thích hợp điền vào chỗ chấm là:', '$38$', '$380$', r'$3\,800$', r'$38\,000$', 'B'),
        'c9': (r'$6\,\text{m}^2\,40\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$6{,}04$', '$64{,}0$', '$6{,}4$', '$640$', 'C'),
        'c10': (r'$4\,\text{tấn}\,500\,\text{kg} = \dots\,\text{tấn}$. Số thích hợp điền vào chỗ chấm là:', '$4{,}5$', '$45{,}0$', '$4{,}05$', '$450$', 'A'),
        'c11': (r'Một thửa ruộng hình chữ nhật có chiều dài $400\,\text{m}$, chiều rộng $250\,\text{m}$. Diện tích thửa ruộng đó là:', r'$100\,\text{ha}$', r'$10\,\text{ha}$', r'$1\,\text{ha}$', r'$1\,000\,\text{ha}$', 'B'),
        'c12': ('Số tự nhiên $x$ thỏa mãn $7{,}2 < x < 8{,}3$ là:', '$7$', '$8$', '$9$', '$8{,}5$', 'B'),
        'b1': ('$45{,}6 + 37{,}8$', '$83{,}5 - 46{,}2$', '$15{,}3 \\times 5$', '$52{,}8 : 4$'),
        'b1_ans': ('83{,}4', '37{,}3', '76{,}5', '13{,}2'),
        'b2': [('x - 18{,}6 = 25{,}7', 'x = 25{,}7 + 18{,}6', 'x = 44{,}3'),
               ('64{,}5 - x = 31{,}2', 'x = 64{,}5 - 31{,}2', 'x = 33{,}3'),
               ('x \\times 5 = 65{,}5', 'x = 65{,}5 : 5', 'x = 13{,}1'),
               ('x : 4 = 14{,}2', 'x = 14{,}2 \\times 4', 'x = 56{,}8')],
        'b3': [(r'4{,}2\,\text{ha}', r'\text{m}^2', r'42\,000'),
               (r'5\,\text{km}^2\,60\,\text{ha}', r'\text{ha}', '560'),
               (r'7\,\text{m}^2\,80\,\text{dm}^2', r'\text{m}^2', '7{,}8'),
               (r'3\,\text{tấn}\,500\,\text{kg}', r'\text{tấn}', '3{,}5')]
    },
    {
        'code': '503',
        'c1': ('Chữ số $8$ trong số $62{,}185$ có giá trị là:', r'$\dfrac{8}{10}$', r'$\dfrac{8}{100}$', r'$\dfrac{8}{1000}$', '$8$', 'B'),
        'c2': (r'Phân số thập phân $\dfrac{7}{10}$ viết dưới dạng số thập phân là:', '$0{,}7$', '$0{,}07$', '$7{,}0$', '$0{,}70$', 'A'),
        'c3': (r'Hỗn số $9\dfrac{15}{100}$ viết dưới dạng số thập phân là:', '$9{,}15$', '$9{,}015$', '$91{,}5$', '$0{,}915$', 'A'),
        'c4': (r'Điền dấu thích hợp vào chỗ chấm: $12{,}35 \dots 12{,}305$:', '$<$', '$>$', '$=$', 'Không so sánh được', 'B'),
        'c5': (r'Số bé nhất trong các số $8{,}12;\; 8{,}21;\; 8{,}102;\; 8{,}201$ là:', '$8{,}12$', '$8{,}21$', '$8{,}102$', '$8{,}201$', 'C'),
        'c6': ('Làm tròn số $35{,}7$ đến hàng đơn vị ta được số:', '$35$', '$36$', '$35{,}0$', '$37$', 'B'),
        'c7': (r'$4\,\text{ha} = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$400$', r'$4\,000$', r'$40\,000$', r'$400\,000$', 'C'),
        'c8': (r'$1{,}8\,\text{km}^2 = \dots\,\text{ha}$. Số thích hợp điền vào chỗ chấm là:', '$180$', '$18$', r'$1\,800$', r'$18\,000$', 'A'),
        'c9': (r'$3\,\text{m}^2\,75\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$3{,}075$', '$3{,}75$', '$37{,}5$', '$375$', 'B'),
        'c10': (r'$5\,\text{tấn}\,250\,\text{kg} = \dots\,\text{tấn}$. Số thích hợp điền vào chỗ chấm là:', '$52{,}5$', '$5{,}025$', '$5{,}25$', '$525$', 'C'),
        'c11': (r'Một khu đất hình chữ nhật có chiều dài $600\,\text{m}$, chiều rộng $150\,\text{m}$. Diện tích khu đất đó là:', r'$9\,\text{ha}$', r'$90\,\text{ha}$', r'$900\,\text{ha}$', r'$0{,}9\,\text{ha}$', 'A'),
        'c12': ('Số tự nhiên $x$ thỏa mãn $11{,}6 < x < 12{,}8$ là:', '$11$', '$12$', '$13$', '$12{,}5$', 'B'),
        'b1': ('$28{,}9 + 43{,}5$', '$65{,}4 - 29{,}1$', '$16{,}2 \\times 4$', '$58{,}5 : 5$'),
        'b1_ans': ('72{,}4', '36{,}3', '64{,}8', '11{,}7'),
        'b2': [('x - 23{,}4 = 35{,}8', 'x = 35{,}8 + 23{,}4', 'x = 59{,}2'),
               ('72{,}8 - x = 45{,}3', 'x = 72{,}8 - 45{,}3', 'x = 27{,}5'),
               ('x \\times 3 = 54{,}6', 'x = 54{,}6 : 3', 'x = 18{,}2'),
               ('x : 6 = 11{,}5', 'x = 11{,}5 \\times 6', 'x = 69')],
        'b3': [(r'2{,}8\,\text{ha}', r'\text{m}^2', r'28\,000'),
               (r'3\,\text{km}^2\,15\,\text{ha}', r'\text{ha}', '315'),
               (r'6\,\text{m}^2\,35\,\text{dm}^2', r'\text{m}^2', '6{,}35'),
               (r'4\,\text{tấn}\,250\,\text{kg}', r'\text{tấn}', '4{,}25')]
    },
    {
        'code': '504',
        'c1': ('Chữ số $4$ trong số $71{,}349$ có giá trị là:', r'$\dfrac{4}{10}$', r'$\dfrac{4}{100}$', r'$\dfrac{4}{1000}$', '$4$', 'B'),
        'c2': (r'Phân số thập phân $\dfrac{62}{100}$ viết dưới dạng số thập phân là:', '$6{,}2$', '$0{,}62$', '$0{,}062$', '$62{,}0$', 'B'),
        'c3': (r'Hỗn số $5\dfrac{8}{10}$ viết dưới dạng số thập phân là:', '$5{,}08$', '$58{,}0$', '$5{,}8$', '$0{,}58$', 'C'),
        'c4': (r'Điền dấu thích hợp vào chỗ chấm: $15{,}702 \dots 15{,}72$:', '$>$', '$<$', '$=$', 'Không so sánh được', 'B'),
        'c5': (r'Số lớn nhất trong các số $6{,}85;\; 6{,}58;\; 6{,}805;\; 6{,}508$ là:', '$6{,}85$', '$6{,}58$', '$6{,}805$', '$6{,}508$', 'A'),
        'c6': ('Làm tròn số $42{,}4$ đến hàng đơn vị ta được số:', '$42$', '$43$', '$42{,}0$', '$41$', 'A'),
        'c7': (r'$6\,\text{ha} = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$600$', r'$6\,000$', r'$60\,000$', r'$600\,000$', 'C'),
        'c8': (r'$4{,}2\,\text{km}^2 = \dots\,\text{ha}$. Số thích hợp điền vào chỗ chấm là:', '$420$', '$42$', r'$4\,200$', r'$42\,000$', 'A'),
        'c9': (r'$5\,\text{m}^2\,60\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$5{,}06$', '$5{,}6$', '$56{,}0$', '$560$', 'B'),
        'c10': (r'$3\,\text{tấn}\,750\,\text{kg} = \dots\,\text{tấn}$. Số thích hợp điền vào chỗ chấm là:', '$3{,}75$', '$37{,}5$', '$3{,}075$', '$375$', 'A'),
        'c11': (r'Một công viên hình chữ nhật có chiều dài $800\,\text{m}$, chiều rộng $250\,\text{m}$. Diện tích công viên đó là:', r'$2\,\text{ha}$', r'$20\,\text{ha}$', r'$200\,\text{ha}$', r'$2\,000\,\text{ha}$', 'B'),
        'c12': ('Số tự nhiên $x$ thỏa mãn $15{,}4 < x < 16{,}5$ là:', '$15$', '$16$', '$17$', '$16{,}2$', 'B'),
        'b1': ('$53{,}8 + 29{,}6$', '$91{,}7 - 54{,}3$', '$18{,}4 \\times 3$', '$64{,}8 : 6$'),
        'b1_ans': ('83{,}4', '37{,}4', '55{,}2', '10{,}8'),
        'b2': [('x - 16{,}7 = 42{,}5', 'x = 42{,}5 + 16{,}7', 'x = 59{,}2'),
               ('81{,}6 - x = 38{,}2', 'x = 81{,}6 - 38{,}2', 'x = 43{,}4'),
               ('x \\times 6 = 78{,}6', 'x = 78{,}6 : 6', 'x = 13{,}1'),
               ('x : 3 = 16{,}4', 'x = 16{,}4 \\times 3', 'x = 49{,}2')],
        'b3': [(r'5{,}6\,\text{ha}', r'\text{m}^2', r'56\,000'),
               (r'6\,\text{km}^2\,40\,\text{ha}', r'\text{ha}', '640'),
               (r'8\,\text{m}^2\,50\,\text{dm}^2', r'\text{m}^2', '8{,}5'),
               (r'1\,\text{tấn}\,750\,\text{kg}', r'\text{tấn}', '1{,}75')]
    },
    {
        'code': '505',
        'c1': ('Chữ số $9$ trong số $53{,}891$ có giá trị là:', r'$\dfrac{9}{10}$', r'$\dfrac{9}{100}$', r'$\dfrac{9}{1000}$', '$9$', 'B'),
        'c2': (r'Phân số thập phân $\dfrac{85}{100}$ viết dưới dạng số thập phân là:', '$8{,}5$', '$0{,}85$', '$0{,}085$', '$85{,}0$', 'B'),
        'c3': (r'Hỗn số $8\dfrac{4}{10}$ viết dưới dạng số thập phân là:', '$8{,}04$', '$84{,}0$', '$8{,}4$', '$0{,}84$', 'C'),
        'c4': (r'Điền dấu thích hợp vào chỗ chấm: $20{,}15 \dots 20{,}148$:', '$>$', '$<$', '$=$', 'Không so sánh được', 'A'),
        'c5': (r'Số bé nhất trong các số $7{,}34;\; 7{,}43;\; 7{,}304;\; 7{,}403$ là:', '$7{,}34$', '$7{,}43$', '$7{,}304$', '$7{,}403$', 'C'),
        'c6': ('Làm tròn số $29{,}8$ đến hàng đơn vị ta được số:', '$29$', '$30$', '$29{,}0$', '$31$', 'B'),
        'c7': (r'$7\,\text{ha} = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$700$', r'$7\,000$', r'$70\,000$', r'$700\,000$', 'C'),
        'c8': (r'$3{,}5\,\text{km}^2 = \dots\,\text{ha}$. Số thích hợp điền vào chỗ chấm là:', '$350$', '$35$', r'$3\,500$', r'$35\,000$', 'A'),
        'c9': (r'$4\,\text{m}^2\,65\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$4{,}65$', '$4{,}065$', '$46{,}5$', '$465$', 'A'),
        'c10': (r'$5\,\text{tấn}\,125\,\text{kg} = \dots\,\text{tấn}$. Số thích hợp điền vào chỗ chấm là:', '$51{,}25$', '$5{,}125$', '$5{,}0125$', '$512{,}5$', 'B'),
        'c11': (r'Một nông trường hình chữ nhật có chiều dài $500\,\text{m}$, chiều rộng $300\,\text{m}$. Diện tích nông trường đó là:', r'$15\,\text{ha}$', r'$150\,\text{ha}$', r'$1{,}5\,\text{ha}$', r'$15\,000\,\text{ha}$', 'A'),
        'c12': ('Số tự nhiên $x$ thỏa mãn $23{,}5 < x < 24{,}7$ là:', '$23$', '$24$', '$25$', '$24{,}5$', 'B'),
        'b1': ('$36{,}7 + 45{,}8$', '$74{,}2 - 38{,}6$', '$17{,}5 \\times 4$', '$73{,}5 : 5$'),
        'b1_ans': ('82{,}5', '35{,}6', '70', '14{,}7'),
        'b2': [('x - 27{,}3 = 34{,}9', 'x = 34{,}9 + 27{,}3', 'x = 62{,}2'),
               ('68{,}4 - x = 29{,}5', 'x = 68{,}4 - 29{,}5', 'x = 38{,}9'),
               ('x \\times 4 = 72{,}8', 'x = 72{,}8 : 4', 'x = 18{,}2'),
               ('x : 5 = 15{,}6', 'x = 15{,}6 \\times 5', 'x = 78')],
        'b3': [(r'1{,}75\,\text{ha}', r'\text{m}^2', r'17\,500'),
               (r'2\,\text{km}^2\,80\,\text{ha}', r'\text{ha}', '280'),
               (r'4\,\text{m}^2\,65\,\text{dm}^2', r'\text{m}^2', '4{,}65'),
               (r'5\,\text{tấn}\,125\,\text{kg}', r'\text{tấn}', '5{,}125')]
    },
    {
        'code': '506',
        'c1': ('Chữ số $6$ trong số $84{,}267$ có giá trị là:', r'$\dfrac{6}{10}$', r'$\dfrac{6}{100}$', r'$\dfrac{6}{1000}$', '$6$', 'B'),
        'c2': (r'Phân số thập phân $\dfrac{19}{100}$ viết dưới dạng số thập phân là:', '$1{,}9$', '$0{,}19$', '$0{,}019$', '$19{,}0$', 'B'),
        'c3': (r'Hỗn số $6\dfrac{7}{10}$ viết dưới dạng số thập phân là:', '$6{,}07$', '$67{,}0$', '$6{,}7$', '$0{,}67$', 'C'),
        'c4': (r'Điền dấu thích hợp vào chỗ chấm: $18{,}409 \dots 18{,}41$:', '$>$', '$<$', '$=$', 'Không so sánh được', 'B'),
        'c5': (r'Số lớn nhất trong các số $9{,}42;\; 9{,}24;\; 9{,}402;\; 9{,}204$ là:', '$9{,}42$', '$9{,}24$', '$9{,}402$', '$9{,}204$', 'A'),
        'c6': ('Làm tròn số $51{,}3$ đến hàng đơn vị ta được số:', '$51$', '$52$', '$51{,}0$', '$50$', 'A'),
        'c7': (r'$8\,\text{ha} = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$800$', r'$8\,000$', r'$80\,000$', r'$800\,000$', 'C'),
        'c8': (r'$5{,}4\,\text{km}^2 = \dots\,\text{ha}$. Số thích hợp điền vào chỗ chấm là:', '$540$', '$54$', r'$5\,400$', r'$54\,000$', 'A'),
        'c9': (r'$9\,\text{m}^2\,20\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$9{,}02$', '$9{,}2$', '$92{,}0$', '$920$', 'B'),
        'c10': (r'$3\,\text{tấn}\,600\,\text{kg} = \dots\,\text{tấn}$. Số thích hợp điền vào chỗ chấm là:', '$3{,}6$', '$36{,}0$', '$3{,}06$', '$360$', 'A'),
        'c11': (r'Một khu sinh thái hình chữ nhật có chiều dài $700\,\text{m}$, chiều rộng $400\,\text{m}$. Diện tích khu sinh thái đó là:', r'$28\,\text{ha}$', r'$280\,\text{ha}$', r'$2{,}8\,\text{ha}$', r'$28\,000\,\text{ha}$', 'A'),
        'c12': ('Số tự nhiên $x$ thỏa mãn $30{,}7 < x < 31{,}9$ là:', '$30$', '$31$', '$32$', '$31{,}5$', 'B'),
        'b1': ('$48{,}5 + 36{,}9$', '$86{,}3 - 49{,}5$', '$19{,}2 \\times 3$', '$85{,}2 : 4$'),
        'b1_ans': ('85{,}4', '36{,}8', '57{,}6', '21{,}3'),
        'b2': [('x - 31{,}5 = 26{,}8', 'x = 26{,}8 + 31{,}5', 'x = 58{,}3'),
               ('85{,}2 - x = 47{,}6', 'x = 85{,}2 - 47{,}6', 'x = 37{,}6'),
               ('x \\times 5 = 85{,}5', 'x = 85{,}5 : 5', 'x = 17{,}1'),
               ('x : 4 = 18{,}3', 'x = 18{,}3 \\times 4', 'x = 73{,}2')],
        'b3': [(r'6{,}25\,\text{ha}', r'\text{m}^2', r'62\,500'),
               (r'7\,\text{km}^2\,35\,\text{ha}', r'\text{ha}', '735'),
               (r'9\,\text{m}^2\,20\,\text{dm}^2', r'\text{m}^2', '9{,}2'),
               (r'3\,\text{tấn}\,600\,\text{kg}', r'\text{tấn}', '3{,}6')]
    },
    {
        'code': '507',
        'c1': ('Chữ số $3$ trong số $92{,}374$ có giá trị là:', r'$\dfrac{3}{10}$', r'$\dfrac{3}{100}$', r'$\dfrac{3}{1000}$', '$3$', 'A'),
        'c2': (r'Phân số thập phân $\dfrac{56}{100}$ viết dưới dạng số thập phân là:', '$5{,}6$', '$0{,}56$', '$0{,}056$', '$56{,}0$', 'B'),
        'c3': (r'Hỗn số $3\dfrac{9}{10}$ viết dưới dạng số thập phân là:', '$3{,}09$', '$39{,}0$', '$3{,}9$', '$0{,}39$', 'C'),
        'c4': (r'Điền dấu thích hợp vào chỗ chấm: $25{,}62 \dots 25{,}618$:', '$>$', '$<$', '$=$', 'Không so sánh được', 'A'),
        'c5': (r'Số bé nhất trong các số $4{,}78;\; 4{,}87;\; 4{,}708;\; 4{,}807$ là:', '$4{,}78$', '$4{,}87$', '$4{,}708$', '$4{,}807$', 'C'),
        'c6': ('Làm tròn số $64{,}9$ đến hàng đơn vị ta được số:', '$64$', '$65$', '$64{,}0$', '$66$', 'B'),
        'c7': (r'$9\,\text{ha} = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$900$', r'$9\,000$', r'$90\,000$', r'$900\,000$', 'C'),
        'c8': (r'$6{,}5\,\text{km}^2 = \dots\,\text{ha}$. Số thích hợp điền vào chỗ chấm là:', '$650$', '$65$', r'$6\,500$', r'$65\,000$', 'A'),
        'c9': (r'$3\,\text{m}^2\,75\,\text{dm}^2 = \dots\,\text{m}^2$. Số thích hợp điền vào chỗ chấm là:', '$3{,}75$', '$3{,}075$', '$37{,}5$', '$375$', 'A'),
        'c10': (r'$6\,\text{tấn}\,450\,\text{kg} = \dots\,\text{tấn}$. Số thích hợp điền vào chỗ chấm là:', '$64{,}5$', '$6{,}45$', '$6{,}045$', '$645$', 'B'),
        'c11': (r'Một cánh đồng lúa hình chữ nhật có chiều dài $600\,\text{m}$, chiều rộng $350\,\text{m}$. Diện tích cánh đồng đó là:', r'$21\,\text{ha}$', r'$210\,\text{ha}$', r'$2{,}1\,\text{ha}$', r'$21\,000\,\text{ha}$', 'A'),
        'c12': ('Số tự nhiên $x$ thỏa mãn $45{,}2 < x < 46{,}4$ là:', '$45$', '$46$', '$47$', '$46{,}5$', 'B'),
        'b1': ('$57{,}4 + 28{,}8$', '$95{,}1 - 58{,}7$', '$24{,}3 \\times 3$', '$92{,}4 : 6$'),
        'b1_ans': ('86{,}2', '36{,}4', '72{,}9', '15{,}4'),
        'b2': [('x - 24{,}8 = 43{,}6', 'x = 43{,}6 + 24{,}8', 'x = 68{,}4'),
               ('93{,}7 - x = 56{,}4', 'x = 93{,}7 - 56{,}4', 'x = 37{,}3'),
               ('x \\times 3 = 84{,}9', 'x = 84{,}9 : 3', 'x = 28{,}3'),
               ('x : 6 = 14{,}5', 'x = 14{,}5 \\times 6', 'x = 87')],
        'b3': [(r'4{,}8\,\text{ha}', r'\text{m}^2', r'48\,000'),
               (r'8\,\text{km}^2\,50\,\text{ha}', r'\text{ha}', '850'),
               (r'3\,\text{m}^2\,75\,\text{dm}^2', r'\text{m}^2', '3{,}75'),
               (r'6\,\text{tấn}\,450\,\text{kg}', r'\text{tấn}', '6{,}45')]
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

