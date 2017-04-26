try:
    from StringIO import StringIO
except:
    from io import StringIO


def to_rna(dna):
    # tdna = dna.strip().lower()
    tdna = StringIO()
    tdna.write(dna.strip().lower())
    trna = StringIO()
