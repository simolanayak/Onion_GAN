import scrapy
from scrapy import linkextractors

class OnionSpider(scrapy.Spider):
    name = 'onion-arts'
    allowed_domains = ['https://politics.theonion.com']
    rules = [
        Rule(LinkExtractor(allow=()))
    ]
    
    def parse(self, response):
        page = response.url.split('/')[-1]
        #TODO: page title is basically article title
        with open(filename, 'wb') as f:
            f.write("""whatever the article is""")