from telethon.sync import TelegramClient, events
import time
import asyncio

api_id = 29383914
api_hash = '840159bfcf1d014d7fd1ff90a6b89352'

debug_group = -1001826665605
free_group = -1001403599306

interval = 1800

with TelegramClient('name', api_id, api_hash) as client:
   def send_live_message():
      client.send_message(debug_group, 'Enviando comando /live...')
      client.send_message(free_group, '/live')
      time.sleep(60)
      client.send_message(debug_group, 'Reenviando comando /live...')
      client.send_message(free_group, '/live')


   def send_tiktok_message():
      client.send_message(debug_group, 'Enviando comando /tiktok...')
      client.send_message(free_group, '/tiktok')
      time.sleep(60)
      client.send_message(debug_group, 'Reenviando comando /tiktok...')
      client.send_message(free_group, '/tiktok')


   def execute_interval(interval):
      print(f"Executando a função a cada {interval} segundos.")
      alternate = False
      while True:
         if alternate:
            send_live_message()
         else:
            send_tiktok_message()

         alternate = not alternate
         # await asyncio.sleep(interval)
         time.sleep(interval)


   asyncio.run(execute_interval(interval))
   client.run_until_disconnected()