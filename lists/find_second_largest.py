test_data = [
    [10, 20, 30, 40, 50],  # List with distinct elements
    [3, 3, 3, 3],          # List with all identical elements
    [-1, -2, -3, -4],      # List with all negative numbers
    [5, 1, 5, 2, 5],       # List with duplicates of the maximum
    [100],                 # List with only one element
    [],                    # Empty list
    [1, 5, 10, 25, 100, 50], # Mixed list of positive numbers
    [-10, -20, 5, 15, 30, -5], # Mixed positive and negative numbers
    [999, 1000, 1000, 998], # Large numbers with duplicates
    [42, 42, 42, 42, 43],   # Mostly identical with one distinct
]

def find_second_largest(lst):
    if not lst:
        return None    
    
    max_num = 0
    second_max = 0
    for x in lst:
        if(max_num < x ):
            max_num = x

        if(second_max < x):
            second_max = max_num 
        print('setting max number', x, second_max, max_num)

    return second_max, max_num


print(find_second_largest(test_data[0]))