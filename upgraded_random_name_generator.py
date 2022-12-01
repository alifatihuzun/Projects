import random

isim_listesi = []
soyisim_listesi = []

selection = input("Yapmak istediğiniz işlemi seçiniz (isim_ekleme, isim_çıkarma, isim_görüntüleme, rastgele,"
                  "soyisim_ekleme, soyisim_çıkarma, soyisim_görüntüleme)")

if selection == "isim_ekleme":
    ekleme = input("Eklemek istediğiniz isim: ")
    isim_listesi.append(ekleme)

elif selection == "isim_çıkarma":
    çıkarma = input("Çıkarmak istediğiniz ismi seçiniz "+print(isim_listesi))
    isim_listesi.remove(çıkarma)
    selection

elif selection == "isim_görüntüleme":
    print(isim_listesi)
    selection

elif selection == "rastgele":
    print(random.choice(isim_listesi)+" "+ soyisim_listesi)
    selection
