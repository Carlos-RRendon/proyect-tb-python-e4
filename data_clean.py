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

        # Quita los saltos de linea
        content = content.replace("\n", " ")
        f.close()

        # Actualiza el atributo content
        self.content = self.content + content

    def extract_info(self):

        self.abrir_archivo()

        pattern = '(module.*\(.*\)|input.*|output.*|inout.*)'
        data_clean = []

        self.content = self.content.split(";")

        for line in self.content:

            match = re.search(pattern, line)

            if match:
                data = match.group(1)
                data_clean.append(data)

        return data_clean

    def find_module(self):
        content = self.extract_info()

        for i in content:

            pattern_module = re.search('module\s+([a-zA-Z]\w*)', i)

            if pattern_module:

                string_module = pattern_module.group(1)
                print(string_module)
                self.elements['module'] = string_module
                break

            else:
                print("No se encontro nombre del modulo")
                break

    def find_inputs(self):
        content = self.extract_info()


        for i in content:
            input_regex= r'(input.*?)(output|\))'
            print(f"List element data clean:  {i}")
            pattern_input = re.search(input_regex,i)
            if pattern_input:
                string_input = pattern_input.group(1)
                print(string_input)
            else:
                input_regex = r'(input.*)'
                pattern_input = re.search(input_regex,i)
                if pattern_input:
                    string_input = pattern_input.group(1)
                    print(string_input)



if __name__ == "__main__":

    files = [
        "design.sv", "design1.sv", "prueba.sv", "regex_breaker.sv", "prueba2.sv"
    ]


    for file in files:
        creator = tesbench_creator(file)
        print("This file is: ", file)
        creator.find_inputs()
        print("\n")

