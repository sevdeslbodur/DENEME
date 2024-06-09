import pandas as pd
import datetime
from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

try:
    # Personel nesnelerini oluşturma ve yazdırma
    print("Personel Bilgileri:")
    personel1 = Personel("1001", "Ege", "Yılmaz", "Sekreter", 3000)
    personel2 = Personel("1002", "Mira", "Çelik", "İnsan Kaynakları",3500)
    print(personel1)
    print(personel2)
    print("-----------------------------------")

    # Doktor nesnelerini oluşturma ve yazdırma
    print("Doktor Bilgileri:")
    doktor1 = Doktor("1003", "Hakan", "Kaya", "Doktor", "Dahiliye", 8, 7500.00, "Şehir Hastanesi" )
    doktor2 = Doktor("1004", "Rasim", "Bodur",  "Doktor", "Ortopedi", 5, 6000.00, "Eğitim Hastanesi")
    doktor3 = Doktor("1005", "Ahmet", "Yıldız", "Doktor", "Nöroloji", 10, 9000.00, "Özel Hastane")
    print(doktor1)
    print(doktor2)
    print(doktor3)
    print("-----------------------------------")
          
          
      # Hemşire nesnelerini oluşturma ve yazdırma
    print("Hemşire Bilgileri:")
    hemsire1 = Hemsire("1006", "Rüzgar", "Gül", "Pediatri", 4500.00, 36, "A Sertifikası", "Eğitim Hastanesi")
    hemsire2 = Hemsire("1007", "Mehmet", "Can", "Diyaliz", 4000.00, 28, "B Sertifikası", "Özel Hastane")
    hemsire3 = Hemsire("1008", "Hatice", "Örs", "Onkoloji", 5000.00, 40, "C Sertifikası", "Şehir Hastanesi")
    print(hemsire1)
    print(hemsire2)
    print(hemsire3)
    print("-----------------------------------")
    
          
    # Hasta nesnelerini oluşturma
    hasta1 = Hasta("H-0001", "Ümmü", "Özdemir", "1979-04-20", "Grip", "Antibiyotik", 0)
    hasta2 = Hasta("H-0002", "Ayşe", "Demir", "1994-11-15", "Migren", "Ağrı kesici", 0)
    hasta3 = Hasta("H-0003", "Fatma", "Kara", "1982-03-05", "Diyabet", "İnsülin", 0)

  
      
          