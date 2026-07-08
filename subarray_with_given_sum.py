# Program to find the subarray in given array whose subarray sum is N
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  &  given_sum = 21
# subarray = [1, 2, 3, 4, 5, 6] & [6, 7, 8]

""""
#To genertae all the possible subarray
for i in range(len(given_arr)):
    subarray = []
    for j in range(i, len(given_arr)):
        subarray.append(given_arr[j])
        print(subarray)
"""


given_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

given_sum = int(input("Enter the required sum: "))

# Empty list to hold all the possible subarray whose sum is equal to given sum
required_details = []

flag = False

for i in range(len(given_arr)):
    subarray = []
    for j in range(i, len(given_arr)):
        subarray.append(given_arr[j])
        if sum(subarray) == given_sum:
            print(f"{subarray} are the subarray whose sum is equal to {given_sum}")
            flag = True

if not flag:
    print(f"No such subarray found whose sum is equal to {given_sum}")


