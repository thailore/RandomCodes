def quicksort(arr):
    """Quicksort implementation
    Best Case: O(n log(n))
    Average Case: O(n log(n))
    Worst Case: O(n^2)
    """
    if not arr:
        return []

    return quicksort([x for x in arr if x < arr[0]]) \
           + [x for x in arr if x == arr[0]] \
           + quicksort([x for x in arr if x > arr[0]])

