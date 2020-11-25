def binarySearch(alist, item):  # From Book
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)


def binary_search_no_slice(alist, start, last, item):  # A binary search without slicing or creating lists
    if last - start == 1 and last != 1:  # if last == 1 then that means we are actuially looking at the first item in our list
        return False
    else:
        midpoint = (start + last) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search_no_slice(alist, 0, midpoint, item)
            else:
                return binary_search_no_slice(alist, midpoint, last, item)


def main():
    testlist2 = [0, 2, 4, 10, 13, 18]
    print(binary_search_no_slice(testlist2, 0, len(testlist2), 9))
    print(binary_search_no_slice(testlist2, 0, len(testlist2), 0))

    testlist = [0, 2, 4, 5, 13, 18, 28, 35, 49, ]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))


if __name__ == '__main__':
    main()