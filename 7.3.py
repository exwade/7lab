import os
from PIL import Image, ImageFilter

def apply_filter_to_images(input_files, output_dir, filter):
    # Создание выходной директории, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in input_files:
        try:
            with Image.open(file_name) as img:
                # Применение фильтра
                filtered_img = img.filter(filter)
                
                # Сохранение нового изображения
                base_name = os.path.basename(file_name)
                new_name = f"filtered_{base_name}"
                output_path = os.path.join(output_dir, new_name)
                filtered_img.save(output_path)
                print(f"Фильтр применен и изображение сохранено как '{output_path}'")
        
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка с файлом '{file_name}': {e}")

if __name__ == "__main__":
    # Список файлов для обработки
    input_files = ["images/1.jpg", "images/2.jpg", "images/3.jpg", "images/4.jpg", "images/5.jpg"]
    # Директория для сохранения обработанных изображений
    output_dir = "filtered_images"
    # Выбранный фильтр (CONTOUR)
    selected_filter = ImageFilter.CONTOUR

    apply_filter_to_images(input_files, output_dir, selected_filter)