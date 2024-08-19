print("Olá mundo!")
# comentario
'''
comentario de bloco
'''

x = 10 #inteiro
y = 3.14 #float
nome = "predo"# string
ativo = True #booleano
'''
print(x)
print(y)
print(nome)
print(ativo)
'''

idade = 20
if idade >= 19 :
    print("Você é maior de idade.")
elif idade < 19 and idade > 12: 
    print("Você é adolecente")
else:
    print("Você é pia.")

for i in range(5) :
    print(i)

for i in range (10) :
    print(i)

contador = 0
while contador < 5:
    print(contador)
    contador += 1 
def saudacao(nome): 
    print (f"olá, {nome}") 

saudacao("sim")
class Carro:
    def __init__(self, marca, modelo, ano): 
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def acelerar(self):
        print(f"O {self.modelo} está acelerando.") 
        
    def frear(self):
        print(f"O {self.modelo} está freando")
        
# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.acelerar()  # Saída: O Corolla está acelerando.
