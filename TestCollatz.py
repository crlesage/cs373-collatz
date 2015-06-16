#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ---
    # additional read tests
    # ---

    def test_read_2 (self) :
        s    = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    def test_read_3 (self) :
        s    = "1000000 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1000000)
        self.assertEqual(j,       1)

    def test_read_4 (self) :
        s    = "1 812\n"
        i, j = collatz_read(s)
        self.assertEqual(i,   1)
        self.assertEqual(j, 812)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    # ---
    # additional eval tests
    # ---

    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(420, 69)
        self.assertEqual(v, 144)

    def test_eval_7 (self) :
        v = collatz_eval(1, 812)
        self.assertEqual(v, 171)

    def test_eval_8 (self) :
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # ---
    # additional print tests
    # ---

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 420, 69, 144)
        self.assertEqual(w.getvalue(), "420 69 144\n")
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 1, 812, 171)
        self.assertEqual(w.getvalue(), "1 812 171\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # ---
    # additional solve tests
    # ---

    def test_solve_1 (self) :
        r = StringIO("1 1\n420 69\n1 812\n1 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n420 69 144\n1 812 171\n1 2 2\n")

    def test_solve_2 (self) :
        r = StringIO("70 991\n634 174\n332 526\n90 526 144\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "70 991 179\n634 174 144\n332 526 142\n90 526 144\n")

    def test_solve_3 (self) :
        r = StringIO("72 729\n44 364\n87 459\n320 91\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "72 729 171\n44 364 144\n87 459 144\n320 91 131\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1
% coverage3 report -m                   >> TestCollatz.out
% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s
OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""