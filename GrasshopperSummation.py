def summation(num):
    sum = 0
    while num > 0:
        sum += num
        num = num - 1
    return sum


def summation_range(num):
    return sum(range(num + 1))
