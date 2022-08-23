# Find the largest and the smallest number in a given array

def largest_smallest(an_array):
    an_array.sort()
    # largest = an_array[-1]
    # smallest = an_array[0]
    print(an_array[-1], an_array[0])


largest_smallest([12, 65, 2, 87, 44, 9])