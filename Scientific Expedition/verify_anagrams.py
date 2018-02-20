def verify_anagrams(first_word, second_word):
    first_word_sort = sorted(first_word.lower())
    second_word_sort = sorted(second_word.lower())
    first_string = "".join(first_word_sort).strip()
    second_string = "".join(second_word_sort).strip()

    if first_string == second_string:
        return True
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
