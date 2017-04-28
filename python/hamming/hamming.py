try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def distance(odna, mdna):
    '''
    odna: origin DNA
    mdna: mutation DNA
    '''
    def_char = 0
    if len(odna) != len(mdna):
        raise ValueError
    with StringIO() as sodna:
        with StringIO() as smdna:
            sodna.write(odna)
            smdna.write(mdna)
            sodna.seek(0)
            smdna.seek(0)
            while True:
                och = sodna.read(1)
                mch = smdna.read(1)
                if och == '':
                    break
                if och != mch:
                    def_char += 1
    return def_char
