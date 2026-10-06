yas = int(input("kaç yaşındasın kirve = "))
if yas<0:
  print("ÖYLE Bİ YAŞ YOK KOLPACU") 
elif 0<=yas<18:
  print("Çocuksun yaw") 
elif 18<=yas<65:
  print("Sıkıcı yetişkin") 
elif yas>=65:   
  print("Emekli")
