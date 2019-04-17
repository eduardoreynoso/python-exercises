
# 1.- Make a function that receives a string positional argument and a list of characters (implement this using `*args`)
# 2.- The list of characters will be tuples of a `char` and an `int`
# 3.- The function will add all the characters that have been passed in the list
# Example `my_function('aaabc', ('a', 3), ('b', 1))` (edited)
# O(n^m) - Before
# O(m+n) - After


def count_chars(param1, *args, **kwargs):

    if len(args) < 1:
        return 0

    if type(param1) != str:
        return 0

    total_sum = 0
    char_values = {}
    # Put the tuple in the dictionary
    for a in args:
        if type(a) != tuple:
            continue
        if type(a[1]) != int:
            continue
        char_values[a[0]] = a[1]

    for c in param1:
        if c in char_values:
            total_sum += char_values[c]

    return total_sum


if __name__ == '__main__':
    # Application entry point
    print(count_chars('aaa', ('a', 5)))



