"""
     length the longest substring that consists of the same char
 """

def long_repeat(line):

    if len(line) == 0:
        return 0

    record = 1
    count = 1

    for index in range(1, len(line)):
        if line[index] == line[index - 1]:
            count += 1
        else:
            count = 1

        if count > record:
            record = count

    return record


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')