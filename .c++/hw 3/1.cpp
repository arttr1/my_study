#include <iostream>
#include <cmath>
using namespace std;

int main(){
    setlocale(0, "");

    double m, S, n, p, r;
    cin >> S >> n >> p;
    r = p/100;
    m = (S*r*pow((1+r), n))/(12 * (pow((1+r), n)-1));
    cout << m;
    

    return 0;
}
// 1000000 20 15
// 13313.5