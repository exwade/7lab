import os
from PIL import Image, ImageDraw, ImageFont

def add_watermark(image, watermark_text, position, font_path, font_size=30):
    # Создание копии изображения
    watermark_image = image.copy().convert("RGBA")
    drawable = ImageDraw.Draw(watermark_image)
    
    # Использование TrueType шрифта с заданным размером
    font = ImageFont.truetype(font_path, font_size)
    
    # Определение размеров текста
    bbox = drawable.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x, y = position
    if x + text_width > watermark_image.width:
        x = watermark_image.width - text_width
    if y + text_height > watermark_image.height:
        y = watermark_image.height - text_height
    
    # Наложение водяного знака
    drawable.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)
    return watermark_image

def apply_watermark_to_images(input_files, output_dir, watermark_text, position, font_path, font_size=30):
    # Создание выходной директории, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in input_files:
        try:
            with Image.open(file_name) as img:
                watermarked_img = add_watermark(img, watermark_text, position, font_path, font_size)
                
                # Сохранение нового изображения
                base_name = os.path.basename(file_name)
                new_name = f"watermarked_{base_name[:-4]}.png"
                output_path = os.path.join(output_dir, new_name)
                watermarked_img.save(output_path)
                print(f"Водяной знак добавлен и изображение сохранено как '{output_path}'")
        
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка с файлом '{file_name}': {e}")

# Список файлов для обработки
input_files = ["images/1.jpg", "images/2.jpg", "images/3.jpg", "images/4.jpg", "images/5.jpg"]
# Директория для сохранения обработанных изображений
output_dir = "watermarked_images"
# Текст водяного знака
watermark_text = "Sample Watermark"
# Позиция водяного знака
position = (10, 10)
# Путь к файлу шрифта
font_path = "arial.ttf"  # Замените на путь к вашему шрифту, если необходимо
# Размер шрифта водяного знака
font_size = 30

apply_watermark_to_images(input_files, output_dir, watermark_text, position, font_path, font_size)
