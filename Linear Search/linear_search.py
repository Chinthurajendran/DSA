def linear(list,key):
    for i in range(len(list)):
        if key == list[i]:
            return "The element is found"
    else:
        return "The elements is not found"

list=[1,2,3,4,5]
key = int(input("Enter a value :"))
print(linear(list,key))
