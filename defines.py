# -*- coding: utf-8 -*-
FIRST_NAME = 'fn'
LAST_NAME = 'ln'
EMAIL = 'em'
EMPLOYER = 'emp'
WORKPLACE = 'wrk'
ACCOMODATION = 'acc'
RESIDENCE = 'res'
ROOMMATE = 'rmt'
CHARACTER = 'fig'

GENDER = 'gender'

labels = {
    FIRST_NAME :    u'krstné meno',
    LAST_NAME :     u'priezvisko',
    EMAIL :         u'email',
    EMPLOYER :      u'zamestnávateľ',
    WORKPLACE :      u'pracovisko',
    ACCOMODATION :  u'záujem o ubytovanie',
    RESIDENCE :     u'bydlisko',
    ROOMMATE :      u'spolubývajúci',
}

MAX_CHARACTER_COUNT_MALE = 15
MAX_CHARACTER_COUNT_FEMALE = 35

ID_BOND        = 0
ID_MIA         = 1
ID_ROCKY       = 2
ID_BONNIE      = 3
ID_CLYDE       = 4
ID_SPARROW     = 5
ID_BATMAN      = 6
ID_CATWOMAN    = 7
ID_GUMP        = 8
ID_ZUZI        = 9
ID_BELLA       = 10
ID_EDWARD      = 11
ID_JONES       = 12
ID_POPPINS     = 13
ID_ADDAMS      = 14
ID_SANDY       = 15
ID_TERMINATOR  = 16
ID_DOROTHY     = 17
ID_BOHUS       = 18
ID_DIVKA       = 19

characters = {
    ID_BOND         : u'JAMES BOND',
    ID_MIA          : u'MIA WALLACE (Pupl fiction)',
    ID_ROCKY        : u'CIGÁŇ MICKEY O\'NEIL(Podfu(c)k)',
    ID_BONNIE       : u'BONNIE PARKER (Bonnie & Clyde)',
    ID_CLYDE        : u'CLYDE BARROW (Bonnie & Clyde)',
    ID_SPARROW      : u'JACK SPARROW (Piráti z Karibiku)',
    ID_BATMAN       : u'BATMAN',
    ID_CATWOMAN     : u'CATWOMAN',
    ID_GUMP         : u'FORREST GUMP',
    ID_ZUZI         : u'SLADKÁ ZUZI (Niekto to rád horúce)',
    ID_BELLA        : u'ČARODEJNICA Z EASTWICKU',
    ID_EDWARD       : u'EDWARD (Twilight Saga)',
    ID_JONES        : u'INDIANA JONES',
    ID_POPPINS      : u'ALICA V KRAJINE ZÁZRAKOV',
    ID_ADDAMS       : u'MORTICIA ADDAMS',
    ID_SANDY        : u'SANDY OLSEN (Pomáda)',
    ID_TERMINATOR   : u'TERMINÁTOR',
    ID_DOROTHY      : u'FANTAGHÍRO',
    ID_BOHUS        : u'BOHUMIL STEJSKAL (Bohuš)',
    ID_DIVKA        : u'DÍVKA NA KOŠTETI',
}

characterImgs = {
    ID_BOND         : '00',
    ID_MIA          : '01',
    ID_ROCKY        : '02',
    ID_BONNIE       : '03',
    ID_CLYDE        : '04',
    ID_SPARROW      : '05',
    ID_BATMAN       : '06',
    ID_CATWOMAN     : '07',
    ID_GUMP         : '08',
    ID_ZUZI         : '09',
    ID_BELLA        : '10',
    ID_EDWARD       : '11',
    ID_JONES        : '12',
    ID_POPPINS      : '13',
    ID_ADDAMS       : '14',
    ID_SANDY        : '15',
    ID_TERMINATOR   : '16',
    ID_DOROTHY      : '17',
    ID_BOHUS        : '18',
    ID_DIVKA        : '19',
}

