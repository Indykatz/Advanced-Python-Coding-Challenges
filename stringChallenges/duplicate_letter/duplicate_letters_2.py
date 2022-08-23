# Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The function should return True if the sentence has any word with duplicate letters, else return False.

def duplicate_letters_2(a_string):
    a_string = a_string.lower()
    return_value = False
    an_array = a_string.split()
    for each_word in an_array:
        each_word_array = list(each_word)
        for each_char in range(len(each_word_array)):
            for compare_char in range(each_char + 1, len(each_word_array)):
                if each_word_array[each_char] == each_word_array[compare_char]:
                    return_value = True
    print(return_value)

duplicate_letters_2("hello world")
duplicate_letters_2("heLlo world")
duplicate_letters_2("hi world")