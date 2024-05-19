import os
from PIL import Image

def process_image(image_path):
    try:
        # Открытие изображения
        with Image.open(image_path) as img:
            # Получение оригинальных размеров
            original_width, original_height = img.size
            
            # Создание уменьшенной в три раза копии изображения
            new_width = original_width // 3
            new_height = original_height // 3
            smaller_img = img.resize((new_width, new_height), Image.LANCZOS) # Алгоритм ресемплинга
            smaller_img.save("images/smaller_image.jpg")
            print(f"Уменьшенное изображение сохранено как 'smaller_image.jpg'")
            
            # Создание горизонтального зеркального изображения
            horizontal_flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
            horizontal_flip_img.save("images/horizontal_flip_image.jpg")
            print(f"Горизонтально зеркальное изображение сохранено как 'horizontal_flip_image.jpg'")
            
            # Создание вертикального зеркального изображения
            vertical_flip_img = img.transpose(Image.FLIP_TOP_BOTTOM)
            vertical_flip_img.save("images/vertical_flip_image.jpg")
            print(f"Вертикально зеркальное изображение сохранено как 'vertical_flip_image.jpg'")
    
    except FileNotFoundError:
        print(f"Файл '{image_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


image_path = "images/Grisha.jpg" # Путь к нашей картинке
process_image(image_path)