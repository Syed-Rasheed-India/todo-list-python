library_book_list = {
    "Horror": [
        "Dracula",
        "Frankenstein",
        "The Shining",
        "It",
        "Pet Sematary",
        "The Haunting of Hill House",
        "Bird Box",
        "Coraline",
        "The Exorcist",
        "Ghost Story"
    ],

    "Fantasy": [
        "Harry Potter and the Sorcerer's Stone",
        "The Hobbit",
        "The Lord of the Rings",
        "Percy Jackson and the Lightning Thief",
        "The Name of the Wind",
        "Eragon",
        "The Lion, the Witch and the Wardrobe",
        "Mistborn",
        "The Last Unicorn",
        "A Game of Thrones"
    ],

    "Science Fiction": [
        "Dune",
        "Foundation",
        "The Martian",
        "Ender's Game",
        "Neuromancer",
        "Ready Player One",
        "The Time Machine",
        "I, Robot",
        "Snow Crash",
        "Hyperion"
    ],

    "Mystery": [
        "Sherlock Holmes",
        "Murder on the Orient Express",
        "The Da Vinci Code",
        "Gone Girl",
        "The Girl with the Dragon Tattoo",
        "Big Little Lies",
        "And Then There Were None",
        "The Silent Patient",
        "In the Woods",
        "Rebecca"
    ],

    "Biography": [
        "Wings of Fire",
        "The Diary of a Young Girl",
        "Long Walk to Freedom",
        "Steve Jobs",
        "Becoming",
        "Einstein: His Life and Universe",
        "Shoe Dog",
        "The Story of My Experiments with Truth",
        "Elon Musk",
        "Educated"
    ]
}

def add_book(list_cat):

    print("Select the category you want to add:")
    j=1
    for i  in list_cat:
        print(j,i)
        j=j+1
    choice = int(input("Enter your choice: "))
    book_name = input("Enter your book name: ")
    library_book_list[list_cat[choice-1]].append(book_name)
    print("Book added")
    print(library_book_list)


def borrow_book(list_cat):

    print("Select the category you want to return:")

    j = 1
    for i in list_cat:
        print(j, i)
        j = j + 1
    choice = int(input("Enter your category: "))

    # book_name = list_cat[choice-1]
    book_list = library_book_list[list_cat[choice-1]]
    print("here the list of book are avilable")
    for i in book_list:
        print(i)
    name = input("enter the book name: ")
    library_book_list[f"{list_cat[choice-1]}"].remove(f"{name}")
    print("Book Borrowed")

def return_book(list_cat):

    print("Select the category you want to Return:")

    j = 1
    for i in list_cat:
        print(j, i)
        j = j + 1
    choice = int(input("Enter your category: "))
    book_name = input("enter the book name: ")
    library_book_list[f"{list_cat[choice-1]}"].append(f"{book_name}")
    print("Book returned")

def search_book(list_cat):

    print("Select the category you want to Search:")

    j = 1
    for i in list_cat:
        print(j, i)
        j = j + 1
    choice = int(input("Enter your category: "))
    book_name = input("enter the book name: ")
    book_list = library_book_list[f"{list_cat[choice-1]}"]
    if book_name in book_list:
        print("Book Is Available you can borrow")
    else:
        print("Book Is Not Available")

while True:

    print("Welcome to Our Library")
    print("----------------------")
    print("1. Add Books")
    print("2. Borrow Books")
    print("3. Return Books")
    print("4. Search Books")
    list_cat = ["Horror", "Fantasy", "Science Fiction", "Mystery", "Biography"]

    try:
        option = int(input("Enter your choice: "))
    except ValueError or KeyError:
        print("Invalid Choice")
    else:
        if option == 1:
            add_book(list_cat)
        elif option == 2:
            borrow_book(list_cat)
        elif option == 3:
            return_book(list_cat)
        elif option == 4:
            search_book(list_cat)
        else:
            print("enter a valid option")
            exit()


