import random
import time

def cetak_lambat(teks):
    for karakter in teks:
        print(karakter, end='', flush=True)
        time.sleep(0.01)
    print()

def game_matematika():
    print("=" * 60)
    print("   🎮 SELAMAT DATANG DI GAME PETUALANGAN MATH DUNGEON 🎮   ")
    print("=" * 60)
    nama = input("Masukkan nama hero kamu: ")
    print(f"\nHalo {nama}! Kamu memasuki gerbang Dungeon Matematika.")
    print("Kalahkan monster dengan menjawab soal untuk mendapatkan Mahkota Emas!\n")
    time.sleep(1)

    # Daftar soal (Materi: Pangkat, Kuadrat, Mean, Median, Modus, Peluang, Aritmatika, Fungsi Kuadrat)
    soal_list = [
        {
            "materi": "Perpangkatan (Pangkat)",
            "pertanyaan": "Sebuah ramuan ajaib menggandakan kekuatanmu sebanyak 2^5 kali. Berapa kekuatan barumu?",
            "jawaban": "32",
            "pilihan": ["10", "25", "32", "64"]
        },
        {
            "materi": "Akar & Kuadrat",
            "pertanyaan": "Kamu ingin membuat markas berbentuk persegi dengan luas 144 m2. Berapa panjang sisi markasmu?",
            "jawaban": "12",
            "pilihan": ["12", "14", "24", "72"]
        },
        {
            "materi": "Statistika (Mean/Rata-rata)",
            "pertanyaan": "Lima monster menjatuhkan koin emas: 80, 85, 90, 75, dan 70 koin. Berapa rata-rata (mean) koin mereka?",
            "jawaban": "80",
            "pilihan": ["75", "80", "85", "400"]
        },
        {
            "materi": "Statistika (Median/Nilai Tengah)",
            "pertanyaan": "Skor lompatan katakmu dalam 5 kali percobaan: 5, 9, 3, 8, dan 6 meter. Berapa MEDIAN dari skor tersebut?",
            "jawaban": "6",
            "pilihan": ["3", "5", "6", "8"]
        },
        {
            "materi": "Statistika (Modus)",
            "pertanyaan": "Dari peti, kamu dapat 3 permata Merah, 6 Biru, dan 2 Hijau. Warna permata apa yang menjadi MODUS-nya?",
            "jawaban": "biru",
            "pilihan": ["merah", "biru", "hijau", "semua sama"]
        },
        {
            "materi": "Peluang",
            "pertanyaan": "Kamu melempar satu dadu bermata 6. Berapa peluang munculnya angka GENAP? (Tulis dalam pecahan paling sederhana, misal: 1/2)",
            "jawaban": "1/2",
            "pilihan": ["1/6", "1/3", "1/2", "2/3"]
        },
        {
            "materi": "Barisan Aritmatika",
            "pertanyaan": "Kamu menabung koin dengan pola: hari ke-1 (2 koin), hari ke-2 (5 koin), hari ke-3 (8 koin). Berapa koin di hari ke-10?",
            "jawaban": "29",
            "pilihan": ["27", "29", "30", "32"]
        },
        {
            "materi": "Fungsi Kuadrat",
            "pertanyaan": "Lintasan lompat karaktermu mengikuti fungsi f(x) = -x^2 + 4x. Di x berapakah karaktermu mencapai titik TERTINGGI?",
            "jawaban": "2",
            "pilihan": ["1", "2", "4", "-2"]
        }
    ]

    # Mengacak urutan soal agar seru
    random.shuffle(soal_list)
    skor = 0
    nyawa = 3

    for i, soal in enumerate(soal_list):
        if nyawa <= 0:
            break
            
        print("-" * 50)
        cetak_lambat(f"⚔️ TANTANGAN {i+1} [{soal['materi']}] ⚔️")
        cetak_lambat(soal['pertanyaan'])
        
        # Menampilkan pilihan ganda
        for idx, pil in enumerate(soal['pilihan']):
            print(f"   {idx + 1}. {pil}")
            
        print(f"\n❤️ Nyawa: {nyawa} | ⭐ Skor: {skor}")
        jawaban_user = input("Jawab (ketik angka pilihannya atau teks jawabannya): ").strip().lower()

        # Cek jawaban (bisa pakai nomor pilihan atau teks langsung)
        jawaban_benar = soal['jawaban'].lower()
        pilihan_benar_idx = [p.lower() for p in soal['pilihan']].index(jawaban_benar) + 1
        
        if jawaban_user == jawaban_benar or jawaban_user == str(pilihan_benar_idx):
            cetak_lambat("🎉 BENAR! Monster berhasil dikalahkan! (+10 Skor)")
            skor += 10
        else:
            nyawa -= 1
            cetak_lambat(f"💥 SALAH! Kamu terkena serangan monster! (Jawaban benar: {soal['jawaban']})")
            cetak_lambat(f"❤️ Nyawa berkurang! Sisa nyawa: {nyawa}")
        
        time.sleep(1.5)

    # Akhir Game
    print("\n" + "=" * 60)
    if nyawa > 0 and skor == len(soal_list) * 10:
        print(f"🏆 SELAMAT {nama.upper()}! Kamu berhasil menyelesaikan Dungeon dengan SEMPURNA! 🏆")
        print(f"✨ Kamu mendapatkan MAHKOTA EMAS MATEMATIKA dengan Skor: {skor}/{len(soal_list)*10} ✨")
    elif nyawa > 0:
        print(f"👍 KERJA BAGUS {nama}! Kamu berhasil keluar dari Dungeon hidup-hidup!")
        print(f"⭐ Skor Akhir Kamu: {skor}/{len(soal_list)*10}")
    else:
        print("☠️ GAME OVER! Kamu kehabisan nyawa di dalam dungeon. Jangan menyerah, coba lagi! ☠️")
    print("=" * 60)

# Menjalankan game
if __name__ == "__main__":
    game_matematika()
