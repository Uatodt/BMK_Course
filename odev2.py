# 1) Bir aracın yakıt tipine göre (benzin, dizel, lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

fuelPrices = {
    "gasoline" : 39.35,
    "diesel" : 41.71,
    "lpg" : 20.28
}

fuelType = str(input("What type of fuel (gasoline, diesel, LPG) have you used? "))

while fuelType.casefold() not in fuelPrices:
    fuelType = str(input("There seems to be a typo, please try again: "))

km = float(input(f"For how many kilometres have you used {fuelType.capitalize()}? "))

cost = fuelPrices[fuelType.casefold()] * km

print(f"Your total cost is {cost}$.")

# 2) Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#    90-100 => AA
#    80-89  => BA
#    70-79  => BB
#    60-69  => CB
#    50-59  => CC
#    40-49  => DC

notlar = {
    9 : "AA", 
    8 : "BA", 
    7 : "BB", 
    6 : "CB", 
    5 : "CC", 
    4 : "DC"
}
ilkvize = float(input("Birinci arasınav notunuzu giriniz: "))
sonvize = float(input("İkinci arasınav notunuzu giriniz: "))
final = float(input("Anasınav notunuzu giriniz: "))

ortalama = (0.3 * (ilkvize + sonvize) + 0.4 * final) // 10
if ortalama not in notlar:
    print("Geçemediniz.")
else:
    print(notlar[ortalama] + " aldınız!")