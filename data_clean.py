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
        
        
        #
        string_aux = " ".join(content)
        result_search_aux = re.findall("\W*((input)\s*(\[\d+:\d+\]\s*|\s+)\s*(((,\s*|\s*)((?!input|output|inout)[_a-zA-Z]\w*\s*))*))", string_aux)

        inputs = []
        for i in range(len(result_search_aux)) :
            string_raw_inputs = result_search_aux[i][0].replace("input", "")
            string_input_aux_2 = re.search("^\[(.*?)\]", string_raw_inputs)
            if string_input_aux_2 :
                input_bus_width = string_input_aux_2.group(0);
                string_input_aux_3 = string_raw_inputs.replace(input_bus_width, "")
                string_input_aux_3 = string_input_aux_3.replace(" ", "")





                inputs.append(input_bus_width)



                
                






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
        "regex_breaker.sv"
    ]


    for file in files:
        creator = tesbench_creator(file)
        print("This file is: ", file)
        creator.find_inputs()
        print("\n")

