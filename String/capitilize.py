def capiital(string):
    words = string.split()
    result = ''

    for word in words:
        cap = word[0].upper()+word[1:]
        result += cap+" "
    return result

string = input("Enter a value:")
print(capiital(string))