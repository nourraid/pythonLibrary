from book import book
from category import category
import os

print("=============================== nour raid shaheen - 2301195237 ==================================")

categories = []
books = []
cat_choice = 0

cwd = os.getcwd()
path = os.path.join(cwd, "library")

os.makedirs(path, 0o666, exist_ok=True)


def readCategories():
    global path
    global categories
    cat_list = os.listdir(path);
    for i in cat_list:
        c = category(i[:len(i) - 4])
        categories.append(c)


def readBooks():
    global books
    global categories
    global cat_choice

    for c in categories:
        fin = open(os.path.join(path, f"{c.getName()}.txt"), 'rt')
        for l in fin:
            if not l:
                break
            record = l.split(',')
            bookName = record[0]
            bookAuthor = record[1]
            bookPageNum = int(record[2])
            cat_id = int(record[3])
            b = book(bookName, bookAuthor, bookPageNum, cat_id)
            books.append(b)
        fin.close()


def createFile(fileName):
    global path
    fout = open(os.path.join(path, f"{fileName}.txt"), 'wt')
    fout.close()


def writebook(fileName, bookObj):
    file1 = open(os.path.join(path, f'{fileName}.txt'), 'a+')
    file1.writelines(bookObj.__str__() + "\n")
    file1.close()


def mainMenu():
    print("=============================== Welcom in Books Library ========================================= \n1_ Show Categories\n2_Create Category\n3_Exit")


def subMenu():
    global categories
    print(
        f"=============================== Category Menu ==================================\n {categories[cat_choice - 1].getName()}")
    print("1_ Show Category Books\n2_ Create New Book\n3_ Delete Category Books\n4_Exit Main Menu")


def showCategories():
    count = 0
    global categories
    if len(categories) == 0:
        print("no category add !!")
    else:
        print("=============================== Categories ==================================")
        for i in categories:
            count += 1
            print(f"{count}_ {i.getName()}")
        global cat_choice
        try:
            cat_choice = int(input("choice category number: "))
            if len(categories) < cat_choice:
                print("your selection must be one of list")
                showCategories()
        except:
            print("can not enter String")
            showCategories()
        else:
            sub()


def showCatBooks():
    global categories
    global books
    global cat_choice
    if len(books) == 0:
        print("no books add !!")
    else:
        print(
            f"=============================== {categories[cat_choice - 1].getName()} Books ==================================")
        for i in books:
            if (i.getIdCat() == categories[cat_choice - 1].getId()):
                print(i.__str__())


def createCategory():
    global categories
    try:
        name = input("Enter category name: ")
        if '*' == name or '' == name:
            raise ValueError("That is not a allow file name!")
    except ValueError as v:
        print(v)
    except:
        print()
    else:
        c = category(name)
        categories.append(c)
        createFile(name)
        print(f"{name} category created successfully")


def createBook():
    global books
    global categories
    global cat_choice
    try:
        bookName = input("Enter book name: ")
        bookAuthor = input("Enter book author: ")
        bookPageNum = input("Enter book page number: ")
        if not bookPageNum.isdigit():
            raise ValueError("page number must br digit !")
    except ValueError as val:
        print(val)
    else:
        b = book(bookName, bookAuthor, int(bookPageNum), categories[cat_choice - 1].getId())
        books.append(b)
        writebook(categories[cat_choice - 1].getName(), b)
        print(f"{bookName} Book created successfully")


def deleteCatBooks():
    global categories
    global books
    global cat_choice
    if len(books) == 0:
        print("no books already !!")
    else:
        for i in books:
            if (i.getIdCat() == categories[cat_choice - 1].getId()):
                books.remove(i)
                deleteCatBooks()

    createFile(categories[cat_choice - 1].getName())


def sub():
    global categories
    global books

    subMenu()
    try:
        cat_choice = int(input("Enter your choice: "))
        if cat_choice not in range(1, 5):
            raise ValueError("That is not in range !")
    except ValueError as ee:
        print(ee)
        sub()
    except:
        print("can not enter String")
    else:
        while cat_choice != 4:
            if cat_choice == 1:
                showCatBooks()
            elif cat_choice == 2:
                createBook()
            elif cat_choice == 3:
                deleteCatBooks()
                print("books deleted successfully")
            subMenu()
            try:
                cat_choice = int(input("Enter your choice: "))
                if cat_choice not in range(1, 5):
                    raise ValueError("That is not in range !")
            except ValueError as veee:
                print(veee)
                sub()



readCategories()
readBooks()
mainMenu()
choice = 0
try:
    choice = int(input("Enter your choice: "))
    if choice not in range(1, 4):
        raise ValueError("That is not in range !")
except ValueError as vee:
    print(vee)

finally:
    while choice != 3:
        if choice == 1:
            showCategories()
        elif choice == 2:
            createCategory()

        mainMenu()
        try:
            choice = int(input("Enter your choice: "))
            if choice not in range(1, 4):
                raise ValueError("That is not in range !")
        except ValueError as vee:
            print(vee)
