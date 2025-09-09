#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(){
    setlocale(0, "");
    string s = "pyfgcrlaoeuidhtnsqjkxbmwtijbvz";
    // cout << s.length()<<endl;
    char c[30];
    for(int i = 0; i < 30; i++){
        c[i] = s[i];
    }
    for (int i = 0; i < 30; i++){
      cout << c[i] << ' ';
    }
    
    

     for (int i = 0; i < 30; i++)
    {
      for (int j = 0; j < 30-1; j++)
      {
        if (c[j] > c[j + 1])
        {
          int b = c[j]; 
          c[j] = c[j + 1]; 
          c[j + 1] = b; 
        }
      }
    }
     
    for (int i = 0; i < 30; i++) {
    cout << c[i] << " "; 
    }


    
}