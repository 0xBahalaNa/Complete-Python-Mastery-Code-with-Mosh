"""
5. Data Structures, 23. Exercise

Find the most repeated character in this string:
sentence = "This is a common interview question"

Create an empty dictionary.
Use a for loop to loop over the string.
if statement to increment the frequency. (value)
else statement adds it to the dictionary. (key)

pprint for pretty printing. Makes its more readable. 

Take each key value pair and make it into a list of tuples. (use .items())

Uses sorted function, with a lambda function, using key value pair. 

"""
from pprint import pprint
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint(char_frequency, width=1)
char_frequency_sorted = (
    sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))
print(char_frequency_sorted[0])
"""
Output: 
('i', 5)
"""
