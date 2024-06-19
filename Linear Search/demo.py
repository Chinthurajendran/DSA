# def linear(list):
#     value = 110
#     new_list = []
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i] + list[j] == value:
#                 new_list.append((i,j))
#     print(new_list)

# list = [10,20,30,40,50,60,70,80,90]
# linear(list)


def value(list):
    result = [i for i in list if i!= 6]

    count_six = list.count(6)
    result.extend([6]*count_six)

    print(count_six)
    print(result)
list = [6,1,0,3,6,8,9,4,5,7,6]
value(list)

