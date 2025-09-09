#include <iostream>
#include <cmath>
#include <string>


using namespace std;

int main(){
    int const height = 31, width = 101;
    char grafik[height][width];
    for (int i = height - 1; i >= 0; i--){
        for (int j = 0; j < width; j++){
            grafik[i][j] =  ' ';

        }
        
    }
    for (int i = 0; i < height - 1; i++){
        grafik[i][0] = '|';
    }
    for (int i = 1; i < width-1; i++){
        grafik[15][i] = '-';

    }
    grafik[height - 1][0] = '^';
    grafik[15][width - 1] = '>';
    double sin_value[100];
    int j = 0;
    for (double i = 0; i <= 6.28; i+=0.0628){
        // cout << round(sin(i)*10) << ' ';
        sin_value[j] = round(sin(i)*10);
        j++;
    }


    for (int i = 1; i < width; i++ ){
        int y = sin_value[i-1];
        grafik[15+y][i] = '*';
    }

// output 
    for (int i = height - 1; i >= 0; i--){
        for (int j = 0; j < width; j++){
            cout<<grafik[i][j];

        }
        cout << endl;
    }



    return 0;
}


