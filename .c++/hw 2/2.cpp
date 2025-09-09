
#include <iostream>
#include <cmath>
using namespace std;

int main(){
    setlocale(0, "");
    double x, a,  w ;
        cin >> x >> a;
        if (abs(x)<1){
            w = a * log(abs(x));
        }
        else {
            if (a >= x*x)
                w = sqrt(a - x*x);
            else
                cout << "нельзя извлечь корень";

        }
        cout << w;
   
    return 0;
}