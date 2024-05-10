stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)

if len(stack) == 0:
    print("stack is empty")
else:
    print("element in stack")



stack = []
def puch():
    if len(stack)  == limit:
        print("List is full")
    else:
        elemnt = int(input("Enter the elements:"))
        stack.append(elemnt)
        print("Added successfully")
        print(stack)

def pop():
    if not stack:
        print("List is empty")
    else:
        stack.pop()
        print("Removed successfullly..")
        print(stack)


limit = int(input("Enter your limit :"))
while True:
    print("Select your choice :\n 1.Push \n 2.Pop\n 3.Quit")
    choice =int(input("Enter the number:"))
    if choice == 1:
        puch()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Enter the correct choices")