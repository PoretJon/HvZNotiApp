from dotenv import load_dotenv
import os, requests


class PushoverNotifier:
    def __init__(self):
        load_dotenv()
        self.pushover_token = os.getenv("PUSHOVER_TOKEN")

    def send_noti(self, ratio, user_id):
        status_code = 0
        while status_code != 200:
            resp = requests.post(
                "https://api.pushover.net:443/1/messages.json",
                data={
                    "token": self.pushover_token,
                    "user": user_id,
                    "message": f"The ratio of humans to zombies is now {ratio}",
                },
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            )
            status_code = resp.status_code
        print("notification sent")
