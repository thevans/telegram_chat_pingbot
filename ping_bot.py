from telethon.sync import TelegramClient, events
import time
import asyncio

api_id = 1234
api_hash = 'xxxxx'

debug_group = -11111111111111
free_group = -11111111111111

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