import os

def count(path):
    if os.path.exists(path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print(f"{path} papkasida {len(files)} ta fayl bor.")
    else:
        print(f"{path} topilmadi.")
