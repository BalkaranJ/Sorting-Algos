"""
Pancake Sort

Idea: sort an array using only one operation, a "flip", which reverses
the first k elements of the array (like flipping a stack of pancakes
with a spatula).

Algorithm:
1. Find the index of the largest unsorted element.
2. Flip the array up to that index, bringing the largest element to the front.
3. Flip the array up to the end of the unsorted portion, sending it to its
   correct final position.
4. Shrink the unsorted portion by one and repeat.

Time complexity: O(n^2) comparisons, O(n) flips.
Space complexity: O(1) extra space (sorts in place).
"""


def flip(arr, k):
    """Reverse arr[0..k] in place."""
    arr[:k + 1] = arr[:k + 1][::-1]


def find_max_index(arr, n):
    """Return the index of the largest element in arr[0..n]."""
    max_idx = 0
    for i in range(1, n + 1):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx


def pancake_sort(arr, verbose=False):
    n = len(arr)
    for size in range(n - 1, 0, -1):
        max_idx = find_max_index(arr, size)

        if max_idx == size:
            continue

        if max_idx != 0:
            flip(arr, max_idx)
            if verbose:
                print(f"Flip first {max_idx + 1} -> {arr}")

        flip(arr, size)
        if verbose:
            print(f"Flip first {size + 1} -> {arr}")

    return arr


if __name__ == "__main__":
    data = [23, 10, 20, 11, 12, 6, 7]
    print("Unsorted array:", data)
    print()

    pancake_sort(data, verbose=True)

    print()
    print("Sorted array:  ", data)
