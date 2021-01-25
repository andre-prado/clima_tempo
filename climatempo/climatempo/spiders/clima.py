import scrapy
from scrapy_splash import SplashRequest
from datetime import datetime

class ClimaSpider(scrapy.Spider):
    name = 'clima'
    allowed_domains = ['www.tempoagora.com.br']


    script = """
        function main(splash, args)
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(2))
            
            return splash:html()
        end
    """

    def start_requests(self):
        yield SplashRequest(url="https://www.tempoagora.com.br", callback=self.parse, endpoint="execute", args={
            "lua_source": self.script
        })

    def parse(self, response):
        temperatura = response.xpath("//div[@class='weather-temperature']/span[1]/text()").get()
        cidade = response.xpath("normalize-space(//div[@class='weather-temperature']/span[2]/text())").get()
        sensacao_termica = response.xpath("//ul[@data-v-70bf4055][2]/li[@title='Sensação Térmica'][1]/text()").get()
        velocidade_vento = response.xpath("//ul[@data-v-70bf4055][2]/li[@title='Velocidade do vento'][1]/text()").get()
        pressao_atmosferica = response.xpath("//ul[@data-v-70bf4055][2]/li[@title='Pressão atmosférica'][1]/text()").get()
        umidade_relativa = response.xpath("//ul[@data-v-70bf4055][2]/li[@title='Umidade relativa'][1]/text()").get()
        status = response.xpath("//div[@class='hidden-sm col-md-4 col-xs-5']/div/@title").get()
        data = datetime.now()

        yield {
            "temperatura(º)": temperatura.split()[0],
            "status": status,
            "cidade": cidade,
            "sensacao termica(º)": sensacao_termica.split()[0].replace("º",""),
            "velocidade do vento(KM/h)": velocidade_vento.split()[0],
            "pressao atmosferica": pressao_atmosferica.split()[0],
            "umidade relativa(%)": umidade_relativa.split()[0].replace("%",""),
            "data e hora": f"{data.day}/{data.month}/{data.year} - {data.hour}:{data.minute}"
        }
