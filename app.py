import os
import time
import requests
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
@app.route('/keepalive')
def home():
    return "Technocore Agent Bot is Active!", 200

MY_DID = os.environ.get("MY_DID", "did:key:z6MkpNsj9a2q7kLr3UmDoMy8nYvePMV3uAhE7SRTT6KWE19U")

def send_checkin():
    url = "https://overheard-five.vercel.app/api/checkin"
    payload = {"did": MY_DID}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Check-in response: {response.status_code}")
    except Exception as e:
        print(f"Error sending check-in: {e}")

def checkin_loop():
    time.sleep(5)
    while True:
        send_checkin()
        time.sleep(900)

Thread(target=checkin_loop, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
  
