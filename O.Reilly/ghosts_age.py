# create Fib number
x = 0
y = 1
fb_list = []
while True:
    x, y = y, x + y
    if x > 5000:
        break
    fb_list.append(x)


def checkio(opacity):
    new = 10000
    age = 0
    if opacity == 10000:
        return 0
    for i in range(1, 5000):
        if i in fb_list:
            new -= i
        else:
            new += 1
        age += 1
        if new == opacity:
            return (age)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"