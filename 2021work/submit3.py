import sys
from itertools import combinations

import numpy as np

from utils.extract import extract_numbers
from utils.magic import run_magic, submit_easy, submit_hard

sys.setrecursionlimit(5000)

def get_rating(mat, most=True):
    if mat.shape[0] == 1:
        return ''.join(map(str, mat[0]))
    counts =  np.bincount(mat[:, 0])
    to_select = int(most == (counts[1] >= counts[0]))
    return str(to_select) + get_rating(mat[mat[:, 0] == to_select, 1:], most)


def solve(contents, test_mode):
    lines = [line for line in contents.split('\n') if line]
    # xss = extract_numbers(lines)
    mat = np.array([list(map(int, line)) for line in lines])
    gamma = int(''.join(str(np.argmax(np.bincount(col, minlength=2))) for col in mat.T), base=2)
    epsilon = int(''.join(str(np.argmin(np.bincount(col, minlength=2))) for col in mat.T), base=2)
    submit_easy(gamma * epsilon)
    oxygen = int(get_rating(mat, True), base=2)
    co2 = int(get_rating(mat, False), base=2)
    submit_hard(oxygen * co2)



if __name__ == '__main__':
    run_magic(solve)