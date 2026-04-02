# Список тестов:
1. test_add_new_book_with_valid_title_length - добавление книги с валидным названием
2. test_add_new_book_with_invalid_title_length - прверяем некорректную длину названия при добавлении книги
3. test_set_book_genre_existing_genre_is_set - успешное установление жанра книге
4. test_get_book_genre_for_existing_book - получение жанра для существующей книги
5. test_get_books_genre_one_book - возвращает словарь с одной книгой
6. test_get_books_for_children_returns_child_books - возвращает книги разрешенные для детей
7. test_get_books_for_children_all_books_with_age_rating - проверяет, что книги с возрастным рейтингом не попадут в список детских книг
8. test_get_books_with_specific_genre_two_books_same_genre - проверяем, что в списке будет всего две книги одного жанра
9. test_add_book_in_favorites_add_one_book - добавляем в список избранного одну книгу
10. test_delete_book_from_favorites_deletes_book_successfully - успешное удаление книги из избранного
11. test_get_list_of_favorites_books_two_books - в список избранного добавлено две книги