def positive_sum(arr):
    sumOfPositives = 0
    for num in arr:
        if num > 0:
            sumOfPositives += num
    return sumOfPositives


# Solution with usage of 'List comprehensions' and 'Generator Expressions'
def positive_sum_short(arr):
    return sum(x for x in arr if x > 0)
