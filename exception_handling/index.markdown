# Exception Handling
mekanisme dalam python untuk menangani error atau kondisi tidak terduga yang terjadi selama eksekusi program.

## Penggunaan `Try`, `Except` dan `Finally`
- `try` blok kode yang berpotensi menyebabkan error
- `except` blok yang menangani error yang terjadi
- `finally` blok selalu kita jalankan, walaupun error ataupun tidak

## Beberapa Exception Umum
- `ZeroDivisionError` pembagian dengan nol
- `ValueError` nilai yang tidak sesuai
- `TypeError` tipe data yang tidak sesuai
- `IndexError` akses indeks yang tidak ada di dalam list
- `KeyError` mengakses kunci yang tidak ada di dalam dictonary


## Study Case
Program untuk menghitung rata-rata nilai inputan pengguna, menangani jika inputan bukan angka dan pembagian nol

## Latihan
Latihan 1: Buat program yang menerima dua angka dari pengguna dan membaginya. Tangani ValueError dan ZeroDivisionError.

Latihan 2: Buat program yang meminta input index dan menampilkan elemen dari list [10, 20, 30]. Tangani IndexError dan ValueError.

Latihan 3: Buat program yang membaca data dictionary dan menangani KeyError jika kunci tidak ada.




