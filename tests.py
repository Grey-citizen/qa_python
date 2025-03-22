import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
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

    def test_get_genre_of_non_existing_book(self, collector):
        assert collector.get_book_genre('Пикник на обочине') is None

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

    def test_get_books_for_children_genre_good_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        books = collector.get_books_for_children()
        assert 'Хоббит' in books

    def test_get_books_for_children_genre_bad_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Фантастика')
        books = collector.get_books_for_children()
        assert 'Сияние' not in books

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Цвет из иных миров')
        collector.add_book_in_favorites('Цвет из иных миров')
        assert 'Цвет из иных миров' in collector.favorites

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
