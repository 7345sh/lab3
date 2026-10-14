class Book:
    # Инициализация книги с названием и автором
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    # Строковое представление книги (экранируем кавычки)
    def __str__(self) -> str:
        return f"\"{self.title}\", автор — {self.author}"


if __name__ == "__main__":
    book = Book("Преступление и наказание", "Фёдор Достоевский")
    print(book)
    print(f"Название: {book.title}")
    print(f"Автор: {book.author}")
