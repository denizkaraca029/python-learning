bakiye = 1000 
while True:
  print("""1-Bakiye görüntüle 
  2-Para yatır
  3-Para çek
  4-Çık""")
  secim = input("Ne yapmak istiyorsunuz?:")
  if secim == "1":
    print(bakiye,"TLniz var")
  elif secim == "2":
    parayatir=int(input("Ne kadar yatırmak istiyorsunuz?:"))
    if parayatir<=0:
      print("POZİTİF BİR DEĞER GİRMELİSİNİZ KNKM")
    else:
      bakiye = bakiye + parayatir
      print("Hesabınızda",bakiye,"TL var para başarıyla yatırıldı")
  elif secim == "3":
    paracek=int(input("Ne kadar çekmek istiyorsunuz?:"))
    if paracek<=0:
      print("POZİTİF BİR DEĞER GİRMELİSİNİZ KNKM")
    elif paracek>bakiye:
      print("yetersiz bakiye olmayan parayı nasıl çekcen")
    else:
      bakiye = bakiye - paracek
      print("Hesabınızda",bakiye,"TL var para başarıyla çekildi")
  elif secim == "4":
    print("Çıkış")
    break
  else:
    print("1 2 3 4 seçebilirsin başka sayı ya da harf geçersiz")
