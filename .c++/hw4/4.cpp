#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
    setlocale(0, "");
    for (int i = 0; i < 13; i++){
        if(i < 6){
            for(int j = 0; j < 8; j++){
                cout << "*";
            }
            for(int j = 0; j < 22; j++){
                cout << "_";
            }
        }
        else{
             for(int j = 0; j < 30; j++){
                cout << "_";
            }
        }
        cout << endl;
    }
    
    
    return 0;
}