nilai = int(input("Masukkan nilai: "))

if nilai < 1 or nilai > 100:
    print("Nilai tidak valid! Silakan masukkan nilai antara 1-100")
    exit()

if nilai >= 90 and nilai <= 100:
    print("Grade A")
elif nilai >= 80 and nilai <= 89:
    print("Grade B")
elif nilai >= 70 and nilai <= 79:
    print("Grade C")
elif nilai >= 60 and nilai <= 69:
    print("Grade D")
else:
    print("Grade E")
