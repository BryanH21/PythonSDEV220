#Sort 0s, 1s and 2s
def sort012(arr):
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


# Binary Search
def binary_search(arr, k):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            result = mid      
            right = mid - 1     
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return result