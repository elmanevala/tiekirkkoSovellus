# User stories






Sovelluksessa on neljä käyttäjäryhmää: ei-kirjautuneet, kirjautuneet peruskäyttäjät, oppaat ja admin.






### Ei-kirjautuneena vierailijana haluan:

* nähdä etusivulla tietoja kirkkojen vierailuista.

* etsiä tiettyä kirkkoa ja lukea sen kommentteja. **TEHTY**


```
SELECT V.comment, V.date_created, 
(SELECT U.username FROM Account U WHERE U.id=V.account_id)
FROM Church C JOIN Visit V ON C.id=V.church_id AND C.church='Keski-Porin kirkko'
```





* rekisteröityä sovelluksen käyttäjäksi.


Salasanan luomisessa käytetetään Bcryptautsta joten todellisuudessä salasana ei mene sellaisenaan tietokantaan, mutta teoriassa tämä onnistuisi koodilla:

```
INSERT INTO Account (name, username, password, date_created) 
VALUES ('Jari Litmanen', 'litti', 'ajax4ever', '2020-06-14 16:20')
```







### Kirjautuneen peruskäyttäjänä haluan:


* lisätä omia vierailuja eri kirkkoihin. **TEHTY**

```
INSERT INTO Visit (church_id, account_id, comment, tourguide) 
VALUES (178, 3, 'Hieno peruskorjaus vuonna 1996', TRUE)
```





* selata eri paikkakuntia, tietyn paikkakunnan kaikkia tiekirkkoja ja niiden kommentteja. **TEHTY**

Lista paikkakunnista, jossa merkittynä myös tiekirkkojen sekä sovellukseen jätettyjen kommenttien määrä:
```
SELECT DISTINCT A.town AS town,
(SELECT COUNT(*) FROM Church B WHERE B.town=A.town) AS churches,
(SELECT COUNT(V.comment) FROM Church C LEFT JOIN Visit V ON C.id=V.church_id AND C.town=A.town) AS visits
FROM Church A
```
Lista tietyn paikkakunnan kirkoista:
```
SELECT church FROM Church WHERE town='Pori'
```
Kommettien selaus onnistuu samalla kyselyllä kuin ei-kirjautuneella käyttäjällä.






* muokata, lukea ja poistaa kirjoittamiani kommentteja.  **TEHTY**

Kommentin muokkaus:
```
UPDATE Visit SET comment='En sittenkään tykännyt vuoden 1996 peruskorjauksesta:(',
date_modified='2020-06-14 16:20' WHERE id=1
```
Oppaan statuksen muokkaus:
```
UPDATE Visit SET tourguide=FALSE,
date_modified='2020-06-14 16:20' WHERE id=1
```
Omien kommenttien lukeminen:
```
SELECT Church.church, Visit.comment, Visit.tourguide, Visit.id 
FROM Visit JOIN Church ON Visit.church_id = Church.id AND Visit.account_id = 1
```
Oman kommentin poistaminen:
```
DELETE FROM Visit WHERE id=1
```





* tarkastella oman käyttäjätunnukseni tietoja. **TEHTY**

```
SELECT username, name FROM Account WHERE user_id=3
```





* muokata omien käyttäjätunnusteni tietoja. **TEHTY**

Nimen muokkaus:
```
UPDATE Account SET name='Vannevar Bush',
date_modified='2020-06-14 16:20' WHERE id=3
```
Käyttäjänimen muokkaus:
```
UPDATE Account SET username='hyperlinkittäjä', 
date_modified='2020-06-14 16:20' WHERE id=3
```
Kuten rekisteröiyessä todellisuudessa salasana on kryptattu tietokannassa, mutta tässä teoreettinen koodi salasanan muutokselle:
```
UPDATE Account SET password='salis1234', 
date_modified='2020-06-14 16:20' WHERE id=3
```





* poistaa käyttäjätunnukseni. **TEHTY**

```
DELETE FROM Account WHERE id=3
```






### Oppaana haluan:

* tarkastella omia työpaikkojani ja niiden kommentteja. **TEHTY**
```
SELECT C.church, C.town FROM Church C JOIN Tourguide T 
ON C.id=T.church_id AND T.user_id=2
```
Kommettien selaus onnistuu samalla kyselyllä kuin ei-kirjautuneella käyttäjällä.






* merkata, kuinka monta vierailijaa tiekirkossa kävi päivän aikana. **TEHTY**
```
INSERT INTO Visitors (church_id, visitors. date) 
VALUES (178, 95, '2020-06-14')
```





* tarkastella tilastoja työpaikkojeni vierailijamääristä. **TEHTY**

Vierailijat kaikissa työpaikoissani yhteensä:
```
SELECT SUM(A.visitors) AS sum 
FROM Visitors A JOIN Tourguide T 
ON A.church_id=T.church_id AND T.user_id=2
```
Vierailijoiden summat, keskiarvot ja sovellukseen jätettyjen kommenttien määrä työpaikkakirjoissani:
```
SELECT C.church AS church,
(SELECT SUM(V.visitors) FROM Visitors V WHERE church_id = C.id) AS sum,
(SELECT AVG(V.visitors) FROM Visitors V WHERE church_id = C.id) AS avg,
(SELECT COUNT(comment) FROM Visit WHERE Visit.church_id=C.id) AS comment_sum, C.id, C.town
FROM Church C JOIN Tourguide T ON T.church_id=C.id AND T.user_id=2
```








### Adminina halua:

* listata kaikki sovelluksen käyttäjät paitsi itseni ja nähdä kuinka monta kirkkoa on jo merkitty käyttäjän työpaikoiksi. Listan kärjessä on käyttäjät joilla on eniten kirkkoja. **TEHTY**
```
SELECT U.username, U.date_created, U.id,
(SELECT COUNT(*) FROM Tourguide WHERE Tourguide.user_id=U.id) AS nbm
FROM Account U WHERE U.id!=1 ORDER BY nbm DESC
```





* muuttaa peruskäyttäjiä oppaiksi lisäämällä niille kirkkoja.  **TEHTY**
```
INSERT INTO Tourguide (user_id, church_id) VALUES (2, 178)
```

