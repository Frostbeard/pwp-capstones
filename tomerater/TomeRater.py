class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def email_is_valid(self, email):
        if '@' in email:
            if '.com' in email:
                return True
            elif '.edu' in email:
                return True
            elif '.org' in email:
                return True
        else:
            return False

    def get_email(self):
        return self.email

    def change_email(self, address):
        if self.email_is_valid(self, address):
            self.email = address
            print("{n}'s email updated to {e}".format(n=self.name, e=self.email))
        else:
            print("{e} is not a valid email address!".format(e=address))

    def __repr__(self):
        return "User {n}, Email {e}, books read {b}".format(n=self.name, e=self.email, b=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        count = 0
        for rating in self.books.values():
            if rating is not None:
                total += rating
                count += 1
        return total / count


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return self.title

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn, tomerater=None):
        if tomerater is None:
            print("Missing TomeRater object.  Can't check for ISBN duplication. ISBN not updated.")
            return
        if isbn not in tomerater.get_isbns():
            self.isbn = isbn
            print("{n}'s ISBN has been updated to {i}".format(n=self.title, i=self.isbn))
        else:
            print("ISBN {i} already exists.  {t}'s ISBN has not been updated.".format(i=isbn, t=self.title))

    def add_rating(self, rating):
        if rating is not None and rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid rating!")

    def get_average_rating(self):
        count = 0
        total = 0
        for rating in self.ratings:
            if rating is not None:
                count += 1
                total += rating
        return total / count


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{t} by {a}".format(t=self.title, a=self.author)


class Nonfiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "Users: {u}\nBooks: {b}".format(u=list(self.users.values()), b=self.books)

    def __eq__(self, other):
        if len(self.users) != len(other.users) or len(self.books) != len(other.books):
            return False
        for user in self.users:
            if user not in other.users:
                return False
        for book in self.books:
            if book not in other.books:
                return False
        return True

    def get_isbns(self):
        isbns = []
        for book in self.books:
            isbns.append(book.isbn)
        return isbns

    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def email_is_valid(self, email):
        if '@' in email:
            if '.com' in email:
                return True
            elif '.edu' in email:
                return True
            elif '.org' in email:
                return True
        else:
            return False

    def create_book(self, title, isbn):
        book = self.get_book_by_isbn(isbn)
        if book is None:
            return Book(title, isbn)
        else:
            print("ISBN {i} already exists. Using existing book {b}".format(i=isbn, b=book))
            return book

    def create_novel(self, title, author, isbn):
        book = self.get_book_by_isbn(isbn)
        if book is None:
            return Fiction(title, author, isbn)
        else:
            print("ISBN {i} already exists. Using existing book {b}".format(i=isbn, b=book))
            return book

    def create_non_fiction(self, title, subject, level, isbn):
        book = self.get_book_by_isbn(isbn)
        if book is None:
            return Nonfiction(title, subject, level, isbn)
        else:
            print("ISBN {i} already exists. Using existing book {b}".format(i=isbn, b=book))
            return book

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {e}!".format(e=email))

    def add_user(self, name, email, books=None):
        if self.email_is_valid(email):
            user = User(name, email)
        else:
            print("{e} is not a valid email address".format(e=email))
            return
        if email not in self.users:
            self.users[email] = user
        else:
            print("User with email {e} already exists!".format(e=email))
            return
        if books is not None:
            for book in books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def get_most_read_book(self):
        most_cnt = 0
        most_book = None
        for book, count in self.books.items():
            if count > most_cnt:
                most_cnt = count
                most_book = book
        return most_book

    def highest_rated_book(self):
        high_rate = 0
        high_book = None
        for book in self.books.keys():
            if book.get_average_rating() > high_rate:
                high_rate = book.get_average_rating()
                high_book = book
        return high_book

    def most_positive_user(self):
        high_user = None
        high_rate = 0
        for user in self.users.values():
            if user.get_average_rating() > high_rate:
                high_rate = user.get_average_rating()
                high_user = user
        return high_user
