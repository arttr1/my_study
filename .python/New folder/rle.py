import numpy as np
import cv2

def rle_encode(image):
    """
    Кодирование изображения методом RLE.
    
    :param image: Входное изображение в формате numpy array.
    :return: Список пар (значение пикселя, количество повторений) для каждого канала.
    """
    encoded = []
    for channel in range(image.shape[2]):
        flat_channel = image[:, :, channel].flatten()  # Преобразуем канал в одномерный массив
        channel_encoded = []
        prev_pixel = flat_channel[0]
        count = 1

        for pixel in flat_channel[1:]:
            if pixel == prev_pixel:
                count += 1
            else:
                channel_encoded.append((prev_pixel, count))
                prev_pixel = pixel
                count = 1

        # Добавляем последний элемент
        channel_encoded.append((prev_pixel, count))
        encoded.append(channel_encoded)

    return encoded

def rle_decode(encoded, shape):
    """
    Декодирование изображения из формата RLE.
    
    :param encoded: Список пар (значение пикселя, количество повторений) для каждого канала.
    :param shape: Исходная форма изображения (высота, ширина, каналы).
    :return: Восстановленное изображение в формате numpy array.
    """
    decoded = np.zeros(shape, dtype=np.uint8)
    for channel in range(shape[2]):
        decoded_channel = []
        for value, count in encoded[channel]:
            decoded_channel.extend([value] * count)
        
        decoded[:, :, channel] = np.array(decoded_channel).reshape((shape[0], shape[1]))

    return decoded

# Пример использования
if __name__ == "__main__":
    # Загрузка цветного изображения
    image_path = "Untitled.png"  # Укажите путь к вашему изображению
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    if image is not None:
        print("Изображение загружено успешно.")
        print("Размерность изображения:", image.shape)
        
        # Кодирование
        encoded_image = rle_encode(image)
        print("Сжатое изображение:")
        for i, channel in enumerate(encoded_image):
            print(f"Канал {i+1}: {channel}")

        # Декодирование
        decoded_image = rle_decode(encoded_image, image.shape)

        # Проверка результата
        cv2.imshow("Original Image", image)
        cv2.imshow("Decoded Image", decoded_image)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Ошибка при загрузке изображения.")
