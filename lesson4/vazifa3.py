class MyDict:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def delete(self, key):
        if key in self.data:
            del self.data[key]
        else:
            print(f"Kalit '{key}' topilmadi")

    def replace(self, key, new_value):
        if key in self.data:
            self.data[key] = new_value
        else:
            print(f"Kalit '{key}' topilmadi")

    def clear(self):
        self.data = {}


a = MyDict()
a.add('ism', 'Bobur')
print(a.data)  

a.add('yosh', 17)
print(a.data)  

a.delete('ism')
print(a.data)  

a.replace('yosh', 18)
print(a.data)  

a.clear()
print(a.data)  