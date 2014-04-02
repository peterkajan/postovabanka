from defines import *
from model import *
import random
import logging

def assignCharacter( preferenceList, male ):
    chosenId = chooseCharacter( preferenceList, Character.getCnts(), male)
    Character.update( chosenId )
    return chosenId   

def calculateCharacterHlpr( results, chars ):
    preferenceList = []
    list = []
    for chr in chars:
        list.append( (results[chr], chr) )
            
    list.sort()
    for pair in reversed( list ):
        preferenceList.append( pair[1] )
        
    logging.info('preference list: ' + str(preferenceList))
    return preferenceList

def calculateCharacter( male, results):
    logging.info(male)
    if male:
        return calculateCharacterHlpr( results, maleCharacters)
    return calculateCharacterHlpr( results, femaleCharacters)
    
def chooseCharacter( preferenceList, counts, male ):
    
    if male:
        max = MAX_CHARACTER_COUNT_MALE
    else:
        max = MAX_CHARACTER_COUNT_FEMALE
    
    for chr in preferenceList:
        if counts[ chr ] < max:
            return chr
    #todo log        
    return preferenceList[ random.randint(0,len(preferenceList)-1)]

   
