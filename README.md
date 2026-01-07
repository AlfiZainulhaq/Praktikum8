# Praktikum8

## Penjelasan Program (README.md)
Deskripsi Programm lab8.py

Program ini dibuat untuk mengelola daftar nilai mahasiswa menggunakan konsep Object Oriented Programming (OOP) dengan class di Python.

Class dan Method

Class NilaiMahasiswa
Digunakan untuk menyimpan dan mengelola data mahasiswa.

Method tambah()
Menambahkan data mahasiswa berupa nama dan nilai ke dalam list.

Method tampilkan()
Menampilkan seluruh data mahasiswa yang tersimpan.

Method hapus(nama)
Menghapus data mahasiswa berdasarkan nama.

Method ubah(nama)
Mengubah nilai mahasiswa berdasarkan nama.

## Latihan 1
Deskripsi

Program ini merupakan kalkulator sederhana yang menerima dua angka dan satu operator dari pengguna. Program dilengkapi dengan penanganan error agar aman dari kesalahan input.

Penanganan Error

ValueError
Digunakan untuk menangani input yang bukan angka.

ZeroDivisionError
Digunakan untuk mencegah pembagian dengan nol.

Exception (custom error)
Digunakan untuk menampilkan pesan error jika operator yang dimasukkan tidak valid.

## Latihan 2
Deskripsi

Program ini digunakan untuk menghitung rata-rata nilai mahasiswa dari sebuah list yang berisi data angka dan non-angka.

Cara Kerja

Program melakukan iterasi pada setiap elemen list menggunakan for.

Saat menjumlahkan nilai:

Jika data berupa angka, nilai akan dijumlahkan dan dihitung.

Jika data berupa string, akan terjadi TypeError dan program akan melewati data tersebut tanpa berhenti.

Rata-rata dihitung hanya dari data yang valid (angka).

Hasil

Data string seperti 'A' dan 'B' tidak mempengaruhi perhitungan rata-rata.
