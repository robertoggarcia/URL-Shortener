import string
from sequences import get_next_value, Sequence

CORPUS = string.ascii_letters + string.digits
seed = Sequence('url_seeds')


def to_base62(number, corpus=CORPUS):
    if number == 0:
        return corpus[0]
    result = []
    base = len(corpus)

    while number:
        number, mod = divmod(number, base)
        result.append(corpus[mod])

    result.reverse()
    return ''.join(result)


def get_hash():
    return to_base62(seed.get_next_value())
