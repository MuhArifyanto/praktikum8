### PRAKTIKUM 8

# NilaiMahasiswa Class

## Class Methods

### `__init__(self) -> None`
- Initializes an instance of the class with an empty dictionary to store student data.

### `tambah(self, nama: str, nilai: int) -> str`
- Adds a new student to the records with the given name (`nama`) and grade (`nilai`).
- Returns a success message if the student is added, or an error message if the student already exists.

### `tampilkan(self) -> str`
- Displays the list of students and their corresponding grades.
- Returns a message indicating that there is no student data if the records are empty.

### `hapus(self, nama: str) -> str`
- Removes a student from the records based on the provided name (`nama`).
- Returns a success message if the student is deleted, or an error message if the student is not found.

### `ubah(self, nama: str, nilai: int) -> str`
- Updates the grade of an existing student with the provided name (`nama`) to the new grade (`nilai`).
- Returns a success message if the update is successful, or an error message if the student is not found.

```python
# Creating an instance of the Nilai Mahasiswa class
daftar_nilai = DaftarNilaiMahasiswa()

daftar_nilai.tambah("Freya", 90)
daftar_nilai.tambah("Firman", 92)
daftar_nilai.tambah("Dimas", 80)

daftar_nilai.tampilkan()

daftar_nilai.hapus("Firman")
daftar_nilai.tampilkan()

daftar_nilai.ubah("Dimas", 90)
daftar_nilai.tampilkan()

```

## CATATAN 
- Pastikan nama yang diberikan (`nama`) berupa string, dan nilai (`nilai`) berupa bilangan bulat saat menggunakan metode `tambah`, `hapus`, dan `ubah` method.
- Kelas menyediakan templat dasar untuk mengelola catatan siswa dan dapat diperluas untuk menyertakan fitur tambahan berdasarkan kebutuhan spesifik
