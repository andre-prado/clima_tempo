import schedule
import os
import time



print("Cronograma iniciado")
schedule.every(30).seconds.do(lambda: os.system('scrapy crawl clima'))
print(f"Próximo trabalho está configurado para rodar as {str(schedule.next_run())}")


while True:
    schedule.run_pending()
    time.sleep(1)
