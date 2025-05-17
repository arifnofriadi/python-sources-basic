greetings = lambda name: f"Hello {name}"

sapa = greetings

hasil = (lambda x,y : x**2 + y**2)(4,6)

print(hasil)

bilangan = [10, 8, 3, 1, 9, 4, 2, 5, 6, 7]
filtered_result = map(lambda x : x**2, bilangan)
print(list(filtered_result))

hasil = list(map(lambda x : x**2, bilangan))

print(hasil)