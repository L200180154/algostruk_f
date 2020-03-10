#no1

class Pesan(object):
    """Sebuah class bernama Pesan.
       Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru

        
#(a)
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else :
            return False
        
#(b)
    def hitungKonsonan(self):
        jmlhkon = 0
        x = self.teks
        alfaKon = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        for i in x:
            if i in alfaKon:
                jmlhkon += 1
        return jmlhkon
    
#(c)
    def hitungVokal(self):
        jmlhvoc = 0
        x = self.teks
        alfaVoc = "aiueoAIUEO"
        for i in x:
            if i in alfaVoc:
                jmlhvoc += 1
        return jmlhvoc
