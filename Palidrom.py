sayi = (input("Sayi giriniz:"))
ters=(sayi[::-1])
if ters == sayi:
    print("Girilen sayi palindromdur.")
else:
    print("Girilen sayi palindrom değildir...")