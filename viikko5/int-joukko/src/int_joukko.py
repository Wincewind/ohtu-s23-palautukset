KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti: int=KAPASITEETTI, kasvatuskoko: int=OLETUSKASVATUS):
        self.kapasiteetti = self._tarkista_argumentin_tyyppi(kapasiteetti)
        self.kasvatuskoko = self._tarkista_argumentin_tyyppi(kasvatuskoko)
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _tarkista_argumentin_tyyppi(self,argumentti):
        if not isinstance(argumentti, int) or argumentti < 0:
            raise TypeError("Kapasiteetin ja kasvatuskoon täytyy olla tyyppiä int ja >= 0")
        return argumentti

    def kuuluu(self, n):
        try:
            self.ljono.index(n)
            return True
        except ValueError:
            return False

    def lisaa(self, n):
        luku_ei_ollut_viela_listassa = not self.kuuluu(n)
        if luku_ei_ollut_viela_listassa:
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                taulukko_old = self.ljono
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)

            return luku_ei_ollut_viela_listassa

        return luku_ei_ollut_viela_listassa

    def poista(self, poistettava_luku):
        poistettava_loytyi = False

        for i in range(0, self.alkioiden_lkm):
            if poistettava_luku == self.ljono[i] and not poistettava_loytyi:
                poistettava_loytyi = True
                self.alkioiden_lkm = self.alkioiden_lkm - 1
            if poistettava_loytyi:
                self.ljono[i] = self.ljono[i+1]

        return poistettava_loytyi

    def kopioi_lista(self, lahde_lista, kohde_lista):
        for i,_ in enumerate(lahde_lista):
            kohde_lista[i] = lahde_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i,_ in enumerate(taulu):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        tulos_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for _,i in enumerate(a_taulu):
            tulos_joukko.lisaa(i)
        for _,i in enumerate(b_taulu):
            tulos_joukko.lisaa(i)

        return tulos_joukko

    @staticmethod
    def leikkaus(a, b):
        tulos_joukko = IntJoukko()
        a_taulu = a.to_int_list()

        for _,i in enumerate(a_taulu):
            if b.kuuluu(i):
                tulos_joukko.lisaa(i)

        return tulos_joukko

    @staticmethod
    def erotus(vahennettava, vahentaja):
        tulos_joukko = IntJoukko()
        vahennettava_taulu = vahennettava.to_int_list()
        vahentaja_taulu = vahentaja.to_int_list()

        for _, i in enumerate(vahennettava_taulu):
            tulos_joukko.lisaa(i)

        for _, i in enumerate(vahentaja_taulu):
            tulos_joukko.poista(i)

        return tulos_joukko

    def __str__(self):
        tuotos = "{"
        if self.alkioiden_lkm > 0:
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i])+ ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
        return tuotos + "}"
