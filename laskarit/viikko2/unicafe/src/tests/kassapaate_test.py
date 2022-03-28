import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = 0
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    #def test_kassapaate_on_olemassa(self):     ???
    #    self.assertNotEqual(self.kassapaate)

    def syo_edullisesti_kateisella_lisaa_kassaan_rahaa_oikein(self): #syo_edullisesti maksaa 240
        self.kassassa_rahaa.syo_edullisesti_kateisella(500)
        self.assertEqual(str(self.kassassa_rahaa), 500-240)

    def syo_edullisesti_kateisella_ei_anna_ostaa_jos_liian_vahan_rahaa(self):
        self.kassassa_rahaa.syo_edullisesti_kateisella(100)
        self.assertEqual(str(self.kassassa_rahaa), 100)