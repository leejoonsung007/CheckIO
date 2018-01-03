def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    highest_count = 0
    str = ''
    for string in data:
        string_count = data.count(string)
        if string_count > highest_count:
            highest_count = string_count
            st = string
    return st

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')