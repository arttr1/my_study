#include <iostream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;

int main(){
    setlocale(0, "");
    int var, m1 = 37, i1 = 3, c1 = 64, m2 = 25173, i2 = 13849, c2 = 65537,s0, s;
    cin >> s0;
    s = s0;
    for (int i=i1; i < i1 + 10; i++){
        s = (m1*s+i)%c1;
        cout << s << endl;
    }
    cout << "===================="<< endl;
    s = s0;
    for (int i=i2; i < i2 + 10; i++){
        s = (m2*s+i)%c2;
        cout << s << endl;
    }

    
    
    return 0;
}