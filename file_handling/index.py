# menulis file
with open('index.txt', 'w') as file:
    file.write('Pengenalan file handling\n')

# menambah file (text)
with open('index.txt', 'a') as file:
    file.write('Tujuan dari file handling\n')

# membaca file
with open('index.txt', 'r') as file:
    value = file.read()
    print(value)


