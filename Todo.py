# to do list program
todo = []
Item_List = []


def menu():
    i_num = input("Chose a mode by entering the the number: \n1: Add a task\n2: View List\n3: Exit\n: ")
    return i_num


while True:
    num = menu()

    if num == "1":
        item = input("What would you like to do?")
        Item_Time = input("when would you like it to be done by?")
        Item_List.append(item)
        Item_List.append("by " + Item_Time)
        todo.append(Item_List)
        Item_List = []
    elif num == "2":
        x = 1
        for i in (0, len(todo) - 1):
            print(x, ".", " ".join(todo[i]))
            x += 1
    elif num == "3":
        break
    else:
        print("unexpected value, please choose an option between 1 and 3")
