def square(x):
    x = x * x
    return x


def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a + b + c


def count_freqs(stri):
    char_d = dict()
    for c in stri:
        if c not in char_d:
            char_d[c] = 0
        char_d[c] = char_d[c] + 1
    return char_d


def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far


def most_common_letter(s):
    frequencies = count_freqs(s)
    best_key1 = best_key(frequencies)
    return best_key1, frequencies[best_key1]
