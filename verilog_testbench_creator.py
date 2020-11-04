#!/usr/bin/env python
import re

class tesbench_creator:

    def __init__(self,path):

        self.path = path


    def abrir_archivo(self):
        f = open(self.path, 'r')
        content = f.read()
        patterns = 'module'
        word = str()

        is_capital = re.search(patterns, content)
        print(is_capital)





if __name__ == "__main__":

    creator = tesbench_creator("design.sv")
    creator.abrir_archivo()





'''
#def text_match (text) :
patterns = '^[A-Z]'

f = open('design.sv', 'r')
content = f.read()

word = str()

for x in content :
    is_capital = re.search(patterns, x)

    if is_capital :
        word = word + " " + x
    else :
        word = word + x

print(word)'''