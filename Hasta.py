import datetime

class Hasta:
    def _init_(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi, tedavi_suresi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi
        self.__tedavi_suresi = tedavi_suresi

    def get_hasta_no(self):
        return self.__hasta_no

    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no

    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_dogum_tarihi(self):
        return self.__dogum_tarihi

    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    def get_hastalik(self):
        return self.__hastalik

    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik

    def get_tedavi(self):
        return self.__tedavi

    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi

    def get_tedavi_suresi(self):
        return self.__tedavi_suresi

    def set_tedavi_suresi(self, tedavi_suresi):
        self.__tedavi_suresi = tedavi_suresi

    def tedavi_suresi_hesapla(self, baslangic_tarihi, bitis_tarihi):
        baslangic = datetime.datetime.strptime(baslangic_tarihi, "%Y-%m-%d")
        bitis = datetime.datetime.strptime(bitis_tarihi, "%Y-%m-%d")
        tedavi_suresi = (bitis - baslangic).days
        return tedavi_suresi


    def _str_(self):
        return f"Hasta No: {self.get_hasta_no()}, Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Doğum Tarihi: {self.get_dogum_tarihi()}, Hastalık: {self.get_hastalik()}, Tedavi: {self.get_tedavi()}, Tedavi Süresi: {self.get_tedavi_suresi()}"