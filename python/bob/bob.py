def hey(str):
    if str.isupper():    # all letter is upper
        return 'Whoa, chill out!'
    if str.strip().endswith('?'):  # end with "?"
        return 'Sure.'
    if len(str.strip()) == 0:
        return 'Fine. Be that way!'
    return 'Whatever.'
