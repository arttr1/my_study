#include <iostream>
using namespace std;


int digit(char x) { // римские числа в арабские
	switch(x) {
		case 'I': return 1;
		case 'V': return 5;
		case 'X': return 10;
		case 'L': return 50;
		case 'C': return 100;
		case 'D': return 500;
		case 'M': return 1000;
	}
	return -1;
}


int convert(string x) {
	int i;
	int j = 0;
	int lenX;
	int result = 0;
	lenX = x.length() - 1;
	
	for(i = lenX; i >= 0; i--) {
		if (digit(x[i]) >= j)
			result += digit(x[i]);
		else
			result -= digit(x[i]);
		j = digit(x[i]);
	}
	return result;
}

int main() {
  string x;
  cin >> x;
  cout << convert(x) << endl;
  main();
}