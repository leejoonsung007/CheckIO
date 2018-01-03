def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    #tuple cannot be editted, so use list and then convert it
    new_list = [elements[0]]
    new_list.append(elements[2])
    new_list.append(elements[-2])
    # conver the list to tuple
    new_tuple = tuple(new_list)
    return new_tuple

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')