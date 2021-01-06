import scrapy
from scrapy import linkextractors

class OnionSpider(scrapy.Spider):
    name = "onionspider"
    start_urls = ['https://politics.theonion.com', 'https://entertainment.theonion.com', 'https://ogn.theonion.com', 'https://sports.theonion.com']
    ##Every Onion Article
    
    def parse(self, response):
        
        page = response.url.split('/')[-1]
        filename = 'article-%.html' % page
        #TODO: page title is basically article title
        with open(filename, 'wb') as f:s
            f.write(response.body)