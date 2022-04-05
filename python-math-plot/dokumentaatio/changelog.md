# Changelog

## Viiko 3
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
