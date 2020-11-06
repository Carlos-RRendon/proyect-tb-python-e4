#!/usr/bin/env python
import re
import string

class tesbench_creator:

    def __init__(self,path):
        self.path = path


    def abrir_archivo(self):
        f = open(self.path, 'r')
        content = f.read()  
              
        content = re.sub("\/.*", "", content)

        result_search = re.search("module\s+(\w*)", content)
        if result_search :
            module_name = result_search.group(1)
        else :
            print("El módulo no puede ser instanciado")

        result_search = re.search("(?s)#\((.*?)\)", content)
        parameters = []
        if result_search :

            string_raw = result_search.group(1)
            string_raw = string_raw.translate({ord(c): None for c in string.whitespace})
            string_raw = re.sub("parameter", '', string_raw)
            
            aux_list_A = re.findall("(?:\,|^)(.*?)\=", string_raw)
            aux_list_B = re.findall("=(.*?)(?:\,|$)", string_raw)

           
            for x in range(len(aux_list_A)) :
                parameters.append(tuple((aux_list_A[x], aux_list_B[x])))
 
        #==========================================================================================    

        postcontent = content.replace("\t", " ")
        postcontent = content.replace("\n", " ")
  
        result_search = re.findall("\(([^)\;]+)", postcontent) 

        if (parameters) and (result_search) :
            string_raw = result_search[1]
        elif (not parameters) and (result_search) :
            string_raw = result_search[0]
        
        if (result_search) :
            result_search_aux = re.findall(\
            "\W*((input)\s*(\[\d+:\d+\]\s*|\s+)\s*(((,\s*|\s*)((?!input|output|inout)[_a-zA-Z]\w*\s*))*))", \
                string_raw)

            if result_search_aux : 
                for x in range(len(result_search_aux)) :
                    string_raw_aux = result_search_aux[x]
                    string_raw_aux = string_raw_aux.replace("input", "")



        print("123")        






    



        # groups_number = len(result_search.groups())
        # pattern_module = re.search("\W*((input|output|inout)\s*(\[\d+:\d+\]\s*|\s+)\s*(((,\s*|\s*)((?!input|output|inout)[_a-zA-Z]\w*\s*))*))", content)
        # name = pattern_module.group(1)
        # name2 = pattern_module.group(2)
        
               
        # pattern_module = re.search("(.*)", content)
        # ports = pattern_module.group(1)









if __name__ == "__main__":

    creator = tesbench_creator("regex_breaker.sv")
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