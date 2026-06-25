import requests
import json
import urllib.parse

studentCode = "2023101496"
electiveBatchCode = "0b215876e50f4bd192016ad490e5ed4c"
campus = "2"
isMajor = "1"

token = "ae190584-ce2f-43ee-a042-408475157683"
cookie = "Secure; Secure; _WEU=bKq7L2j6KPkOHle7vQsoCd4SRBodNxWYiDBARyc304OqxktAngGijo..; JSESSIONID=DD5FB95715167A253257AF9D396AC554; JNU_AUTH_VERIFY_TOKEN=Q1rCqyTJRYOxeTZ46C0BNhL9CvMRZLYbjZw/hCuKW5icvp7FuZIwcP8dA0AQG/n3; CASTGC=pAGXtJUsaIR3j7Luq86XRYgDumaZmeaH3bVgWPDkJKFzba+7o2o+yQ==; MOD_AMP_AUTH=MOD_AMP_487d3a40-7765-49ee-bf78-4daa93d4f219; route=80ae6795ea91a965731c5c10fa8d9efa; Secure"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "token": token,
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
}

def fetch_courses(url, payload_dict):
    json_str = json.dumps(payload_dict, ensure_ascii=False)
    encoded_data = urllib.parse.quote(json_str)
    payload = f"querySetting={encoded_data}"
    
    print(f"[*] Fetching: {url}")
    try:
        res = requests.post(url, headers=headers, data=payload, timeout=10)
        print(f"[*] HTTP Status: {res.status_code}")
        data = res.json()
        if "dataList" in data:
            print(f"[*] Got {len(data['dataList'])} courses")
            if len(data['dataList']) > 0:
                print(f"[*] First course: {data['dataList'][0].get('courseName', data['dataList'][0].get('departmentName', 'unknown'))}")
        else:
            print(f"[*] Response text: {res.text[:200]}")
    except Exception as e:
        print(f"[!] Error: {e}")

payload_prog = {
    "data": {
        "studentCode": studentCode,
        "campus": campus,
        "electiveBatchCode": electiveBatchCode,
        "isMajor": "1",
        "teachingClassType": "FANKC",
        "queryContent": ""
    },
    "pageSize": "100",
    "pageNumber": "0",
    "order": ""
}
fetch_courses("https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/elective/programCourse.do", payload_prog)

payload_rec = payload_prog.copy()
payload_rec["data"]["teachingClassType"] = "TJKC"
fetch_courses("https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/elective/recommendCourse.do", payload_rec)

payload_pub = payload_prog.copy()
payload_pub["data"]["teachingClassType"] = "QXKC"
payload_pub["data"]["queryContent"] = "体育" # test keyword search
fetch_courses("https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/elective/publicCourse.do", payload_pub)

