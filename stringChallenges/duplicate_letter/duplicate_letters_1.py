# Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The function should return True if the sentence has any word with duplicate letters, else return False.

def duplicate_letters_1(a_string):
    a_string = a_string.lower()
    return_value = False
    an_array = a_string.split()
    for each_word in an_array:
        each_word_array = list(each_word)
        each_char_set = set(each_word_array)
        if len(each_word_array) != len(each_char_set):
            return_value = True
    print(return_value)

duplicate_letters_1("hello world")
duplicate_letters_1("heLlo world")
duplicate_letters_1("hi world")