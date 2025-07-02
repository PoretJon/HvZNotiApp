from WebScraper.scraper import Scraper
from PushoverNotifier.pushover_notifier import PushoverNotifier
import time
import os
from dotenv import load_dotenv

load_dotenv()

scraper = Scraper("https://hvzrit.club")
pushover_notifier = PushoverNotifier()


def run(minutes=30, ratios=[0.7, 0.5, 0.3]):
    #  setup
    notified = {ratio: False for ratio in ratios}
    while True:
        # main loop
        time.sleep(60 * minutes)  # run every 60 seconds, can be adjusted
        # run on some interval, idk yet
        human_count = scraper.get_human_count()
        zombie_count = scraper.get_zombie_count()
        ratio = human_count / zombie_count if zombie_count > 0 else 1
        for ratio in ratios.keys():
            if notified[ratio] is False and ratio >= ratios[ratio]:
                print(f"ratio {ratio} has been hit!")


def tester():
    pushover_notifier.send_noti(0.5, os.getenv("PUSHOVER_USER_ID"))
