import requests

class Valyuta:
    def __init__(self):
        self.base_url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/'

    def usd_rate(self):
        try:
            response = requests.get(self.base_url)
            data = response.json()
            for currency in data:
                if currency['Ccy'] == 'USD':
                    return float(currency['Rate'])
            raise ValueError('USD topilmadi togri kiriting')
        except requests.exceptions.RequestException as e:
            print(f"Error rate: {e}")
            return None


a = Valyuta()
usd_rate = a.usd_rate()

if usd_rate:
    print(f"Hozirgi dollar narxi: {usd_rate} UZS")
else:
    print("Dollar narxi topilmadi")
