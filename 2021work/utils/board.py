from collections import Counter
from typing import Union

import numpy as np


def ensure_valid_slice(i: Union[slice, int], m: int) -> slice:
    if not isinstance(i, slice):
        assert isinstance(i, int)
        i = slice(i, i + 1)
    assert i.step is None or i.step == 1
    if i.start is None or i.start < 0:
        i = slice(0, i.stop)
    if i.stop is None or i.stop > m:
        i = slice(i.start, m)
    if i.start >= i.stop:
        i = slice(0, 0)
    return i


class CharCounter:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        # self.counts is a double fenwick Tree
        self.counts = np.zeros((self.m + 1, self.n + 1), dtype=np.int32)

    def up_to(self, i: int, j: int) -> int:
        assert 0 <= i <= self.m and 0 <= j <= self.n
        if i == 0 or j == 0:
            return 0
        s = 0
        i1 = i - 1
        while i1 >= 0:
            j1 = j - 1
            while j1 >= 0:
                s += self.counts[i1, j1]
                j1 = (j1 & (j1 + 1)) - 1
            i1 = (i1 & (i1 + 1)) - 1
        return s

    def sum(self):
        return self.up_to(self.m, self.n)

    def __getitem__(self, coordinates) -> int:
        i, j = coordinates
        i = ensure_valid_slice(i, self.m)
        j = ensure_valid_slice(j, self.n)
        return self.up_to(i.stop, j.stop) \
               - self.up_to(i.stop, j.start) \
               - self.up_to(i.start, j.stop) \
               + self.up_to(i.start, j.start)

    def __setitem__(self, coordinates, value):
        i, j = coordinates
        assert isinstance(i, int) and isinstance(j, int)
        assert 0 <= i < self.m and 0 <= j < self.n
        current_value = self.__getitem__((i, j))
        to_add = value - current_value
        i1 = i
        while i1 <= self.m:
            j1 = j
            while j1 <= self.n:
                self.counts[i1, j1] += to_add
                j1 = j1 | (j1 + 1)
            i1 = i1 | (i1 + 1)

    def sum_radius(self, i, j, r):
        return self[(slice(i - r, i + r + 1), slice(j - r, j + r + 1))]

    def vanilla_counts(self):
        vanilla_counts = np.zeros((self.m, self.n), dtype=np.int32)
        for i in range(self.m):
            for j in range(self.n):
                vanilla_counts[i, j] = self[i, j]
        return vanilla_counts

    def __repr__(self):
        return self.vanilla_counts().__repr__()

    def __str__(self):
        return self.vanilla_counts().__str__()


class Board:
    def __init__(self, lines, chars=None):
        self.m = len(lines)
        self.n = len(lines[0])
        self.board = lines
        if chars is None:
            self.chars = set()
            for line in lines:
                self.chars |= set(line)
        self.char_counters = {char: CharCounter(self.m, self.n) for char in self.chars}
        for i, row in enumerate(self.board):
            for j, char in enumerate(row):
                self.char_counters[char][i, j] = 1

    def count_dist_l_inf(self, i, j, r):
        return self.count_within(slice(i - r, i + r + 1), slice(j - r, j + r + 1))

    def count_within(self, i_slice, j_slice):
        return Counter({
            char: counter[(i_slice, j_slice)] for char, counter in self.char_counters.items()
        })

    def full_count(self):
        return self.count_within(slice(None), slice(None))

    def __getitem__(self, coordinates):
        i, j = coordinates
        return self.board[i][j]

    def __setitem__(self, coordinates, char):
        i, j = coordinates
        assert char in self.chars
        old_char = self.board[i][j]
        if old_char != char:
            self.char_counters[old_char][i, j] -= 1
            self.char_counters[char][i, j] += 1
            self.board[i][j] = char

    def _to_skewed(self, i, j):
        return i + j, i - j + (self.n - 1)

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.board)

    def __str__(self):
        return self.__repr__()