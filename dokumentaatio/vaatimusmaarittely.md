# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi laskea antamalleen funktiolle määräämässään pisteessä approksimoivan Taylor polynomin.
Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, jotka kaikki näkevät omat aiemmin ajamansa funktiot ja käyttämänsä parametrit.
Näiden avulla on helppo regeneroida ajo uudelleen.

##Käyttäjät

Alkuvaiheessa sovelluksella on vain yksi käyttäjärooli, normaalikäyttäjä. Myöhemmin sovellukseen lisätään pääkäyttäjä, jolla on suuremmat oikeudet.

Perusversion tarjoama toiminnallisuus

##Käyttöliittymäluonnos

![](./dokumentaatio/kayttoliittymaluonnos.pdf)

*Ennen kirjautumista*

Käyttäjä voi luoda järjestelmään käyttäjätunnuksen, jolloin siirrytään näkymään 2.

Käyttäjä voi kirjautua järjestelmään, jolloin siirrytään näkymään 3.

*Kirjautumisen jälkeen*

Käyttäjä näkee aiemmin tutkimansa funktiot ja parametrit sekä pari malliajoa

Käyttäjä voi generoida uuden funktion tutkimisen, jolloin siirrytään näkymään 4.

Käyttäjä voi kirjautua ulos, jolloin siirrytään näkymään 1.

*Tutkimuksen ajon jälkeen*

Käyttäjä näkee kuvaajan, jossa tutkittu funktio sekä sitä vastaan generoitu Taylor polynomi sekä käyttämänsä parametrit ja funktion ja polynomin virhe käsitellyssä pisteessä.

Käyttäjä voi ajaa uuden tutkimuksen, jolloin palataan näkymään 3.

Käyttäjä voi kirjautua ulos, jolloin palataan näkymään 1.



