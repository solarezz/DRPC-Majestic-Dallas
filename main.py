import requests
from pypresence import Presence
import time

client_id = "1268152698667008010"  # Replace this with your own client id

r = requests.get('https://api.alt-mp.com/servers/dallas')
count_players = r.json()['playersCount']

rpc = Presence(client_id)
rpc.connect()


rpc.update(
    state="Твой путь - твои правила",
    details=f'Игроков на сервере: {count_players}',
    large_image="majmax",
    large_text="https://majestic-rp.ru",
    start=time.time()
)

try:
    print("Подключение...")
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    print("Отключение...")
    rpc.close()