def recursion_search(arr):
    if len(arr) < 1:
        return "Array is empty. Please provide at least two elements."
    elif len(arr) == 1:
        return (arr[0], arr[0])

    mid = len(arr) // 2
    left = recursion_search(arr[:mid])
    right = recursion_search(arr[mid:])

    return find_min_max(left, right)

def find_min_max(left, right):
    min_val = 0
    max_val = 0

    if left[0] < right[0]:
        min_val = left[0]
    else:
        min_val = right[0]

    if left[1] > right[1]:
        max_val = left[1]
    else:
        max_val = right[1]

    return (min_val, max_val)

# Example usage
arr = [1, 1, 38, 27, 43, 3, 9, 92, 10, 1, 56]
min_max = recursion_search(arr)
print(min_max)  # (1, 92)