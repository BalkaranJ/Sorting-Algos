"""
Tim Sort

Idea: a hybrid of insertion sort and merge sort. Real-world data is often
already partially ordered, so Tim Sort breaks the array into small chunks
called "runs", sorts each run with insertion sort (fast for small/nearly
sorted data), then merges the runs together with the standard merge sort
merge step.

Tim Sort is the algorithm behind Python's built-in sort() / sorted() and
Java's Arrays.sort() for objects.

Algorithm:
1. Split the array into runs of size MIN_RUN.
2. Sort each run in place using insertion sort.
3. Merge runs together in pairs, doubling the merged size each pass,
   until the whole array is one sorted run.

Time complexity: O(n log n) worst case, O(n) best case (already sorted).
Space complexity: O(n) for the merge step.
"""

# Real-world Tim Sort implementations use MIN_RUN = 32 or 64. It's set
# small here so a modest-size array still produces multiple runs and
# merge passes worth showing in a demo.
MIN_RUN = 4


def insertion_sort(arr, left, right):
    """Sort arr[left..right] in place using insertion sort."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    """Merge two sorted runs arr[left..mid] and arr[mid+1..right] in place."""
    left_run = arr[left:mid + 1]
    right_run = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_run) and j < len(right_run):
        if left_run[i] <= right_run[j]:
            arr[k] = left_run[i]
            i += 1
        else:
            arr[k] = right_run[j]
            j += 1
        k += 1

    while i < len(left_run):
        arr[k] = left_run[i]
        i += 1
        k += 1

    while j < len(right_run):
        arr[k] = right_run[j]
        j += 1
        k += 1


def tim_sort(arr, verbose=False):
    n = len(arr)

    # Step 1: sort individual runs of size MIN_RUN using insertion sort.
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)
        if verbose:
            print(f"Insertion sort run [{start}:{end}] -> {arr}")

    # Step 2: merge runs, doubling the size each pass.
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right)
                if verbose:
                    print(f"Merge [{left}:{mid}] and [{mid + 1}:{right}] -> {arr}")
        size *= 2

    return arr


if __name__ == "__main__":
    data = [5, 21, 7, 23, 19, 1, 15, 3, 25, 9, 17, 11, 13, 2, 8, 6, 4, 20, 14, 18]
    print("Unsorted array:", data)
    print()

    tim_sort(data, verbose=True)

    print()
    print("Sorted array:  ", data)
