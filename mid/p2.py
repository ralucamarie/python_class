tuple_example = (-1, 3, -2, 4, 0, -5, -7, 6, 5)


def countNegative(tuple_ex: tuple):
    sum_neg = 0
    for item in tuple_ex:
        if item >= 0:
            sum_neg += 1
    return sum_neg


print(countNegative(tuple_example))
