import logging
import requests
import os
from dotenv import load_dotenv


class TelegramHandler(logging.Handler):
    def __init__(self, token, chat_id, nome_robo):
        super().__init__()
        self.token = token
        self.chat_id = chat_id
        self.nome_robo = nome_robo

    def emit(self, record):
        log_entry = self.format(record)
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": f"🚨 **Erro no Robô: {self.nome_robo}!**\n\n```\n{log_entry[-3500:]}\n```",
            "parse_mode": "Markdown"
        }
        try:
            requests.post(url, json=payload, timeout=5)
        except Exception:
            pass


def setup_monitoring(nome_robo, log_filename):
    """
    Configura o monitoramento de forma obrigatória.
    :param nome_robo: Nome exibido no Telegram.
    :param log_filename: Nome do arquivo de log (obrigatório).
    """
    load_dotenv()

    TOKEN = os.getenv(
        "TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    # Garante que o arquivo tenha a extensão .log
    if not log_filename.lower().endswith(".log"):
        log_filename += ".log"

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Handler para o arquivo
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Handler para o Telegram
    tg_handler = TelegramHandler(TOKEN, CHAT_ID, nome_robo)
    tg_handler.setLevel(logging.ERROR)
    tg_handler.setFormatter(formatter)
    logger.addHandler(tg_handler)

    print(
        f"✅ Monitoramento iniciado para [{nome_robo}]. Arquivo: {log_filename}")
