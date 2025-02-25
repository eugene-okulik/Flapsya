class Book:
    pages_material = "бумага"
    presence_text = True

    def __init__(self, title, author, number_of_pages, isbn, is_reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def book_info(self):
        if self.is_reserved:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},"
                  f" материал: {self.pages_material}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages}")


book_1 = Book("Война и мир", "Лев Толстой", 1300, "1234567890", True)
book_2 = Book("1984", "Джордж Оруэлл", 320, "1534567890", False)
book_3 = Book("Анна Каренина", "Лев Толстой", 864, "7834567890", True)
book_4 = Book("Собачье Сердце", "Михаил Булгаков", 352, "6824567890", True)
book_5 = Book("Мастер и Маргарита", "Михаил Булгаков", 296, "2534567890", False)

book_1.book_info()
book_2.book_info()
book_3.book_info()
book_4.book_info()
book_5.book_info()


class SchoolTextbook(Book):

    def __init__(self, title, author, number_of_pages, isbn, is_reserved, item, school_class, availability_tasks):
        super().__init__(title, author, number_of_pages, isbn, is_reserved)
        self.item = item
        self.school_class = school_class
        self.availability_tasks = availability_tasks

    def book_info(self):
        if self.is_reserved:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},"
                  f" предмет: {self.item}, класс: {self.school_class} зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.number_of_pages},"
                  f" предмет: {self.item}, класс: {self.school_class}")


textbook_1 = SchoolTextbook("Алгебра", "Петров", 300, "3234567890",
                            True, "Математика", 9, True)
textbook_2 = SchoolTextbook("Физика", "Петров", 250, "15134567890",
                            False, "Физика", 6, True)
textbook_3 = SchoolTextbook("География", "Антонов", 120, "1234657890",
                            True, "География", 4, True)
textbook_4 = SchoolTextbook("История 20 века", "Иванов", 450, "1232346890",
                            False, "История", 7, True)

textbook_1.book_info()
textbook_2.book_info()
textbook_3.book_info()
textbook_4.book_info()
