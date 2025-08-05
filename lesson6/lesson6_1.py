import string

input_str = input()
all_letters = string.ascii_letters
start, end = input_str.split('-')
start_index = all_letters.index(start)
end_index = all_letters.index(end)
print(all_letters[start_index:end_index +1])