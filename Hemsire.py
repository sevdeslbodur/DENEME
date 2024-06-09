from Personel import Personel

class Hemsire(Personel):
    def _init_(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super()._init_(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def get_calisma_saati(self):
        return self.__calisma_saati

    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika
        
    def get_hastane(self):
        return self.__hastane

    def set_hastane(self, hastane):
        self.__hastane = hastane


    def maas_arttir(self, oran):
        self.set_maas(float(self.get_maas()) * (1 + oran / 100))


    def _str_(self):
        return f"Personel No: {self.get_personel_no()}, Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Departman: {self.get_departman()}, Maaş: {self.get_maas()}, Çalışma Saati: {self.get_calisma_saati()}, Sertifika: {self.get_sertifika()}, Hastane: {self.get_hastane()} "