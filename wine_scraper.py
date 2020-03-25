import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider

class WineScraper(CrawlSpider):
    name = 'menu-bot'
    allowed_links = []
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(WineScraper, self).__init__(*args, **kwargs)
        self.start_urls.append(kwargs.get("url"))
        self.allowed_links.append(kwargs.get("url_no_protocol"))

    def parse(self, response):
        global menu_links
        found_menu_links = LinkExtractor(allow=r'.*speise.*|menu|essen|food').extract_links(response)
        if len(found_menu_links) > 0:
            for link in found_menu_links:
                if self.allowed_links[0] not in link.url:
                    yield scrapy.Request(link.url, callback=self.log_nothing())
                else:
                    yield scrapy.Request(link.url, callback=self.add_menu_link(link))

    @staticmethod
    def add_menu_link(link):
        global menu_links
        print("ADDED")
        menu_links.append(link.url)

    def log_nothing(self):
        pass


