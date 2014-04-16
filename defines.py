# -*- coding: utf-8 -*-
DOMAIN = 'http://htcinvite.appspot.com/'
PAGE_FLOW_2 = True

MAIL_FROM = 'peter.kajan@infinit.sk'
MAIL_INVITATION_SUBJECT = u'Pozvánka na predstavenie HTC One (M8)'
MAIL_INVITATION_TEXT = u"""
Dobrý deň,

pozývame Vás na predstavanie HTC One (M8). Prosím zaregistrujte sa na tejto adrese {link}.
Ďakujeme

S pozdravom
organizačný tím

V prípade akýchkoľvek nejasností, kontaktujte prosím organizačný tím na e-mailovej adrese {mail_from}.
"""

MAIL_CONFIRMATION_SUBJECT = u'Potvrdenie účasti na predstavení HTC One (M8)'

MAIL_CONFIRMATION_TEXT = u"""
Ďakujeme za registristráciu.

Uvidíme sa X.X. o 18 00 v XXX
Tešíme sa na Vás  

S pozdravom
organizačný tím

V prípade akýchkoľvek nejasností, kontaktujte prosím organizačný tím na e-mailovej adrese {mail_from}.
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
