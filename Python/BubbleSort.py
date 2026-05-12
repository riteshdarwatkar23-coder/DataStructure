# AUTHOR : RITESH DARWATKAR
# DATE : 11 MAY 2026
# NAME : BubbleSort


def bubble_sort(arr):

    n = len(arr)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():

    n = int(input("Enter number of elements: "))

    arr = []

    for i in range(n):

        value = int(input("Enter values: "))

        arr.append(value)

    print("Array before sorting:", arr)

    bubble_sort(arr)

    print("Array after sorting:", arr)


main()