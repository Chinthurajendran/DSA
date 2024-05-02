import string

def remove_punctuations(input_string):
    new = []
    for chr in input_string:
        if chr not in string.punctuation:
            new.append(chr)
    return ''.join(new)

input_string = "Hello, World! This is a test string."
cleaned_string = remove_punctuations(input_string)
print(cleaned_string)