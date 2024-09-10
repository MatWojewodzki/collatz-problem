import functools


@functools.cache
def collatz_length(n: int) -> int:
    counter = 1
    while n > 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        counter += 1
    return counter


def find_longest(start: int, stop: int) -> int:
    longest_cycle = 1
    for n in range(start, stop):
        cycle_lentgh = collatz_length(n)
        longest_cycle = max(longest_cycle, cycle_lentgh)
    return longest_cycle


def main():
    with open('random_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            start, stop = list(map(int, line.split(' ')))
            longest_cycle = find_longest(start, stop)
            print(f'{start} {stop} {longest_cycle}')


if __name__ == '__main__':
    main()
