# Implementation of Kadane's Algorithm
# Purpose: Find the maximum sum of a contiguous subarray in a given array
# Usage: Call the function with an integer list as input
# Time Complexity: O(n) — single pass through the array
# Space Complexity: O(1) — only a few variables used


def subarray_maximum_sum(arr):
    current_sum = best_sum = arr[0]
    current_subarray = [arr[0]]
    best_subarray = current_subarray.copy()

    for num in arr[1:]:
        if current_sum + num > num:
            current_sum += num
            current_subarray.append(num)
        else:
            current_sum = num
            current_subarray = [num]

        if current_sum > best_sum:
            best_sum = current_sum
            best_subarray = current_subarray.copy()

    return (best_subarray, best_sum)

given_arr = [1, 2, -2, 3, 0, -1, -3, 5, 0, 2, 1]

required_details = subarray_maximum_sum(given_arr)

print(f"{required_details[0]} is the subarrya whose sum is maximum i.e {required_details[1]} in given array {given_arr}")
        


