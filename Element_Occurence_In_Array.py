# Program to find the frequency of each element in a given Array/List
# Example:- given_arr = [1, 2, 3, 4, 5, 6, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6]
# Frequency(Element->Frequency):- 1->1, 2->2, 3->3, 4->4, 5->5, 6->6
# Time Complexity: O(n)


def frequency_of_element(given_arr):
    # Empty Dictionary to holds the Frequency of each element
    element_frequency = {}

    # loop to iterate over each element of a list and update its frequency
    for element in given_arr:
        # get() will return the value at the specified key and if key doesn't exist it will return 0
        element_frequency[element] = element_frequency.get(element, 0) + 1

    return element_frequency


given_arr = [1, 2, 3, 4, 4, 3, 2, 1, 4, 3, 2, 4, 3, 4]

print(f"Each Element Frequency in {given_arr} are as follows.")

for key, value in frequency_of_element(given_arr).items():
    print(f"{key} --> {value}")