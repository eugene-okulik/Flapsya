task_text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' +
    ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
words = task_text.split()
fin_words = []


for word in words:
    word_ing = word + 'ing'
    if '.' in word:
        word_ing = word_ing.replace('.', '') + '.'
        fin_words.append(word_ing)
    elif ',' in word:
        word_ing = word_ing.replace(',', '') + ','
        fin_words.append(word_ing)
    elif '.' not in word or ',' not in word:
        fin_words.append(word_ing)
print(' '.join(fin_words))
