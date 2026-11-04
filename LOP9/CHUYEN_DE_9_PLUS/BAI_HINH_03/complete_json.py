import os
import sys
import json

data = {
  "bai_toan": {
    "ma_bai": "BAI_HINH_03",
    "nguon": "Đề 03 - Tuyển tập 55 Đề Thi Vào Lớp 10",
    "mo_hinh": "Đường tròn đường kính BC, trực tâm tam giác nhọn và tiếp tuyến từ trung điểm đường cao (Bổ đề Euler)",
    "de_bai": "Cho tam giác ABC có ba góc nhọn (AB < AC). Vẽ đường tròn (O) đường kính BC, cắt các cạnh AB, AC lần lượt tại D và E (D khác B, E khác C). Gọi H là giao điểm của BE và CD. a) Chứng minh bốn điểm A, D, H, E cùng nằm trên một đường tròn và xác định tâm I của đường tròn đó. b) Chứng minh AE . AC = AB . AD và tam giác ADE đồng dạng với tam giác ACB. c) Gọi I là trung điểm của AH. Chứng minh IE là tiếp tuyến của đường tròn (O) đường kính BC."
  },
  "luu_y_hieu_chinh": [
    "Kẻ AH vuông góc với BC tại K (do H là trực tâm của tam giác ABC).",
    "Tia HI đối tia HK, tia HE đối tia HB nên góc IHE đối đỉnh với góc KHB.",
    "Điểm H thuộc đoạn BE nên góc HEO chính là góc BEO. Tam giác OBE cân tại O (OB = OE = R) nên góc BEO = góc KBE.",
    "Trong tam giác BHK vuông tại K, ta có góc KHB + góc KBH = 90 độ, do đó góc IEO = góc IEH + góc HEO = 90 độ."
  ],
  "mo_hinh_cot_loi": {
    "bo_de_1": "D, E thuộc (O) đường kính BC nên góc BDC = góc BEC = 90 độ => CD vuông góc AB và BE vuông góc AC. H là giao điểm của hai đường cao nên H là trực tâm của tam giác ABC, dẫn tới AH vuông góc BC tại K.",
    "bo_de_2": "Tam giác AEH vuông tại E có I là trung điểm cạnh huyền AH => trung tuyến IE = IH = IA = AH/2. Do đó tam giác IEH cân tại I => góc IEH = góc IHE = góc KHB (đối đỉnh).",
    "diem_nghen": "Học sinh thường khó khăn khi chứng minh tiếp tuyến mà không nhận ra kỹ thuật chẻ đôi góc: góc IEO = góc IEH + góc HEO, sau đó dùng tính chất hai tam giác cân (đỉnh I và đỉnh O) để đưa tổng hai góc về góc nhọn của tam giác vuông BHK."
  },
  "so_do_tu_duy_nguoc": [
    {
      "tang": 1,
      "tieu_de": "TẦNG 1: XÁC ĐỊNH ĐÍCH ĐẾN",
      "muc_tieu": "Chứng minh IE là tiếp tuyến của (O) tại điểm E",
      "cong_thuc": "IE \\perp OE \\iff \\widehat{IEO} = 90^\\circ \\quad (E \\in (O))",
      "cau_hoi_truy_van": "Để chứng minh IE là tiếp tuyến của (O) tại điểm E đã thuộc (O), ta cần chứng minh điều gì?",
      "phan_tich_logic": "Điểm E đã thuộc đường tròn (O). Do đó, theo dấu hiệu nhận biết tiếp tuyến, ta chỉ cần chứng minh đường thẳng IE vuông góc với bán kính OE tại tiếp điểm E, tức là chứng minh góc IEO = 90 độ.",
      "huong_suy_luan_nguoc": "Làm thế nào để tính hoặc chứng minh góc IEO = 90 độ khi góc này nằm lơ lửng giữa tam giác?"
    },
    {
      "tang": 2,
      "tieu_de": "TẦNG 2: PHÂN RÃ GÓC IEO THÀNH HAI GÓC KỀ NHAU",
      "muc_tieu": "Chẻ góc IEO thành tổng hai góc qua đường cao BE",
      "cong_thuc": "\\widehat{IEO} = \\widehat{IEH} + \\widehat{HEO}",
      "cau_hoi_truy_van": "Tia EH (cũng là tia EB) có nằm giữa hai tia EI và EO không?",
      "phan_tich_logic": "Điểm I thuộc đoạn AH và O thuộc đoạn BC nằm về hai phía khác nhau đối với đường thẳng BE, do đó tia EH nằm giữa hai tia EI và EO. Vậy góc IEO = góc IEH + góc HEO.",
      "huong_suy_luan_nguoc": "Làm sao biến đổi góc IEH và góc HEO về các góc của một tam giác vuông cụ thể?"
    },
    {
      "tang": 3,
      "tieu_de": "TẦNG 3: CHUYỂN GÓC QUA HAI TAM GIÁC CÂN ĐỈNH I VÀ ĐỈNH O",
      "muc_tieu": "Đưa góc IEH và HEO về góc của tam giác BHK",
      "cong_thuc": "\\begin{cases} \\triangle IEH \\text{ cân tại } I \\implies \\widehat{IEH} = \\widehat{IHE} = \\widehat{KHB} \\ (\\text{đối đỉnh}) \\\\ \\triangle OBE \\text{ cân tại } O \\implies \\widehat{HEO} = \\widehat{BEO} = \\widehat{KBH} \\end{cases}",
      "cau_hoi_truy_van": "Đoạn thẳng IE và OE có đặc điểm gì đặc biệt so với các cạnh huyền AH và BC?",
      "phan_tich_logic": "Tam giác AEH vuông tại E có I là trung điểm cạnh huyền AH => trung tuyến EI = IH = AH/2, do đó tam giác IEH cân tại I => góc IEH = góc IHE. Mặt khác tia HI đối tia HK, tia HE đối tia HB nên góc IHE = góc KHB. Tương tự, OE = OB = R nên tam giác OBE cân tại O => góc HEO = góc BEO = góc KBH.",
      "huong_suy_luan_nguoc": "Tổng hai góc KHB + KBH bằng bao nhiêu?"
    },
    {
      "tang": 4,
      "tieu_de": "TẦNG 4: KHÉP GÓC VÀO TAM GIÁC VUÔNG BHK",
      "muc_tieu": "Chứng minh tổng hai góc bằng 90 độ qua tam giác vuông BHK",
      "cong_thuc": "\\widehat{IEO} = \\widehat{KHB} + \\widehat{KBH} = 90^\\circ \\quad (\\text{do } \\triangle BHK \\text{ vuông tại } K)",
      "cau_hoi_truy_van": "Tam giác BHK có phải là tam giác vuông không? Vuông tại đâu?",
      "phan_tich_logic": "H là trực tâm tam giác ABC (giao của hai đường cao BE và CD). Suy ra đường thẳng AH vuông góc với cạnh đối diện BC tại điểm K. Do đó tam giác BHK vuông tại K, suy ra hai góc nhọn phụ nhau: góc KHB + góc KBH = 90 độ.",
      "huong_suy_luan_nguoc": "Cần điều kiện khởi phát nào để khẳng định H là trực tâm?"
    },
    {
      "tang": 5,
      "tieu_de": "TẦNG 5: ĐIỀU KIỆN KHỞI PHÁT - GÓC NỘI TIẾP CHẮN NỬA ĐƯỜNG TRÒN",
      "muc_tieu": "Xác lập hai đường cao BE và CD từ đường kính BC của (O)",
      "cong_thuc": "\\widehat{BDC} = \\widehat{BEC} = 90^\\circ \\implies CD \\perp AB, \\ BE \\perp AC \\implies H \\text{ là trực tâm } \\triangle ABC",
      "cau_hoi_truy_van": "Tại sao CD vuông góc AB và BE vuông góc AC?",
      "phan_tich_logic": "Điểm D và E thuộc đường tròn (O) có đường kính là BC. Theo tính chất góc nội tiếp chắn nửa đường tròn, góc BDC = 90 độ và góc BEC = 90 độ. Do đó CD và BE là hai đường cao của tam giác ABC, giao điểm H là trực tâm.",
      "huong_suy_luan_nguoc": "Chuỗi lập luận đã truy ngược hoàn toàn về giả thiết gốc của bài toán!"
    }
  ],
  "cay_thong_cong_thuc": {
    "dinh_ngon": "\\boxed{\\mathbf{IE \\text{ LÀ TIẾP TUYẾN CỦA } (O) \\text{ TẠI } E}}",
    "than_cay": [
      "\\Updownarrow",
      "IE \\perp OE \\iff \\widehat{IEO} = 90^\\circ \\quad (E \\in (O))",
      "\\Uparrow",
      "\\widehat{IEO} = \\widehat{IEH} + \\widehat{HEO} = 90^\\circ",
      "\\Uparrow",
      "\\widehat{KHB} + \\widehat{KBH} = 90^\\circ \\quad (\\text{trong } \\triangle BHK \\text{ vuông tại } K)",
      "\\Uparrow",
      "AH \\perp BC \\text{ tại } K \\implies H \\text{ là trực tâm của } \\triangle ABC"
    ],
    "hai_nhanh": {
      "nhanh_trai": "\\triangle AEH \\text{ vuông tại } E, \\ I \\text{ là trung điểm } AH \\implies IE = IH = \\frac{AH}{2} \\implies \\widehat{IEH} = \\widehat{IHE} = \\widehat{KHB}",
      "nhanh_phai": "E, B \\in (O) \\implies OE = OB = R \\implies \\triangle OBE \\text{ cân tại } O \\implies \\widehat{HEO} = \\widehat{BEO} = \\widehat{KBH}"
    },
    "goc_re": "\\widehat{BDC} = \\widehat{BEC} = 90^\\circ \\quad (\\text{Góc nội tiếp chắn nửa đường tròn } (O) \\text{ đường kính } BC)"
  },
  "binh_luan_su_pham": {
    "tai_sao_nghi_ra": "Điểm E là giao điểm chung của hai đường tròn (I, AH/2) và (O, BC/2). Đường nối hai đỉnh tam giác vuông là EH. Nhờ có đoạn thẳng EH, góc IEO được tách thành hai phần riêng biệt: một phần thuộc về tam giác cân đỉnh I (tâm của đường tròn ngoại tiếp tứ giác ADHE), một phần thuộc về tam giác cân đỉnh O (tâm của đường tròn đáy BC). Khi chuyển hai góc đáy về đỉnh H và đỉnh B, ta lập tức nhận ra chúng chính là hai góc nhọn của tam giác vuông BHK!",
    "cau_hoi_goi_mo": [
      "Câu 1: Điểm E đã thuộc đường tròn (O) chưa? Vậy muốn chứng minh IE là tiếp tuyến của (O) tại E cần chỉ ra điều gì?",
      "Câu 2: Đoạn thẳng BE chia góc IEO thành tổng của hai góc nào?",
      "Câu 3: Tam giác AEH vuông tại E có I là trung điểm cạnh huyền AH, vậy tam giác IEH có tính chất gì? Góc IEH bằng góc nào?",
      "Câu 4: Bán kính OE và OB có mối liên hệ gì? Khi thay hai góc cân vào, tổng của chúng là hai góc nhọn của tam giác nào?"
    ],
    "sai_lam_thuong_gap": "Học sinh thường quên chỉ ra E thuộc (O) trước khi kết luận vuông góc là tiếp tuyến; hoặc lúng túng khi xác định góc đối đỉnh của góc IHE (dễ nhầm với góc BHD thay vì góc KHB).",
    "bai_tap_tuong_tu": [
      "Bài toán phát triển 1: Chứng minh ID cũng là tiếp tuyến của đường tròn (O) đường kính BC, từ đó suy ra bốn điểm I, D, O, E cùng thuộc một đường tròn và IO vuông góc với DE.",
      "Bài toán phát triển 2: Kéo dài AH cắt (O) tại hai điểm M và N. Chứng minh tứ giác BDNC là hình thang cân và diện tích tam giác ADE bằng S_ABC . cos^2 A."
    ]
  },
  "loi_giai_chi_tiet": [
    {
      "buoc": "Bước 1: Chứng minh tứ giác ADHE nội tiếp đường tròn tâm I đường kính AH",
      "noi_dung": "Vì D, E thuộc đường tròn (O) đường kính BC nên góc BDC = 90 độ và BEC = 90 độ (góc nội tiếp chắn nửa đường tròn). Suy ra CD vuông góc AB và BE vuông góc AC. Xét tứ giác ADHE có góc ADH + AEH = 90 độ + 90 độ = 180 độ, nên tứ giác ADHE nội tiếp đường tròn đường kính AH. Tâm I của đường tròn là trung điểm của AH.",
      "diem": "0.75đ"
    },
    {
      "buoc": "Bước 2: Chứng minh AE . AC = AB . AD và tam giác ADE đồng dạng tam giác ACB",
      "noi_dung": "Xét hai tam giác vuông AEB và ADC có góc A chung, góc AEB = ADC = 90 độ => tam giác AEB đồng dạng tam giác ADC (g-g) => AE/AD = AB/AC => AE . AC = AB . AD. Từ đó suy ra AE/AB = AD/AC, kết hợp với góc A chung => tam giác ADE đồng dạng tam giác ACB (c-g-c).",
      "diem": "0.75đ"
    },
    {
      "buoc": "Bước 3: Thiết lập các tam giác cân đỉnh I và đỉnh O",
      "noi_dung": "Kẻ AH vuông góc BC tại K (do H là trực tâm của tam giác ABC). Trong tam giác vuông AEH vuông tại E có I là trung điểm AH => IE = IH = AH/2 => tam giác IEH cân tại I => góc IEH = IHE. Mà tia HI đối tia HK, tia HE đối tia HB nên góc IHE = KHB (hai góc đối đỉnh) => góc IEH = KHB. Lại có OE = OB = R (bán kính của (O)) nên tam giác OBE cân tại O => góc HEO = BEO = KBH.",
      "diem": "0.75đ"
    },
    {
      "buoc": "Bước 4: Chứng minh IE vuông góc OE và kết luận tiếp tuyến",
      "noi_dung": "Xét tam giác BHK vuông tại K có góc KHB + KBH = 90 độ. Do tia EH nằm giữa hai tia EI và EO nên: góc IEO = IEH + HEO = KHB + KBH = 90 độ. Suy ra IE vuông góc với OE tại điểm E thuộc (O). Vậy IE là tiếp tuyến của đường tròn (O) đường kính BC.",
      "diem": "0.75đ"
    }
  ]
}

out_path = os.path.join(os.path.dirname(__file__), 'so_do_tu_duy_nguoc.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved complete JSON successfully!")

