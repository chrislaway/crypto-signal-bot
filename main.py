
import os
import random
import time
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME").replace("@", "")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

MESSAGES = [
    {
        "crypto": "OP (Optimism)",
        "analysis": "Layer 2 molto attivo con TVL in crescita.",
        "entry": "1.45€ - 1.55€",
        "target": "2.20€ entro 2-3 settimane"
    },
    {
        "crypto": "ARPA",
        "analysis": "Bassa capitalizzazione e forte movimento.",
        "entry": "0.042€ - 0.046€",
        "target": "0.070€"
    },
    {
        "crypto": "CKB (Nervos)",
        "analysis": "Blockchain modulare con alto potenziale.",
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

def send_message(text):
    payload = {
        "chat_id": f"@{CHANNEL}",
        "text": text
    }
    requests.post(URL, data=payload)

def main():
    for msg in random.sample(MESSAGES, 3):
        send_message(format_message(msg))
        time.sleep(5)

if __name__ == "__main__":
    main()
