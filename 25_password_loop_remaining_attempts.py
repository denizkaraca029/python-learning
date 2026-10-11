hak = 5
while True:
  sifre = input("Şifrenizi giriniz-->")
  if sifre == "python456":
    print("Giriş başarılı")
    break
  hak = hak - 1
  if hak == 0:
    print("Hakkınız kalmadı")
    break
  else:
    print("Yanlış şifre tekrar deneyin kalan hak",hak)
