def text(value):
    result ="".join([i for i in value if not i.isdigit()])
    return result



data = "Geeks123for127geeks"

print(text(data))
