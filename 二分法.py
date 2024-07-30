def binary_search(func, x1, x2, exact=0.00001):
    """
    Performs binary search on a function f(x) on the interval [x1, x2] with a given epsilon.

    This function assumes that the function f(x) is continuous and monotonic on the interval [x1, x2].
    It returns an approximate root of the function within the specified precision, or None if no root exists
    in the interval or if the function changes sign more than once within the interval.

    :param func: The function to find the root of.
    :param x1: A float representing the lower bound of the interval.
    :param x2: A float representing the upper bound of the interval.
    :param exact: A float representing the desired accuracy of the root.
    :return: The approximate root of the function or None if the function does not satisfy the conditions.

    Note:
        - Ensure that the function is continuous and monotonic on the given interval.
        - If there are multiple roots, the one closest to x1 will be returned.
        - If the function does not change sign between x1 and x2, no root will be found.

    请确保此函数在给定区间内连续且单调，否则结果可能不准确。
    此函数在给定区间 [x1, x2] 上对函数 f(x) 执行二分法搜索，精度为给定的 epsilon。
    如果函数在该区间上不连续或有多个根，函数将返回 None。

    :param func: 要搜索根的函数。
    :param x1: 一个浮点数，表示区间的下界。
    :param x2: 一个浮点数，表示区间的上界。
    :param exact: 一个浮点数，表示所需的根的精度。
    :return: 函数的大致根或 None，如果函数在区间上不连续或有多个根。

    注意：
        - 确保函数在给定区间上连续且单调。
        - 如果有多个根，将返回最接近 x1 的根。
        - 如果函数在 x1 和 x2 之间不变号，则不会找到根。
    """

    if func(x1) * func(x2) > 0:
        return None
    while abs(x2 - x1) > exact:
        c = (x1 + x2) / 2
        if func(x1) * func(c) < 0:
            x2 = c
        else:
            if func(c) == 0:
                x1 = c
                return x1
            else:
                x1 = c

    return x1


def f(x):
    return 2**x + 3*x - 7


# 测试
a = eval(input("Enter the lower bound: "))
b = eval(input("Enter the upper bound: "))
epsilon = eval(input("Enter the epsilon: "))
print(f"Approximating f(x) = 2^x + 3x - 7 on [{a}, {b}] with epsilon = {epsilon}")
solution = binary_search(f, a, b, epsilon)
print("Approximate solution:", solution)
