import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):    
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(250)
        self.assertEqual(str(self.maksukortti), "saldo: 2.6")

    def test_kortilta_voi_ottaa_rahaa(self):   
        self.maksukortti.lataa_rahaa(250)
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 2.1")

    def test_kortilta_ei_voi_ottaa_liikaa_rahaa(self):   
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")    

    #Metodi palauttaa True, jos rahat riittivät ja muuten False <-- miten toteutetaan?