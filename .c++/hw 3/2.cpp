#include <iostream>
#include <cmath>
using namespace std;

int main(){
    setlocale(0, "");

    double S, m0, n, r, m, eps = 1;
    cin >> S >> m0 >> n;
    for (double p = 1; p<=100; p++){
        r = p/100;
        m = (S*r*pow((1+r), n))/(12 * (pow((1+r), n)-1));
 
        if (abs(m-m0)<eps){
            cout << p;
            break;
        }
        } 

    return 0;
    
    // 1000000 13313.5 20
}