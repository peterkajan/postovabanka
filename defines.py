# -*- coding: utf-8 -*-
DOMAIN = 'http://www.htc-one-m8.sk/'
PAGE_FLOW_2 = True

MAIL_FROM = 'pozvanka@htc-one-m8.sk'
MAIL_INVITATION_SUBJECT = u'Pozvánka na predstavenie HTC One (M8)'
MAIL_INVITATION_TEXT = u"""
Dobrý deň {name},
Pozývame Vás na slávnostné predstavenie nového HTC One (M8), ktoré sa usutoční v utorok 29. apríla 2014 v reštaurácii Flow Eurovea. Začíname o 19:00.
RSVP: {link}
Pozvánka platí pre jednu osobu.
Prosíme o potvrdenie Vašej účati najneskôr do 25. apríla 2014. 
Ďakujeme.
HTC
"""

MAIL_CONFIRMATION_SUBJECT = u'Potvrdenie účasti na predstavení HTC One (M8)'
MAIL_CONFIRMATION_TEXT = u"""
Dobrý deň {name},
Ďakujeme za potvrdenie Vašej účasti na predstavení nového HTC One (M8). 
Tešíme sa na Vás v utorok 29. apríla v reštaurácii Flow Eurovea o 19:00.
S pozdravom,
HTC.
"""

MAIL_REJECTION = True
MAIL_REJECTION_SUBJECT = u'Odmientutie účasti na predstavení HTC One (M8)'
MAIL_REJECTION_TEXT = u"""
Dobrý deň {name},
Ďakujeme za Váš čas. Je nám lúto, že sa našej akcie nezúčastníte.
Vaš rozhodnutie môžete do piatku 25. apríla zmeniť prostredníctvom: {link} :).
Ďakujeme.
S pozdravom,
HTC
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
