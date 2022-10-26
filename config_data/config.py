import os
from dotenv import load_dotenv, find_dotenv

import datetime

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

time_offset = datetime.timezone(datetime.timedelta(hours=3))

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
)
