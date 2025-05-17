# *args and **kwargs

### what's different?
name -> variable
*name -> arguments
**name -> keyword arguments

- *args -> menerima banyak arguments posisi (tanpa nama) -> dalam bentuk tuple
- **kwargs -> menerima banyak argumen kata kunci (Dengan nama) -> dalam bentuk dictionary

### `*args` - Positional arguments
`*args` yang digunakan saat kita menerima sejumlah nilai tanpa kita tau berapa banyak nilai tersebut.

### `**kwargs` - Keyword arguments
`**kwargs` digunakan saat kita ingin menerima pasangan ***key=value** yang tidak pasti jumlahnya dan namanya. Nilai-nilai ini dikemas dalam dictonary

### Latihan
1. kalikan semua bilangan yang diberikan, contoh: `data(3,4,2)`
2. gabungkan kalimat, contoh: `kalimat("saya", "anak", "pintar")`
3. print invoice dengan output seperti berikut
   ```json
   {
    "Item": "Laptop",
    "Harga": 15000,
    "Tanggal": 2025-5-7
   }
   ```




