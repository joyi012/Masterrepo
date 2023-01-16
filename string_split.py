# importing re
import re

# storing the string in my_str_2
sample_string = 'Hey! thanks for visiting, Tutorialspoint!'
new_string = sample_string.replace('!', ',').replace(';', ',')
split_string = new_string.split(',')
# printing my_list by replacing it with multiple delimiters
print(split_string)
