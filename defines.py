# -*- coding: utf-8 -*-
ACTIVITY_TYPES=[
    'Pri športe',
    'Keď relaxujem',
    'Pri dobrom pití a jedle',
    'Keď sa zabávam s priateľmi',
    'Pri tvorivej činnosti',
    'Keď poznávam a učím sa nové veci',
]

ACTIVITY_SPORTS=[
    'Klasických kolektívnych športových disciplín ako futbal, volejbal…',
    'Adrenalínových športov',
    'Netradičných a zábavných športových disciplín',
    'Športov zameraných na správne držanie tela a dýchanie',
    'Aeróbne cvičenia',
]

ACTIVITIES=[
    'Gravity jóga',
    'Hoopnotica (cvičenie s obručou)',
    'Jumping (cvičenie na trampolíne)',
    'Lezecká sieť',
    'TRX (kondičný tréning)',
    'Šerm',
    'Nafukovacie športové aktivity (Varifutbal, bungee running..)',
    'Jóga smiechu',
    'Tvárová gymnastika',
    'Mozgostreľba (aktivita zameraná na aktivitu mozgu)',
    'Veštiareň',
    'Workshopy a novinky k téme zdravá strava',
    'Workshopy a prednášky zamerané na duševné zdravie',
]

MAIL_FROM = 'union@branda.sk'

MAIL_SUBJECT = u'Noc filmových hviezd UNION'

MAIL_TEXT = u"""
Ďakujeme za vyplnenie dotazníku, a zároveň potvrdzujeme zaregistrovanie Vašich údajov do databázy potvrdených účastníkov na vianočný večierok – Noc filmových hviezd UNION.

Na základe Vašich odpovedí Vám bola vygenerovaná maska %(fig)s. 
Budeme veľmi radi, ak prídete na vianočný večierok v tejto maske, filmový dress code ale nie je povinný. 

Pripomíname, že vianočný večierok sa koná dňa 20.12.2013 o 19:00 v bratislavskom hoteli Crowne Plaza.

Vaše registračné údaje si môžete skontrolovať tu:

Krstné meno: %(fn)s
Priezvisko: %(ln)s
Zamestnávatel: %(emp)s
Vaše Pracovisko: %(wrk)s
Ubytovanie v hoteli Crowne Plaza: %(acc)s
Váš preferovaný spolubývajúci: %(rmt)s
Adresa Vášho trvalého bydliska: %(res)s

V prípade akýchkoľvek nejasností, kontaktujte prosím organizačný tím na e-mailovej adrese union@branda.sk.
"""

ERROR_EMAIL_INVALID = u'Zadali ste nesprávny email'
ERROR_EMAIL_EXIST = u'Zadaný email bol už použitý'
ERROR_NOT_ENTERED = u'Zabudli ste vyplniť pole %s'

ERROR_NOT_ENTERED_GENDER = u'Prosím uveďte vaše pohlavie'

cities = {
  'BB': u'Banská Bystrica',
  'BD': u'Bardejov',
  'BA': u'Bratislava ',
  'BR': u'Brezno',
  'DK': u'Dolný Kubín',
  'DS': u'Dunajská Streda',
  'GL': u'Galanta',
  'HU': u'Humenné',
  'KO': u'Komárno',
  'KE': u'Košice',
  'LE': u'Levice',
  'LM': u'Liptovský Mikuláš',
  'LC': u'Lučenec',
  'MA': u'Malacky',
  'MT': u'Martin',
  'MI': u'Michalovce',
  'NT': u'Nitra',
  'NZ': u'Nové Zámky',
  'PN': u'Pieštany',
  'PP': u'Poprad',
  'PO': u'Prešov',
  'PD': u'Prievidza',
  'RS': u'Rimavská Sobota',
  'RO': u'Rožnava',
  'RK': u'Ružomberok',
  'SE': u'Senica',
  'SN': u'Snina',
  'SP': u'Spišská Nová Ves',
  'TO': u'Topolčany',
  'TV': u'Trebišov',
  'TN': u'Trenčín',
  'TT': u'Trnava',
  'VK': u'Velký Krtíš',
  'VT': u'Vranov nad Toplou',
  'ZV': u'Zvolen',
  'ZH': u'Žiar nad Hronom',
  'ZA': u'Žilina',   
}

citiesWithAcc = [
  'BB', 
  'BD', 
  'BR', 
  'DK', 
  'HU', 
  'KO', 
  'KE', 
  'LE', 
  'LM', 
  'LC', 
  'MT', 
  'MI', 
  'NT', 
  'NZ', 
  'PP', 
  'PO', 
  'PD', 
  'RS', 
  'RO', 
  'RK', 
  'SE',
  'SN', 
  'SP', 
  'TO', 
  'TV', 
  'TN', 
  'VK', 
  'VT', 
  'ZV', 
  'ZH', 
  'ZA', 
]
