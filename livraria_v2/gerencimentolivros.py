from livros import Livro

class GerenciamentoLivros:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []  # Lista para armazenar os livros disponíveis na livraria
        self.livros_reservados = []  # Lista para armazenar os livros reservados
        self.adicionar_livros_exemplo()  # Adiciona alguns livros de exemplo à livraria

    def adicionar_livros_exemplo(self):
        # Cria instâncias de livros de exemplo e as adiciona à lista de livros
        livro1 = Livro("Harry Potter e a Pedra Filosofal", "Fantasia", "J.K Rowling", 1997, "1234567890")
        livro2 = Livro("Cronicas De Narnia A Ultima Batalha", "Fantasia", "C. S. Lewis", 2020, "2345678901")
        livro3 = Livro("O Senhor dos Anéis", "Fantasia", "J.R.R Tolkien", 1954, "3456789012")
        livro4 = Livro("O Assassinato no Expresso do Oriente", "Mistério", "Agatha Christie", 1934, "4567890123")
        livro5 = Livro("O Falcão Maltês", "Mistério", "Dashiell Hammett", 1930, "5678901234")
        livro6 = Livro("O Código Da Vinci", "Mistério", "Dan Brown", 2003, "6789012345")
        livro7 = Livro("Duna", "Ficção Científica", "Frank Herbert", 1965, "7890123456")
        livro8 = Livro("Neuromancer", "Ficção Científica", "William Gibson", 1984, "8901234567")
        livro9 = Livro("1984", "Ficção Científica", "George Orwell", 1949, "9012345678")
        livro10 = Livro("A Mão Esquerda da Escuridão", "Ficção Científica", "Ursula K. Le Guin", 1969, "0123456789")

        self.livros.extend([livro1, livro2, livro3, livro4, livro5, livro6, livro7, livro8, livro9, livro10])

    def listar_livros(self):
        # Retorna uma string formatada com a lista de todos os livros disponíveis ou uma mensagem de aviso se não houver livros
        return "\n\n".join(str(livro) for livro in self.livros) if self.livros else "Nenhum livro disponível na livraria."

    def adicionar_livro(self, livro):
        # Adiciona um livro ao catálogo se o objeto fornecido for uma instância da classe Livro
        if isinstance(livro, Livro):
            self.livros.append(livro)
            return f"O livro '{livro.nome}' foi adicionado ao catálogo com sucesso!"
        else:
            return "Erro: Só é possível adicionar instâncias da classe Livro."

    def buscar_livro(self, nome):
        # Busca livros pelo nome (ou parte do nome) e retorna uma string formatada com os resultados
        nome_lower = nome.lower()
        encontrados = [livro for livro in self.livros if nome_lower in livro.nome.lower()]
        return "\n\n".join(str(livro) for livro in encontrados) if encontrados else f"Nenhum livro encontrado com o nome contendo '{nome}'."

    def criar_catalogo_por_genero(self, genero):
        # Cria um catálogo de livros filtrado pelo gênero e retorna uma string formatada com os resultados
        catalogo = [livro for livro in self.livros if genero.lower() in livro.genero.lower()]
        return "\n\n".join(str(livro) for livro in catalogo) if catalogo else f"Nenhum livro encontrado do gênero '{genero}'."

    def reservar_livro(self, livro):
        # Reserva um livro se ele ainda não estiver reservado
        if livro not in self.livros_reservados:
            self.livros_reservados.append(livro)
            return f"O livro '{livro.nome}' foi reservado com sucesso!"
        return f"O livro '{livro.nome}' já está reservado."

    def ver_livros_reservados(self):
        # Retorna uma lista formatada dos livros reservados ou uma mensagem se não houver reservas
        return "\n\n".join(str(livro) for livro in self.livros_reservados) if self.livros_reservados else "Não há livros reservados."

    def cancelar_reserva(self, nome):
        # Cancela a reserva de um livro pelo nome (ou parte do nome) e remove-o da lista de livros reservados
        nome_lower = nome.lower()
        encontrados = [livro for livro in self.livros_reservados if nome_lower in livro.nome.lower()]
        if encontrados:
            for livro in encontrados:
                self.livros_reservados.remove(livro)
            return f"A reserva dos livros com nome '{nome}' foi cancelada."
        return f"Nenhum livro encontrado com o nome contendo '{nome}' nas reservas."