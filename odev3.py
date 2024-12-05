numbers = [3, 5, 7, 2, 12, 32, 45]

# 1- "numbers" listesindeki her bir elemanı yazdırınız.
print("Sayılar listesindeki elemanlar:")
for i in numbers:
    print(i) 

# 2- "numbers" listesinde hangi sayılar 3' ün katıdır?
print("Sayılar listesinde üçe bölünen elemanlar:")
for n in numbers:
    if n % 3 == 0:
        print(n)

# 3- "numbers" listesinde tüm sayıların toplamı nedir?
print("Sayılar listesindeki elemanların toplamı: " + str(sum(numbers)))


products = ["iPhone 13","Samsung S24","Samsung S22","iPhone 15","iPhone 14"]

# 4- "products" listesindeki tüm iPhone marka ve Samsung marka ürünleri listeleyiniz. (index() ve find() komutlarından yararlanınız.)
Samsung_products = []
iPhone_products = []

print("iPhone ürünleri: ")
for x in products:
    if x.find("iPhone") != -1:
        iPhone_products.append(x)
print(", ".join(iPhone_products))

print("Samsung ürünleri: ")
for x in products:
    if x.find("Samsung") != -1:
        Samsung_products.append(x)
print(", ".join(Samsung_products))

# 5- "products" listesinde kaç adet Samsung ürünü vardır? (find metodu)
print("Samsung ürünü sayısı: " + len(Samsung_products))

