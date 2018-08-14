from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", [book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())
print(Tome_Rater)

novel1.set_isbn(9781536831139, Tome_Rater)

#Create a new, empty TomeRater and compare it to the existing one
Tome_Rater2 = TomeRater()
print(Tome_Rater == Tome_Rater2)

#Make the new TomeRater have the same contents as the previously created one
book1 = Tome_Rater2.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater2.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater2.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater2.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater2.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater2.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)
Tome_Rater2.add_user("Alan Turing", "alan@turing.com")
Tome_Rater2.add_user("David Marr", "david@computation.org")
Tome_Rater2.add_user("Marvin Minsky", "marvin@mit.edu", [book1, novel1, nonfiction1])
Tome_Rater2.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater2.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater2.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater2.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater2.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater2.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater2.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater2.add_book_to_user(novel3, "david@computation.org", 4)

print(Tome_Rater == Tome_Rater2)
Tome_Rater2.add_book_to_user(nonfiction1, 'marvin@mit.edu', 1)
#Objects are equal because the list of books and list of users is still the same, even though the contents of the User are different
print(Tome_Rater == Tome_Rater2)

novel4 = Tome_Rater2.create_novel("Snow Crash", "Neal Stephenson", 1100110011)
Tome_Rater2.add_book_to_user(novel4, 'marvin@mit.edu', 2)
#Objects are unequal because the list of books is now different
print(Tome_Rater == Tome_Rater2)

novel5 = Tome_Rater2.create_novel("Second Snow Crash", "Neal Stephenson", 1100110011)
print(Tome_Rater2.get_book_by_isbn(1100110011))