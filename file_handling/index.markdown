# File Handling
Fungsi pada python untuk membaca, mengedit dan menulis file berupa `.csv`, `.txt`, dll.

# Fungsi Dasar 
| Fungsi           | Keterangan       |
|------------------|------------------|
| `open()`         | membuka file     |
| `read()`         | membaca file     |
| `write()`        | menulis file (overwrite)    |
| `close()`        | menutup file     |
| `with open(...) as` | cara terbaik untuk membuka file (otomatis menutup file) |

# Metode dalam Open
| Metode            | Keterangan        |
|-------------------|-------------------|
| `r`               | Baca file         |
| `w`               | Menulis file      |
| `a`               | Menambah file     |
| `x`               | Membuka file      |
| `b`               | biner (binay mode)|
| `t`               | text (default)    |

# Tugas 
- Buat file data.txt dan isi dengan data berikut
  - Nama 
  - Umur
  - Hobby

# Baca File `.json`
| Fungsi              | Penjelasan      |
|---------------------|-----------------|
| `json.load(file)`   | membaca file json dan mengubah isinya menjadi string|
| `json.load(string)` | membaca json dari string bukan file |
| `json.dump(data, file)` | menulis data ke file dalam bentuk json |
| `json.dump(data)` | menulis data ke string json |


