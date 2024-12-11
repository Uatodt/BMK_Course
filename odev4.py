# 1 - Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def yineleyici(str, n, ind = "\n"):
    for _ in range(n):
        print(str, end = ind)

# 2 - Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def cevre_alan(a, b):
    circumference = 2 * (a + b)
    area = a * b
    return circumference, area

# 3 - Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
def yazi_tura():
    import random
    x = random.randint(0, 2)
    match x:
        case 0:
            return "Yazı"
        case 1:
            return "Tura"

# 4 - Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def asal_bulucu(n):
    asal = set()
    for k in range(2, n + 1): # [2, n] aralığında
        prime = True
        # "Trial division" teoremi: p∈ℕ sayısı, 2 <= n <= sqrt(p) olan ∀n∈ℕ sayıları için p !≡ 0 (mod n) ise asaldır. 
        for i in range(2, int(k ** 0.5) + 1): # [2, √k] aralığı
            if k % i == 0:
                prime = False
                break
        if prime:
            asal.add(k)
    return asal

def asal_aralik(a, b):
    if a is b:
        return set()
    else:
        if b < a:
            temp = b
            b = a
            a = temp
        return asal_bulucu(b).difference(asal_bulucu(a))

# 5 - Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def bolenler(n):
    bolen = []
    for i in range(1, n + 1):
        if n % i == 0:
            bolen.append(i)
    return bolen