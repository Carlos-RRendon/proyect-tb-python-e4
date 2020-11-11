# Inout ports
        # ======================================================================================
        # ======================================================================================
        content = self.data_clean
        string_aux = " ".join(content)
        result_search_aux = re.findall(
            "\W*((inout)\s*(logic|reg|\s*)\s*(\[\d+:\d+\]\s*|\s+)\s*(((,\s*|\s*)((?!input |output |logic )[_a-zA-Z]\w*\s*))*))",
            string_aux)

        inout = []
        for i in range(len(result_search_aux)):
            string_raw_inout = result_search_aux[i][0].replace("inout", "")
            string_raw_inout = string_raw_inout.replace("reg", "")
            string_raw_inout = string_raw_inout.replace("logic", "")
            string_raw_inout = string_raw_inout.replace("module", "")
            string_inout_aux_2 = re.search("(^|\s+)\[(.*?)\]", string_raw_inout)
            if string_inout_aux_2:
                inout_bus_width = string_inout_aux_2.group(0);
                inout_bus_width = inout_bus_width.replace(" ", "")
                string_inout_aux_3 = string_raw_inout.replace(inout_bus_width, "")
                string_inout_aux_4 = re.findall("\s+(\w*)", string_inout_aux_3)
                if string_inout_aux_4:
                    for j in range(len(string_inout_aux_4)):
                        if (not (string_inout_aux_4[j] in dict(inout))) and (string_inout_aux_4[j]):
                            inout.append(tuple((string_inout_aux_4[j], inout_bus_width)))
                else:
                    string_inout_aux_3 = string_inout_aux_3.replace(" ", "")
                    if (not (string_inout_aux_3 in dict(inout))) and (string_inout_aux_3):
                        inout.append(tuple((string_inout_aux_3, inout_bus_width)))

            else:
                inout_bus_width = tuple();
                string_inout_aux_3 = re.findall("\s+(\w*)", string_raw_inout)
                if string_inout_aux_3:
                    for j in range(len(string_inout_aux_3)):
                        if (not (string_inout_aux_3[j] in dict(inout))) and (string_inout_aux_3[j]):
                            inout.append(tuple((string_inout_aux_3[j], inout_bus_width)))
                else:
                    string_inout_aux_3 = string_raw_inout.replace(" ", "")
                    if (not (string_inout_aux_3 in dict(inout))) and (string_inout_aux_3):
                        inout.append(tuple((string_inout_aux_3, inout_bus_width)))

        self.elements["inout"] = inout