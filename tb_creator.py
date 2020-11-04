#!/usr/bin/env python
import re


class tesbench_creator:

    def __init__(self, path):
        self.path = path
        self.content = ""

    def abrir_archivo(self):
        f = open(self.path, 'r')
        content = f.read()

        '''pattern_module = re.search('module\s(.*)', content)
        string_module = pattern_module.group(1)'''

        # Quita los saltos de linea
        content = content.replace("\n", " ")
        f.close()

        # Actualiza el atributo content
        self.content = self.content + content

    def extract_info(self):

        import re
        self.abrir_archivo()

        pattern = "module|input|output|inout"
        data_clean = []

        self.content = self.content.split(";")

        for line in self.content:
            if re.search(pattern, line):
                data_clean.append(line)


        return data_clean

    def find_module(self):
        content = self.extract_info()

        for i in content :
            
            pattern_module = re.search('module\s(.*)', i)
            string_module = pattern_module.group(1)


            pattern_module_2 = re.search("(.*)\s*\((.*?)\)", string_module)
            module_name = pattern_module_2.group(1)
            ports = pattern_module_2.group(2)
            
            if pattern_module :
                print(module_name)
                print(ports)
                break
            else :
                print("No es posible instanciar, falta el nombre del modulo")
                break


if __name__ == "__main__":
    creator = tesbench_creator("design.sv")
    creator.find_module()
