def repeat_str(repeat, string):
    repeated = ""
    while repeat > 0:
        repeated += string
        repeat = repeat - 1
    return repeated


def shorter_repeat_str(repeat, string):
    return repeat * string
