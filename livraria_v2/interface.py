import tkinter as tk
from tkinter import simpledialog, messagebox, Scrollbar, Text
from gerencimentolivros import GerenciamentoLivros, Livro

class InterfaceGrafica:
    def __init__(self, root):
        self.livraria = GerenciamentoLivros(nome="Magic Books")
        self.root = root
        self.root.title("Magic Books - Livraria")
        self.botoes_interativos()

    def botoes_interativos(self):
        # Configura o layout e os elementos da interface gráfica
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.text_area = Text(self.main_frame, wrap=tk.WORD, font='Garamond')
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = Scrollbar(self.main_frame, command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        # Configura o menu da interface gráfica com opções para interagir com a livraria
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu.add_command(label="Listar Livros", command=self.listar_livros)
        self.menu.add_command(label="Adicionar Livro", command=self.adicionar_livro)
        self.menu.add_command(label="Buscar Livro", command=self.buscar_livro)
        self.menu.add_command(label="Criar Catálogo por Gênero", command=self.criar_catalogo_por_genero)
        self.menu.add_command(label="Reservar Livro", command=self.reservar_livro)
        self.menu.add_command(label="Ver Livros Reservados", command=self.ver_livros_reservados)
        self.menu.add_command(label="Cancelar Reserva", command=self.cancelar_reserva)
        self.menu.add_command(label="Sair", command=self.root.quit)

        # Mensagem de boas-vindas inicial
        self.text_area.insert(tk.END, "Bem-vindo à Livraria Magic Books!\nOnde a magia dos livros ganha vida.\n")

    def listar_livros(self):
        # Exibe a lista de todos os livros disponíveis
        self.text_area.delete(1.0, tk.END)
        livros = self.livraria.listar_livros()
        self.text_area.insert(tk.END, f"--- Lista de Livros ---\n\n{livros}\n")

    def adicionar_livro(self):
        # Adiciona um novo livro ao catálogo solicitando os detalhes ao usuário
        nome = simpledialog.askstring("Adicionar Livro", "Digite o nome do livro:")
        if not nome:
            messagebox.showinfo("Informação", "Operação de adição de livro cancelada.")
            return

        genero = simpledialog.askstring("Adicionar Livro", "Digite o gênero do livro:")
        if not genero:
            messagebox.showinfo("Informação", "Operação de adição de livro cancelada.")
            return

        autor = simpledialog.askstring("Adicionar Livro", "Digite o autor do livro (opcional):") or None
        ano_publicacao = simpledialog.askstring("Adicionar Livro", "Digite o ano de publicação (opcional):") or None
        isbn = simpledialog.askstring("Adicionar Livro", "Digite o ISBN do livro (opcional):") or None

        ano_publicacao = int(ano_publicacao) if ano_publicacao and ano_publicacao.isdigit() else None
        livro = Livro(nome=nome, genero=genero, autor=autor, ano_publicacao=ano_publicacao, isbn=isbn)
        resultado = self.livraria.adicionar_livro(livro)
        messagebox.showinfo("Resultado", resultado)
        self.listar_livros()

    def buscar_livro(self):
        # Busca livros pelo nome e exibe os resultados
        nome = simpledialog.askstring("Buscar Livro", "Digite o nome (ou parte do nome) do livro:")
        resultado = self.livraria.buscar_livro(nome)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"--- Resultado da Busca por '{nome}' ---\n\n{resultado}\n")

    def criar_catalogo_por_genero(self):
        # Cria e exibe um catálogo de livros filtrado pelo gênero
        genero = simpledialog.askstring("Criar Catálogo por Gênero", "Digite o gênero:")
        resultado = self.livraria.criar_catalogo_por_genero(genero)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"--- Catálogo de Livros do Gênero '{genero}' ---\n\n{resultado}\n")

    def reservar_livro(self):
        # Solicita o nome do livro para reservar e atualiza a lista de livros reservados
        nome = simpledialog.askstring("Reservar Livro", "Digite o nome do livro a ser reservado:")
        if nome:
            livro = next((livro for livro in self.livraria.livros if livro.nome == nome), None)
            if livro:
                resultado = self.livraria.reservar_livro(livro)
                messagebox.showinfo("Resultado", resultado)
                self.ver_livros_reservados()
            else:
                messagebox.showinfo("Erro", "Livro não encontrado.")
        else:
            messagebox.showinfo("Informação", "Operação de reserva cancelada.")

    def ver_livros_reservados(self):
        # Exibe a lista de livros reservados
        resultado = self.livraria.ver_livros_reservados()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"--- Livros Reservados ---\n\n{resultado}\n")

    def cancelar_reserva(self):
        # Cancela a reserva de um livro pelo nome e atualiza a lista de livros reservados
        nome = simpledialog.askstring("Cancelar Reserva", "Digite o nome do livro a ser removido da reserva:")
        if nome:
            resultado = self.livraria.cancelar_reserva(nome)
            messagebox.showinfo("Resultado", resultado)
            self.ver_livros_reservados()
        else:
            messagebox.showinfo("Erro", "Operação de cancelamento de reserva cancelada.")

if __name__ == "__main__":
    # Inicia a interface gráfica
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()