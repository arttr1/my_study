// #include <iostream>

// using namespace std;

// int main(){

//     int t;
//     cin >> t;
//     int arr[t][2];

//     for (int i = 0; i < t; i++){
//         for (int j = 0; j < 2; j++){
//             cin >> arr[i][j];
//         }    
//     }

//     for (int i = 0; i < t; i++){
//         long long sum = 0, ra = arr[i][1] - arr[i][0]+1,l = arr[i][0], r = arr[i][1];
        
//         for (int j = 0; j < ra;j++){
//             sum += (l+j)*(r - j);
//         }
        
//         // if (r%2==0){
//         //     sum += (l+ra )*(r - ra)*2;
//         // }
//         // else{
//         //     sum += (l+ra )*(r - ra);
//         // }
//         cout << sum << endl;
//     }


//     return 0;
// }