characterTexts = {
    ID_BOND         : u'Neľútostný, neodolateľný, vždy spravodlivý a oddaný svojej misii. Taký je James Bond a taký ste aj Vy! Predveďte sa preto vo Vašom hviezdnom šate a dokážte, že ste ten najlepší agent 007 spomedzi všetkých. Vyberte sa na špionážnu cestu aj počas Noci filmových hviezd UNION.',
    ID_MIA          : u'Tak záhadná a tak atraktívna, pre niekoho zdá sa hriešna, rozhodne však nedosiahnuteľná. Keď sa rozhodne ísť na parket a zatancovať, vyhráva trofeje skôr ako poviete “borúvkový koláč”.  Ukážte aj Vy svoju jedinečnú choreografiu v prevleku pani Wallace počas Noci filmových hviezd UNION! ',
    ID_ROCKY        : u'Prostoreký a uštipačný bitkár, ktorý je aj napriek svojej neohrabanosti, strnisku a špinavým šatám istým spôsobom atraktívny. Miluje stávky, hazard, box a psov. Nasaďte si klobúk, pridajte trochu viac zlata a stavme sa, že viete mať s týmto írskym kočovníkom naozaj niečo spoločné. ',
    ID_BONNIE       : u'Tá čo píše básne zo slávnej gangsterskej dvojice. Sympatická, rebelantská bojovníčka proti spoločenskému poriadku a cudzím bankovým kontám. Tak trochu zabijak, ale s osobným kúzlom a šarmom. Ak počas Noci filmových hviezd pridáte k neľútostnej zbrani aj štýlovú baretku, určite  ohúrite nejedného Clyda.',
    ID_CLYDE        : u'Mužská polovička azda najznámejšej gangsterskej dvojice všetkých čias. Kradne, zabíja, miluje a neľutuje. Buďte aj vy nachvíľu nekompromisný a šarmantný, nahoďte sa do pásikavého obleku a štýlového klobúku a počas Noci filmových hviezd UNION bude aj na Vás vypísaná vysoká odmena.',
    ID_SPARROW      : u'Svojej povesti šialenca a obávaného rebela nezostáva nič dlžný. Z bezvýchodiskových situácii vyviazne s dôvtipom jemu vlastným, čo mu však nestačí. Vezme si aj korisť, poklady a krásne ženy. Splňte si svoj detský sen a priplávajte ako pirátsky kapitán na Noc filmových hviezd UNION!',
    ID_BATMAN       : u'Inteligencia, sila vôle, tvrdý tréning a špičkové technológie sú zbraňami komiksového hrdinu. Ak ste Batman, noc patrí Vám. Nielen Gotham City, ale aj Noc filmových hviezd UNION potrebuje superhrdinu.',
    ID_CATWOMAN     : u'Nedolapiteľná drsná sexica žijúca bez strachu. Riadi sa vlastnými pravidlami a rovnako ako noc jej pristane čierna koža. Príďte ako mačacia pomstiteľka na Noc filmových hviezd UNION.',
    ID_GUMP         : u'Bež, Forrest, bež! Žije vo Vás Forrestove odhodlanie a vôľa. Oblečte si károvanú košeľu alebo si nechajte narásť bradu, dajte sa do trička so smajlíkom a pribehnite si získať jeho popularitu na Noc filmových hviezd UNION!',
    ID_ZUZI         : u'Dajte dievčaťu správne topánky a ona dobije svet. Počas Noci filmových hviezd UNION platí pre Vás dvojnásobne. Rozkošná ženskosť, rafinovaný outfit,  blond kučery a červený rúž – to je Vaša voľba pre túto noc. Pá-dídly-dídly-dídly-dam, pu-pu-bí-du',
    ID_BELLA        : u'Krásna, zmyselná a obdarená nevšednou magickou mocou, ktorú neváha použiť, keď ide o získanie vysnívaného muža. “Hókus – fókus”, kúzla, veštby a zaklínadlá, to všetko je dovolené počas Noci filmových hviezd UNION.',
    ID_EDWARD       : u'Večne mladý krásavec, tak tajomný a príťažlivý. Jeho krása a pohľad taja dych každému kdekoľvek sa zjaví. Myšlienky sa pred ním neutaja. A pozor aj keď nešteká, čas od času hryzie! Zažite lov v koži upíra počas Noci filmových hviezd UNION.',
    ID_JONES        : u'Dobrodružstvo, svetácka povaha a hrdina, ktorý sem tam utrží aj nejakú tu facku. Šťastie mu však nosí klobúk, kožená bunda a dlhý bič. Možno prinesú šťastie aj Vám. Zastavte sa počas Vašej cesty za pokladom a zabavte sa s ostatnými hviezdami počas Noci filmových hviezd UNION.',
    ID_POPPINS      : u'Zasnená, nevinná a odvážna. Tá, ktorá je vyvolená zachrániť zázračnú krajinu. Nemusíte skákať do králičej nory, aby ste mohli prísť ako Alica na Noc filmových hviezd UNION.',
    ID_ADDAMS       : u'Tak bizarná až je charizmatická, tak nekonvenčná až je atraktívna. A aký je jej štýl? Stačí si obliecť priliehavé čierne šaty, napúdrovať pleť múkou, postrihať ružiam hlavičky a ste pripravená na Noc filmových hviezd UNION.',
    ID_SANDY        : u'Mladá, nevinná a tak sladká. Ak však treba mení sa na poriadnu rebelku. Ukážte všetkým ako Vám pristanú “sladké sedemdesiate” počas Noci filmových hviezd UNION.',
    ID_TERMINATOR   : u'Silný, takmer nezničiteľný robotický zabijak. Neumierajúca ikona akčných filmov sa vracia, aby prišla na Noc filmových hviezd UNION, kde zaznie jeho povestné „Hasta la vista baby!“',
    ID_DOROTHY      : u'Krása, vznešenosť a odvaha umocnená láskou silnejšou než všetky kúzla. Aby bránila svoju lásku a bojovala so Zlom, prezlieka sa za chlapca. Zvoľte si aj Vy, ktorú podobu tvrdohlavej princeznej na seba vezmete, keď prídete na Noc filmových hviezd UNION.',
    ID_BOHUS        : u'Rázovitý dedinský chlapík kamaráta nikdy nenechá v štichu, najmä keď sa jedná o popíjanie slivovice. Obliekajte šušťáky, nasaďte rádiovku a pripravte sa, lebo počas Noci filmových hviezd UNION možno nastane “nová doba” a hostia budú vyhadzovať vrchného.',
    ID_DIVKA        : u'Mladosť, pochabosť, zvedavosť a túžba zažiť niečo nepoznané. Nepotrebujete “dexempo šupoplext” ani iné zaklínadlá, rozhodne však potrebujete metlu a budete tou pravou Saxanou počas Noci filmových hviezd UNION.',
}

