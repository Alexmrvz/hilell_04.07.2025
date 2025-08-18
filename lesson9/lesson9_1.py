from typing import List, Dict


def popular_words(text: str, words: List[str]) -> Dict[str, int]:

    text_words: List[str] = text.lower().split()
    result: Dict[str, int] = {word: 0 for word in words}

    for word in text_words:
        if word in words:
            result[word] += 1
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')


print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))