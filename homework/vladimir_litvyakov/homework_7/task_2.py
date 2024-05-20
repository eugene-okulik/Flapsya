words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def words_multiply(key, value):
    result = list(words)[key] * words[value]
    print(result)


words_multiply(0, 'I')
words_multiply(1, 'love')
words_multiply(2, 'Python')
words_multiply(3, '!')
