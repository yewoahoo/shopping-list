#shopping list 
shopping_list = []


#define name, when def name we have to add the reject section, and empty section that reqiures while true,if statements continue, return, print, so reject empty , reject numbers .isdidgit() 
def get_name():
    while True:
        name = input("Enter your name: ")
        if name == "":
            print("you have left it empty. ")
            continue

        if name.isdigit():
            print("Please enter letters, not number's ")
            continue

        print(f"Hello {name}")
        return name 


#def add
def add_item(item):
    shopping_list.append(item)
    print("Added: " + item)
#def remove
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print("remove: " + item)
    else:
        print("item not found")
    

#def showlist 
def show_list():
    if len(shopping_list) == 0:
        print("your lis is empty")
    else:
        for item in shopping_list:
            print("- " + item)

user = get_name()
print(user + "'s shopping list: ")
while True:
    print("1. Add  2. Remove  3. Show  4. Quit")
    choice = input("What would you like to do? ")

    if choice == "1":
        item = input("What do you want to add? ")
        add_item(item)
    elif choice == "2":
        item = input("What do you want to remove? ")
        remove_item(item)
    elif choice == "3":
        show_list()
    elif choice == "4":
        print("Bye")
        break
    else:
        print("Please choose 1, 2, 3 or 4")

