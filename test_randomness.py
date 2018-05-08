from collections import Counter
from random import seed, randint
from secrets import SystemRandom


def random_without_seed():
    result = []
    for i in range(1000):
        result.append(randint(1, 10))
    counter = Counter(result)
    for key, value in sorted(counter.items()):
        print(key, ': ', value)


def random_with_seed(n):
    result = []
    seed(n)
    for i in range(1000):
        result.append(randint(1, 10))
    counter = Counter(result)
    for key, value in sorted(counter.items()):
        print(key, ': ', value)


def system_random_without_seed():
    result = []
    system_random = SystemRandom()
    for i in range(1000):
        result.append(system_random.randint(1, 10))
    counter = Counter(result)
    for key, value in sorted(counter.items()):
        print(key, ': ', value)


def system_random_with_seed(n):
    result = []
    system_random = SystemRandom()
    system_random.seed(seed)
    for i in range(1000):
        result.append(system_random.randint(1, 10))
    counter = Counter(result)
    for key, value in sorted(counter.items()):
        print(key, ': ', value)


if __name__ == '__main__':
    print('Random without seed')
    print('First try: ')
    random_without_seed()
    print('Second try: ')
    random_without_seed()
    print()

    print('Random with seed 1')
    print('First try: ')
    random_with_seed(1)
    print('Second try: ')
    random_with_seed(1)
    print()

    print('Random with seed 2')
    print('First try: ')
    random_with_seed(2)
    print('Second try: ')
    random_with_seed(2)
    print()

    print('System Random without seed')
    print('First try: ')
    system_random_without_seed()
    print('Second try: ')
    system_random_without_seed()
    print()

    print('System Random with seed 1')
    print('First try: ')
    system_random_with_seed(1)
    print('Second try: ')
    system_random_with_seed(1)
    print()

    print('System Random with seed 2')
    print('First try: ')
    system_random_with_seed(2)
    print('Second try: ')
    system_random_with_seed(2)
    print()
