import scrapy
import scraping.variables_scraping.variables_scraping


class SpiderTransparencies(scrapy.Spider):

    name = 'transparencies'

    def start_requests(self):
        url = variables_scraping.portal_link
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.status)
