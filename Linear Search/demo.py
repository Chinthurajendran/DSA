name = 'chinthu rajendran'
word = name.split()
result = ''
for i in word:
    cap = i[0].upper()+i[1:]
    result+=cap+' '
print(result)
