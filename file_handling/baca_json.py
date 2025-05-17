import json

data = {
    "name": "Arff",
    "age": 23,
    "address": "Bandung",
    "position": "Software Engineer"
}

with open('biodata.json', 'w') as file:
    json.dump(data, file)

with open('biodata.json', 'r') as file:
    data = json.load(file)

print('Nama : ', data['name'])
print('Alamat : ', data['address'])
print('Profesi : ', data['position'])