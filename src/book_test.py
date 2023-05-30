from author import Author
from book import Book


class BookTest:
    def __init__(*args):
        # TODO Initialize authors below
        author1 = Author("Alex", "badara.jammeh@hotmail.com", "male")
        author2 = Author("Simon", "simon@gmail.com", "female")
        author3 =  Author("Nazar", "nazir2022@gmail.com", "male")

        print(author1)
        print(author2)
        print(author3)  # Test __str__(self)
        author3.set_email("changedemail@email.com")  # Test email setter
        print("name is: " + author3.get_name())  # Test getter
        print("email is: " + author3.get_email())  # Test getter
        print("gender is: " + author3.get_gender())  # Test getter
        print(
            "Author after changed email: "
            + str(author3)  # pay attention! author3 now has a changed email
        )
        print("========================")

        # TODO Initialize books below
        book1 = Book("Harry Potter", author1, 23.5, 4)
        book2 = Book("Simon", author2, 11.5, 2)
        book3 = Book("Victor", author3, 13.8, 6)

        print(book1)
        print(book2)
        print(book3)

        # Test Getters and Setters
        book3.set_price(29.95)
        book3.set_qty(28)
        print("name is: " + book3.get_name())
        print("price is: " + str(book3.get_price()))
        print("qty is: " + str(book3.get_qty()))
        print("Author is: " + str(book3.get_author()))
        # Author's __str__(self)
        print("Author's name is: " + book3.get_author().get_name())
        print("Author's email is: " + book3.get_author().get_email())
        print("Book after changed price and quantity: " + str(book3))
