from smartphone import Smartphone

smartphone_list = [
    Smartphone("Nokia", "66290", "7999000111"),
    Smartphone("iPhone", "16", "7999000221"),
    Smartphone("Samsung", "Galaxy S23", "7999000331"),
    Smartphone("Huawei", "Herliphone 2", "7999000441"),
    Smartphone("Xiaomi", "Readme 5", "7999000551"),
    ]

for sf in smartphone_list:
    print(f"{sf.brand}-{sf.model}. {sf.phone_number}")