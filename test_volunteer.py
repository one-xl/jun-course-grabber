import requests
import json
import urllib.parse

# 1. 目标课程信息
target_id = "2627104598"  # 班号 teachingClassId
course_type = "QXKC"  # 假设是全校课程，也可以试着填 FANKC

# 2. 从用户的报文中提取信息
studentCode = "2023101496"
electiveBatchCode = "0b215876e50f4bd192016ad490e5ed4c"
campus = "2"
isMajor = "1"

token = "ae190584-ce2f-43ee-a042-408475157683"
cookie = "Secure; Secure; _WEU=bKq7L2j6KPkOHle7vQsoCd4SRBodNxWYiDBARyc304OqxktAngGijo..; JSESSIONID=DD5FB95715167A253257AF9D396AC554; JNU_AUTH_VERIFY_TOKEN=Q1rCqyTJRYOxeTZ46C0BNhL9CvMRZLYbjZw/hCuKW5icvp7FuZIwcP8dA0AQG/n3; CASTGC=pAGXtJUsaIR3j7Luq86XRYgDumaZmeaH3bVgWPDkJKFzba+7o2o+yQ==; MOD_AMP_AUTH=MOD_AMP_487d3a40-7765-49ee-bf78-4daa93d4f219; route=80ae6795ea91a965731c5c10fa8d9efa; Secure"

inner_data = {
    "operationType": "1",
    "studentCode": studentCode,
    "electiveBatchCode": electiveBatchCode,
    "teachingClassId": target_id,
    "isMajor": isMajor,
    "campus": campus,
    "teachingClassType": course_type,
}

outer_data = {"data": inner_data}
json_str = json.dumps(outer_data, ensure_ascii=False)
encoded_data = urllib.parse.quote(json_str)
payload = f"addParam={encoded_data}"

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "token": token,
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
    "Origin": "https://jwxk.jnu.edu.cn",
    "Referer": f"https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/*default/grablessons.do?token={token}"
}

print(f"[*] 发送请求: {target_id}")
try:
    res = requests.post("https://jwxk.jnu.edu.cn/xsxkapp/sys/xsxkapp/elective/volunteer.do", headers=headers, data=payload, timeout=10)
    print(f"[*] HTTP Status: {res.status_code}")
    print(f"[*] Response: {res.text}")
except Exception as e:
    print(f"[!] Error: {e}")
