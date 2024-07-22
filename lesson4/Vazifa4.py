class Calculator:
    def plus(self, a, b):
        return a + b
    
    def minus(self, a, b):
        return a - b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("divide bilan ulanishda xatolik")
        return a / b
    
    def multiply(self, a, b):
        return a * b

natija = Calculator()

print("5 + 3 =", natija.plus(5, 3))


print("8 - 4 =", natija.minus(8, 4))


print("10 / 2 =", natija.divide(10, 2))


print("6 * 7 =", natija.multiply(6, 7))
