# program mencetak segitiga dengan for loop
print("Segitiga sama kaki dengan for loop")

tinggi = int(input("Masukkan tinggi segitiga: "))

print('\n') 

for i in range(tinggi):
    for j in range(tinggi - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()