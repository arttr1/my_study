// #include <iostream>
// using namespace std;

// int main(){

//     setlocale(0, "");
//     int a[11] = {136, 173, 228, 174, 224, 172, 160, 226, 168, 170, 160};
//     for (int i = 0; i < 11; i ++){
//         cout << char(a[i]) << " ";
//     }


//     return 0;
// }

#include <vector>
#include <iostream>
// Данные о цвете (три байта)
struct Colour
{
unsigned char r;
unsigned char g;
unsigned char b;
};
// Оператор сравнения цветов
bool operator==(const Colour& c1, const Colour& c2)
{
return c1.r == c2.r && c1.g == c2.g && c1.b == c2.b;
}
// Ширина и высота холста
const size_t WIDTH = 800;
const size_t HEIGHT = 600;
// «Радиус» квадрата
const size_t SQUARE_SIZE = 10;
//Функция кодирования числа переменной длины
template <typename T>
std::vector<unsigned char> encode_to_varlength (T number)
{
std::vector<unsigned char> res {};
size_t shift = 0;
while (number >> shift > 0)
{
shift += 7;
}
if (shift == 0)
{
res.push_back(0);
return res;
}
shift -= 7;
while (shift > 0)
{
res.push_back(0x10 | ((number>>shift) & 0x7F));
shift -= 7;
}

res.push_back((number>>shift) & 0x7F);
return res;
}
int main()
{
// Холст
Colour image[WIDTH*HEIGHT] {};
for (size_t row=0; row<HEIGHT; ++row)
{
for (size_t col=0; col<WIDTH; ++col)
{
if
(
row >= HEIGHT/2-SQUARE_SIZE &&
row < HEIGHT/2+SQUARE_SIZE &&
col >= WIDTH/2-SQUARE_SIZE &&
col < WIDTH/2+SQUARE_SIZE
)
{
// Закраска квадрата
image[WIDTH*row+col] = Colour{r: 0xFF, g: 0, b: 0};
}
else
{
// Закраска фона
image[WIDTH*row+col] = Colour{r: 0, g: 0, b: 0xFF};
}
}
}
// Переменная для хранения байтов сжатого файла
std::vector<unsigned char> bytes {};
// Запись ширины
for (unsigned char byte : encode_to_varlength(WIDTH))
{
bytes.push_back(byte);
};
//Запись высоты
for (unsigned char byte : encode_to_varlength(HEIGHT))
{
bytes.push_back(byte);

}
// Переменная для длины последовательности одного цвета
size_t sequence_length{0};
// Переменная для цвета текущей последовательности
Colour sequence_colour{};
for (Colour colour : image)
{
if (colour == sequence_colour)
{
// Приращение длины последовательности
sequence_length += 1;
}
else
{
if (sequence_length > 0)
{
// Запись длины последовательности
for (unsigned char byte :
 encode_to_varlength(sequence_length))
{
bytes.push_back(byte);
}
// Запись цвета
bytes.push_back(sequence_colour.r);
bytes.push_back(sequence_colour.g);
bytes.push_back(sequence_colour.b);
}
// «Обнуление» последовательности
sequence_colour = colour;
sequence_length = 1;
}
}
// Запись оставшейся последовательности
for (unsigned char byte : encode_to_varlength(sequence_length))
{
bytes.push_back(byte);
}
bytes.push_back(sequence_colour.r);
bytes.push_back(sequence_colour.g);
bytes.push_back(sequence_colour.b);

// Вывод длины сжатого файла
std::cout << bytes.size() << '\n';
return 0;
}
