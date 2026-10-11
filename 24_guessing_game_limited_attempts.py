hak = 3
while True:
  tahminn=int(input("Tuttuğum sayıyı bilebilecek misin?3 hakkın var.3 denemede oyun sona erer.Gönder tahminini:"))
  if tahminn==7:
    print("NASIL BİLDİN DOĞRU BİLDİN KRAL")
    break
  hak=hak - 1
  if hak==0:
    print("HAKLARIN SONA ERDİİİ OYUN BİTTİ GOOD GAME")
    break
  elif tahminn<7:
    print("Daha büyük bir sayı tahmin etmelisin")
  elif tahminn>7:
    print("Daha küçük bir sayı tahmin etmelisin")
