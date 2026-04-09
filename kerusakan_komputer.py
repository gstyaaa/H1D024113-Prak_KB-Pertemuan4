import os

database_kerusakan = {
    "RAM Rusak": {
        "gejala": ["komputer_nyala_tak_gambar", "beep_berulang"],
        "solusi": "Bersihkan pin RAM dengan penghapus, pasang ulang RAM, atau ganti RAM baru."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["komputer_mati_sendiri", "tidak_menyala_sama_sekali"],
        "solusi": "Cek kabel PSU, ganti PSU dengan watt yang lebih tinggi dan berkualitas."
    },
    "Overheat (Prosesor)": {
        "gejala": ["komputer_mati_sendiri", "kipas_berisik"],
        "solusi": "Bersihkan debu pada heatsink, ganti thermal paste, pastikan kipas bekerja normal."
    },
    "VGA Bermasalah": {
        "gejala": ["komputer_nyala_tak_gambar", "layar_berkedip"],
        "solusi": "Bersihkan pin VGA, pasang ulang, atau update driver."
    },
    "Hardisk Corrupt": {
        "gejala": ["lambat_saat_dipakai", "suara_klik_dari_hardisk"],
        "solusi": "Backup data, jalankan chkdsk, dan ganti hardisk jika rusak."
    }
}
semua_gejala = [
    ("komputer_nyala_tak_gambar", "Apakah komputer menyala tapi tidak ada tampilan?"),
    ("beep_berulang", "Apakah terdengar bunyi beep berulang saat booting?"),
    ("komputer_mati_sendiri", "Apakah komputer sering mati sendiri?"),
    ("kipas_berisik", "Apakah kipas prosesor berbunyi keras/berisik?"),
    ("lambat_saat_dipakai", "Apakah komputer terasa sangat lambat?")
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header():
    print("=" * 60)
    print(" SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER")
    print("=" * 60)
    print()

def diagnosa():
    gejala_terpilih = []

    clear_screen()
    tampilkan_header()

    print("Jawab pertanyaan berikut dengan (y/t)\n")

    for i, (kode, pertanyaan) in enumerate(semua_gejala, 1):
        while True:
            jawab = input(f"{i}. {pertanyaan} (y/t): ").lower()
            if jawab in ['y', 't', 'ya', 'tidak']:
                break
            print("Input tidak valid.")

        if jawab in ['y', 'ya']:
            gejala_terpilih.append(kode)

    clear_screen()
    tampilkan_header()

    hasil = []

    for kerusakan, data in database_kerusakan.items():
        gejala_dibutuhkan = data["gejala"]
        jumlah_gejala = len(gejala_dibutuhkan)
        gejala_terpenuhi = sum(1 for g in gejala_dibutuhkan if g in gejala_terpilih)

        if gejala_terpenuhi >= jumlah_gejala * 0.6:
            persentase = (gejala_terpenuhi / jumlah_gejala) * 100
            tingkat = "TINGGI" if persentase >= 75 else "SEDANG"
            hasil.append((kerusakan, data["solusi"], tingkat, persentase))

    hasil.sort(key=lambda x: x[3], reverse=True)

    if hasil:
        print("HASIL DIAGNOSA")
        print("-" * 60)
        for kerusakan, solusi, tingkat, persentase in hasil[:3]:
            print(f"\nKerusakan: {kerusakan}")
            print(f"Tingkat Kepastian: {tingkat} ({persentase:.0f}%)")
            print(f"Solusi: {solusi}")
            print("-" * 60)
    else:
        print("kerusakan yang spesifik tdk ditemukan.")
        print("langsung saja ke service center ngab.")

    print("\nGejala yang dipilih:")
    for kode, pertanyaan in semua_gejala:
        if kode in gejala_terpilih:
            print(f"- {pertanyaan}")

def main():
    while True:
        diagnosa()
        ulang = input("\nUlangi diagnosa? (y/t): ").lower()
        if ulang not in ['y', 'ya']:
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()