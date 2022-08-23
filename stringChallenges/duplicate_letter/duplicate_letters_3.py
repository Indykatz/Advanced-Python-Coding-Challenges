 # Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. The function should return True if the sentence has any word with duplicate letters, else return False.

def duplicate_letters_3(a_string):
    a_string = a_string.lower()
    return_value = False
    an_array = a_string.split()
    each_word_array = map(None, an_array)
    print(each_word_array)






duplicate_letters_3("hello world")
duplicate_letters_3("heLlo world")
duplicate_letters_3("hi world")