#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    setlocale(0, "");

    cout << "x"<< "       "<< "y" << endl;
    double x = - 4, y;
    while (x <= 4){
        if (x != 1){
            y = (x*x - 2*x + 2)/(x-1);
            cout<< setw(4) << x <<"   "<< y << endl;
        }
        else {
            cout<< setw(4) << x << "  " << "деление невозможно"<< endl;
        }        
        x+=0.5;
    }

    return 0;
}