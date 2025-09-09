#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int sign(double n){
    if (n > 0)
        return 1;
    else if(n == 0)
        return 0;
    else 
        return -1;
}


int main(){
    double n;
    cin >> n;
    cout << sign(n);
    
    return 0;
}