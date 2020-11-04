#!/usr/bin/env python
import re

class tesbench_creator:

    def __init__(self,path):

        self.path = path
        self.content = ""


    def abrir_archivo(self):

        #Abre archivo
        f = open(self.path, 'r')

        #Lee el contenido y lo almacena en la variable local content
        content = f.read()

        #Quita los saltos de linea
        content = content.replace("\n"," ")
        f.close()

        #Actualiza el atributo content
        self.content = self.content + content

    def extract_info(self):
        import re
        self.abrir_archivo()

        pattern = "module|input|output|inout"
        data_clean = []

        self.content = self.content.split(";")

        for line in self.content:
            if re.search(pattern,line):
                data_clean.append(line)

        for i in range (len(data_clean)):
            print(data_clean[i])






if __name__ == "__main__":

    creator = tesbench_creator("prueba.sv")
    creator.extract_info()


