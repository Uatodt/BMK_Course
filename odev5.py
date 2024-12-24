# Bankamatik Uygulaması
# Hesap bilgileri tutulacak. (dictionary)
# menu, bakiyeSorgula, paraCekme, paraYatirma fonksiyonları tanımlanacak.
# Çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.
hesapBilgileri = {
    "Ahmet DÜNDAR" : {
        "Hesap Numarası" : "12345678", 
        "Bakiye" : 25000, 
        "Ek Hesap" : 5000
    }, 
    "Busenaz AKTAŞ" : {
        "Hesap Numarası" : "87654321", 
        "Bakiye" : 15000, 
        "Ek Hesap" : 3000
    },
    "Eyüp Nuri GÜLER" : {
        "Hesap Numarası" : "13577531", 
        "Bakiye" : 31000, 
        "Ek Hesap" : 7000
    }
}


def menu():
    answer = int(input("\nNe işlem yapmak istersiniz? \n1. Bakiye Sorgulama \n2. Para Yatırma \n3. Para Çekme \n0. İptal \n(Sayı giriniz): "))
    return answer

def bakiye_sorgula(user):
    hesap = hesapBilgileri[user]
    print(f"Hesap Bakiyeniz: {hesap['Bakiye']}₺\nEk Hesap Limitiniz: {hesap['Ek Hesap']}₺")

def para_cekme(name):
    hesap = hesapBilgileri[name]
    amount = float(input("Çekmek istediğiniz tutarı giriniz: "))
    if  hesap["Bakiye"]>= amount:
        hesap["Bakiye"] -= amount 
        print(f"İşleminiz onaylandı. Yeni bakiyeniz: {hesap["Bakiye"]}₺")
    else:
        answer = str(input("Yetersiz bakiye. Ek hesabınızı kullanmak ister misiniz? (Y/N) "))
        while answer.casefold() not in {"y", "n"}:
            answer = str(input("Bilinmeyen komut. Yeniden deneyiniz: (Y/N) "))
        match answer.casefold():
            case "y":
                hesap["Ek Hesap"] -= amount - hesap["Bakiye"]
                hesap["Bakiye"] = 0
                print(f"İşleminiz onaylandı. Bakiyeniz sıfırlandı. Kalan ek hesabınız: {hesap["Ek Hesap"]}")
            case "n":
                print("İşlem bitirildi.")

def para_yatirma(name):
    amount = float(input("Nice para yatıracağınızı giriniz: "))
    hesapBilgileri[name]["Bakiye"] += amount
    print(f"İşleminiz onaylandı. Yeni bakiyeniz: {hesapBilgileri[name]["Bakiye"]}")


name = str(input("Adınızı giriniz: "))
while name not in hesapBilgileri.keys() and name is not None:
    yanit = str(input("Adınızı bulamadık. Devam etmek istiyor musunuz? (Y/N) "))
    while yanit.casefold() not in {"y", "n"}:
        yanit = str(input("Bilinmeyen komut. Yeniden deneyiniz: "))
    match yanit.casefold():
        case "y":
            name = str(input("Adınızı giriniz: "))
        case "n":
            name = None


bool = True
while bool and name is not None:
    answer = menu()    
    match answer:
        case 0:
            bool = False
        case 1:
            bakiye_sorgula(name)
        case 2:
            para_yatirma(name)
        case 3:
            para_cekme(name)
        case _:
            print("Bilinmeyen komut. Yeniden deneyiniz, iptal etmek istiyorsanız '0' giriniz.")