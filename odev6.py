# ** BankaHesabi isminde bir sınıf tanımlayınız.
class BankaHesabi:
# ** Üretilen her bir nesne "hesapSahibi" isminde biz özelliğe sahip olmalıdır. BankaHesabi("Ad Soyad")
   def __init__(self, hesapSahibi):
      self.hesapSahibi = hesapSahibi
# ** Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
      self.bakiye = 0.0
# ** Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiye üzerine ekleyin ve bakiye miktarını geriye döndürün.
   def paraYatir(self, amount):
      self.bakiye += amount
      return self.bakiye
# ** Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye değerinden çıkarıp geriye döndürün.
   def paraCek(self, amount):
      if amount < 0:
         print("Geçersiz miktar.")
      elif amount > self.bakiye:
         print("Yetersiz bakiye.")
      else:
         self.bakiye -= amount
         return self.bakiye

name = str(input("Adınız: "))
hesap = BankaHesabi(name)
print(hesap.hesapSahibi)
print(hesap.bakiye)
miktar = float(input("Yatırmak istediğiniz miktar (İptal için 0 giriniz): "))
print(hesap.paraYatir(miktar))
cek = float(input("Çekmek istediğiniz miktar (İptal için 0 giriniz): "))
print(hesap.paraCek(cek))