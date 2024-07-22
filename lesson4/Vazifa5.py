class Converter:
    def __init__(self, dollar_kursi):
        self.dollar_kursi = dollar_kursi  

    def usd_uzs(self, usd):
        return usd * self.dollar_kursi

    def uzs_usd(self, uzs):
        return uzs / self.dollar_kursi


narx = 12500  
converter = Converter(narx)


dollar_miqdori = 100
almashtirish = converter.usd_uzs(dollar_miqdori)
print(f"{dollar_miqdori} USD {almashtirish} somga teng")

som_miqdori = 1250000
almashtirish = converter.uzs_usd(som_miqdori)
print(f"{som_miqdori} som {almashtirish} USD ga teng")
