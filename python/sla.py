class Calculadora:
    def __init__(self, operacao, num, num2):
        self._resultado = 0
        self._operacao = operacao
        self._num = num
        self._num2 = num2

    def somar(self):
        self._resultado = self._num + self._num2

    def subtrair(self):
        self._resultado = self._num - self._num2

    def multiplicar(self):
        self._resultado = self._num * self._num2

    def dividir(self):
        self._resultado = self._num / self._num2

    def get_resultado(self):
        if self._operacao == 1:
            self.somar()
        elif self._operacao == 2:
            self.subtrair()
        elif self._operacao == 3:
            self.multiplicar()
        elif self._operacao == 4:
            self.dividir()
        else:
            print("nao deu")
        return self._resultado

    def reset(self):
        self._resultado = 0


operacao = int(input("Digite a operação (1. +, 2. -, 3. *, 4. /): "))
num = float(input("Digite o valor do numero 1: "))
num = float(input("Digite o valor numero 2: "))
calc = Calculadora(operacao, num, num )

print(calc.get_resultado())  # Saída: 6.0
calc.reset()