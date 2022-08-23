# Find the second largest number in the integer array

def second_largest(an_array):
    an_array.sort()
    # second_largest = an_array[-2]
    print(an_array[-2])


second_largest([12, 65, 2, 87, 44, 9])