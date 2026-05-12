# AUTHOR : RITESH DARWATKAR
# DATE : 11 MAY 2026
# NAME : Merge Sort with User Input


def mergesort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    sortedleft = mergesort(lefthalf)
    sortedright = mergesort(righthalf)

    return merge(sortedleft, sortedright)


def merge(left, right):

    result = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():

    n = int(input("Enter number of elements: "))

    arr = []

    for i in range(n):

        value = int(input("Enter value: "))
        arr.append(value)

    print("Array before sorting:", arr)

    sorted_arr = mergesort(arr)

    print("Array after sorting:", sorted_arr)


main()