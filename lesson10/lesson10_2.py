def first_word(text: str) -> str:


    text = text.strip()

    if not text:
        return ""
    start = 0
    while start < len(text) and not text[start].isalpha() and text[start] != "'":
        start += 1
    if start >= len(text):
        return ""
    result = ""
    for i in range(start, len(text)):
        char = text[i]
        if char.isalpha() or char == "'":
            result += char
        elif char in ",." and result:
            break
        elif char.isspace() and result:
            break
    return result if result else text[start] if text[start].isalpha() else ""

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
