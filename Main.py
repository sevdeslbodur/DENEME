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
              
    # Doktor maaşlarını %10 artırma
    doktor1.maas_arttir(10)  # %10 arttırmak için oran 10 olarak geçilir
    doktor2.maas_arttir(10)
    doktor3.maas_arttir(10)
    
    # Güncellenmiş doktor maaşlarını yazdırma
    print("Güncellenmiş Doktor Maaşları:")
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
    
     # Hemşire maaşlarını %10 artırma
    hemsire1.maas_arttir(10)  # %10 arttırmak için oran 10 olarak geçilir
    hemsire2.maas_arttir(10)
    hemsire3.maas_arttir(10)

    # Güncellenmiş hemşire maaşlarını yazdırma
    print("Güncellenmiş Hemşire Maaşları:")
    print(hemsire1)
    print(hemsire2)
    print(hemsire3)
    print("-----------------------------------")

      
    # Hasta nesnelerini oluşturma
    hasta1 = Hasta("H-0001", "Ümmü", "Özdemir", "1979-04-20", "Grip", "Antibiyotik", 0)
    hasta2 = Hasta("H-0002", "Ayşe", "Demir", "1994-11-15", "Migren", "Ağrı kesici", 0)
    hasta3 = Hasta("H-0003", "Fatma", "Kara", "1982-03-05", "Diyabet", "İnsülin", 0)

     # Başlangıç ve bitiş tarihlerini içeren bir liste oluşturma
    tedavi_tarihleri = [
        ("2024-05-01", "2024-05-08"),
        ("2024-05-02", "2024-05-30"),
        ("2024-05-03", "2024-06-14")
    ]

    # Tedavi Süreleri:
    print("Tedavi Süreleri:")
    for i, (baslangic, bitis) in enumerate(tedavi_tarihleri):
        if i == 0:
            hasta = hasta1
        elif i == 1:
            hasta = hasta2
        else:
            hasta = hasta3
        tedavi_suresi = hasta.tedavi_suresi_hesapla(baslangic, bitis)
        hasta.set_tedavi_suresi(tedavi_suresi)  # Tedavi süresini hasta nesnesine kaydet
        print(f"Başlangıç Tarihi: {baslangic}, Bitiş Tarihi: {bitis}")
        print(f"Hasta {i+1} Tedavi Süresi: {tedavi_suresi} gün")
        print("-----------------------")

    # Hasta Bilgilerini Yazdırma
    print("Hasta Bilgileri:")
    print(hasta1)
    print(hasta2)
    print(hasta3)
    print("-----------------------")



      # Tüm nesnelerden DataFrame oluşturma
    data = {
        "nesne": ["personel1", "personel2", "doktor1", "doktor2", "doktor3", "hemsire1", "hemsire2", "hemsire3", "hasta1", "hasta2", "hasta3"],

        "personel_no": [personel1.get_personel_no(), personel2.get_personel_no(), doktor1.get_personel_no(), doktor2.get_personel_no(), doktor3.get_personel_no(), hemsire1.get_personel_no(), hemsire2.get_personel_no(), hemsire3.get_personel_no(), 0, 0, 0],
        
        "ad": [personel1.get_ad(), personel2.get_ad(), doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(), hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(), hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
        
        "soyad": [personel1.get_soyad(), personel2.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(), hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad(), hasta1.get_soyad(), hasta2.get_soyad(), hasta3.get_soyad()],
        
        "departman": [personel1.get_departman(), personel2.get_departman() , doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(), hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman(), 0, 0, 0],
        
        "maas": [personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(), hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(), 0, 0, 0],
        
        "uzmanlik": [0, 0, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), 0, 0, 0, 0, 0, 0],
        
        "deneyim_yili": [0, 0, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(), 0, 0, 0, 0, 0, 0],
        
        "hastane": [0, 0, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(), hemsire2.get_hastane(), hemsire3.get_hastane(), 0, 0, 0],
        
        "calisma_saati": [0, 0, 0, 0, 0, hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(), 0, 0, 0],
        
        "sertifika": [0, 0, 0, 0, 0, hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(), 0, 0, 0],
        
        "hasta_no": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
        
        "dogum_tarihi": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
        
        "hastalik": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
        
        "tedavi": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()],
        
        "tedavi_suresi": [0, 0, 0, 0, 0, 0, 0, 0, hasta1.get_tedavi_suresi(), hasta2.get_tedavi_suresi(), hasta3.get_tedavi_suresi()]
    }

    df = pd.DataFrame(data)

      
    # Eksik değerleri içeren satırları silme
    df.dropna(inplace=True)

    # DataFrame'de NaN değerlerini kontrol etme
    nan_values = df.isna().sum().sum()

    if nan_values > 0:
        print("DataFrame'de NaN değerleri var.")
    else:
        print("DataFrame'de NaN değerleri yok.")

    print("DataFrame:")
    print(df)
    print("-----------------------------------")
    
    # Boş olan değişken değerlerine 0 atama
    df.fillna(0, inplace=True)


     # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama ve yazdırma
    doktor_uzmanlik_gruplari = df[df['uzmanlik'] != 0].groupby('uzmanlik').size()
    print("Doktor Uzmanlık Grupları ve Sayıları:")
    print(doktor_uzmanlik_gruplari)
    print("-----------------------------------")

    # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
    deneyimli_doktorlar = df[(df['deneyim_yili'] > 5) & (df['deneyim_yili'] != 0)].shape[0]
    print("5 yıldan fazla deneyime sahip doktorların sayısı:", deneyimli_doktorlar)
    print("-----------------------------------")

    # Hasta adına göre DataFrame’i alfabetik olarak sıralama ve yazdırma
    df_hasta_sirali = df[df['hasta_no'] != 0].sort_values(by='ad')
    print("Alfabetik Sıralanmış Hasta Bilgileri:")
    print(df_hasta_sirali)
    print("-----------------------------------")
    
    # Maaşı 7000 TL üzerinde olan personelleri bulup ve yazdırın
    maas_7000_uzeri = df[df['maas'] > 7000]
    print("Maaşı 7000 TL üzerinde olan personeller:")
    print(maas_7000_uzeri)
    print("-----------------------------------")
    
    # Doğum tarihi 1990 ve sonrası olan hastaları gösterme
    df['dogum_tarihi'] = pd.to_datetime(df['dogum_tarihi'], errors='coerce')  # Hatalı tarihleri NaT yapar
    df_dogum_tarihi_1990_sonrasi = df[(df['dogum_tarihi'] >= '1990-01-01') & (df['dogum_tarihi'].notna())]
    print("Doğum Tarihi 1990 ve Sonrası Olan Hastalar:")
    print(df_dogum_tarihi_1990_sonrasi)
    print("-----------------------------------")

     
    # Ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastalik, tedavi bilgilerini içeren yeni bir DataFrame oluşturma
    yeni_df = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi", "tedavi_suresi"]]
    print("Yeni DataFrame:")
    print(yeni_df)

    
except Exception as e:
    print(str(e))