hak = 5
deneme = 0
while True:
  sifre = input("Şifrenizi giriniz-->")
  deneme = deneme + 1
  if sifre == "python456":
    print("Giriş başarılı",deneme,". denemede girdiniz")
    break
  hak = hak - 1
  if hak == 0:
    print("Hakkınız kalmadı")
    break
  else:
    print("Yanlış şifre tekrar deneyin kalan hak",hak)
