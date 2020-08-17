import scrapy

class OnionSpider(scrapy.Spider):
    name = "onion_art_spider"
    
    def start_requests(self):
        return super().start_requests(self):
            urls = [
                'https://politics.theonion.com',
                'https://entertainment.theonion.com',
                'https://sports.theonion.com',
                'https://ogn.theonion.com',
                'https://local.theonion.com'
            ]
            for url in urls:
                yield scrapy.Request