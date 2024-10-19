import os

def remove_empty_folder(path):
    if os.path.exists(path):
        try:
            os.rmdir(path)
            print(f"{path} bo'sh papka o'chirildi.")
        except OSError:
            print(f"{path} bo'sh emas yoki o'chirib bo'lmadi.")
    else:
        print(f"{path} topilmadi.")
