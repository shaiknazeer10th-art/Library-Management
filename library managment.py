class Book:
  def __init__(self,book_id,title,author,copies):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.copies = copies

  
  def borrow_book(self):
    if self.copies <= 0:
      print("book is not available")
    else:
      self.copies -= 1

  def return_book(self):
    self.copies += 1
    print("book is returned")

class Member: 
  def __init__(self,name):
    self.name = name
    self.borrowed_books = []

  def borrow_book(self,book:Book):
    if len(self.borrowed_books) >= 3:
      raise ValueError("Member cannot borrow more than 3 books")
    
    book.borrow_book()
    self.borrowed_books.append(book.title)

  def return_book(self,book):
    if book.title not in self.borrowed_books:
      raise ValueError("Member has not borrowed this book")
    
    book.return_book()
    self.borrowed_books.remove(book.title)


class Library:
    books = {}
    members = {}

    @classmethod
    def add_book(cls,book:Book):
      cls.books[book.book_id] = book

    @classmethod
    def register_member(cls,member_obj:Member): 
      if isinstance(cls.members, dict):
          
          cls.members[member_obj.name] = member_obj
      else:
          
          cls.members.append(member_obj)

    @classmethod
    def view_books(cls):
      if not cls.books:
        print("No books available")
        print(f"{'available books:':^40}")

      for book in cls.books.values():
        print(f"Title: {book.title}, Author: {book.author}, Copies: {book.copies}")

    @classmethod
    def generate_borrowed_books_report(cls):
      print(f"{'Library report':^40}") 
      if isinstance(cls.members, dict):
          for member_name, member_obj in cls.members.items():
              if member_obj.borrowed_books:
                  print(f"\nMember: {member_obj.name}")
                  for book_title in member_obj.borrowed_books:
                      print(f"  - {book_title}")
              else:
                  print(f"\nMember: {member_obj.name} has not borrowed any books.")
      else:
          
          for member_obj in cls.members:
              print(f"\nMember: {member_obj.name}")
              if member_obj.borrowed_books:
                  for book_title in member_obj.borrowed_books:
                      print(f"  - {book_title}")
              else:
                  print("  No books borrowed.")


def menu():
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View all Books")
    print("6. Generate Borrowed Books Report")
    print("7. Exit")

while True:
    menu()
    choice= input("Enter your choice: ")
    if choice == "1":
      book_id = input("Enter book ID: ") 
      title = input("Enter book title: ")
      author = input("Enter book author: ")
      copies = int(input("Enter number of copies: "))

      book = Book(book_id, author, title, copies) 
      Library.add_book(book)
      print("Book added successfully")

    elif choice == "2":
      name = input("Enter member name: ")
      member = Member(name)
      Library.register_member(member)
      print("Member registered successfully")

    elif choice == "3":
      member_name = input("Enter member name: ")
      book_title = input("Enter book title: ")

      member = next((m for m in Library.members if m.name == member_name), None)
      book = next((b for b in Library.books.values() if b.title == book_title), None)

      if member in None:
        raise ValueError(f"Member '{member_name}' not found")
      if book in None:
        raise ValueError(f"Book '{book_title}' not found")

      member.borrow_book(book)
      print(f"{member_name} borrowed '{book_title}' succesfully")

    elif choice == "4":
      member_name = input("Enter member name: ")
      book_title = input("Enter book title: ")

      member = next((m for m in Library.members if m.name == member_name), None)
      book = next((b for b in Library.books.values() if b.title == book_title), None)

      if member in None:
        raise ValueError(f"Member '{member_name}' not found")
      if book in None:
        raise ValueError(f"Book '{book_title}' not found")

      member.return_book(book)
      print(f"{member_name} returned'{book_title}'succesfully")

    elif choice == "5":
      Library.view_books()

    elif choice == "6":
      Library.generate_borrowed_books_report()

    elif choice == "7":
      print("Exiting the program")
      break