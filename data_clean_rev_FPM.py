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
        
        
        # INPUTS
        # ======================================================================================
        # ======================================================================================

        string_aux = " ".join(content)
        result_search_aux = re.findall("\W*((input)\s*(\[\d+:\d+\]\s*|\s+)\s*(((,\s*|\s*)((?!input|output|inout)[_a-zA-Z]\w*\s*))*))", string_aux)

        inputs = []
        for i in range(len(result_search_aux)) :
            string_raw_inputs = result_search_aux[i][0].replace("input", "")
            string_input_aux_2 = re.search("(^|\s+)\[(.*?)\]", string_raw_inputs)
            if string_input_aux_2 :
                input_bus_width = string_input_aux_2.group(0);
                input_bus_width = input_bus_width.replace(" ", "")
                string_input_aux_3 = string_raw_inputs.replace(input_bus_width, "")
                #string_input_aux_4 = re.findall("([_a-z0-9-]+)(?:,|\s)", string_input_aux_3)
                string_input_aux_4 = re.findall("\s+(\w*)", string_input_aux_3)
                if string_input_aux_4 :
                    for j in range(len(string_input_aux_4)) :
                        if not ((string_input_aux_4[j] in dict(inputs))) and (string_input_aux_4[j]):
                            inputs.append(tuple((string_input_aux_4[j], input_bus_width)))
                else :
                    string_input_aux_3 = string_input_aux_3.replace(" ", "")
                    if not ((string_input_aux_3 in dict(inputs))) and (string_input_aux_3):
                        inputs.append(tuple((string_input_aux_3, input_bus_width)))
            
            else :
                input_bus_width = tuple();
                string_input_aux_3 = re.findall("\s+(\w*)", string_raw_inputs)
                if string_input_aux_3 : 
                    for j in range(len(string_input_aux_3)) :
                        if (not (string_input_aux_3[j] in dict(inputs))) and (string_input_aux_3[j]):
                            inputs.append(tuple((string_input_aux_3[j], input_bus_width)))
                else :         
                    string_input_aux_3 = string_raw_inputs.replace(" ", "")
                    if not (string_input_aux_3 in dict(inputs)) and (string_input_aux_3) :
                        inputs.append(tuple((string_input_aux_3, input_bus_width)))


        # OUTPUTS
        # ======================================================================================
        # ======================================================================================
        
        result_search_aux = re.findall("\W*((output)\s*(reg|\s*)\\s*(\[\d+:\d+\]\s*|\s+)\s*(((,\s*|\s*)((?!input|output|inout)[_a-zA-Z]\w*\s*))*))", string_aux)

        outputs = []
        for i in range(len(result_search_aux)) :
            string_raw_output = result_search_aux[i][0].replace("output", "")
            string_raw_output = string_raw_output.replace("reg", "")
            string_output_aux_2 = re.search("(^|\s+)\[(.*?)\]", string_raw_output)
            if string_output_aux_2 :
                output_bus_width = string_output_aux_2.group(0);
                output_bus_width = output_bus_width.replace(" ", "")
                string_output_aux_3 = string_raw_output.replace(output_bus_width, "")
                string_output_aux_4 = re.findall("\s+(\w*)", string_output_aux_3)
                if string_output_aux_4 :
                    for j in range(len(string_output_aux_4)) :
                        if (not (string_output_aux_4[j] in dict(outputs))) and (string_output_aux_4[j]):
                            outputs.append(tuple((string_output_aux_4[j], output_bus_width)))
                else :
                    string_output_aux_3 = string_output_aux_3.replace(" ", "")
                    if (not (string_output_aux_3 in dict(outputs))) and (string_output_aux_3):
                        outputs.append(tuple((string_output_aux_3, output_bus_width)))
            
            else :
                output_bus_width = tuple();
                string_output_aux_3 = re.findall("\s+(\w*)", string_raw_output)
                if string_output_aux_3 : 
                    for j in range(len(string_output_aux_3)) :
                        if (not (string_output_aux_3[j] in dict(outputs))) and (string_output_aux_3[j]):
                            outputs.append(tuple((string_output_aux_3[j], output_bus_width)))
                else :         
                    string_output_aux_3 = string_raw_output.replace(" ", "")
                    if (not (string_output_aux_3 in dict(outputs))) and (string_output_aux_3) :
                        outputs.append(tuple((string_output_aux_3, output_bus_width)))              




                
                






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
        "regex_breaker_rev_FPM.sv"
    ]


    for file in files:
        creator = tesbench_creator(file)
        print("This file is: ", file)
        creator.find_inputs()
        print("\n")

