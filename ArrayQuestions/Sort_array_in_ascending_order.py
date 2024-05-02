def order(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                # temp = arr[i]
                # arr[i]=arr[j]
                # arr[j]=temp
                arr[i],arr[j]= arr[j],arr[i]
    return arr

arr=[2,4,6,1,4]
result = order(arr)
print(result)
print()


def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j]= arr[j],arr[i]
    return arr

arr=[2,4,6,1,4]
result=sort(arr)
print(result)

arr.sort()
print(arr)