import requests
import time
from datetime import datetime

USERNAME = "swind"
PASSWORD = "lisa100861"
LOGIN_URL = "https://chunfeng.mentalout.top/api/user/login?turnstile="
CHECKIN_URL = "https://chunfeng.mentalout.top/api/user/checkin"
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "New-API-User": "1317",
    "Origin": "https://chunfeng.mentalout.top",
    "Referer": "https://chunfeng.mentalout.top/login",
    "User-Agent": "Mozilla/5.0"
}

def main():
    print(f"[{datetime.now()}] 开始签到")
    session = requests.Session()
    session.headers.update(HEADERS)
    
    # 登录
    try:
        r = session.post(LOGIN_URL, json={"username": USERNAME, "password": PASSWORD}, timeout=30)
        if r.json().get("success"):
            print(f"[{datetime.now()}] ✅ 登录成功")
        else:
            print(f"[{datetime.now()}] ❌ 登录失败")
            return
    except Exception as e:
        print(f"[{datetime.now()}] ❌ 登录出错: {e}")
        return
    
    # 签到
    try:
        r = session.post(CHECKIN_URL, timeout=30)
        result = r.json()
        if result.get("success"):
            print(f"[{datetime.now()}] ✅ 签到成功")
        elif "已签到" in str(result):
            print(f"[{datetime.now()}] ℹ️ 今日已签到")
        else:
            print(f"[{datetime.now()}] ❌ 签到失败: {result}")
    except Exception as e:
        print(f"[{datetime.now()}] ❌ 签到出错: {e}")

if __name__ == "__main__":
    main()
