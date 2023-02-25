import re
import sys

games = sys.stdin.readline()
assert re.match(r"[1-5]\n", games), games

for _ in range(int(games.strip())):
    hand = sys.stdin.readline()
    assert re.match(r"([2-9]|10|[JQKA]) ([2-9]|10|[JQKA]) ([2-9]|10|[JQKA])\n", hand), hand

assert sys.stdin.readline() == ""
sys.exit(42)


