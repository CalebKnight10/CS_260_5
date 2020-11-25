import random
import time


def recursivebinarySearch(alist, item):  # From Book
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return recursivebinarySearch(alist[:midpoint], item)
            else:
                return recursivebinarySearch(alist[midpoint + 1:], item)


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1


def ran_sorted_list(num, start=1, end=10000):
    alist = []
    tmp = random.randint(start, end)
    for x in range(num):
        while tmp in alist:
            tmp = random.randint(start, end)
        alist.append(tmp)
    alist.sort()
    return alist


def recursion_time(alist, search_index):
    start = time.time()
    recursivebinarySearch(alist, alist[search_index])
    time.sleep(0.00000001)
    stop = time.time()
    return f"Recursive search on index {search_index} took {stop - start}"


def iterative_time(alist, search_index):
    start = time.time()
    binarySearch(alist, alist[search_index])
    time.sleep(0.00000001)
    stop = time.time()
    return f"Iterative search on index {search_index} took {stop - start}"


def main():
    search_list = ran_sorted_list(5500)  # sorted list of x amount of items
    print(recursion_time(search_list, 0))  # Speed for first
    print(recursion_time(search_list, len(search_list) // 2))  # Speed for middle
    print(recursion_time(search_list, len(search_list) - 1))  # Speed for last
    print()
    print()
    print(iterative_time(search_list, 0))  # First
    print(iterative_time(search_list, len(search_list) // 2))  # Middle
    print(iterative_time(search_list, len(search_list) - 1))  # Last


if __name__ == '__main__':
    main()