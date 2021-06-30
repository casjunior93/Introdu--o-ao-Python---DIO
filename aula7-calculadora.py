class Calculadora:

    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

calculadora = Calculadora()

print(calculadora.soma(10,2))
print(calculadora.sub(10,2))
print(calculadora.mult(10,2))
print(calculadora.div(10,2))