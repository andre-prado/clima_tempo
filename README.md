# clima_tempo
Projeto criado com Scrapy e Splash.<br>
Dados coletados do site *https://www.climatempo.com.br/*<br>
Mongodb foi utilizado como database para guardar as informações coletadas pelo Scrapy.<br>

## Instalando Dependências do Projeto
De preferência utilize um ambiente virtual como o virtualenv para instalar os pacotes<br>
Para não dar erro na instalação dos pacotes, utilize a versão do Python3.8 ou superior<br>
Na raiz do projeto rode o comando a seguir para instalar as depêndencias:<br> 
```pip install -r requirements.txt```

## Splash e Docker
Este scrapy foi criado utilizando Splash e Docker para poder pegar dados da página *tempoagora.com.br* que é gerada em Javascript<br>
O Scrapy não funcionará caso não esteja instalado e rodando o Splash e o Docker<br>
Assumindo que o Docker esteja instalado, instale o Splash com o comando:<br>
```docker pull scrapinghub/splash```<br>

Após o termino do comando a cima, execute o comando a seguir para rodar o Splash:<br>
```docker run -it -p 8050:8050 scrapinghub/splash```<br>
O Splash ficará rodando em *http://localhost:8050/*<br>
Não interrompa o Splash para o Scrapy funcionar normalmente<br>

## Rodando o Scrapy
Acesse a pasta *climatempo* onde terá um arquivo *scrapy.cfg* e execute o comando:<br>
```scrapy crawl clima```<br>
O programa deve funcionar perfeitamente e os dados estarão no Mongodb para visualização.<br>

## Executando o Scrapy a cada uma hora automaticamente
Há um arquivo chamado *cronograma.py* dentro da pasta *climatempo*, a mesma pasta onde foi executado o ```scrapy crawl climatempo```<br>
Ao executar este arquivo o Scrapy ficará sendo executado automaticamente a cada uma hora, *desde que o terminal não seja interrompido*<br>
Para rodar o cronograma:<br>
```python cronograma.py```
