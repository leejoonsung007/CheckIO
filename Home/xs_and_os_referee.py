def checkio(game_result):
    check_list1 = []
    check_list2 = []
    check_list3 = []
    check_list4 = []
    check_list5 = []
    check_list6 = []

    for i in range(0, 3):
        check_list1.append(game_result[i][0])
        test1 = ''.join(check_list1)

        check_list2.append(game_result[i][1])
        test2 = ''.join(check_list2)

        check_list3.append(game_result[i][2])
        test3 = ''.join(check_list3)

        check_list4 = [game_result[0][2], game_result[1][1], game_result[2][0]]
        test4 = ''.join(check_list4)

        check_list5.append(game_result[i][i])
        test5 = ''.join(check_list5)

        check_list = [test1, test2, test3, test4, test5, game_result[0], game_result[1], game_result[2]]

    if 'XXX' in check_list:
        return 'X'
    elif 'OOO' in check_list:
        return 'O'
    else:
        return 'D'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")