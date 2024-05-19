import os
from PIL import Image

# Открытие изображения
image_path = "images/Grisha.jpg" 
image = Image.open(image_path)

# Вывод изображения на экран
image.show()

# Получение информации об изображении
image_size = image.size  # Размер изображения (ширина, высота)
image_format = image.format  # Формат изображения (JPEG, PNG)
image_mode = image.mode  # Цветовая модель (RGB, RGBA)

# Вывод информации в консоль
print(f"Размер изображения: {image_size}")
print(f"Формат изображения: {image_format}")
print(f"Цветовая модель изображения: {image_mode}")