test_cases = [
    ([1, 5, 10, 25, 100, 50], 100),
    ([-10, -20, 5, 15, 30, -5], 30),
    ([-100, -50, -200, -1, -25], -1),
    ([3, 7, 7, 5, 10, 10], 10),
    (list(range(-1_000_000, 1_000_000)), 999999),
    ([42], 42),
    ([], None),
]


def find_max(lst):
    max_num = 0

    for number in lst:
        print(number, max_num)
        if(number > max_num):
            max_num = number

    return max_num 


find_max(test_cases[0][0])
# for i, (lst, excepted) in enumerate(test_cases):
#     result = find_max(lst)
#     print(f"Test {i + 1}: {'Passed' if result == excepted else 'Failed'} - Result: {result}")