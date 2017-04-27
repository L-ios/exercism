try:
    from StringIO import StringIO
except:
    from io import StringIO


def to_rna(dna):
    '''
    * `G` -> `C`
    * `C` -> `G`
    * `T` -> `A`
    * `A` -> `U`
    '''
    with StringIO() as tdna:
        with StringIO() as trna:
            tdna.write(dna)
            tdna.seek(0)
            while True:
                ch = tdna.read(1)
                if ch == '':
                    break
                if ch == 'G':
                    trna.write('C')
                elif ch == 'C':
                    trna.write('G')
                elif ch == 'T':
                    trna.write('A')
                elif ch == 'A':
                    trna.write('U')
                elif ch.isalpha():
                    return ''
                else:
                    continue
            trna.flush()
            ret = trna.getvalue()
            return ret
