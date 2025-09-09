#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
    setlocale(0, "");

    ofstream f;
    f.open("3.txt");
    for (int i=0; i <= 10; i++){
        f << i << endl;
    }   
    f.close();


    ifstream g;
    g.open("3.txt");
    string temp;
    while(getline(g,temp)){
        cout << temp << endl;}
    g.close();
    return 0;
}