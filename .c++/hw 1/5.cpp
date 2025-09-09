#include <iostream>

using namespace std;

int main(){
    setlocale(0, "");
    // 1 - да 
    // 0 - нет
    bool a, b, c, f;
    cout << "на улице день?";
    cin >> a;
    cout << "открыты шторы?";
    cin >> b;
    cout << "включена лампа?";
    cin >> c;

    f = (a&&b) || c;
    if (f == 1)
        cout << "в комнате светло";
    else 
        cout << "в комнате темно";


    return 0;
}