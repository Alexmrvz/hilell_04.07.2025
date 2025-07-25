import string
import keyword

name = input("Enter name, pls: ")

if (
    name[0].isdigit() or
    any(c.isupper() for c in name) or
    any(c in string.punctuation and c != '_' for c in name) or
    name in keyword.kwlist or
    name.count('_') > 1
):
    print(False)
else:
    print("True")