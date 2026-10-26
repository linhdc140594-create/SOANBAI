import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
doc = pymupdf.open(r'd:\GitHub\SOANBAI-main\LOP7\DETHIGHK1\bo-de-on-tap-giua-hoc-ki-1-mon-toan-7-nam-2026-2027-theo-cau-truc-moi.pdf')
print('Total pages:', len(doc))

test_pages = []
sol_pages = []

for p in range(len(doc)):
    text = doc[p].get_text()
    if 'ĐỀ SỐ 11' in text:
        if p < 100:
            test_pages.append(p)
        else:
            sol_pages.append(p)

print('Test Đề 11 pages (0-indexed):', test_pages)
print('Sol Đề 11 pages (0-indexed):', sol_pages)

# Check where Đề 12 starts to find end of Đề 11
for p in range(len(doc)):
    text = doc[p].get_text()
    if 'ĐỀ SỐ 12' in text:
        if p < 100:
            print('Đề 12 test starts at page index:', p)
            break

for p in range(len(doc)):
    text = doc[p].get_text()
    if 'ĐỀ SỐ 12' in text and p >= 100:
        print('Đề 12 sol starts at page index:', p)
        break
