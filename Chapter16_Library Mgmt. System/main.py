  
StudentList=["Armaan","Amaan","Sanjita","Aaryan","Suyog"]
BookList=["DSA","SAD","Database","Python","C#"]
IssuedStudents=[]
IssuedBooks=[]
        




def addNewBooks(BookName):
    try:
        if (BookName in BookList):
                print("The Book You Want to Add Already Exists!!!.")
                
        else:     
            BookList.append(BookName)
            print("The Book You Entered has been Added Successfully.")
            print(BookList)


    except Exception as e:
        print(e)


def addNewStudents(StudentName):
    try:
        if (StudentName in StudentList):
                print("The Book You Want to Add Already Exists!!!.")
                
        else:     
            StudentList.append(StudentName)
            print("The Book You Entered has been Added Successfully.")
            print(StudentList)


    except Exception as e:
        print(e)


def borrowBook(bName,sName):
    try:
        if(bName in IssuedBooks):
            print(" Sorry!!! The Book Has Already Been Issued to Someone.")
        elif(sName in IssuedStudents):
            print("Sorry!!! One Book Has Already been Issued to you.")

        else:
            IssuedStudents.append(sName)
            IssuedBooks.append(bName)
            print(f"Book named {bName} Has been Successfully Issued to {sName}. Return it within 30 days.")
            print(f"All issued Books are : {IssuedBooks}")
            print(f"Students Having Books Issued  are : {IssuedStudents}")




    except Exception as e:
        print(e)


def returnBook(BookName,StudentName):
    try:
        if(bName in IssuedBooks):
            IssuedBooks.remove(bName)
        elif(sName in IssuedStudents):
            IssuedStudents.remove(sName)

        else:
            print("The Book Has not been Issued Yet.")

    except Exception as e:
        print(e)

def listOfStudents():
    print("Students Affailated to this Library Are : ")
    for item in StudentList:
        print("*  " + item)

def listOfBooks():
    print("Books Available in this Library Are : ")
    for book in BookList: 
        print("*  " + book)

while(True):
    WelcomeMessage='''\n ====== Welcome to Our Library ======
            Please choose an option:
            1. List all the books
            2. Request a book
            3. Return a book
            4. Add New Books
            5. Add New Students
            6. List All The Students
            7. Exit The System
            '''




    print(WelcomeMessage)

    choice=int(input("Enter Your Choice : "))

    if choice==1:
        listOfBooks()

    elif choice==2:
        bName=input("Enter The Name of Book : ")
        sName=input("Enter The Name of The Student : ")
        borrowBook(bName,sName)

    elif choice==3:
        returnBook()

    elif choice==4:
        BookName=input("Enter The Name of Book : ")
        addNewBooks(BookName)

    elif choice==5:
        StudentName=input("Enter The Name of Student : ")
        addNewStudents(StudentName)

    elif choice==6:
        listOfStudents()

    elif choice==7:
        exit()






            











