def no_space(x):
    without_space = ''
    for letter in x:
        if letter != ' ':
            without_space += letter

    return without_space


def no_space_replace(x):
    return x.replace(' ', '')
