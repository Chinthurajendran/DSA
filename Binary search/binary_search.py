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
        print("Key is found")
    else:
        print("Key is not found")
        
list=[2,3,4,5,6,67,10]
list.sort()
key = int(input("Enter your key :"))
binary(list,key)
