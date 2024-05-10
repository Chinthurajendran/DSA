stack = []
stack.append(10)
stack.append(20)
print(stack)
stack.pop()
print(stack)


stack = []
def puch():
    if len(stack) == limit:
        print("List is full")
    else:
        data = int(input("Enter the values :"))
        stack.append(data)
        print("Added")
        print(stack)



def pop():
    if stack is None:
        print("list is ematy")
    else:
        stack.pop()
        print(stack)

limit = int(input("Enter the limit :"))
while True:
    print("Select the options \n 1.Push \n 2.Pop \n 3.Quit")
    choice = int(input("Enter:"))
    if choice == 1:
        puch()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Enter the correct options")


