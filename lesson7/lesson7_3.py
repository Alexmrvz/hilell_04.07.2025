def second_index(text, some_str):


    first_occurrence = text.find(some_str)

    if first_occurrence == -1:
        return None

    second_occurrence = text.find(some_str, first_occurrence + len(some_str))

    if second_occurrence == -1:
        return None
    return second_occurrence


print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
print(second_index("Hello, hello", "lo"))