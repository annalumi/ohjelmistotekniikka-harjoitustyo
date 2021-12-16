# Testausdokumentti

Ohjelmaa on testattu unittestillä yksikkö- ja integraatiotestein

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

*ShopService*-luokkaa, joka vastaa sovelluslogiikasta, testataan *TestShopService*-testiluokalla. Jotta testeissä ei käytettäisi pysyväistallennusta, testeihin on luotu luokat *FakeUserRepository*, *FakeItemRepository* sekä *FakeMessageRepository* tiedon tallennukseen testien aikana

### Repositiot

Repositio-luokkia *UserRepository*, *ItemRepository* ja *MessageRepository* testataan *TestUsers*, *TestItems* ja *TestMessages* - luokilla

### Testikattavuus

Testikattavuus on ??? Lisää kuva testikattavuusraportista!!!

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on tehty manuaalisesti

### Asennus ja konfigurointi

Sovellus on käynnistetty käyttöohjeiden nukaan ja sitä on käytetty Window- ja Linux ympäristöissä

### Toiminnallisuudet

Kaikki määrittelydokumentissa ja käyttöohjeessa mainitut toiminnallisuudet on käyty läpi. Sovelluksessa on myös testattu laajasti mahdolliset virheelliset syötteet ja niiden tuottamat virheilmoitukset