"""
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution(A):
    my_list: list[int] = A
    my_list = [x for x in my_list if x > 0]  # filter out negative numbers, keep only positive

    my_set: set[int] = set(my_list)  # remove duplicate values
    my_list = sorted(my_set)
    result: int = 0
    counter: int = 1

    for value in my_list:
        if counter != value:
            result = counter
            break

        counter += 1

    if result == 0:
        result = len(my_list) + 1

    return result


def main():
    print(solution([1, 3, 6, 4, 1, 2]))


if __name__ == "__main__":
    main()


