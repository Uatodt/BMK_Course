"""
    module1 (db)      : urunler
    module2 (methods) : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)     :
        yeni ürün ekleme => urunEkle("iPhone 15", 60000)
        ürün güncelle    => urunGuncelle(1, "iPhone 15 Pro", 80000)
        ürünleri listele => urunleriGetir() 
"""
from db import products as p
from methods import urunleri_getir, urun_ekle, urun_guncelle

urunleri_getir(p)
urun_ekle(p, 11, "iPhone 15 Pro", 60000)
urun_guncelle(p, 11, 89999)
urunleri_getir(p)
