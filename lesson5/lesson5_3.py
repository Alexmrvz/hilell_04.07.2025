import string

    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    words = clean_text.split()
    words_capitalized = [word.capitalize() for word in words]
    hashtag = '#' + ''.join(words_capitalized)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    return hashtag

print(to_hashtag("Python Community"))
print(to_hashtag("Should, I. subscribe? Yes!"))