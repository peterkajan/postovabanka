from anketePoints import *
from movie import *
from defines import *
import random

def addList( list, listToAdd ):
    for i in range( len(list) ):
        list[i] += listToAdd[i]
        
def test(male, results, cnts):
    return chooseCharacter( calculateCharacter( male, results ), cnts, male)

def generateResults():
    results = [ 0 for ch in characters ]
    for ap in anketePoints:
        answer = random.randint(0,len(ap['points']))
        print ap['question'] + ' ' + str(answer)
        if answer > 0:
            addList( results, ap['points'][chr(97 + answer - 1)])
            
    if ( random.randint(0,1) == 1):
        male = True
    else:
        male = False
    return male, results


res = [ 0 for ch in characters ]
for i in range (0,500):
    id = test( *generateResults(), cnts=res )
    res[id] += 1

    
print res
sum = 0
for i in res:
    sum += i
    
print sum