femaleCharacters = [
    ID_MIA          ,
    ID_BONNIE       ,
    ID_CATWOMAN     ,
    ID_ZUZI         ,
    ID_BELLA        ,
    ID_POPPINS      ,
    ID_ADDAMS       ,
    ID_SANDY        ,
    ID_DOROTHY      ,
    ID_DIVKA        ,
]    

maleCharacters = [
    ID_BOND         ,
    ID_ROCKY        ,
    ID_CLYDE        ,
    ID_SPARROW      ,
    ID_BATMAN       ,
    ID_GUMP         ,
    ID_EDWARD       ,
    ID_JONES        ,
    ID_TERMINATOR   ,
    ID_BOHUS        ,
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

orderedWorkplaces = [
  'BB',
  'BD',
  'BA',
  'BR',
  'DK',
  'DS',
  'GL',
  'HU',
  'KO',
  'KE',
  'LE',
  'LM',
  'LC',
  'MA',
  'MT',
  'MI',
  'NT',
  'NZ',
  'PN',
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
  'TT',
  'VK',
  'VT',
  'ZV',
  'ZH',
  'ZA',
]

workplaces = {
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

workplacesWithAcc = [
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
  'SE',  #presne 90 km tak este uvidime
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

eployerLabels = {
     'UP' : u'Union poisťovňa',
     'UZP': u'Union zdravotná poisťovňa',            
}

accomodationLabels = {
     'yes' : u'áno',
     'no'  : u'bez ubytovania',
}
