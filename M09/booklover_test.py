import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        book_reader = BookLover("John Doe", "jd@g.com", "novel")
        test_name = "Test Book"
        test_rating = 5
        book_reader.add_book(test_name, test_rating)
        self.assertTrue(book_reader.has_read(test_name))

    def test_2_add_book(self):
        book_reader = BookLover("John Doe", "jd@g.com", "novel")
        test_name = "Test Book"
        test_rating = 5
        book_reader.add_book(test_name, test_rating)
        book_reader.add_book(test_name, test_rating)
        expected = 1
        actual = len(book_reader.book_list[book_reader.book_list.book_name == test_name])
        self.assertEqual(expected, actual)

    def test_3_has_read(self): 
        book_reader = BookLover("John Doe", "jd@g.com", "novel")
        test_name = "Test Book"
        test_rating = 5
        book_reader.add_book(test_name, test_rating)
        self.assertTrue(book_reader.has_read(test_name))

    def test_4_has_read(self): 
        book_reader = BookLover("John Doe", "jd@g.com", "novel")
        test_name = "Test Book"
        self.assertFalse(book_reader.has_read(test_name))

    def test_5_num_books_read(self): 
        book_reader = BookLover("John Doe", "jd@g.com", "novel")
        test_books = [
            ("To Kill a Mockingbird", 5),
            ("The Great Gatsby", 5),
            ("Twelve Angry Men", 4),
            ("The Call of the Wild", 3.0),
            ("test book", 1),
            ("rest book 2", 0)
        ]
        for book in test_books:
            book_reader.add_book(*book)

        self.assertEqual(len(test_books), book_reader.num_books_read())

    def test_6_fav_books(self):
        book_reader = BookLover("John Doe", "jd@g.com", "novel")
        test_books = [
            ("To Kill a Mockingbird", 5),
            ("The Great Gatsby", 5),
            ("Twelve Angry Men", 4),
            ("The Call of the Wild", 3.0),
            ("test book", 1),
            ("rest book 2", 0)
         ]
        for book in test_books:
            book_reader.add_book(*book)

        actual = len(book_reader.fav_books())
        expected = len([x for x, y in test_books if y > 3])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=3)