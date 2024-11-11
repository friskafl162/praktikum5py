# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

while True:
    # Input data mahasiswa
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai_tugas = int(input("Nilai Tugas: "))
    nilai_uts = int(input("Nilai UTS: "))
    nilai_uas = int(input("Nilai UAS: "))

    # Hitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

    # Tambahkan data mahasiswa ke dalam list
    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "tugas": nilai_tugas,
        "uts": nilai_uts,
        "uas": nilai_uas,
        "akhir": nilai_akhir
    })   

    # Tanyakan apakah ingin menambah data lagi
    tambah_data = input("Tambah data(y/t)? ")
    if tambah_data.lower() != 'y':
        break
    
# Cetak tabel data mahasiswa
print("\n| No | Nama     | NIM  | Tugas | UTS | UAS | Akhir |")
print("|----|----------|------|-------|-----|-----|-------|")
print("~" * 5)
for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"| {i:2} | {mhs['nama']:<8} | {mhs['nim']:<4} | {mhs['tugas']:<5} | {mhs['uts']:<3} | {mhs['uas']:<3} | {mhs['akhir']:.2f} |")
