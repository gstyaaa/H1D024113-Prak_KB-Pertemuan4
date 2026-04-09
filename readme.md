# Sistem Pakar Diagnosa Kerusakan Komputer Console

## Deskripsi singkat
Program ini adalah sistem pakar sederhana berbasis Python yang digunakan untuk mendiagnosa kerusakan komputer berdasarkan gejala yang dipilih pengguna.

Sistem menggunakan pendekatan rule-based (berbasis aturan) dengan mencocokkan gejala yang dipilih dengan data kerusakan yang tersedia.

---

## Cara Kerja

1. Pengguna menjawab 5 pertanyaan (ya/tidak)
2. Jawaban disimpan sebagai gejala terpilih
3. Sistem membandingkan gejala dengan database
4. Jika minimal 60% gejala cocok → dianggap valid
5. Hasil ditampilkan berdasarkan kecocokan tertinggi

---

## Struktur Program

### 1. Database Kerusakan
```python
database_kerusakan = { ... }
```
Berisi:
- Nama kerusakan
- Daftar gejala
- Solusi

---

### 2. Daftar Gejala
```python
semua_gejala = [ ... ]
```
Berisi:
- Kode gejala
- Pertanyaan ke user

---

### 3. Fungsi Utama

#### `diagnosa()`
- Mengambil input user
- Menyimpan gejala yang dipilih
- Menghitung kecocokan
- Menampilkan hasil diagnosa

#### `clear_screen()`
Membersihkan terminal agar tampilan rapi

#### `main()`
Loop utama program (ulang diagnosa)

---

## Contoh Output

```
HASIL DIAGNOSA
------------------------------------------------------------

Kerusakan: RAM Rusak
Tingkat Kepastian: TINGGI (100%)
Solusi: Bersihkan pin RAM...

------------------------------------------------------------
```
## Cara Menjalankan

```bash
python kerusakan_komputer.py
```

---