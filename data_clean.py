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
        self.abrir_archivo()
        self.data_clean = self.extract_info()

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
        content = self.data_clean

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
        content = self.data_clean
        inputs = []
        input_regex = r'(input.*?\s)output|\)|(input.*)'

        for i in content:
            print(f"List element data clean:  {i}")
            matches = re.finditer(input_regex,i,re.MULTILINE)

            for num,match in enumerate(matches,start=1):

                groups = match.groups()

                for groupnum in range (1,len(groups)+1):
                    data = match.group(groupnum)

                    if data!= None:
                        inputs.append(data)
        if inputs:
            print(inputs)
            self.elements["inputs"] = inputs

        else:
            print("No hay declaraciones de entradas en el archivo")



    def find_outputs(self):
        pass

    def tc_create(self):

        self.find_module()
        self.find_inputs()

        import os
        name = os.path.splitext(self.path)
        new_name = name[0]+"_tb"+name[1]

        #f = open(new_name,"w")

        for key in self.elements.keys():

            if key == "module":

                print(self.elements[key] + "_tb;")
            if key == "inputs":
                for inputs in self.elements[key]:
                    inputs = inputs.replace("input","reg")
                    print(inputs)

            if key == "outputs":
                pass



if __name__ == "__main__":

    files = [
         "design.sv","design1.sv","prueba.sv","prueba2.sv","regex_breaker.sv","regex_breaker2.sv","strings.sv"
    ]


    for file in files:
        creator = tesbench_creator(file)
        print("This file is: ", file)
        creator.tc_create()
        print("\n")
