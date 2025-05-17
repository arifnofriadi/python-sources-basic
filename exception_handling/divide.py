def safe_divide(a, b):
    try:
        return a / b
    except Exception as e:
        print('Terjadi kesalahan : ', e)
        return None
    
print(safe_divide(10, 2))
print(safe_divide(10, 0))
