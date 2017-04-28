try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def word_count(string):
    '''
    count word in string, number is also word
    '''
    word_dict = {}
    with StringIO() as origin_str:
        origin_str.write(string.lower())
        origin_str.seek(0)
        word = ''
        while True:
            char = origin_str.read(1)
            if char == '':
                add_word_to_dict(word, word_dict)
                break
            if char.isnumeric() or char.isalpha():
                word += char
            else:
                add_word_to_dict(word, word_dict)
                word = ''
    return word_dict


def add_word_to_dict(word, word_dict):
    if len(word):
        if word_dict.get(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1
