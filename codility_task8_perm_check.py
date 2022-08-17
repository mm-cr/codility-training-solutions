"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.
"""


def solution(a):
    my_list: list[int] = a
    my_list.sort()
    n: int = len(my_list)
    is_permutation: int = 0
    pattern: list[int] = list(range(1, n+1))

    if my_list == pattern:
        is_permutation = 1

    return is_permutation


def main():
    print(solution([4, 1, 3, 2]))


if __name__ == "__main__":
    main()
