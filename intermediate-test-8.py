# Implement the binary search algorithm to find the position of a target value within a sorted list.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target is not present in the array
    return -1


# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = int(input("Enter the target value: "))

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Target value {target_value} found at index {result}.")
else:
    print(f"Target value {target_value} not found in the list.")
