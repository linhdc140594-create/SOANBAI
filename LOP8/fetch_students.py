import urllib.request, json, sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'apikey': 'sb_publishable_9co-50aMwmxNnE1Bd5Ou3Q_IuTdSZtD',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVsemNxeXB4ZnZleGpwbnh1eGdvIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3ODU4ODU5OSwiZXhwIjoyMDk0MTY0NTk5fQ.qPPEHTYlwRp-2NuynRXbSbrmNvMTJoHQN5KI1LfYerc'
}

url = 'https://ulzcqypxfvexjpnxuxgo.supabase.co/rest/v1/enrollments?select=class_id,status,students(id,student_code,full_name,status)'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    enrollments = json.loads(resp.read().decode('utf-8'))

class_ids = {
    '4aaddb9f-ee67-42df-97ed-f14c84a00014': '2013 TOÁN 8 - TÂY SƠN',
    '43fe96f1-f397-40d2-9aaf-41b9f9601049': '2013 - TOÁN 8 - KT',
    'a509c6e2-4824-4b89-8b7c-1d1452832a3e': '2013 KÈM RIÊNG'
}

for cid, cname in class_ids.items():
    print(f'=== {cname} ===')
    st_list = [e for e in enrollments if e.get('class_id') == cid and e.get('status') == 'active']
    print(f'Total students: {len(st_list)}')
    for e in st_list:
        st = e.get('students')
        if st and st.get('status') == 'active':
            code = st.get('student_code')
            name = st.get('full_name')
            print(f'  - Code: {code}, Name: {name}')
