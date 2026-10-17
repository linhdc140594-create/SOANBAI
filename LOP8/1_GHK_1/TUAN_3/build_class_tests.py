import os, sys, json, urllib.request, subprocess, re

sys.stdout.reconfigure(encoding='utf-8')

SUPABASE_URL = "https://ulzcqypxfvexjpnxuxgo.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVsemNxeXB4ZnZleGpwbnh1eGdvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3ODU4ODU5OSwiZXhwIjoyMDk0MTY0NTk5fQ.qPPEHTYlwRp-2NuynRXbSbrmNvMTJoHQN5KI1LfYerc"
ANON_KEY = "sb_publishable_9co-50aMwmxNnE1Bd5Ou3Q_IuTdSZtD"

HEADERS = {
    'apikey': ANON_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}'
}

CLASS_CONFIG = [
    {
        'id': '4aaddb9f-ee67-42df-97ed-f14c84a00014',
        'raw_name': '2013 TOÁN 8 - TÂY SƠN',
        'display_name': 'TOÁN 8 - TÂY SƠN',
        'folder_name': 'LOP_TOAN_8_TAY_SON'
    },
    {
        'id': '43fe96f1-f397-40d2-9aaf-41b9f9601049',
        'raw_name': '2013  - TOÁN 8 - KT',
        'display_name': 'TOÁN 8 - KIẾN THIẾT',
        'folder_name': 'LOP_TOAN_8_KT'
    },
    {
        'id': 'a509c6e2-4824-4b89-8b7c-1d1452832a3e',
        'raw_name': '2013 KÈM RIÊNG',
        'display_name': 'TOÁN 8 - KÈM RIÊNG',
        'folder_name': 'LOP_TOAN_8_KEM_RIENG'
    }
]

def fetch_students_for_classes():
    url = f"{SUPABASE_URL}/rest/v1/enrollments?select=class_id,status,students(id,student_code,full_name,status)"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        enrollments = json.loads(resp.read().decode('utf-8'))

    result = {}
    for cfg in CLASS_CONFIG:
        cid = cfg['id']
        st_list = []
        for e in enrollments:
            if e.get('class_id') == cid and e.get('status') == 'active':
                st = e.get('students')
                if st and st.get('status') == 'active':
                    st_list.append({
                        'code': st.get('student_code'),
                        'name': st.get('full_name')
                    })
        # Sort alphabetically by full_name
        st_list.sort(key=lambda s: s['name'].split()[-1] if s['name'] else '')
        result[cid] = st_list
    return result

if __name__ == '__main__':
    data = fetch_students_for_classes()
    for cfg in CLASS_CONFIG:
        cid = cfg['id']
        students = data[cid]
        print(f"{cfg['display_name']}: {len(students)} học sinh")
        for i, s in enumerate(students):
            made = 101 if (i % 2 == 0) else 102
            print(f"  {i+1:02d}. [{s['code']}] {s['name']} -> Đề {made}")
