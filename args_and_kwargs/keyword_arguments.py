def profil_pengguna(**data):
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")

profil_pengguna(nama="Arif", kota="Bandung", profesi="Project Manager")