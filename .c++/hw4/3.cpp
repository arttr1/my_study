#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <windows.h>


using namespace std;

int main(){
    setlocale(0, "");
    int cs;
    double s, a, b, c, pi = 3.1415, p;
    cout << "1 - треугольник \n" <<"2 - прямоугольник\n" <<"3 - круг\n";
    cin >> cs;
    // 1 - triangle 
    // 2 - rectangle 
    // 3 - circle

    switch(cs){
        case 1:
            cout << "введите стороны треугольника "<< endl;
            cin >> a >> b >> c;
            p = (a+b+c)/2;
            s = sqrt(p*(p-a)*(p-b)*(p-c));
            cout << s;
            break;
        case 2:
            cout << "введите строны прямоугольника "<< endl;
            cin >> a >> b;
            cout << a*b;
            break;
        case 3:
            cout <<"введите радиус круга" <<endl; 
            cin >> a;
            cout << pi*a*a;
            break;
    }
    


    
    return 0;
}