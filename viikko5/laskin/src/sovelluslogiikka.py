class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo
    
    @property
    def arvo(self):
        return self._arvo
    

class Summa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, get_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.get_syote = get_syote
        self._arvo = 0

    def _jasentele_luku(self):
        arvo = 0
        try:
            arvo = int(self.get_syote())
        except Exception:
            pass
        return arvo
    
    def suorita(self):
        self._arvo = self._jasentele_luku()
        self.sovelluslogiikka.plus(self._arvo)
        

    def kumoa(self):
        self.sovelluslogiikka.miinus(self._arvo)

class Erotus(Summa):
    def suorita(self):
        self._arvo = self._jasentele_luku()
        self.sovelluslogiikka.miinus(self._arvo)

    def kumoa(self):
        self.sovelluslogiikka.plus(self._arvo)

class Nollaus(Summa):
    def suorita(self):
        self._arvo = self.sovelluslogiikka.arvo
        self.sovelluslogiikka.nollaa()
    
    def kumoa(self):
        self.sovelluslogiikka.aseta_arvo(self._arvo)
