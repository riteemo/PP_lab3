from RegexpFinder import RegexpFinder
from regexp import regexp


rf = RegexpFinder(regexp) # экземпляр класса
input_string: str # введённая пользователем строка
choice: str # выбор пользователя для цикла

while True:
    print("1 - find tandem words in your string\n2 - find tandem words on page by URL\n3 - find tandem words in file\n4 - Exit")
    choice = input("Enter the number (1 - 4): ")
    while all(["1" != choice, "2" != choice, "3" != choice, "4" != choice]):
        choice = input("Wrong input, human. Enter the number (1 - 4): ")
    if choice == "1":
        input_string = input("Enter the string: ")
        print(rf.find_in_string(input_string))
    elif choice == "2":
        input_string = input("Enter the URL: ")
        print(rf.find_on_page(input_string))
    elif choice == "3":
        input_string = input("Enter the filename: ")
        print(rf.find_in_file(input_string))
    else:
        break