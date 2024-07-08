import os
from PIL import Image

# Функция для чтения изображений из локальной папки
def load_images_from_folder(folder_path):
    images = []
    if not os.path.exists(folder_path):
        print(f"Путь не существует: {folder_path}")
        return images

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path).convert('RGB')
                images.append(img)
            except Exception as e:
                print(f"Не удалось открыть изображение {img_path}: {e}")
    return images

# Функция для размещения изображений на одном холсте
def create_collage(images, output_path, cols=3, rows=3, thumb_width=300, thumb_height=300, padding=20):
    if not images:
        print("Нет изображений для создания коллажа.")
        return

    collage_width = cols * (thumb_width + padding) + padding
    collage_height = rows * (thumb_height + padding) + padding
    collage_image = Image.new('RGB', (collage_width, collage_height), (255, 255, 255))

    x_offset = padding
    y_offset = padding

    for i, img in enumerate(images):
        if i >= cols * rows:
            break
        img.thumbnail((thumb_width, thumb_height))
        collage_image.paste(img, (x_offset, y_offset))
        x_offset += thumb_width + padding
        if x_offset >= collage_width - padding:
            x_offset = padding
            y_offset += thumb_height + padding

    collage_image.save(output_path, "TIFF", compression="tiff_lzw", dpi=(72, 72))
    print(f"Коллаж успешно сохранен в {output_path}")

# Главная функция
def main(folder_paths, output_file, cols, rows, thumb_width, thumb_height, padding):
    all_images = []

    for folder_path in folder_paths:
        images = load_images_from_folder(folder_path)
        all_images.extend(images)

    create_collage(all_images, output_file, cols, rows, thumb_width, thumb_height, padding)

if __name__ == "__main__":
    # Укажите реальные пути к папкам с изображениями
    folder_paths = ['images_folder1']
    output_file = "Result.tif"
    
    # Параметры коллажа
    cols = 3  # количество столбцов
    rows = 3  # количество строк
    thumb_width = 300  # ширина миниатюры
    thumb_height = 300  # высота миниатюры
    padding = 20  # отступ между изображениями

    main(folder_paths, output_file, cols, rows, thumb_width, thumb_height, padding)
