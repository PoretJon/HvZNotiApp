import mechanicalsoup


class Scraper:
    def __init__(self, url):
        self.url = url
        self.browser = mechanicalsoup.StatefulBrowser()
        self.browser.open(url)

    def get_player_count(self):
        return self.browser.page.find_all(id="humancountnumber")[0].text

    def get_zombie_count(self):
        return self.browser.page.find_all(id="zombiecountnumber")[0].text
