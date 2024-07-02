def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage:
array = [3, 6, 8, 10, 1, 2, 1]
print("Original Array:", array)
sorted_array = quicksort(array)
print("Sorted Array:", sorted_array)
