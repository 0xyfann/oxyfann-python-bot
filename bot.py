
import os
import json
import urllib.request
import urllib.parse
import time

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"

def kirim_pesan(chat_id, teks):
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": teks
    }).encode()

    req = urllib.request.Request(
        BASE_URL + "sendMessage",
        data=data
    )

    urllib.request.urlopen(req, timeout=15)

def balas(pesan):
    pesan = pesan.lower().strip()

    if "halo" in pesan:
        return "Halo juga! 👋 Selamat datang di OXYFANN Bot."
    elif "nama" in pesan:
        return "Saya OXYFANN Bot, asisten otomatis."
    elif "kabar" in pesan:
        return "Saya baik! Ada yang bisa saya bantu?"
    elif "terima kasih" in pesan:
        return "Sama-sama! 😊"
    else:
        return "Maaf, saya belum mengerti. Coba ketik: halo, nama, atau kabar."

offset = 0

print("OXYFANN Telegram Bot aktif!")

while True:
    try:
        url = BASE_URL + "getUpdates?" + urllib.parse.urlencode({
            "offset": offset,
            "timeout": 25
        })

        with urllib.request.urlopen(url, timeout=35) as response:
            hasil = json.loads(response.read().decode())

        for update in hasil.get("result", []):
            offset = update["update_id"] + 1
            pesan = update.get("message", {})
            teks = pesan.get("text")
            chat = pesan.get("chat", {})

            if teks and chat.get("id"):
                kirim_pesan(chat["id"], balas(teks))

    except Exception as error:
        print("Koneksi bermasalah:", error)
        time.sleep(5)
        
