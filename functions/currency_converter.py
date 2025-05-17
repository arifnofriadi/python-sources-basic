def idr_to_usd(money, exchange_rate):
    return money / exchange_rate

def usd_to_idr(money, exchange_rate):
    return money * exchange_rate  

def currency_converter(money, from_curency, to_curency):
    """
    Function to convert currency.
    """
    if from_curency == "IDR" and to_curency == "USD":
        return idr_to_usd(money, 16.841)
    elif from_curency == "USD" and to_curency == "IDR":
        return usd_to_idr(money, 16.841)
    else:
        return "Mata uang tidak valid"


# Example usage
input_money = int(input("Masukkan jumlah uang: "))

from_currency = input("Masukkan mata uang asal (IDR/USD): ")
to_currency = input("Masukkan mata uang tujuan (IDR/USD): ")

converted_money = currency_converter(input_money, from_currency, to_currency)

print(converted_money)
