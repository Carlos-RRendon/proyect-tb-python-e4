#!/usr/bin/env python
import re

#def text_match (text) :
patterns = '^[A-Z]' 

f = open('text_lab_8.txt', 'r')
content = f.read()

word = str()

for x in content : 
    is_capital = re.search(patterns, x)

    if is_capital :
        word = word + " " + x
    else :
        word = word + x

print(word)