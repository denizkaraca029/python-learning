urun = input("Hangi ürünü alırsın bro???!:")
fiyat = int(input("Ürünün fiyatı kaça?:"))
print("Ürünnnn:",urun)
print("Fiyatttt:",fiyat,"TLcik")
kactene=int(input("Yavas lan gac tene alıyon??:"))
tutar=fiyat*kactene
print("Ürün:",urun,"Toplam:",tutar)
if tutar>=200:
    indirimsonrasi=tutar-tutar*0.10
    print("Tebrikler %10 indirim aldınız!Artık ödemeniz gereken",indirimsonrasi,"TL")
else:
    print("İndirim yok bro ödenecek:",tutar,"TL")
