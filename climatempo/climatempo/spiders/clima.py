import scrapy


class ClimaSpider(scrapy.Spider):
    name = 'clima'
    allowed_domains = ['www.tempoagora.com.br']
    start_urls = ['http://www.tempoagora.com.br/']

    def parse(self, response):
        pass
