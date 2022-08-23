# Merge two sorted arrays into a single sorted array

def merge_two_sorted_arrays(array_1, array_2):
    new_array = array_1 + array_2
    new_array.sort()
    print(new_array)

merge_two_sorted_arrays([1,3,5,7,9], [2,4,6,8])