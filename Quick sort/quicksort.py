# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less_than_pivot = [x for x in arr[1:] if x <= pivot]
#         greater_than_pivot = [x for x in arr[1:] if x > pivot]
#         return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# # Example usage:
# my_list = [3, 6, 8, 10, 1, 2, 1]
# sorted_list = quicksort(my_list)
# print(sorted_list)

def quicksort(arr,left,right):
    if left < right:
        partiton_pos = partition(arr,left,right)
        quicksort(arr,left,partiton_pos - 1)
        quicksort(arr,partiton_pos + 1,right)

def partition(arr,left,right):
    i = left
    j = right -1
    pivot = arr[right]

    while i <j:

        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
        print(arr)
        print()

    if arr[i] > pivot:
        arr[i],arr[right] = arr[right],arr[i]
    print(arr)
    return i

arr = [22,1,88,66,55,77,33,44]
quicksort(arr,0,len(arr)-1)
print(arr)