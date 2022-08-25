#Create a library

class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lenddict={}

    def displayBooks(self):
        print("we have fallowing books in our library:",self.name)
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("book dict has been updated")
        else:
            print(f"book is already used by {self.lenddict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print("book has been added to the book list")

    def returnBook(self,book):
        self.booklist.remove(book)

if __name__ == '__main__':
    harry =Library(['python','rich','harrypotter','c++','clrs'],'codewithharry')

    while(True):
          print("welcome to the {harry.name} library.enter your choice to continue")
          print("1.display book")
          print("2.lend book")
          print("3.add book")
          print("4.return book")
          user_choice =int(input('enter your choice: '))

          if user_choice == 1 :
              harry.displayBooks()

          elif user_choice == 2 :
              book =input("enter the name of the book u want to len")
              user =input("enter your name")
              harry.lendBook(user,book)

          elif user_choice ==3 :
              book = input('enter the name of the book you want to add')
              harry.addBook(book)
          elif user_choice ==4:
              book = input('enter the name of the book you want to add')
              harry.returnBook(book)

          else:
              print('not a valid option')


          print("prsee q to quite and c to continue")
          user_choice2 = input()
          while(user_choice2 != "c" and user_choice2 != "q"):
              if user_choice2 =="q":
                  exit()

              elif user_choice2 == 'c':
                  continue