def check(arr,element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
arr=[1,2,3,5]
element = int(input('Enter the element you want to find in the array:'))
result = check(arr,element)
if result is None:
    print("no element in array")
else:
    print("index is :",result)