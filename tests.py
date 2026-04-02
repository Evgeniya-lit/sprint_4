import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_with_valid_title_length(self):
        collector = BooksCollector()
        name_1 = 'Гордость и предубеждение'
        collector.add_new_book(name_1)
        assert name_1 in collector.get_books_genre()

    @pytest.mark.parametrize('name_book',['', 'A'*41])
    def test_add_new_book_with_invalid_title_length(self, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        assert name_book not in collector.get_books_genre()

    def test_set_book_genre_existing_genre_is_set(self):
        collector = BooksCollector()
        book_name = 'Вокруг света за 80 дней'
        book_genre = 'Комедии'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        books = collector.get_books_genre()
        assert books[book_name] == book_genre

    def test_get_book_genre_for_existing_book(self):
        collector = BooksCollector()
        book_name = 'Вокруг света за 80 дней'
        book_genre = 'Комедии'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        genre = collector.get_book_genre(book_name)
        assert genre == book_genre

    def test_get_books_genre_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Каникулы в Простоквашино')
        books_genre = collector.get_books_genre()
        assert books_genre == {'Каникулы в Простоквашино':''}

    @pytest.mark.parametrize('child_book, child_genre',[['Хроники Нарнии','Фантастика'],['Колобок','Мультфильмы'],['Каникулы в Простоквашино','Комедии']])
    def test_get_books_for_children_returns_child_books(self, child_book, child_genre):
        collector = BooksCollector()
        collector.add_new_book(child_book)
        collector.set_book_genre(child_book, child_genre)
        books_children = collector.get_books_for_children()
        assert child_book in books_children

    @pytest.mark.parametrize('name_book, book_genre',[['Десять негритят','Детективы'], ['Лес', 'Ужасы']])
    def test_get_books_for_children_all_books_with_age_rating(self, name_book, book_genre):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, book_genre)
        books_child = collector.get_books_for_children()
        assert books_child == []

    def test_get_books_with_specific_genre_two_books_same_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')
        collector.add_new_book('Шерлок')
        collector.set_book_genre('Шерлок', 'Детективы')
        collector.add_new_book('Лес')
        collector.set_book_genre('Лес', 'Ужасы')
        spec_genre = collector.get_books_with_specific_genre('Детективы')
        assert len(spec_genre) == 2

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок')
        collector.add_book_in_favorites('Шерлок')
        favorites = collector.get_list_of_favorites_books()
        assert  favorites == ['Шерлок']

    def test_delete_book_from_favorites_deletes_book_successfully(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок')
        collector.add_book_in_favorites('Шерлок')
        collector.delete_book_from_favorites('Шерлок')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []

    def test_get_list_of_favorites_books_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Хроники Нарнии')
        collector.add_book_in_favorites('Хроники Нарнии')
        collector.add_new_book('Колобок')
        collector.add_book_in_favorites('Колобок')
        favorites = collector.get_list_of_favorites_books()
        assert favorites ==['Хроники Нарнии','Колобок']

