class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_nilai = []

    def tambah(self, nama, nilai):
        self.data_nilai.append({'nama': nama, 'nilai': nilai})
        print(f"Data mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan(self):
        print("Daftar Nilai Mahasiswa:")
        for data in self.data_nilai:
            print(f"Nama: {data['nama']}, Nilai: {data['nilai']}")

    def hapus(self, nama):
        for i, data in enumerate(self.data_nilai):
            if data['nama'] == nama:
                del self.data_nilai[i]
                print(f"Data mahasiswa {nama} berhasil dihapus.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for data in self.data_nilai:
            if data['nama'] == nama:
                data['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} berhasil diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

# Contoh penggunaan:
daftar_nilai = DaftarNilaiMahasiswa()

daftar_nilai.tambah("Freya", 90)
daftar_nilai.tambah("Firman", 92)
daftar_nilai.tambah("Dimas", 80)

daftar_nilai.tampilkan()

daftar_nilai.hapus("Firman")
daftar_nilai.tampilkan()

daftar_nilai.ubah("Dimas", 90)
daftar_nilai.tampilkan()