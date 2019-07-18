#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    cache = {
        0: 1,
        1: 1,
        2: 2
    }
    cache_key = 2
    if n in cache:
        return cache[n]
    else:
        while cache_key != n:
            cache[cache_key + 1] = cache[cache_key] + \
                cache[cache_key - 1] + cache[cache_key - 2]
            cache_key += 1
    return cache[cache_key]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
