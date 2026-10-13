def balas_pesan(pesan):
    pesan = pesan.lower()

    if "halo" in pesan:
        return "Halo juga! Selamat datang di OXYFANN Bot."
    elif "nama" in pesan:
        return "Saya OXYFANN Bot, asisten otomatis."
    elif "kabar" in pesan:
        return "Saya baik! Ada yang bisa saya bantu?"
    elif "terima kasih" in pesan:
        return "Sama-sama!"
    else:
        return "Maaf, saya belum mengerti pesan itu."


print("=== OXYFANN BOT ===")
print("Ketik 'keluar' untuk berhenti.")

while True:
    pesan = input("Kamu: ")

    if pesan.lower() == "keluar":
        print("Bot: Sampai jumpa!")
        break

    jawaban = balas_pesan(pesan)
    print("Bot:", jawaban)
  
