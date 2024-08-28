from telethon.sync import TelegramClient
import asyncio
import argparse
import datetime
import logging

# Configurações do script
api_id = 1234  # Seu ID da API do Telegram
api_hash = 'xxxxx'  # Seu hash secreto da API do Telegram
phone_number = "+55...."
free_group = -11111111111111

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - Scrtipt de agendamento de mensagems do grupo free - %(levelname)s - %('
                           'message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

client = TelegramClient(f'session_name_ping_script', api_id, api_hash)


async def send_live_message(time_for_message):
    schedule_date = datetime.datetime.fromtimestamp(time_for_message)
    logging.info(f'Agendando comando /live para {schedule_date}')
    await client.send_message(free_group, '/live', schedule=schedule_date)


async def send_tiktok_message(time_for_message):
    schedule_date = datetime.datetime.fromtimestamp(time_for_message)
    logging.info(f'Agendando comando /live para {schedule_date}')
    await client.send_message(free_group, '/tiktok', schedule=schedule_date)


async def execute_interval(interval):
    logging.info(f"Executando o agendamento das mensagens a cada {int(interval/60)} minutos...")
    alternate = False
    count = 0
    day_duration = 24 * 60 * 60
    total_interactions = day_duration / interval

    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    initial_timestamp = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 0, 0, 0)
    seconds_initial_timestamp = int(initial_timestamp.timestamp())

    while total_interactions > count:
        time_for_message = seconds_initial_timestamp + (count * interval)

        if alternate:
            await send_live_message(time_for_message)
        else:
            await send_tiktok_message(time_for_message)

        alternate = not alternate
        count += 1

    logging.info(f"Agendamento concluído")

async def main():
    """Função principal do script."""
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))

    parser = argparse.ArgumentParser()
    parser.add_argument("--intervalo", type=int, default=15, help="intervalo entre as mensagems em minutos.")
    args = parser.parse_args()

    interval = args.intervalo * 60

    logging.info("Conectado à conta do Telegram.")
    await execute_interval(interval)
    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
