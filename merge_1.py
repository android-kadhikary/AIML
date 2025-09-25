global_counter = 0
merge_counter =0
def merge_sort(arr):
    global global_counter
    global_counter+=1
    print("inserting in merge_sort function with value ",arr, "globalcounter = ",global_counter)
    """
    Sorts a list using the merge sort algorithm (divide and conquer).

    Args:
        arr: The list to be sorted.

    Returns:
        The sorted list.
    """
    # The 'divide' step: Base case for recursion.
    # If the list has 1 or 0 elements, it's already sorted.
    if len(arr) <= 1:
        print("Result with arr lenth <=1")
        return arr

    # Find the middle point of the list to divide it.
    mid = len(arr) // 2
    print(" mid = ",mid)
    left_half = arr[:mid]
    print("left half ",left_half)
    right_half = arr[mid:]
    print("right_half ",right_half)

    # Recursively sort the two halves (the 'conquer' step).
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    print ("left_sorted =",left_sorted, "right_sorte = ", right_sorted)
    # Merge the sorted halves back together (the 'combine' step).
    return merge(left_sorted, right_sorted)

def merge(left, right):
    global merge_counter
    merge_counter+=1
    print ("inserting in merge function with left_sorted =",left, "right_sorte = ", right)
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left: The first sorted list.
        right: The second sorted list.

    Returns:
        A new, merged, and sorted list.
    """
    result = []
    left_idx, right_idx = 0, 0

    # Compare elements from both lists and append the smaller one to the result.
    while left_idx < len(left) and right_idx < len(right):
        print("inside merge === ", merge_counter,"left_idx =",left_idx , " right_idx =",right_idx)
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            print("result when left is less val",result)
            left_idx += 1
        else:
            result.append(right[right_idx])
            print("else result when right is less val",result)
            right_idx += 1

    # Append any remaining elements from either list.
    result.extend(left[left_idx:])
    print("after result.extend(left[left_idx:]) ",left[left_idx:], "    ", result)
    result.extend(right[right_idx:])
    print("after result.extend(",right[right_idx:],") ",right[right_idx:], "    ", result)

    return result

# The list of numbers you want to sort.
numbers = [10, 5, 0, 2, 9, 3, 8, 4, 7, 6]

# Call the merge_sort function and print the result.
sorted_numbers = merge_sort(numbers)
print(f"Original list: {numbers}")
print(f"Sorted list: {sorted_numbers}")
