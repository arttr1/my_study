
#include <iostream>
#include <string>

int minChangesToPalindrome(const std::string& str) {
    int left = 0; // Указатель на начало строки
    int right = str.size() - 1; // Указатель на конец строки
    int changes = 0; // Количество изменений

    while (left < right) {
        if (str[left] != str[right]) {
            changes++; // Если символы не совпадают, увеличиваем счетчик изменений
        }
        left++;
        right--;
    }

    return changes;
}

int main() {
    std::string input;
    std::cout << "Введите строку: ";
    std::getline(std::cin, input); // Считываем строку

    int result = minChangesToPalindrome(input);
    std::cout << "Минимальное количество изменений для превращения строки в палиндром: " << result << std::endl;

    return ;
}