#include <iostream>
#include <cmath>
using namespace std;

int main(){
    setlocale(0, "");

    double h, R, r, l, pi = 3.1415, V, S;
        cout << "введите высоту конуса \n";
        cin >> h;
        cout << "введите больший радиус \n";
        cin >> R;
        cout << "введите меньший радиус \n";
        cin >> r;
        l = sqrt(h*h + (R-r)*(R-r));
        V = pi*h*(R*R + R*r + r*r)/3;
        S = pi*(l*(R+r) + r*r + R*R);
        cout << "объем конуса: " << V << endl << "площадь поверхтности: " << S;


    return 0;
}