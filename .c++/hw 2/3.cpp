#include <iostream>
#include <cmath>
using namespace std;

int main(){
    setlocale(0, "");

    double x,y,b,z;
    cin >> x >> y >> b;

    if ((b > y) && (b >= x)){
        z = log(b - y) * sqrt(b - x);

    }
    else 
        cout << "нельзя вычислить";
    
    cout << z;

    return 0;
}