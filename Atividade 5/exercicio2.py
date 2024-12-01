
# Diagrama de Atividade - Exercício 2 Atividade 5

class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.authenticated = False

    def authenticate_librarian(self):
        print("Sistema: Bibliotecária autenticada com sucesso.")
        self.authenticated = True

    def search_book(self, book_code):
        print(f"Sistema: Buscando livro com código '{book_code}'...")
        return self.books.get(book_code)

    def add_book(self, book_code, book_data):
        print(f"Sistema: Adicionando novo livro '{book_data['title']}' com código '{book_code}'.")
        self.books[book_code] = book_data

    def edit_book(self, book_code, new_data):x
        print(f"Sistema: Editando dados do livro com código '{book_code}'.")
        self.books[book_code] = new_data

    def delete_book(self, book_code):
        print(f"Sistema: Excluindo livro com código '{book_code}'.")
        self.books.pop(book_code, None)

    def validate_book_data(self, book_data):
        print("Sistema: Validando dados do livro...")
        if not book_data.get("isbn") or len(book_data["isbn"]) != 13:
            return False, "ISBN inválido."
        if not book_data.get("year") or len(str(book_data["year"])) != 4:
            return False, "Ano de publicação inválido."
        return True, ""

    def display_book(self, book_code):
        book = self.books.get(book_code)
        if book:
            print(f"Dados do Livro - Código: {book_code}, Título: {book['title']}")
        else:
            print(f"Livro com código '{book_code}' não encontrado.")


# Simulando o fluxo principal e alternativos
def manage_books():
    library = LibrarySystem()
    library.authenticate_librarian()

    # Fluxo principal: busca e edição de livro
    book_code = "12345"
    if library.search_book(book_code):
        library.display_book(book_code)
        new_data = {"title": "Novo Título", "isbn": "1234567890123", "year": 2023}
        valid, message = library.validate_book_data(new_data)
        if valid:
            library.edit_book(book_code, new_data)
        else:
            print(f"Erro de validação: {message}")
    else:
        print("Livro não encontrado. Adicionando um novo livro.")
        # Fluxo alternativo: inclusão de novo livro
        new_data = {"title": "Novo Livro", "isbn": "1234567890123", "year": 2023}
        valid, message = library.validate_book_data(new_data)
        if valid:
            library.add_book(book_code, new_data)
        else:
            print(f"Erro de validação: {message}")

    # Fluxo alternativo: exclusão de livro
    delete_confirmation = True  # Simulando confirmação da exclusão
    if delete_confirmation:
        library.delete_book(book_code)


# Executar fluxo de gerenciamento de livros
manage_books()
