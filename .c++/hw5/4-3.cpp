#include <iostream>
#include <cmath>

int fac(int n){
    if (n == 0) return 1;
    else return n*fac(n-1);
}


using namespace std;

int main(){
    int n;
    cin >> n;
    // cout << fac(n);
    double arr[n];

    for (int i = 1; i <= n; i++){
        int a = fac(i);
        double b = 0;
        for (int j = 1; j <= i; j++){
            b+=sin(2*j);
        }

        arr[i-1] = (a/b);

    }

    double ans = 1; 
    for (int i = 0; i < n; i++){
        ans*=arr[i];
    }
    cout << ans;
    return 0;
}