import json
import os

import pg8000
from dotenv import load_dotenv
from bot.domain.storage import Storage

load_dotenv()


class StoragePostgres(Storage):
    def _get_connection(self):
        ...