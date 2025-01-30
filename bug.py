def function_with_uncommon_error(x):
    if x == 0:
        return 1 / x # ZeroDivisionError
    else:
        return 10 / x # potential error if x is very small leading to overflow

result = function_with_uncommon_error(0)