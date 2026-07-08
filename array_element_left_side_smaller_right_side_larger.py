# Program to find the element in an array/list whose left side element is smaller and right side element is larger than that
# Example: arr = [1, 3, 2, 5, 9, 7, 6]
# Required element: 5

# Method 1: Comparing each element - Time Complexity: O(n^2)

given_arr = [1, 3, 2, 5, 4, 9, 7, 6]

required_data = []

flag = False

for i in range(1, len(given_arr)-1):
    if max(given_arr[:i]) < given_arr[i] < min(given_arr[i+1:]):
        required_data.append(given_arr[i])
        flag = True

if flag:
    print(f"Element in {given_arr} whose left side element are smaller annd right side element are larger are {required_data}")
else:
    print(f"No such Element found in {given_arr} whose left side element are smaller annd right side element are larger.")


    
# Method 2 - Using min and max list - Time Complexity: O(n)

given_arr = [1, 3, 2, 4, 5, 9, 7, 6]

max_value = given_arr[0]
min_value = given_arr[-1]
max_arr = []
min_arr = []

# loop to create a max_arr list - used to check left side
for i in range(len(given_arr)):
    if max_value < given_arr[i]:
        max_value = given_arr[i]
    max_arr.append(max_value)

# loop to create a min_arr list - used to check right side
for j in range(len(given_arr)-1, -1, -1):
    if min_value > given_arr[j]:
        min_value = given_arr[j]
    min_arr.insert(0, min_value)

flag = False

required_data = []

for i in range(1, len(given_arr)-1):
    if max_arr[i-1] < given_arr[i] < min_arr[i+1]:
        required_data.append(given_arr[i])
        flag = True

if flag:
    print(f"Element in {given_arr} whose left side element are smaller annd right side element are larger are {required_data}")
else:
    print(f"No such Element found in {given_arr} whose left side element are smaller annd right side element are larger.")