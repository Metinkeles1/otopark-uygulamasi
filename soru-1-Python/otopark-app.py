import sys
içerdekiaraç = 0  
liste = list()

def İçerik(sayi):     
    global içerdekiaraç    
    global liste
    
    if(sayi == 1):                  
        arac = input("\nAraç Plakasını Giriniz: ")
        içerdekiaraç +=1
        print("İçerdeki Araç Sayısı:" , içerdekiaraç , "\n")
        liste.append(arac)
        if(içerdekiaraç == 2):
            print("İçerdeki Araç Sayısı: " , içerdekiaraç , "Lütfen Araç Çıkışı Yapınız.\n ")
            AnaMenu()                            
        AnaMenu()

    elif(sayi == 2):
        çikicakaraç = input("\nÇıkıcak Olan Araç Plakasını Giriniz: ")    
        if çikicakaraç in liste:
            otoparktaKalinanSüre = int(input("Otoparkta Kalınan Süre: "))
            if(otoparktaKalinanSüre <= 3):
                print("Ödemeniz Gereken Tutar: " , otoparktaKalinanSüre * 5 , " TL\n")
                içerdekiaraç -= 1
                if(içerdekiaraç <= 0):
                    print("İçerdeki Araç Sayısı", içerdekiaraç, "Ana Menuye Yönlendiriliyorsunuz...\n")
                    AnaMenu()
                AnaMenu()
                
            elif(otoparktaKalinanSüre > 3):
                print("Ödemeniz Gereken Tutar: 40 TL\n")
                içerdekiaraç -= 1
                if(içerdekiaraç <= 0):
                    print("İçerdeki Araç Sayısı", içerdekiaraç, "Ana Menuye Yönlendiriliyorsunuz...\n")
                    AnaMenu()
                AnaMenu()
                
        else:
            print("Girdiğiniz Plaka Yanlış\n");
            AnaMenu()
    
    elif(sayi==-1):
        print("Sistemden Çıktınız.")
        sys.exit(0)
                
    else:
        print("Yanlış İfade Girdiniz. ");
        AnaMenu()
    
def AnaMenu():    
    print("Araç Girişi (1): ")
    print("Araç Çıkışı (2): ")
    print("Program Çıkışı (-1): ")
    sayi = int(input("seçiminiz:"))
    İçerik(sayi)
 
AnaMenu()