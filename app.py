import os
import requests
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = Flask(__name__)

DID = "did:key:z6MkpNsj9a2q7kLr3UmDoMy8nYvePMV3uAhE7SRTT6KWE19U"
# გადავცვალოთ სწორ API მისამართზე
CHECKIN_URL = "https://technocore.chat/api/checkin"

def perform_checkin():
    try:
        payload = {"did": DID}
        response = requests.post(CHECKIN_URL, json=payload, timeout=15)
        print(f"Check-in triggered! Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error during check-in: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(func=perform_checkin, trigger="interval", hours=6, next_run_time=datetime.now())
scheduler.start()

@app.route("/")
def home():
    return "Technocore Bot is active and running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
