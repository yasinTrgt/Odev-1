print("3 adet sayi giriniz")
sayi1=int(input("1.sayiyi giriniz:"))
sayi2=int(input("2.sayiyi giriniz:"))
sayi3=int(input("3.sayiyi giriniz:"))
if sayi1==sayi2==sayi3:
    print("Bütün sayilar eşit")
else:
    if sayi1>sayi2 and sayi1>sayi3:
        print("En büyük sayı :", sayi1)
    elif sayi2>sayi3:
        print("En büyük sayı :",sayi2)
    else:
      print("En büyük sayı :",sayi3)
