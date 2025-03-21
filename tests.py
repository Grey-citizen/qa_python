import pytest
from main import BooksCollector

class TestBooksCollector:
    #def test_add_new_book_add_two_books(self):
        #collector = BooksCollector()
        #collector.add_new_book('Гордость и предубеждение и зомби')
        #collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        #assert len(collector.get_books_rating()) == 2


    def test_add_new_book_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Автостопом по галактике')
        collector.add_new_book('Автостопом по галактике')
        assert len(collector.books_genre) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'

    def test_get_genre_of_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    @pytest.mark.parametrize('book_name,expected_genre', [
        ('Пикник на обочине', ''),
        ('Хоббит', 'Фантастика')
    ])
    def test_get_genre_returns_correct_value(self, book_name, expected_genre):
        collector = BooksCollector()
        if book_name == 'Хоббит':
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, "Фантастика")
        elif book_name == 'Пикник на обочине':
            collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize('genre,expected_books', [
        ('Фантастика', ['Солярис']),
        ('Ужасы', ['Оно']),
        ('Детективы', ['Убийство на улице Морг'])
    ])
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Убийство на улице Морг')
        collector.set_book_genre('Убийство на улице Морг', 'Детективы')
        books = collector.get_books_with_specific_genre(genre)
        assert books == expected_books

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        books = collector.get_books_for_children()
        assert 'Хоббит' in books
        assert 'Сияние' not in books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Цвет из иных миров')
        collector.add_book_in_favorites('Цвет из иных миров')
        assert 'Цвет из иных миров' in collector.favorites

    def test_add_book_in_favorites_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Вино из одуванчиков')
        collector.add_book_in_favorites('Вино из одуванчиков')
        collector.add_book_in_favorites('Вино из одуванчиков')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Улитка на склоне')
        collector.add_book_in_favorites('Улитка на склоне')
        collector.delete_book_from_favorites('Улитка на склоне')
        assert 'Улитка на склоне' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Улитка на склоне')
        collector.add_book_in_favorites('Улитка на склоне')
        collector.add_new_book('Вино из одуванчиков')
        collector.add_book_in_favorites('Вино из одуванчиков')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Улитка на склоне', 'Вино из одуванчиков']
