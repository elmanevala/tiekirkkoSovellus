# Asennusohje

Oletetaan, että asentajalla on käytössä:
* [GitHub-tunnukset](https://github.com/)
* [Heroku-tunnukset](https://www.heroku.com/)
* [Pythonin versio 3.5](https://www.python.org/downloads/) tai uudempi
* Pip-tuki python-kirjastojen luomiseen
* Tuki [venv](https://docs.python.org/3/library/venv.html)-kirjastojen luomiseen.
* [PostgreSQL-tietokantajärjestelmä](https://www.postgresql.org/)
* Komentorivityövälineet sekä [git-versiohallintajärjestelmää](https://git-scm.com/downloads/) että [herokua](https://devcenter.heroku.com/articles/heroku-cli) varten.

## Paikallisesti

* Lataa sovellus koneelleesi. Osoitteessa https://github.com/elmanevala/tiekirkkoSovellus sivun ylälaidassa on nappi, jota painamalla voi ladata sovelluksen ZIP-tiedostona.
* Luo sovellukselle kansio omalle koneellesi. Siirrä ZIP-tiedosto kansioon, pura se ja siirry sovelluksen juurikansioon.
* Luo kansioon venv-virtuaaliympäristö komennolla:
```
 python3 -m venv venv
```
* Aktivoi venv komennolla:
```
 source venv/bin/activate
```
* Lataa sovelluksen vaatimat riippuvuudet komennolla:
```
pip install -r requirements.txt
```
* Sovellus käynnistyy komennolla:
```
python run.py
```
* Sovellus löytyy nyt osoitteista http://localhost:5000/ ja http://127.0.0.1:5000/.

## Herokussa

* Luo sovellukselle repositorio GitHubissa ja siirry takaisin sovelluksen juurikansioon.
* Ota käyttöön git-versiohallinta komennolla
```
 git init
```
* Lisää sovellus luotuun repositorioon komennoilla:
```
git remote add origin **projektin_osoite**
git add.
git push -u origin master
```
* Luo sovellukselle paikka Herokuun komennolla:
```
heroku create *sovelluksen_nimi*
```
* Lisää tieto herokusta versiohallintaan:
```
git remote add heroku https://git.heroku.com/*sovelluksen_nimi*.git
```
* Lisää sovellus Herokuun:
```
git add .
git commit -m "Viesti"
git push heroku master
```

* Sovellus löytyy nyt osoitteesta https://*sovelluksen_nimi*.herokuapp.com/

Halutessasi voit ottaa käyttöön Herokun github-integraation, jolloin vain Heroku päivittyy automaattisesti GitHubin mukaan.