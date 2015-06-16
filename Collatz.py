#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

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
    """
    # <your code>
    assert i > 0
    assert j > 0
    assert i <= 1000000
    assert j <= 1000000

    max_cycle_length = 1
    cycle_length = 1

    #Swap i and j if j is smaller
    if (i > j) :
        temp = i
        i = j
        j = temp

    for n in range (i, j + 1) :
        cycle_length = compute_cycle_length (n)

        if cycle_length > max_cycle_length :
            max_cycle_length = cycle_length

    assert cycle_length > 0
    assert max_cycle_length > 0

    return max_cycle_length

# Computes and returns cycle length of n.
def compute_cycle_length (n) :
    assert n > 0
    cycle_length = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = n // 2
        else :
            n = (3 * n) + 1
        cycle_length += 1

    assert cycle_length > 0
    return cycle_length

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