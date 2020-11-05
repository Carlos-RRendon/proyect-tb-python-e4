#!/usr/bin/env python
import re


class tesbench_creator:

    def __init__(self, path):
        self.path = path
        self.content = ""
        self.elements = {
            'module': None,
            'inputs': None,
            'outputs': None
        }

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

        self.abrir_archivo()

        pattern = 'module|input|output|inout'
        data_clean = []

        self.content = self.content.split(";")

        for line in self.content:
            if re.search(pattern, line):

                data_clean.append(line)

        print(data_clean)
        return data_clean

    def find_module(self):
        content = self.extract_info()

        for i in content:

            pattern_module = re.search('((module)+\s+\w+)', i)
            if pattern_module:

                string_module = pattern_module.group(1)
                pattern_module2 = re.search("module\s+([a-zA-Z]\w*)",string_module)
                module_name = pattern_module2.group(1)
                print(module_name)
                break
            else:
                print("No se encontro nombre del modulo")
                break


    def create_tb(self):
        print()
        '''self.find_module()
        print(self.elements['module'])'''


if __name__ == "__main__":

    files = [
        "design.sv", "design1.sv","prueba.sv"
    ]

    for file in files:
        creator = tesbench_creator(file)
        print("This file is: ", file)
        creator.find_module()
        print("\n")
