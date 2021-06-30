class Calculadora:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


#instanciando classe
calculadora = Calculadora(10,2)
print(calculadora.a)
print(calculadora.b)

print(calculadora.soma())
print(calculadora.sub())
print(calculadora.mult())
print(calculadora.div())