#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <windows.h>
#include <cstring>


using namespace std;

string in(int x, int b){
    char s[16] {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
    string c = "";
    int k = 1;
    while (x!=0){
        c += s[(x%b)];
        k *= 10;
        x /= b;
    }
    string c1="";
    for (int i = c.size()-1; i>=0; i--){
        c1+=c[i];
    }
    return c1;
}
int out(string s, int a){
    char sym[] {'0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
    int res = 0;
    for (int i = s.size()-1; i >=0; i--){
        char c = s[i];
        int r = -1;
        for (int j = 0; j < 16; j++){
            if (c == sym[j]){
                r = j;
                // return r;
            }   
        }
        if (r == -1)
            return -1;
        else{
            res += r*pow(a, s.size() - i - 1);
        }

    }
    return res;
}

int main(){
    // ascii code - 55 -> need int 
    string s;
    cin >> s;
    int a, b;
    cout << "из какой сс вы хотите перевести? ";
    cin >> a;
    cout << endl << "в какую сс вы хотите перевести? ";
    cin >> b;
    int r = out(s, a);
    cout << in(r, b);


    return 0;
}