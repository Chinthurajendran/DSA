def linear(list,key):
    for i in range(len(list)):
        if key == list[i]:
            return "list found"
            break
    else:
        return "List not found"
    
list=[23,2,5,6,6,7,2,3]
key = int(input("Enter a value :"))

data = linear(list,key)
print(data)