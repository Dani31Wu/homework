# User: link
# Date: 2023/9/9
# File: 计数器函数

from functools import wraps


def call_count(func):
    count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"func: {func.__name__}, callCount: {count}")
        return func(*args, **kwargs)

    return wrapper


@call_count
def test():
    return 1


@call_count
def test1():
    return 2


if __name__ == '__main__':
    for _ in range(10):
        test()
        test1()
