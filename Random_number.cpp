#include <cstdlib>
#include <iostream>
#include <ctime>
#include <string>
#include <experimental/random>
#include <sstream>
#include <bitset>
#include <iomanip>
#include <bits/stdc++.h> 
#include <bitset> 
#include <stdio.h>     
#include <stdlib.h>    
#include <time.h>   

using namespace std;


int main() 
{
    
    const unsigned long int bus_width = 32;
    unsigned long long int bus_range = pow(2, bus_width);
    bus_range -= 1;
    srand (time(NULL));
    unsigned long long int random_number = rand() % bus_range;


    // Hexadecimal
     stringstream hex_stream;
     hex_stream << hex << random_number; 
     string hex_string = hex_stream.str();
     hex_string =  std::to_string(bus_width) + "'h" + hex_string;

     // Octal
     stringstream oct_stream;
     oct_stream << oct << random_number; 
     string oct_string = oct_stream.str();
     oct_string =  std::to_string(bus_width) + "'o" + oct_string;

     // Binary
     std::string bin_string = std::bitset<bus_width>(random_number).to_string();
     bin_string =  std::to_string(bus_width) + "'b" + bin_string;
     
     std::cout << "El número aleatorio es:   " << random_number << endl;
     std::cout << "El número hexadecimal es: " << hex_string << endl;
     std::cout << "El número octal es:       " << oct_string << endl;
     std::cout << "El número binario es:     " << bin_string << endl;
    
}
