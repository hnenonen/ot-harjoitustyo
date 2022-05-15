# Arkkitehtuurikuvaus

Ohjelma noudattaa pakkauskaaviota

![](./pakkauskaavio_todellinen.png)

Repositoriota ja Entityä ei ole vielä toteuttu normaaliin pakkauskaavio rakenteeseen, koska tietokanta puuttuu.


## Sovelluslogiikka

Toiminnallisuuksista vastaa olio Math_Service. Luokka tarjoaa toiminnoille metodit:
- define(function)
- taylor(function

Olio Ui_plot huolehtii luotujen funktioiden graafisesta esityksestä metodille:
- plotting(function, taylor)

## Päätoiminnallisuudet

Tällä hetkellä oleva toiminnallisuus on esitetty seuraavassa sekvenssikaaviossa:

![](./sekvenssikaavio.png)


## Tulevat ominaisuudet

Seuraavaksi luodaan tietokanta, jolla pidetään muistissa käyttäjät ja heidän tutkimansa funktiot.

Tietomallin, jota ei ole vielä toteutettu muodostavat User ja Functions.


```mermaid
 classDiagram
      Functions "*" --> "1" User
      class User{
          username
      }
      class Functions{
          id
          function
          taylor
      }
```
Tällöin pakkauskaavio noudattaa seuraavaa:
![](./pakkauskaavio_todellinen.png)


