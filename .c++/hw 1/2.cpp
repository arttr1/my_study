

#include <iostream>

using namespace std;

int main(){
    
    int a, b;
    cin >> a >> b;
    cout<< "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    //проверка на ноль
    if (b == 0) // если b равно нулю, то делить нельзя
        cout << "делание не возможно" << endl;
    
    else // если b не равно нулю, то делим
        cout << "a / b = " << a / b << endl;

    return 0;
}