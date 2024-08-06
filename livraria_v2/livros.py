class Livro:
    def __init__(self, nome, genero, autor=None, ano_publicacao=None, isbn=None):
        # Inicializa os atributos do livro
        self.nome = nome
        self.genero = genero
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn

    def __str__(self):
        # Retorna uma representação em string do livro com detalhes
        detalhes = f"Nome: {self.nome}\nGênero: {self.genero}"
        if self.autor:
            detalhes += f"\nAutor: {self.autor}"
        if self.ano_publicacao:
            detalhes += f"\nAno de Publicação: {self.ano_publicacao}"
        if self.isbn:
            detalhes += f"\nISBN: {self.isbn}"
        return detalhes