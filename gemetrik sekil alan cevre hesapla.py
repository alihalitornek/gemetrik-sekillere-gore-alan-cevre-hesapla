class Sekil():
    def __init__(self,sayi1,sayi2,sayi3):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        self.sayi3 = sayi3
        self.pi=3.14159


    def dikdortgencevre(self):
        return 2*self.sayi1+2*self.sayi2
    def dikdortgenalan(self):
        return self.sayi1*self.sayi2
    def karecevre(self):
        return 2*self.sayi1+2*self.sayi1
    def karealan(self):
        return self.sayi1*self.sayi1
    def dairecevre(self):
        return 2*self.pi*self.sayi1
    def dairealan(self):
        return self.pi*self.sayi1*self.sayi1
    def ucgencevre(self):
        return self.sayi1+self.sayi2+self.sayi3
    def ucgenalan(self):
        return ((self.ucgencevre()/2)*(self.ucgencevre()/2-self.sayi1)*(self.ucgencevre()/2-self.sayi2)*(self.ucgencevre()/2-self.sayi3))**(1/2)

sayi1 = 0
sayi2 = 0
sayi3 = 0


while(1):
    print("1. dikdortgen cevre hesapla\n2. dikdortgen alan hesapla\n3. kare cevre hesapla\n4. kare alan hesapla\n5. daire cevre hesapla\n6. daire alan hesapla\n7. ucgen cevre hesapla\n8. ucgen alan hesapla\nlutfen bir secim yapın")
    secim = input()
    if (secim == "1" or secim == "2"):
        sayi1 = float(input("lutfen ilk kenari gir"))
        sayi2 = float(input("lutfen ikinci kenari gir"))
    elif (secim == "3" or secim == "4" or secim == "5" or secim == "6"):
        sayi1 = float(input("lutfen sayiyi gir"))
    elif (secim == "7" or secim == "8"):
        sayi1 = float(input("lutfen ilk kenari gir"))
        sayi2 = float(input("lutfen ikinci kenari gir"))
        sayi3 = float(input("lutfen ucuncu kenari gir"))

    s1 = Sekil(sayi1,sayi2,sayi3)

    if (secim == "1"):
        print("sonuc :", s1.dikdortgencevre())
    elif (secim == "2"):
        print("sonuc :", s1.dikdortgenalan())
    elif (secim == "3"):
        print("sonuc :", s1.karecevre())
    elif (secim == "4"):
        print("sonuc :", s1.karealan())
    elif (secim == "5"):
        print("sonuc :", s1.dairecevre())
    elif (secim == "6"):
        print("sonuc :", s1.dairealan())
    elif (secim == "7"):
        print("sonuc :", s1.ucgencevre())
    elif (secim == "8"):
        print("sonuc :", s1.ucgenalan())
    else :
        print("hatali secim")
