
try:
    from StringIO import StringIO
except:
    from io import StringIO


def is_isogram(text):
    ltext = text.strip().upper()
    with StringIO() as lstring:
        lstring.write(ltext)
        lstring.seek(0)
        char_map = {}
        while True:
            char = lstring.read(1)
            if char is None or char == '':
                break
            if char.isspace():
                continue
            if char.isalpha():
                if char_map.get(char) is not None:
                    return False
                else:
                    char_map[char] = 1
    return True
