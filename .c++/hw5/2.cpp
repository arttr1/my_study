#include <iostream>

using namespace std;

// int* f(int n, int m, int *a){
//     if (m >= n)
//         return a;
//     else {
//         if(a[m]!=0){
//             int j = 2*m;
//             if (j < n){
//                 a[j] = 0;
//                 j+=m;
//             }
//         }
//     }



// }



int main(){
    int n, m = 2;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++){
        a[i] = i;
        if (i < 2){
            a[i] = 0;
        }
        
    }

    for (int i = 0; i < n-1; i++){
        if (a[i]!=0){
            for (int j = i+1; j < n; j++){
                if (a[j] % a[i] == 0)
                    a[j] = 0;
            }
        }

    }





    for (int i = 1; i < n; i++){
        if (a[i] != 0)
            cout << a[i] << ' ';
    }
    return 0;
}