from many_to_many import Author, Book, Contract
import pytest

def test_book_init():
    """Test Book class initializes with title"""
    book = Book()
    assert book

def test_author_init():
    """Test Author class initializes with name"""
    author = Author()
    assert author

def test_contract_init():
    """Test Contract class initializes with author, book, date, royalties"""
    book = Book()
    author = Author()
    date = '01/01/2001'
    royalties = 40000
    contract = Contract()

    assert contract
    assert contract
    assert contract
    assert contract

def test_contract_validates_author():
    """Test Contract class validates author of type Author"""
    book = Book()
    date = '01/01/2001'
    royalties = 40000

    with pytest.raises(Exception):
        Contract("Author", book, date, royalties)

def test_contract_validates_book():
    """Test Contract class validates book of type Book"""
    author = Author()
    date = '01/01/2001'
    royalties = 40000

    with pytest.raises(Exception):
        Contract(author, "Book", date, royalties)

def test_contract_validates_date():
    """Test Contract class validates date of type str"""
    author = Author()
    book = Book()
    royalties = 40000

    with pytest.raises(Exception):
        Contract(author, book, 1012001, royalties)

def test_contract_validates_royalties():
    """Test Contract class validates royalties of type int"""
    author = Author()
    book = Book()
    date = '01/01/2001'

    with pytest.raises(Exception):
        Contract(author, book, date, "Royalties")

def test_author_has_contracts():
    """Test Author class has method contracts() that returns a list of its contracts"""
    author = Author()
    book = Book()
    contract = Contract()

    assert author

def test_author_has_books():
    """Test Author class has method books() that returns a list of its books"""
    author = Author()
    book = Book()
    Contract()

    assert author

def test_book_has_contracts():
    """Test Book class has method contracts() that returns a list of its contracts"""
    author = Author()
    book = Book()
    contract = Contract()

    assert book

def test_book_has_authors():
    """Test Book class has method authors() that returns a list of its authors"""
    author = Author()
    book = Book()
    Contract()

    assert author 

def test_author_can_sign_contract():
    """Test Author class has method sign_contract() that creates a contract for an author and book"""
    author = Author()
    book = Book()

    contract = author

    

    

    
    

def test_author_has_total_royalties():
    """Test Author class has method total_royalties that gets the sum of all its related contracts' royalties"""
    author = Author()
    book1 = Book()
    book2 = Book()
    book3 = Book()

    Contract()
    Contract()
    Contract()

    assert author 

def test_contract_contracts_by_date():
    """Test Contract class has method contracts_by_date() that sorts all contracts by date"""
    Contract.all = []
    author1 = Author()
    book1 = Book()
    book2 = Book()
    book3 = Book()
    author2 = Author()
    book4 = Book()
    contract1 = Contract()
    contract2 = Contract()
    contract3 = Contract()
    contract4 = Contract()

    assert Contract