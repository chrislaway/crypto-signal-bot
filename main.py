
import os
import random
import time
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")

MESSAGES = [
    {
        "crypto": "OP (Optimism)",
        "analysis": "Layer 2 con alta attività e crescita di TVL.",
        "entry": "1.45€ - 1.55€",
        "target": "2.20€ entro 2-3 settimane"
    },
    {
        "crypto": "ARPA",
        "analysis": "Progetto promettente con capitalizzazione bassa.",
        "entry": "0.042€ - 0.046€",
        "target": "0.070€"
    },
    {
        "crypto": "CKB (Nervos)",
        "analysis": "Blockchain modulare con forte sviluppo.",
        "entry": "0.009€ - 0.010€",
        "target": "0.015€ entro 2 settimane"
    }
]

def format_message(data):
    return f"""🚀 Nuovo Segnale Cripto

🪙 Criptovaluta: {data['crypto']}
📊 Analisi: {data['analysis']}
🎯 Prezzo d’ingresso: {data['entry']}
📅 Target: {data['target']}

🔗 Non hai un wallet? Aprilo qui:
https://binance.com/signup 🎁 Vinci premi settimanali!
"""

def main():
    bot = Bot(token=TOKEN)
    for msg in random.sample(MESSAGES, 3):
        bot.send_message(chat_id=CHANNEL, text=format_message(msg), parse_mode="HTML")
        time.sleep(5)  # pausa tra i messaggi

if __name__ == "__main__":
    main()
