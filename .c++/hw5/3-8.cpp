#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(){
    ifstream f;
    f.open("3-2.txt");
    string s;
    while(getline(f, s)){
        for (int i = 0; i < s.size(); i++){
            cout << int(s[i]) << ' ';
        }
    }
    return 0;
}