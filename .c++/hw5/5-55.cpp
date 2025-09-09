#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

// Австрия
// Германия
// Канада
// Китай
// Корея
// Норвегия
// Россия
// США
// Финляндия
// Япония 




int main(){
    setlocale(LC_ALL, "");
    int a[10][5];
    string s[10] = {"Австрия", "Германия", "Канада", "Китай", "Корея", "Норвегия", "Россия", "США", "Финляндия", "Япония"};
    for (int i = 0; i < 10; i++){
        cout << s[i] << ' ';
        for (int j = 0; j < 3; j++){
            cin >> a[i][j]; 
        }
        a[i][3] = a[i][0]+a[i][1]+a[i][2];
        a[i][4] = 7*a[i][0]+6*a[i][1]+5*a[i][2];

        cout << endl;

    }

    for (int i = 0; i < 10; i ++){
        
    }
   
    



    


    return 0;
}