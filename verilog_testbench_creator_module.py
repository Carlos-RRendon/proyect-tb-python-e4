#!/usr/bin/env python
import re

class tesbench_creator:

    def __init__(self,path):

        self.path = path


    def abrir_archivo(self):
        f = open(self.path, 'r')
        content = f.read()        

        pattern_module = re.search("module\s+(\w*)", content)
        module_name = pattern_module.group(1)

        pattern_module = re.search("\W*((input|output|inout)\s*(\[\d+:\d+\]\s*|\s+)\s*(((,\s*|\s*)((?!input|output|inout)[_a-zA-Z]\w*\s*))*))", content)
        name = pattern_module.group(1)
        name2 = pattern_module.group(2)
        
               
        # pattern_module = re.search("(.*)", content)
        # ports = pattern_module.group(1)


        print("hola")







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