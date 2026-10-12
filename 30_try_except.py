try:
    fiyat=float(input("Ürünün fiyatı kaça?:"))
    if fiyat<=0:
        print("Fiyat sıfırdan büyük olmalı ya")
    else:
        print("Fiyat=",fiyat,"TL")
except ValueError:
    print("Knk sayı girmelisin!!!!")
