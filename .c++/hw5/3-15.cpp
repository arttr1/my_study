#include <stdio.h>
#include <conio.h>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
 
int main() {
    setlocale(LC_ALL, "");
    ifstream ifile("3-15.txt");
    string word = "";
    string result = "";
    char letter = ' ';
    
    
	cin >> word;
 
    while (ifile.peek() >= 0) { // проход до конца файла
        ifile >> letter;
		result += letter;
    }
    ifile.close();

    int pos = result.find(word, 0);
    
    if (pos != -1) {
		cout << pos << endl;
	}
    else {
    	cout << "слово не найдено\n";
	}

    return 0;
}