from author import Author


class Book:
    def __init__(self, name: str, author:Author, price: float, qty: int):
        self._name = name
        self._author = author
        self._price = price
        self._qty = qty

    def get_name(self) -> str:
        return self._name
    
    def get_author(self) -> Author:
        return self._author
    
    def get_price(self) -> float:
        return self._price
    
    def set_price(self, price):
        self._price = price
    
    def get_qty(self) -> int:
        return self._qty
    
    def set_qty(self, qty):
        self._qty = qty
    

    def __str__(self) -> str:
       return f"Book[name={self._name}, price={self._price}, qty={self._qty} "
author1 = Author("badara", "badara@hotmail.com" ,"male")
book1 = Book("harry potter", author1, 15.5, 5)
print(book1.__str__())