import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaate_on_alustettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    # syo_edullisesti maksaa 240
    def test_syo_edullisesti_kateisella_lisaa_kassaan_rahaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100240)
        self.assertEqual((self.kassapaate.edulliset), 1)

    def test_syo_edullisesti_kateisella_ei_anna_ostaa_jos_liian_vahan_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)
        self.assertEqual((self.kassapaate.edulliset), 0)

    # syo_maukkaasti maksaa 400
    def test_syo_maukkaasti_kateisella_lisaa_kassaan_rahaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100400)
        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_syo_maukkaasti_kateisella_ei_anna_ostaa_jos_liian_vahan_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)
        self.assertEqual((self.kassapaate.maukkaat), 0)

    def test_kortilla_riittavasti_rahaa_ostetaan_edulliset(self):
        maksukortti = Maksukortti(500)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(tulos, True)
        self.assertEqual((self.kassapaate.edulliset), 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_ei_riittavasti_rahaa_ostetaan_edulliset(self):
        maksukortti = Maksukortti(100)
        tulos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(tulos, False)
        self.assertEqual((self.kassapaate.edulliset), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_riittavasti_rahaa_ostetaan_maukkaasti(self):
        maksukortti = Maksukortti(500)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(tulos, True)
        self.assertEqual((self.kassapaate.maukkaat), 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_ei_riittavasti_rahaa_ostetaan_maukkaasti(self):
        maksukortti = Maksukortti(100)
        tulos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(tulos, False)
        self.assertEqual((self.kassapaate.maukkaat), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataaminen_toimii_oikein_kun_annetaan_rahaa(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
        #maksukortti.lataa_rahaa(200)
        self.assertEqual(str(maksukortti), "saldo: 3.0")
        
    def test_kortille_lataaminen_ei_onnistu_ilman_rahaa(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -10)
        self.assertEqual(str(maksukortti), "saldo: 1.0")
        
