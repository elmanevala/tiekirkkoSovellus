# Tietokantarakenne

Sovellus käyttää tietokannanhallintajärjestelmänään paikkallisesti SQLiteä ja Herokussa PostgreSQL:ää.

## CREATE TABLE -lauseet

```
CREATE TABLE church (
	id INTEGER NOT NULL, 
	church VARCHAR(144) NOT NULL, 
	town VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_church_church ON church (church);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (admin IN (0, 1))
);
CREATE TABLE visit (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	account_id INTEGER NOT NULL, 
	church_id INTEGER NOT NULL, 
	tourguide BOOLEAN NOT NULL, 
	comment VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(church_id) REFERENCES church (id), 
	CHECK (tourguide IN (0, 1))
);
CREATE TABLE tourguide (
	id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	church_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id), 
	FOREIGN KEY(church_id) REFERENCES church (id)
);
CREATE TABLE visitors (
	id INTEGER NOT NULL, 
	church_id INTEGER NOT NULL, 
	visitors INTEGER NOT NULL, 
	date VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(church_id) REFERENCES church (id)
);

```

Koska sovelluksessa tehdään useita kyselyitä Church-taulun church-sarakeesta, se on indeksöity.

## Päivitetty tietokantakaavio

![alt text](https://raw.githubusercontent.com/elmanevala/tiekirkkoSovellus/master/dokumentaatio/tietokantakaavio.png)