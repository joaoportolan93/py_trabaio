class Livro:
    def __init__(self, titulo, autor, ISBN, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponibilidade = disponibilidade
    
    def adicionar(self, quantidade):
        self.disponibilidade += quantidade
        print(f"{quantidade} cópias de '{self.titulo}' foram adicionadas. Total disponível: {self.disponibilidade}")
        
    def buscar(self, nome_livro):
        if self.titulo.lower() == nome_livro.lower():
            print(f"Livro encontrado: {self.titulo} por {self.autor}. Disponibilidade: {self.disponibilidade}")
        else:
            print("Livro não encontrado.")
    
    def emprestar(self):
        if self.disponibilidade > 0:
            self.disponibilidade -= 1
            print(f"Você retirou '{self.titulo}'. Cópias restantes: {self.disponibilidade}")
        else:
            print(f"Desculpe, '{self.titulo}' está indisponível para empréstimo.")
        
    def devolver(self):
        self.disponibilidade += 1
        print(f"Você devolveu '{self.titulo}'. Cópias disponíveis: {self.disponibilidade}")

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

class Usuario:
    def __init__(self, nome_usuario, id, livros_emprestados):
        self.nome_usuario = nome_usuario
        self.id = id
        self.livros_emprestados = livros_emprestados

def main():
    livro = Livro("Percy Jackson e os Olimpianos", "Rick Riordan", 9780756966034, 20)
    autor = Autor("Rick Riordan", "Norte-americano")
    usuario = Usuario("Janice M. Coomes", 1, 2)

    while True:
        print("..................MENU..................")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Sair do programa")
        
        escolha = int(input("Escolha um número: "))

        if escolha == 1:
            quantidade = int(input("Quantas cópias deseja adicionar? "))
            livro.adicionar(quantidade)
        elif escolha == 2:
            nome_livro = input("Escreva o nome do livro que queira buscar: ")
            livro.buscar(nome_livro)
        elif escolha == 3:
            livro.emprestar()
        elif escolha == 4:
            livro.devolver()
        elif escolha == 5:
            print("Encerrando o programa...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
