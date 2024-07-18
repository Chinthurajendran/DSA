def capiital(string):
    words = string.split()
    result = ''

    for word in words:
        cap = word[0].upper()+word[1:]
        result += cap+ " "
        return result


string = input("Enter a value:")
print(capiital(string))


name =  'my name is chinthu'
word = name.split()
print(word)
data  = word[::-1]
print(data)