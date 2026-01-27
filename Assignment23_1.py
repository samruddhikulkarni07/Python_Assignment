class BookStore:

    NoOfBooks = 0

    def __init__(self,BookName,BookAuthor):
        self.Name = BookName
        self.Author = BookAuthor
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name,"by",self.Author,". No of books:",BookStore.NoOfBooks)

obj1 = BookStore("Indian polity","M.Laxmikant")
obj1.Display()

obj2 = BookStore("Indian Art and Culture","Nitin Singhania")
obj2.Display()

obj3 = BookStore("India after Indipendence","Bipin Chandra")
obj3.Display()