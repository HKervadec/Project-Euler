# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact,
# 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

import unittest
from time import time

def gen_cube(minValue, maxValue):
    dest = []
    i = 1
    cube = i**3

    while cube < maxValue:
        if cube > minValue:
            dest.append(cube)

        i += 1
        cube = i**3

    return dest

def are_permutations(a, b):
    return stats_digits(a) == stats_digits(b)


def stats_digits(a):
    list = 10*[0]

    while a > 0:
        list[a%10] += 1
        a //= 10

    return list


def find_set(current_set, remaining_cube, goal, last_index):
    if(len(current_set) == goal):
        return current_set

    for i in range(last_index, len(remaining_cube)):
        copy_set = current_set[:]
        if len(current_set) == 0 or are_permutations(current_set[0], remaining_cube[i]):
            copy_set.append(remaining_cube[i])
            copy_remaining = remove_nth(remaining_cube[:], i)

            tmp = find_set(copy_set, copy_remaining, goal, i)

            if tmp != []:
                return tmp

    return []

def remove_nth(list, n):
    return list[:n] + list[min(len(list), n+1):]

def mother_set(goal):
    min = 1

    tmp = [1]
    while True:
        cubes = gen_cube(min, 10*min)

        tmp = find_set([], cubes, goal, 0)
        if tmp != []:
            break

        min *= 10

    return tmp

def resolve_problem(goal):
    return mother_set(goal)[0]


# ###########################################################
class  TestPermutations(unittest.TestCase):
    def setUp(self):
        self.known_values = [[13, [0, 1, 0, 1, 0, 0, 0, 0, 0, 0]],
                             [20, [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]],
                             [0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]

        self.known_valid = ((13, 31),
                                (13, 13),
                                (41063625, 56623104),
                                (41063625, 66430125),
                                (56623104, 66430125))

        self.known_invalid = ((13, 11),
                              (41063625, 41063626))


    def test_stats_digit(self):
        for couple in self.known_values:
            self.assertEqual(stats_digits(couple[0]), couple[1])

    def test_valid_permutations(self):
        for results in self.known_valid:
            self.assertTrue(are_permutations(results[0], results[1]))

    def test_invalid_permutations(self):
        for results in self.known_invalid:
            self.assertFalse(are_permutations(results[0], results[1]))

    def test_subject_example(self):
        cubes = gen_cube(1, 100000000)
        result = find_set([], cubes, 3, 0)
        result.sort()
        self.assertEqual(result, [41063625, 56623104, 66430125])
        self.assertEqual(result[0], 41063625)

    def test_mother_set(self):
        self.assertEqual(mother_set(3), [41063625, 56623104, 66430125])

    def test_resolve_problem(self):
        self.assertEqual(resolve_problem(3), 41063625)
        self.assertEqual(resolve_problem(5), 127035954683)


# ###########################################################
if __name__ == '__main__':
    unittest.main()