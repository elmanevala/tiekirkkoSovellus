# Asennusohje

## Paikallisesti

* Lataa sovellus koneelleesi. Osoitteessa https://github.com/elmanevala/tiekirkkoSovellus sivun ylälaidassa on nappi, jota painamalla voi ladata sovelluksen ZIP-tiedostona.
* Luo sovellukselle kansio omalle koneellesi. Siirrä ZIP-tiedosto kansioon, pura se ja siirry sovelluksen juurikansioon.
* Luo kansioon venv-virtuaaliympäristö komennolla:
```
 python -m venv venv
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

* To be continued