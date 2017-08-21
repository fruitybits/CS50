#Given an inital input of English or Morse, this program encodes English text to Morse Code and decodes Morse Code to English text
#Program written by Chelsea James for ATA
#There are 3 bugs / TODOs

import sys
import cs50
import os

def main():

#init morse dicts to Encode and Decode
    morseEncodeDict = {}
    morseDecodeDict = {}

#open Morse Dictionary .txt file at correct file path
    morseDictionary = os.path.join(sys.path[0], "MorseDictionary.txt")
    #file = open(morseDictionary, "r")
    with open(morseDictionary) as file:
        if file is None:
            print ("File cannot be opened.")
        for line in file:
            
#strip the new line character and split each line into paired entries
            line = line.strip('\n')
            (key, val) = line.split('  ')
            for i in key:
                for x in val:
                    morseEncodeDict[key] = val

#create a decoding dict that swaps the entry pairs from Encoding dict
    morseDecodeDict = dict((val,key) for (key,val) in morseEncodeDict.items())

#prompt user for input. get user input. (v2, would accept input from .txt file)

    
#user defines which function to use, encode or decode. KNOWN BUG / TODO - Incomplete user input handling   
    print ("Are you entering Morse Code or Plain English?", end=" ")
    initDefinition = input()
    print ("Great! Please enter text:", end=" ")
    userInput = input()
    #while True:
    #    if ["english", "morse"] in initDefinition.tolower():
    #        break
    #    else:
    #        print ("Please enter morse or english")
    
#encode from english to morse. KNOWN BUG / TODO - Make userInput case insensitive
    if "English" in initDefinition:
        for char in userInput:
            for key, val in morseEncodeDict.items():
                if char.upper() == key:
                    print (val, end=" ")
        print ('\n')

#decode from morse to english. KNOWN BUG / TODO - Improper Spacing, Make userInput case insensitive
    if "Morse" in initDefinition:
        #morseHolder = []
        morseChain = userInput.split()
        for i in range (len(morseChain)):
            for key, val in morseDecodeDict.items():
                if morseChain[i] == key:
                    print (val, end=" ")
        #            morseHolder += val
        #    for x in range (len(userInput)):
        #        if x is " ":
        #            morseHolder.insert(x, " ")
        #print (morseHolder, end=" ")
        print ('\n')
        
if __name__ == "__main__":
    main()
