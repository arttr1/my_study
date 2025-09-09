#include <iostream>
#include <cmath>
using namespace std;
// нод делением
int nod(int a, int b){
    a = abs(a);
    b = abs(b);
    if(a!=0 && b!=0){
        if (a > b){
            if (a%b == 0)
                return b;
            else 
                return nod((a%b), b);
        }
        else{
            if (b%a == 0)
                return a;
            else 
                return nod((b%a), a);
        }
    }
    else{
        return a+b;
    }
}
// нод вычитанием
int nod2(int a, int b){
    a = abs(a);
    b = abs(b);
    if (a - b == 0)
        return a;
    else if(a == 0 || b == 0){
        return a+b;
    }
    else{
        if (a > b)
            return nod2(a-b, b);
        else
            return nod2(b-a, a);
    }
}

int main(){
    int a, b;
    cin >> a >> b;
    cout << nod(a, b) << endl;
    cout << nod2(a, b);
    

    return 0;
}