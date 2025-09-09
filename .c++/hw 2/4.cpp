#include <iostream>
#include <cmath>
using namespace std;

int main(){
    setlocale(0, "");

   
    double n;
    cin >> n;
    if (n > 0){
        n = ceil(n);
        for (int i = n; i<n+11; i++){
            cout << i<< endl;
        }
    }
    else{
        for (int i = 1; i<11; i++){
            cout << i<< endl;
    }
    }
    return 0;
}