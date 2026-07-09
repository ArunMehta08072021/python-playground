# Intersection Of Two Sorted Array. Example:- arr1 = [1, 2, 3, 4, 5] & arr2 = [4, 5, 6, 7, 8, 9] --> arr1 intersection arr2 = [4, 5]

# Method 1:- Comparing each element of first array to second array - Time Complexity: O(n^2)
# Note: It will work for sorted or unsorted array

arr1= [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9]
arr2 = [3, 4, 5, 5, 6, 6, 7, 11, 12, 1]

# Empty list to hold the element common in both arrays
intersection_arr = []
for item in arr1:
    # To check if element of arr1 in arr2 and to avoid the duplication as well
    if item in arr2 and item not in intersection_arr:
        intersection_arr.append(item)

print(f"{arr1} Intersection {arr2} is {intersection_arr}")


# Method 2:- Time Complexity: O(n+m)
# Note: It will not work for unsorted array.
# One way to make it work for unsorted array is to sort the array first, but it will change the time complexity : O(nlogn + mlogm + (n+m)) = O(nlogn + mlogm)


arr1= [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9]
arr2 = [3, 4, 5, 5, 6, 6, 7, 11, 12]

if arr1 == sorted(arr1) and arr2 == sorted(arr2):
    arr_intersection = []

    i = j = 0
    while i<len(arr1) and j<len(arr2):
        if arr1[i] == arr2[j]:
            # Only add if list is empty OR last element is different
            if not arr_intersection or arr_intersection[-1] != arr1[i]:
                arr_intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1

    print(f"{arr1} Intersection {arr2} is {arr_intersection}")

else:
    print(f"Given Array: {arr1} and {arr2} is not a sorted Array.")


# Method 3: Using Sets - Time Complexity: O(n+m)

arr1= [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9]
arr2 = [3, 4, 5, 5, 6, 6, 7, 11, 12]

intersection_set = list((set(arr1) & set(arr2)))

print(f"{arr1} Intersection {arr2} is {intersection_set}")