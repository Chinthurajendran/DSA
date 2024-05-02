def binary(list,key):
    low = 0
    high = len(list)-1
    found = False
    while low <= high and not found:
        mid = (low+high)//2
        if key == list[mid]:
            found = True
        elif key > list[mid]:
            low = mid+1
        else:
            high = mid-1
    if found == True:
        print("key is found")
    else:
        print("key is not found")


list=[2,6,3,5,7,23,56,78,88,22,100]
list.sort()
print(list)
key = int(input("Enter the key  :"))
binary(list,key)
