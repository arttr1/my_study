#include <iostream>

using namespace std;

int main(){
    
    // bx + c =  0
    setlocale(0, "");
    int b, c;
    cin >> b >> c;

    if (b == 0){
        if (c == 0){
        cout << "x - любое число";
        }
        else{
        cout << "нет решений";
        }
    }
    else{
        cout << "x = " << -c / b;
    }

    return 0;
}