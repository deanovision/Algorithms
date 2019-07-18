#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    cache = {
        0: [[]],
        1: [['rock'], ['paper'], ['scissors']]
    }
    cache_index = 1
    if n in cache:
        return cache[n]
    else:

        while cache_index != n:
            temp = []
            for i in range(0, len(cache[cache_index])):
                for j in range(0, 3):
                    temp.append(cache[cache_index][i] + cache[1][j])
            cache_index += 1
            cache[cache_index] = temp
    return cache[n]


rock_paper_scissors(3)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
