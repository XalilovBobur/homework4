class Mylist:
    def __init__(self) -> None:
        self.data = []

    def add(self, item):
        self.data.append(item)

    def delete(self, item):
        if item in self.data:
            self.data.remove(item)

    def replace(self, olditem, newitem):
        if olditem in self.data:
            index = self.data.index(olditem)
            self.data[index] = newitem

    def clear(self):
        self.data = []


a = Mylist()

a.add(1)
a.add(2)
a.add(3)
a.add(4)

print(a.data)  

a.delete(2)
print(a.data)  

a.replace(3, 4)
print(a.data)  

a.clear()
print(a.data)  