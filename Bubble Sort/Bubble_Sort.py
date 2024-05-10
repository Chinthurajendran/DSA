def sort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                list[i],list[j]=list[j],list[i]
    return list

list = [10,2,7,12,6,9,1]
data = sort(list)
print(data)
