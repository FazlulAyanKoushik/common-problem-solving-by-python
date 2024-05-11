string = "cabcdabf"

if 'c' in string:
    last_index_of_c = string.rfind('c')
    sliced_string = string[last_index_of_c + 1:]
    print("Last index of 'c' in the string:", last_index_of_c)
    print("Sliced string after 'c':", sliced_string)
else:
    print("'c' is not in the string.")