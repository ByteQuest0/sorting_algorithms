def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(arr)
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after the pivot
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)




def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps were made in this pass
        swapped = False
        # Perform a pass through the array
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set flag to True indicating a swap was made
                swapped = True
        # If no swaps were made, the list is sorted
        if not swapped:
            break


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted portion
        min_index = i
        # Find the index of the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # The current element to be inserted
        key = arr[i]
        # Start from the end of the sorted portion and move elements larger than key
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key into its correct position
        arr[j + 1] = key



#Quickosrt Example usage
arr = [15, 9, 3, 5, -1, 7]
quicksort(arr, 0, len(arr) - 1)
print(arr)
