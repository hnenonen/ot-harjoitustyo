# TaylorApp

Sovelluksen avulla käyttäjän on mahdollista luoda haluamastaan funktiosta approksimaatio Taylor-polynomilla sekä piirtää kuvaaja, jossa molemmat on esitetty suhteessa toisiinsa.

Sovellus on toteutettu Helsingin Tietojenkäsittelytieteen kurssin Ohjelmistotekniikan menetelmät kurssityönä.

## Huomio Python-versiosta

Sovelluksen toimnta on testattu Python-versiolla 3.8. Muiden versioiden toimivuudesta ei takeita.

## Dokumentaatio

- [Käyttöohje] tulossa
- [Vaatimusmäärittely](https://github.com/hnenonen/ot-harjoitustyo/blob/master/python-math-plot/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/hnenonen/ot-harjoitustyo/blob/master/python-math-plot/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti] tulossa
- [Työaikakirjanpito](https://github.com/hnenonen/ot-harjoitustyo/blob/master/python-math-plot/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/hnenonen/ot-harjoitustyo/blob/master/python-math-plot/dokumentaatio/changelog.md)

## Asennus
Koneella täytyy olla poetry asennettuna, muuten poetry install ei toimi. 
Tämä selviää komentoriviltä kysymällä poetry --version, jos poetry löytyy voit siirtyä kohtaan 1.
Muuten asenna poetry, ohjeet löytyvät mm. [täältä](https://ohjelmistotekniikka-hy.github.io/python/viikko2) kohdasta "Asennus".

1. Tarvittavien riippuvuuksien asentamien:

```bash
poetry install
`````

2. Nyt ohjelma käynnistyy seuraavasti:

```bash
poetry run invoke start
```

## Seuraavat invoke käskyt toimivat komentorivillä:

### 1. Ohjelman käynnistäminen

```bash
poetry run invoke start
```

### 2. Ohjelman testien ajaminen

```bash
poetry run invoke test
```

### 3. Testikattavuus raportin generointi

```bash
poetry run invoke coverage-report
```

Raportti löytyy nyt _htmlcov_-hakemistosta.

### 4. Koodin laadun tarkastus pylintillä

```bash
poetry run invoke lint
```

