class Discount():
    percentage = {1:1, 2:0.95, 3:0.9, 4:0.8, 5:0.75}

class Money():
    amount = 0
    
    def __init__(self, amount):
        self.amount = amount
    
    def __eq__(self,other):
        return self.amount == other.amount

    def anadir_cantidad(self, new_amount):
        self.amount = self.amount + new_amount

class Tittle():
    name = None
    
    def __init__(self, name):
        self.name = name

class Book():
    tittle = None

    def __init__(self, name):
        self.tittle = Tittle(name)

    def name(self):
        return self.tittle.name
        
class Cart():
    
    container = {}
    discounts = Discount()

    def __init__(self):
        pass
    
    def price(self):
        total = Money(0)
        while len(self.container) > 0:
            container_size = len(self.container)
            self.delete_uno_de_cada()
            total.anadir_cantidad((8*container_size)*self.discounts.percentage[container_size])
        return total

    def insert_all(self, book, amount):
        for i in range(0, amount):
            self.insert(book)

    def insert(self, book):
        if book.name() not in self.container:
            self.container[book.name()]  = 0
        self.container[book.name()] = self.container[book.name()]+1

    def delete(self):
        if book in self.container:
            if self.container[book] > 1:
                self.container[book] -= 1
            else:
                del self.container[book]        

    def delete_uno_de_cada(self):
        books = list(self.container.keys())
        for book in books:
            self.delete_or_decrement(book)

    def delete_or_decrement(self, book):
        if book not in self.container:
            return
        if self.container[book] > 1:
            self.container[book] -= 1
            return
        del self.container[book]



def test_zero_books():
    c = Cart()
    assert c.price() == Money(0), "Fail test_zero_books"

def test_one_books():
    c = Cart()
    c.insert(Book("A"))
    assert c.price() == Money(8), "Fail test_one_books"

def test_two_diferent_books():
    c = Cart()
    c.insert(Book('A'))
    c.insert(Book('B'))
    assert c.price() == Money(16*0.95), "Fail test_two_diferent_books" + str(c.price().amount)

def test_five_diferent_books():
    c = Cart()
    c.insert(Book('A'))
    c.insert(Book('B'))
    c.insert(Book('C'))
    c.insert(Book('D'))
    c.insert(Book('E'))
    assert c.price() == Money(8*5*0.75), "Fail test_five_diferent_books" + str(c.price().amount)

def test_two_same_books():
    c = Cart()
    c.insert(Book('A'))
    c.insert(Book('A'))
    assert c.price() == Money(16), "Fail test_two_same_books" + str(c.price().amount)

def test_two_same_books_and_one_diferent():
    c = Cart()
    c.insert_all(Book('A'), 2)
    c.insert(Book('B'))
    assert c.price() == Money(8*2*0.95 + 8), "Fail test_two_same_books_and_one_diferent" + str(c.price().amount)

def test_final():
    c = Cart()
    c.insert_all(Book('A'), 5)
    c.insert_all(Book('B'), 3)
    c.insert_all(Book('C'), 2)
    c.insert(Book('D'))
    assert c.price() == Money(8*4*0.80 + 8*3*0.9 + 8*2*0.95 + 8*2)

test_zero_books()
test_one_books()
test_two_diferent_books()
test_five_diferent_books()
test_two_same_books()
test_two_same_books_and_one_diferent()
test_final()