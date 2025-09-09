#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
    // setlocale(0, "");

    ifstream g;
    g.open("4.txt");
    string temp;
    while(getline(g,temp)){
        char c = temp[0];
            if ((int(c) <= 57) && (int(c) >= 48))
             cout << c<< endl;
        }
    g.close();
    // cout << int('0') << " " << int('9');


    return 0;
}