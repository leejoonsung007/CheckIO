def non_repeat(line):
    """
        the longest substring without repeating chars
    """
    result = ""
    for num in range(0,len(line)):
        store = ""
        for letter in line[num:]:
            if letter in store:
                break
            store += letter
        if len(store) > len(result):
            result = store
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')