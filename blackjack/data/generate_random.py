import random as _random
import sys

_random.seed(int(sys.argv[-1])) # fix seed of random generator to last argument

games = _random.randrange(1,6)
print(games)
allowed_chars = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
for _ in range(games):
    fst = _random.randrange(0,len(allowed_chars))
    snd = _random.randrange(0,len(allowed_chars))
    trd = _random.randrange(0,len(allowed_chars))

    print(allowed_chars[fst], allowed_chars[snd], allowed_chars[trd])

