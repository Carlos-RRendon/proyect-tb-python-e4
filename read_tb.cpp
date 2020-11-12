#include <iostream>
#include <regex>
#include <string>
#include <fstream>
#include <map>
#include<vector>
#include<sstream>
#include <time.h>

using namespace std;

string open_file()
{
    fstream  textFile;
    string codeVerilog, tempText;
    string path = "design1.sv";

    textFile.open(path, ifstream::in); //for test_file the path is examples/test.txt
    if(textFile.is_open()){
        cout << "File " << path << " opened" << endl << endl;
        while(!textFile.eof()){
            getline(textFile, tempText);
            codeVerilog += tempText;
            cout << tempText << endl;
        }
        textFile.close();
    }
    else
        cout << "Can't open file " << path << endl;
    return codeVerilog;
}


vector<string> splitText(string text) {
   vector<string> result;
   stringstream s_stream(text); //create string stream from the string
   while(s_stream.good()) {
      string substr;
      getline(s_stream, substr, ','); //get first string delimited by comma
      result.push_back(substr);
    }
    return result;
}

int main()
{
    //map<string, vector<string> > data_tb;
    vector<string> tmp;
    map<string,string> input, output; 
    string module_name;
    string s = open_file();

    smatch m;
    regex re_module("module\\s+([a-zA-Z]\\w*)");

    if(regex_search(s,m,re_module)){
        module_name = m[1];
        //data_tb.insert(pair<string, vector<string> > ("module_name", tmp));
        s = m.suffix().str();
    }
    
    //regex re_inout("\\W*((input|output|inout)\\s*(\\[\\d+:\\d+\\]\\s*|\\s+)\\s*(((,\\s*|\\s*)((?!input|output|inout)[_a-zA-Z]\\w*\\s*))*))");
    regex re_input("\\W*((input)\\s*(\\[\\d+:\\d+\\]\\s*|\\s+)\\s*(((,\\s*|\\s*)((?!input|output|inout)[_a-zA-Z]\\w*\\s*))*))");
    while(regex_search (s,m,re_input)) //s variable, string where the file was opened; m match_results for string objects, re_input regex pattern
    {   tmp = splitText(m[4]);
        for(int i = 0; i < tmp.size(); i++) {    //print all splitted strings
            input.insert(pair <string, string> (tmp.at(i), m[3]));
        }
        s = m.suffix().str();
    }
    cout<<endl<<endl<<s<<endl<<endl;

    regex re_output("\\W*((output)\\s*(reg|\\s*)\\s*(\\[\\d+:\\d+\\]\\s*|\\s+)\\s*(((,\\s*|\\s*)((?!input|output|inout)[_a-zA-Z]\\w*\\s*))*))");
    while(regex_search (s,m,re_output))
    {
        tmp = splitText(m[5]);
        for(int i = 0; i < tmp.size(); i++) {    //print all splitted strings
            output.insert(pair <string, string> (tmp.at(i), m[4]));
        }
        s = m.suffix().str();
    }
    cout<<endl<<endl<<s<<endl<<endl;
    
    //cout << s <<endl;
    cout << "Module name: " << module_name << endl;

    for (auto const& pair: input) {
        cout << "Inputs: " <<"name: "<< pair.first << "| range: " << pair.second << endl;
	}

    for (auto const& pair: output) {
        cout << "Outputs: " <<"name: "<< pair.first << "| range: " << pair.second << endl;
	}

    //Inicio de generacion de testbench 
    string text_tb;
    text_tb = "`timescale 1ns / 1ps\n"
                "module " + module_name + "_TB;\n";

    for (auto const& pair: input) {
        text_tb += "\treg " + pair.second + " " + pair.first + "_TB;\n";
	}
    for (auto const& pair: output) {
        text_tb += "\twire " + pair.second + " " + pair.first + "_TB;\n";
	}
    text_tb += module_name + " UUT(";
    for (auto const& pair: input) {
        text_tb += " ." + pair.first + "("+ pair.first + "_TB),";
	}
    for (auto const& pair: output) {
        text_tb += " ." + pair.first + "("+ pair.first + "_TB),";
	}
    text_tb.pop_back();
    text_tb += ");\n"
            "initial\n"
            "\tbegin\n";


    fstream  outfile;
    outfile.open("output.txt", ofstream::out);
    outfile << text_tb;
    outfile.close();

}