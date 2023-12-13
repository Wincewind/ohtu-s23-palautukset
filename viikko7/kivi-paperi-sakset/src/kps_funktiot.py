from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def luo_peli():
    print("Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
            )
    valinta = input()
    if valinta in ['a','b','c']:
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        if valinta.endswith("a"):
            return KPSPelaajaVsPelaaja()
        if valinta.endswith("b"):
            return KPSTekoaly()
        if valinta.endswith("c"):
            return KPSParempiTekoaly()
