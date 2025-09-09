#include <iostream>
#include <fstream>
using namespace std;

int main() {
  int i = 0; // кол-во цифр
  double sum = 0; // сумма
  double digital = 0;
  
  ofstream file("41.txt");
  while (i != 10) { // ввод чисел
  	i += 1;

  	if (cin >> digital) { // проверка на число
  		file << digital << "\n"; // запись в файл
	  }
	else {
		cout << "Incorrect input!" << endl;
		return 0;
	}
  }
  file.close();
  
  ifstream ifile("41.txt");
  while (i != 20) { // сумма чисел
  	ifile >> digital; // чтение из файла
    sum += digital; 
    i += 1;
  }
  ifile.close();
  
  cout <<sum << endl;
  return 0;
}