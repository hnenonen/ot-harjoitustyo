# Changelog

## Viikko 3
- Käyttäjälle avautuu suroraan ohjelman käynnistyessä Math_view, johon voi syöttää function
- Painamalla "graph it!" ohjelma toimii seuraavasti:
	- oikealla syötteellä luo graafin, jossa käyttäjän antama funktio sekä sen approksimoitu taylor-polynomi
	- tyhjällä syötteellä ohjelma ei tee mitään 
- Testattu, että Approximate-luokan metodit palauttavat oikean output, kun input oikein

Rakenne:

index.py
--src---
services | math_service.py
ui	| math_view.py, ui.py
tests  | math_service_test.py


## Viikko 4
- Luotu login ikkuna, josta ohjelma alkaa. Nappia painalla näkymä vaihtuu matikkaikkunaan.
- Ui elementit keskitetty ui.py, jota kutsutaan index.py
- Arkkitehtuuri.md dokumentti aloitettu
- pylint invoke lisätty, muut toimivat jo viime viikolla - koodin laatu yli 9/10


Rakenne:

index.py
--src---
services | math_service.py
ui       | ui.py, login_view.py, math_view.py
tests    | math_service_test.py

## Viikko 5 
- virheellisten syötteiden käsittely funktiota syötettäessä
- näkymiä ja koodia siistitty
- sekvenssikaavio luotu
- ensimmäinen release

Rakenne:

index.py
--src---
services | math_service.py
ui       | ui.py, login_view.py, math_view.py
tests    | math_service_test.py


## Viikko 6
- koko kurssin vaivannut virheilmoitus terminaalissa ohjelmaa käytettäessä ratkaistu (palaute ohjaaja ja vertais)
- Luotu uusi näkymä CreateView, osa login kokonaisuutta, tietokantaa ei ole vielä
- Luotu Docstringit seuraaviin luokkiin
	- UI, CreateView, Approximate, UIPlot
	- puuttuu: LoginView, MathView
- Korkean tason sovelluslogiikka lisätty arkkitehtuurikuvaukseen

