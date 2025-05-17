# persegi dengan for loop
print("Persegi dengan for loop")

sisi = int(input("Masukkan panjang sisi persegi: "))
print('\n')
for i in range(sisi):
    for j in range(sisi):
        print("*", end=" ")
    print()