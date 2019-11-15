def count_sheeps(arrayOfSheeps):
    sheep_number = 0
    for sheep in arrayOfSheeps:
        if sheep:
            sheep_number = sheep_number + 1

    return sheep_number


def count_sheeps_count(arrayOfSheeps):
    return arrayOfSheeps.count(True)


print(count_sheeps([True, False]))
