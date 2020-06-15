# Käyttöohje

Sovelluksessa voi lisätä omia ja selata muiden kommentteja Suomen eri tiekirkoista. Tiekirkkojen oppaat voivat myös käyttää sovellusta vierailijoiden määrän kirjanpitoon. Kaikilla käyttäjillä on perukäyttäjän toiminnallisuudet. Tämän lisäksi oppailla ja adminilla on lisätoiminnallisuuksia.

## Tunnukset
Herokussa on jo valmiiksi kaikkien käyttäjäryhmien käyttäjiä.

Admin-käyttäjä, joka voi muutta peruskäyttäjiä oppaiksi:
```
 Käyttäjänimi: admin
 Salasana: salasana1
```
Opas, joka voi merkata kuinka monta vierailijaa kävi tänään:
```
 Käyttäjänimi: opas
 Salasana: salasana1
```
Peruskäyttäjä:
```
 Käyttäjänimi: peruskayttaja
 Salasana: salasana1
```
Jos käytät sovellusta paikallisesti, ensimmäinen luotu käyttäjä on admin.

## Käyttöohje ei-kirjautuneelle käyttäjälle:

* Jos haluat katsoa tietyn kirkon kommentteja, kirjoita etsimäsi kirkko oikean yläkulman hakupalkkiin.
* Jos haluat rekisteröityä, paina yläpalkin rekisteröitymisnappulaa ja syötä tarvittavat tiedot lomakkeelle. Saat virhevietejä epäkelvoista syötteistä, kuten jo varatusta käyttäjänimestä.

## Käyttöohje peruskäyttäjälle

* Rekisteröitymisen jälkeen voi kirjautua sovellukseen painamalla yläpalkin kirjautumisnappulaa ja syöttämällä omat tietosi lomakkeelle.
* Valikkonappulaa painamalla, avautuu valikko, josta voi siirtyä eri toimintoihin.
    * Selaa omia vierailuja -nappula vie sinut listanäkymään, jossa on kaikki kirjaamasi vierailut. Tämän listan kautta voit myös poistaa omia kommenttejasi tai muokata niitä. Muokkaus näkymässä näät kommenttisi tarkemmat tiedot ja voit muuttaa kommenttia painamalla Tallenna päivitetty kommentti -nappulaa. Voit myös muuttaa oppaan statusta
    * Selaa kirkkoja kunnittain -nappula vie sinut listanäkymään, jossa on kaikki tiekirkolliset kunnat. Näät listasta kuinka monta kirkkoa kyseisessä kunnassa on ja kuinka monta kommenttia kyseisen kunnan kirkoista on jätetty. Voit siirtyä tarkastelemaan kunnan kirkkoja ja niiden kommentteja painamalla nappuloita Selaa kunnan kirkkoja ja Selaa kirkon vierailuja.
    * Lisää uusi vierailu -nappula vie sinut näkymään, jossa voit lisätä uusia vierailuja. Kuten oikean ylälaidan hakukenttä, myös uuden kirkon lisäämiskenttä ehdottaa valmiiksi tietokannassa olevia kirkkoja. Kun täytät lomakkeen tiedot, uusi kommentti on tietokannassa. Voit nähdä sen omien vierailuidesi listalla ja muut voivat nähdä kommenttisi ja käyttäjänimesi, kun he etsivät kirkkoja tai selailevat kuntia.
    * Omat tiedot -nappula vie sinut sivulle, jossa on käyttäjätunnuksesi tiedot. Voit myös muokata omia tietojasi tässä näkymässä.
        * HUOM: 15.6. ja 16.6. on pieni hetki jolloin muutetulla salasanalla ei enää pääse kirjautumaan sovellukseen!!
    * Kirjaudu ulos -nappula kirjaa sinut ulos ja vie takaisin etusivulle.

## Käyttöohje oppaille

* Jos kuulut opas-käyttäjäryhmään, voit lisätä työpäiväsi päätteksi vierailijoiden määrän.
    * Oppailla näkyy yläpalkissa opasvalikko.
        * Lisää päivän vierailijamäärä -nappulasta pääset näkymään, jossa voit lisätä kyseisen päivän vierailijat. Vierailijat voi lisätä vain kerran päivässä, joten se kannattaa tehdä työpäivän päätyttyä.
        * Tilastonappulasta pääsee tarkastelemaan työpaikkakirkkojesi tilastoja, kuten kuinka monta vierailijaa on käynyt kirkossa yhteensä ja kuinka moni on jättänyt sovellukseen kommentin.
        * Molemmista opasnäkymistä voi kätevästi siirtyä myös tarkastelemaan vierailijoiden jättämiä kommentteja.

## Käyttöohje adminille

* Sovellukseen ensimmäisen kirjautunut käyttäjä on admin.
    * Adminilla näkyy yläpalkissa admin-valikko.
        * Käyttäjätnappulaa painamalla pääsee listanäkymään, jossa on kaikki sovelluksen käyttäjät. Käyttäjat on listattuna sen mukaan, kuinka monta kirkkoa, heillä on työpaikkana. Käyttäjä, jolla on eniten kirkkoja on ylimpänä. Lisää käyttäjälle kirkkoja -nappulaa painamalla voit lisätä käyttäjälle kirkkoja. Voit lisätä yhdelle käyttäjälle yhden kirkon vain kerran ja näkymässä näät käyttäjällä jo olevat kirkot.
        * Kun käyttäjällä on kirkko, hänellä on opas.