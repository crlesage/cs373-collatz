#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ---
# Global Cache 
# ---
"""
Cache dictionary for reference.
Includes eager cache represented by powers of 2.
"""
cache = {1:1, 1:2}
# Eager cache, powers of 2
cache[4] = 3
cache[8] = 4
cache[16] = 5
cache[32] = 6
cache[64] = 7
cache[128] = 8
cache[256] = 9
cache[512] = 10
cache[1024] = 11
cache[2048] = 12
cache[4096] = 13
cache[8192] = 14
cache[16384] = 15
cache[32768] = 16
cache[65536] = 17
cache[131072] = 18
cache[262144] = 19
cache[524288] = 20


# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]

    Computes the max cycle length between i and j. 
    Stores cycle lengths in Cache for a quick reference.
    """

    assert i > 0
    assert j > 0
    assert i < 1000000
    assert j < 1000000

    #Swap i and j if j is smaller
    if (i > j) :
        temp = i
        i = j
        j = temp
    assert j >= i

    max_cycle_length = 0

    for n in range (i, j + 1) :
        # Check to see if already in cache
        if (n in cache) :
            if cache[n] > max_cycle_length :
                max_cycle_length = cache[n]

        # If not, use helper to get cycle length and store in cache
        cache[n] = collatz_helper(n)

        # Update max cycle length if needed
        if cache[n] > max_cycle_length :
            max_cycle_length = cache[n]

    assert max_cycle_length > 0
    return max_cycle_length

def collatz_helper (n) :
    """
    Computes and returns cycle length of n + cycle lengths found in cache
    """

    assert n > 0

    # Cycle length less than 3 is itself
    if (n < 3) :
        return n

    # Compute cycle length otherwise
    cycle_length = 0
    # If not in cache already, find cycle length
    while (n not in cache) :
        if (n % 2) == 0 :
            n = (n // 2)
            cycle_length += 1
            assert cycle_length > 0
        else :
            n += (n >> 1) + 1
            cycle_length += 2
            assert cycle_length > 0

    # Return the current cycle length plus if there is a cache value
    return cycle_length + cache[n]

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)