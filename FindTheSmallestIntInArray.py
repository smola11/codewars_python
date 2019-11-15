def find_smallest_int(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest


def find_smallest_int_simplest(arr):
    return min(arr)
