'''
https://py.checkio.org/mission/most-wanted-letter/
'''

import re
# import string


#my solution
def checkio(text):
    # replace this for solution
    text = re.sub('[^A-Za-z]', '', text.lower())
    # sort the string
    new_text = sorted(text)
    # create dictionary to store character:frequency
    count_frequency = {character: text.count(character) for character in new_text}
    # Based on vlues to sort the text, item[1] stand for using the first element as the object
    # result is a list, and then get the values the question required.
    return (sorted(count_frequency.items(),key=lambda item: item[1],reverse=True)[0][0])

# Best solution
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
