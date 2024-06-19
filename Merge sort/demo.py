def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]

bubble = [38, 27, 43, 3, 9, 82, 10]
bubble_sort(bubble)
print(bubble)

def insertion_sort(list):
    for i in range(len(list)):
        j = i
        while list[j-1]> list[j] and j >0:
            list[j],list[j-1]=list[j-1],list[j]
            j-=1 

insetion = [38, 27, 43, 3, 9, 82, 10]
insertion_sort(insetion)
print(insetion)

def selection_sort(list):
    n = len(list)
    for i in range(n-1):
        mid = i
        for j in range(i+1,n):
            if list[j] < list[mid]:
                mid = j
        list[i],list[mid]=list[mid],list[i]

selection = [38, 27, 43, 3, 9, 82, 10]
selection_sort(selection)
print(selection)


def merge_sort(list):
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i+=1
            else:
                list[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            list[k]=left[i]
            i+=1
            k+=1
            
        while j < len(right):
            list[k] = right[j]
            j+=1
            k+=1
            

merge = [38, 27, 43, 3, 9, 82, 10]
merge_sort(merge)
print(merge)
