from Personel import Personel

class Doktor(Personel):
    def _init_(self, personel_no, ad, soyad, departman , uzmanlik, deneyim_yili,maas,hastane):
        super()._init_(personel_no, ad, soyad, departman, maas,hastane)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane
        

    def get_uzmanlik(self):
        return self.__uzmanlik

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili
        
    def get_hastane(self):
        return self.__hastane

    def set_hastane(self, hastane):
        self.__hastane = hastane
        
    def maas_arttir(self, oran):
        self.set_maas(float(self.get_maas()) * (1 + oran / 100))

    
    def _str_(self):
       return f"Personel No: {self.get_personel_no()}, Ad: {self.get_ad()}, Soyad: {self.get_soyad()},  Departman: {self.get_departman()}, Uzmanlık: {self.get_uzmanlik()}, Deneyim Yılı: {self.get_deneyim_yili()}, Maaş: {self.get_maas()}, Hastane: {self.get_hastane()}"