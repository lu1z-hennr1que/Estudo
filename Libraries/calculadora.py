class Cal:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    def somar(self):
        print(self.valor1+self.valor2)      
        
    def subitrair(self):
        print(self.valor1-self.valor2)
        
    def dividir(self):
        print(self.valor1/self.valor2)
        
    def multiplicar(self):
        print(self.valor1*self.valor2)
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"   
cal = Cal(30, 50)
print(cal.dividir)
cal.somar
cal.multiplicar
cal.subitrair   