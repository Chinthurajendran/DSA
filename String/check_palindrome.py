def palindrome(string):
    length = len(string)
    for i in range(length):
        if string[i] != string[length-1-i]:
            return False
    return True

string = 'chinthu'
print(palindrome(string))