# Program to find Minimum & Maximun in given Array/List without using min() & max() built in function
# given_data = [2, 4, 5, 1, 3, 0, 9, 454, -234, 45, 565]
# Minimum Element: -234 & Maximum Element: 565
# Time Complexity = O(n)
# min() & max() also have Time Complexity O(n) as internally a loop is running out to find the maximun and minimum element in a given Array/ List



given_arr = [2, 4, 5, 1, 3, 0, 9, 454, -234, 45, 565]

min = max = given_arr[0]

for i in range(1, len(given_arr)):
    if min > given_arr[i]:
        min = given_arr[i]

    if max < given_arr[i]:
        max = given_arr[i]
    

print(f"In {given_arr} the Maximun element is {max} and Minimum element is {min}")


