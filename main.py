def summ(*args):
    result = 0
    for arg in args:
        result = result + arg
    return result


if __name__ == '__main__':
    print(summ(-1, -2, -3, -4, -5, -6, -7, -8, -9, -0, -10))
