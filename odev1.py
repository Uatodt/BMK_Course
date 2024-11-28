# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
cars = ["Toyota", "BMW", "Renault", "Mercedes"]
print(cars)

# 2- Liste kaç elemanlıdır?
length = len(cars)
print(f"Liste, {length} elemanlıdır.")

# 3- Listenin ilk ve son elemanı nedir?
print(f"Listenin ilk elemanı {cars[0]} elemanıdır.")
print(f"Listenin son elemanı {cars[3]} elemanıdır.")

# 4- "Renault" markasını "Togg" ile güncelleyiniz.
cars[2] = "Togg"

# 5- "Togg" listenin bir elemanı mıdır?
innit = "Togg" in cars
if innit:
    print(f"{cars[2]} var.")
else:
    print(f"{cars[2]} yok.")

# 6- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
cars += ["Ford", "Citroen"]

# 7- Listenin son elemanını siliniz.
last = len(cars) - 1
del cars[last]
print(cars)
# 8- Aşağıdaki verileri liste içerisinde saklayınız (Liste içinde liste mümkündür.).

    # öğrenci1: Yiğit Bilgi 2010 [70, 80, 90]
    # öğrenci2: Ada Bilgi   2011 [70, 70, 80]
    # öğrenci3: Çınar Turan 2017 [60, 60, 90]

datas = [
    ["Yiğit Bilgi", "Ada Bilgi", "Çınar Turan"], # Names
    [2010, 2011, 2017], # Birth years
    [
        [70, 80, 90], # First student's grades
        [70, 70, 80], # Second student's grades
        [60, 60, 90] # Third student's grades
    ]
]

print(f"1. öğrenci: {datas[0][0]}, doğum yılı {datas[1][0]}, notları {datas[2][0][0]}, {datas[2][0][1]}, {datas[2][0][2]}.")
print(f"2. öğrenci: {datas[0][1]}, doğum yılı {datas[1][1]}, notları {datas[2][1][0]}, {datas[2][1][1]}, {datas[2][1][2]}.")
print(f"3. öğrenci: {datas[0][2]}, doğum yılı {datas[1][2]}, notları {datas[2][2][0]}, {datas[2][2][1]}, {datas[2][2][2]}.")

# 9- Öğrencilerin yaşlarını hesaplayınız.
YEAR = 2024
print("1. öğrencinin yaşı: " + str(YEAR - datas[1][0]))
print("2. öğrencinin yaşı: " + str(YEAR - datas[1][1]))
print("3. öğrencinin yaşı: " + str(YEAR - datas[1][2]))
# 11- Öğrencilerin not ortalamalarını hesaplayınız.
print("1. öğrencinin not ortalaması: " + str(sum(datas[2][0]) / len(datas[2][0])) 
    + "\n2. öğrencinin not ortalaması: " + str(sum(datas[2][1]) / len(datas[2][1]))
    + "\n3. öğrencinin not ortalaması: " + str(sum(datas[2][2]) / len(datas[2][2]))
)