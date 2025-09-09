#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int n;
    cin >> n;
    
    double arr[n];

    for (int i = 1; i <= n; i++){
        
        double b = 0;
        for (int j = 1; j <= i; j++){
            b+=sin(j);
        }

        arr[i-1] = (i/b);

    }

    double ans = 0; 
    for (int i = 0; i < n; i++){
        ans+=arr[i];
    }
    cout << ans;


    return 0;
}