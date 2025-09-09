#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <iomanip>
#include <windows.h>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    setlocale(0, "");
    double a[3][4], b[4][3], s[3], k[3], mini_k = 100000000000, maxi_k = 0,  mini_v = 100000000000, maxi_v = 0, sum_s = 0, sum_k = 0;
    int max_v, min_v,  max_k, min_k; 

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 4; j++){
            cin >> a[i][j];
        }
    }
    
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 2; j++){
            cin >> b[i][j];
        }
    }
    // вычисление выручки и комиссионых продавцов
    for (int i = 0; i < 3; i++){
        double t=0, r = 0;
        for (int j = 0; j < 4; j++){
            t += a[i][j]*b[j][0];
            r += a[i][j]*b[j][1];
        }
            s[i] = t; // выручка 
            k[i] = r; // комиссионные 
    }
    // определение продавцов выручивших больше и меньше всего
    for (int i = 0; i < 3; i ++ ){
        sum_s += s[i];
        sum_k += k[i];

        if (s[i] > maxi_v){
            maxi_v = s[i];
            max_v = i;
        }
        if (s[i] < mini_v){
            mini_v = s[i];
            min_v = i;
        }
        if (k[i] > maxi_k){
            maxi_k = k[i];
            max_k = i;
        }

        if(k[i] < mini_k){
            mini_k = k[i];
            min_k = i;

        }
    }
cout << "-----------------------------------" << endl;
cout<<"summa" << s[0] << " " << s[1] << " " << s[2] << endl;
cout<<"kom" << k[0] << " " << k[1] << " " << k[2] << endl;

//1   
    cout << max_v+1 << " " << min_v+1 << endl;
//2 
    cout << max_k+1 << " " << min_k+1 << endl;
//3
    cout << sum_s << endl;
//4 
    cout << sum_k << endl;
//5
     cout << sum_k + sum_s;
    


    // for (int i = 0; i < 3; i++){
    //     for (int j = 0; j < 4; j++){
    //         cout<<setw(5) << a[i][j] << " ";
    //     }
    //     cout << endl;
    // }



    
    return 0;
}