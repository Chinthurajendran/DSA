def fact(nums):
    if nums <= 0 :
        return 1
    else:
        return nums*fact(nums-1)
    
result=fact(5)
print(result)


def fact(nums):
    if nums <=0:
        return 1
    else:
        return nums*fact(nums-1)
    

result=fact(5)
print(result)

def fact(nums):
    if nums <=0:
        return nums
    else:
        return nums*fact(nums-1)
    
def fact(nums):
    if nums <=1:
        return nums
    else:
        return fact(nums-1)+fact(nums-2)

def Fibonacci(n):
    if n <=1:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
    
result=Fibonacci (10)
print(result)

result=fact(10)
print(result)