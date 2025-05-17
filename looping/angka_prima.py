# program angka prima 
angka = int(input("Masukkan angka: "))

i = 2

while i < angka:
    pembagi = 2
    prima = True

    # fungsi eliminasi
    while pembagi < i:
        if i % pembagi == 0:
            prima = False
            break
        pembagi += 1
    
    if prima:
        print(i, end=" ")

    i += 1