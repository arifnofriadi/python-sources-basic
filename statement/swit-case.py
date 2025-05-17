# pengecekan generasi

generasi = int(input("Masukkan tahun lahir: "))

baby_boomers = "Generasi Baby Boomers"
x = "Generasi X"
y = "Generasi Milinenal"
z = "Generasi Z"
alpha = "Generasi Alpha"

match generasi:
    case generasi if 1946 <= generasi <= 1964:
        print(baby_boomers)
    case generasi if 1965 <= generasi <= 1980:
        print(x)
    case generasi if 1981 <= generasi <= 1996:
        print(y)
    case generasi if 1997 <= generasi <= 2010:
        print(z)
    case generasi if 2011 <= generasi <= 2024:
        print(alpha)
    case _:
        print("Tahun lahir tidak valid")



