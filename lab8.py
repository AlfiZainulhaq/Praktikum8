## Kode Program (Python – Class Nilai Mahasiswa)
class NilaiMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self, nama, nilai):
        self.data.append({"nama": nama, "nilai": nilai})

    def tampilkan(self):
        if not self.data:
            print("Data kosong")
        else:
            for mhs in self.data:
                print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

    def hapus(self, nama):
        for mhs in self.data:
            if mhs["nama"] == nama:
                self.data.remove(mhs)
                print("Data berhasil dihapus")
                return
        print("Data tidak ditemukan")

    def ubah(self, nama, nilai_baru):
        for mhs in self.data:
            if mhs["nama"] == nama:
                mhs["nilai"] = nilai_baru
                print("Data berhasil diubah")
                return
        print("Data tidak ditemukan")


# Contoh penggunaan
mhs = NilaiMahasiswa()
mhs.tambah("Andi", 85)
mhs.tambah("Budi", 90)
mhs.tampilkan()
mhs.ubah("Andi", 88)
mhs.hapus("Budi")
mhs.tampilkan()

## Diagram Class
+----------------------+
|   NilaiMahasiswa     |
+----------------------+
| - data : list        |
+----------------------+
| + tambah(nama,nilai) |
| + tampilkan()        |
| + hapus(nama)        |
| + ubah(nama)         |
+----------------------+

## Flowchart Program
  Mulai
  |
Buat Object Class
  |
Pilih Method
  |—— tambah data
  |—— tampilkan data
  |—— ubah data
  |—— hapus data
  |
Selesai

