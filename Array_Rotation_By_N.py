# Program to rotate the Given Array/List by N
# Example: given_arr = [0, 1, 2, 3, 4, 5]  & n = 2 (Rotation)
# 1st rotation [0, 1, 2, 3, 4, 5] --> [1, 2, 3, 4, 5, 0]
# 2nd Rotation [1, 2, 3, 4, 5, 0] --> [2, 3, 4, 5, 0, 1]

#Method 1: Using loop and del - Time Complexity: O(n^2)

given_arr = [0, 1, 2, 3, 4, 5]

rotation = int(input("\nEnter Number Of Rotation: "))

print(f"\nGiven Array Before Rotation is {given_arr}\n")

for i in range(rotation):
    # first element store in temp
    temp = given_arr[0]
    # first element removed from the list 
    del given_arr[0]
    # temp added at the end of the list i.e first element now moved at the end
    given_arr.append(temp)

print(f"\nGiven Array After Rotation is {given_arr}\n")


#Method 2(More Pythonic): Using List Splicing and Normalisation  - Time Complexity: O(n^2) 

given_arr = [0, 1, 2, 3, 4, 5]

rotation = int(input("\nEnter Number Of Rotation: "))

# Normalissation of rotation to handle the scenario where entered value is more than the length of an array/ list
# rotation = 7  --> 7 % 6 = 1 means if we rotate an array of length 6 by 7 times it will be equivalent to rotating it 1 time
# Example: [1, 2, 3, 4, 5, 6]
# 1st Rotation: [2, 3, 4, 5, 6, 1]
# 2nd Rotation: [3, 4, 5, 6, 1, 2]
# 3rd Rotation: [4, 5, 6, 1, 2, 3]
# 4th Rotation: [5, 6, 1, 2, 3, 4]
# 5th Rotation: [6, 1, 2, 3, 4, 5]
# 6th Rotation: [1, 2, 3, 4, 5, 6]      -> becomes original array if rotation == length of an array
# 7th Rotation: [2, 3, 4, 5, 6, 1]      -> Equivalent to 1st Rotation

rotation = rotation % len(given_arr)

print(f"\nGiven Array Before Rotation is {given_arr}\n")

given_arr = given_arr[rotation:] + given_arr[:rotation]

print(f"\nGiven Array After Rotation is {given_arr}\n")