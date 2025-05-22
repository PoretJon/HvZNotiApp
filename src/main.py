from WebScraper import Scraper

scraper = Scraper("https://hvzrit.club")

while True:
    # main loop

    # run on some interval, idk yet
    human_count = scraper.get_human_count()
    zombie_count = scraper.get_zombie_count()
