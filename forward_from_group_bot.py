import argparse
from telethon import TelegramClient, events
import logging

parser = argparse.ArgumentParser(description="Forward Group Messages Bot")
parser.add_argument("--max_messages", type=int, default=100, help="Número máximo de mensagens para encaminhar")
args = parser.parse_args()

api_id = 1234
api_hash = 'xxxxx'

source_group = -11111111111111
destination_group = -11111111111111

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - Forward Group Messages Bot - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')

logging.warning("Iniciando script.")

async def forward_messages(client, source, destination, max_messages):
    @client.on(events.NewMessage(chats=[source]))
    async def message_group_handler(event):
        logging.warning("Mensagem recebida: {0}.".format(event.message.text))

        with open("messages_saved.txt", "a+") as file:
            file.write(event.message.text + '\n')

        with open("messages_saved.txt", "r+") as file:
            lines_in_file = file.readlines()
            if len(lines_in_file) >= max_messages:
                messages = ''.join(lines_in_file)
                logging.warning("Enviando {0} mensagens para o grupo.".format(len(lines_in_file)))
                await client.send_message(destination, '=== INÍCIO MENSAGENS ===')
                await client.send_message(destination, messages, parse_mode='html')
                await client.send_message(destination, '=== FINAL MENSAGENS ===')
                file.truncate(0)

    await client.run_until_disconnected()

with TelegramClient('name', api_id, api_hash) as client:
    logging.warning("Script iniciado com sucesso, ouvindo group_id {0}.".format(source_group))
    client.loop.run_until_complete(forward_messages(client, source_group, destination_group, args.max_messages))