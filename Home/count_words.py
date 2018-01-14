'''
https://py.checkio.org/mission/monkey-typing/
'''

import re


def count_words(text, words):
    text_handling = re.sub("[^A-Za-z]", ' ', text)
    count = 0
    for word in words:
        if word in text_handling.lower():
            count += 1
    return count


# return sum([1 for d in [text.lower().count(word) for word in words] if d > 0])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
