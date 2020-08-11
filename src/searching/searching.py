def linear_search(arr, target):
    for i in range(len(arr)):  # O(n)
        if target == arr[i]:
            return i  # O(1)
    return -1   # not found

# O(n)

# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    start_position = 0  # O(1)
    end_position = len(arr) - 1  # O(1)

    while start_position <= end_position:  # O(n)
        middle_position = start_position + \
            (end_position - start_position) // 2  # O(1)
        middle_num = arr[middle_position]  # O(1)
        # if the target is the value at the center position return the position
        if middle_num == target:
            return middle_position  # O(1)
        # if the target is less than this value limit the search to the left half
        elif target < middle_num:
            end_position = middle_position - 1  # O(n1/2)
        # if its not equal and its not less limit the search to the right half
        else:
            start_position = middle_position + 1  # O(n1/2)
    # Your code here

    return -1  # not found

# O(log n)
