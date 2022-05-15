#Testidokumentaatio

## Yksikkö- ja intergraatiotestaus

### Sovelluslogiikka

TaylorApp:in matematiikasta vastaavaa `Approximate`-luokkaa testataan [MathTest](https://github.com/hnenonen/ot-harjoitustyo/blob/master/python-math-plot/src/tests/math_service_test.py)-testiluokalla. 

### Testauskattavuus

Käyttöliittymä kerrosta lukuunottamatta ohjelman haaraumakattavuus on 100%.

![](./dokumentaatio/testikattavuus.png)

### Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus- ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla Linux-ympäristössä.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](./vaatimusmaarittely.md#perusversion-tarjoama-toiminnallisuus) ja käyttöohjeen perusversion toiminnallisuudet on käyty läpi ja testattu.
Funktion plottaus ei kaadu väärästä syötteestä, testattu mm. tyhjä.

## Sovellukseen jääneet laatuongelmat	

Nykyisellään sovelluksessa ei ole ongelmia. Seuraava vaihe on rakentaa tietokanta ja siihen testaus.
