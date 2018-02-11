import re


def is_stressful(subj):
    subj_handling = subj.lower();
    string_handling_ori = re.sub("[^A-Za-z]", '', subj)
    string_handling = re.sub("[^A-Za-z]", '', subj).lower()

    if string_handling_ori.isupper():
        return True

    if "help" in subj_handling or "urgent" in subj_handling or "asap" in subj_handling:
        return True
    else:
        list1 = []
        for i in subj:
            list1.append(i)

        list2 = []
        list2 = sorted(set(list1), key=list1.index)
        word = "".join(list2).lower()

    if "!!!" == subj[-3:]:
        return True

    elif "help" in word or "urgent" in word or "asap" in word:
        return True

    elif "help" in string_handling or "urgent" in string_handling or "asap" in string_handling:
        return True

    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')