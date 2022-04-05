Viikko1:

[viikko1: gitlog](https://github.com/hnenonen/ot-harjoitustyo/blob/master/laskarit/viikko1/gitlog.txt)

[viikko1: komentorivi](https://github.com/hnenonen/ot-harjoitustyo/blob/master/laskarit/viikko1/komentorivi.txt)

Viikko2:

[viikko2: testikattavuus](https://github.com/hnenonen/ot-harjoitustyo/blob/master/laskarit/viikko2/testcoverage.png)

**Ohjelmistotekniikan harjoitustyö**

[vaatimusmäärittely](https://github.com/hnenonen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/hnenonen/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

Viikko3:
x
x

# TaylorApp

Sovelluksen avulla käyttäjän on mahdollista luoda haluamastaan funktiosta approksimaatio Taylor-polynomilla sekä piirtää kuvaaja, jossa molemmat on esitetty suhteessa toisiinsa.

Sovellus on toteutettu Helsingin Tietojenkäsittelytieteen kurssin Ohjelmistotekniikan menetelmät kurssityönä.

## Huomio Python-versiosta

Sovelluksen toimnta on testattu Python-versiolla 3.8. Muiden versioiden toimivuudesta ei takeita.

## Dokumentaatio

- [Käyttöohje] tulossa
- [Vaatimusmäärittely](https://github.com/hnenonen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus] tulossa
- [Testausdokumentti] tulossa
- [Työaikakirjanpito](https://github.com/hnenonen/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/hnenonen/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

1. Tarvittavien riippuvuuksien asentamien:

```bash
poetry install
```

2. Invoke suorittaa vaadittavat alustustoimenpiteet:

```bash
poetry run invoke build
```

3. Nyt ohjelma käynnistyy seuraavasti:

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

### 2. Testikattavuus raportin generointi

```bash
poetry run invoke coverage-report
```

Raportti löytyy nyt _htmlcov_-hakemistosta.
