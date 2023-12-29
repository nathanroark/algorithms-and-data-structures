from quick_sort import quick_sort

if __name__ == "__main__":
    unsorted = [3, 5, 1, 2, 4, 9, 7, 6, 8, 0]
    print("Unsorted list:")
    print(unsorted)
    print("-" * 20)
    print("Sorted list:")
    print(quick_sort(unsorted))
