#include <iostream>
#include <cmath>
using namespace std;

int main(){
    setlocale(0, "");

    double a,b,c;
    cin >> a >> b >>c;
    if (a==0){
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
    }
    else {
        double d = b*b - 4*a*c;
        if (d < 0){
            cout << "решений нет";
        
        }
        else if (d == 0){
            cout << "x = " << -b / (2*a);
        }
        else{
            cout << "x1 = " << (-b + sqrt(d)) / (2*a) << endl;
            cout << "x2 = " << (-b - sqrt(d)) / (2*a);
        }
    }

    return 0;
}