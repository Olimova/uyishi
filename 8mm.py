import os

def remove(file):

    if os.path.isfile(file):
        os.remove(file)
        print(f"{file} o'chirildi.")
    else:
        print(f"{file} topilmadi yoki bu fayl emas.")
