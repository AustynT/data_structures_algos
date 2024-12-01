test_lists = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([-5, -10, -15, -20], [-20, -15, -10, -5]),
    ([0, -3, 5, 10, -7], [-7, 10, 5, -3, 0]),
    (["apple", "banana", "cherry", "date"], ["date", "cherry", "banana", "apple"]),
    ([42], [42]),
    ([], []),
    ([[1, 2], [3, 4], [5, 6]], [[5, 6], [3, 4], [1, 2]]),
    ([1.1, 2.2, 3.3, 4.4], [4.4, 3.3, 2.2, 1.1]),
    ([1, "two", 3.0, [4, 5]], [[4, 5], 3.0, "two", 1]),
    (list(range(1, 101)), list(range(100, 0, -1))),
]


def reverse_list(lst):
    # Your code here
    print(lst)
    count = len(lst) - 1 
    new_list = []
    while (count >= 0):
        new_list.append(lst[count])        
        count -= 1
    return new_list
    
    


for i, (test_input, expected_output) in enumerate(test_lists):
    result = reverse_list(test_input)
    assert result == expected_output, f"Test {i + 1} failed: {result} != {expected_output}"
    print(f"Test {i + 1} passed!")

print("All tests passed!")