class Book:
    def __init__(self,Serial_no,author,Issue_period,copies):
        self.Serial_no=Serial_no
        self.author=author
        self.Issue_period=Issue_period
        self.copies=copies
    def info(self):
        print(f'Serial no.= {self.Serial_no}')
        print(f'Author={self.author}')
        print(f'Issue Period= {self.Issue_period}')
        print(f'Available copies= {self.copies}')
class LibraryManagment:
    def __init__(self):
        self.library={}
    def add_book(self,Serial_no,author,Issue_period,copies):
        if Serial_no in self.library:
            print(f'The book with serial no-{Serial_no}')
        else:
            book=Book(Serial_no,author,Issue_period,copies)
            self.library[Serial_no]=book
            print(f'Book with serial no-{Serial_no} added succesfully')
    def view_book(self):
        if not self.library:
            print('Book not found in record')
        else:
            for book in self.library.values():
                book.info()
                print()
    def search_book(self):
        if not  self.library:
            print('Book not found')
        else:
            print('Book with the given Serial no is found')
    def issue_book(self,Serial_no):
        if Serial_no not in self.library:
             if Serial_no not in self.library:
              print('Book not found')
        else:
            book = self.library[Serial_no]
            if book.copies > 0:
                book.copies -= 1
                print(f'Book issued successfully! Remaining copies: {book.copies}')
            else:
                print('No copies left of this book')
    def return_book(self, Serial_no):
        if Serial_no not in self.library:
            print('Book not found')
        else:
            book = self.library[Serial_no]
            book.copies += 1
            print(f'Book returned successfully! Available copies: {book.copies}')



    
        
BookManager=LibraryManagment()
BookManager.add_book(1, 'Ruskin', 12, 2)
BookManager.add_book(2, 'Premchand', 15, 1)

BookManager.view_book()

BookManager.issue_book(1)
BookManager.issue_book(1)
BookManager.issue_book(1)   

BookManager.return_book(1)
BookManager.search_book(2)
    

                      
