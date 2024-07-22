class Convertor:
    def sm_metr(self, sm):
        return sm / 100

    def km_metr(self, km):
        return km * 1000


convertor = Convertor()
natija1 = convertor.sm_metr(200)  
print(natija1)  

natija2 = convertor.km_metr(2)  
print(natija2)  