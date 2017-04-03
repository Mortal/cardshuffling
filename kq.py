import os
import re
from random import shuffle
from multiprocessing import Pool


def sample(deck):
    shuffle(deck)
    return bool(adjacent_or_one_apart(deck))


def main():
    suit = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    deck = 4*suit
    n = 0
    m = 0
    while True:
        n += 1
        m += sample(deck)
        print_ratio(m, n)


def samples(n):
    try:
        suit = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        deck = 4*suit
        return sum(sample(deck) for _ in range(n))
    except KeyboardInterrupt:
        return


def parallel():
    p = os.cpu_count()
    n = 0
    b = 10000
    m = 0
    with Pool(p) as pool:
        while True:
            n += p*b
            m += sum(pool.map(samples, [b]*p))
            print_ratio(m, n)


def adjacent_or_one_apart(deck):
    return re.search('Q.?K|K.?Q', ''.join(deck))


def print_ratio(m, n):
    print('\r%6.2f%% %s/%s' % (100*m/n, m, n), end='', flush=True)


if __name__ == '__main__':
    try:
        parallel()
    except KeyboardInterrupt:
        print('')
