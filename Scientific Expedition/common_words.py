def checkio(first, second):
    x = first.split(",")
    y = second.split(",")
    x_sort = sorted(x)
    y_sort = sorted(y)

    common_list = []
    for item in x_sort:
        if item in y_sort:
            common_list.append(item)
    return ",".join(common_list)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
