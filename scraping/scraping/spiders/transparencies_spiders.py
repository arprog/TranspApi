import scrapy


class SpiderTransparencies(scrapy.Spider):

    name = 'transparencies'

    def start_requests(self):
        url = "http://quotes.toscrape.com/page/1/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.status)