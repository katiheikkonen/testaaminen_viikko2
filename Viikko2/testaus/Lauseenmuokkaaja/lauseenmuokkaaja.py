def clausemachine(sentence):
    list = []
    words = sentence.split()
    for word in words:
        if len(word) > 4:
            list.append(word[::-1])
        elif len(word) == 2:
            list.append(word.upper())
        else:
            list.append(word)
    return ' '.join(list)