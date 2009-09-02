# encoding: utf-8
from main.color import Color
from main.mastermind import Mastermind


def greetings():
    numberOfColors = 0
    numberOfGuesses = 0
    sameColor = False
    sameColorAnswer = ""
    sameColorAllowedAnswers = ["y","n","Y","n","nei","já","j","J"]
    print ""
    print "--------------------------------"
    print "    Velkominn í Mastermind"
    print "--------------------------------"
    print ""
    while numberOfColors not in range(2,8):
        numberOfColors = int(raw_input("Veldu hversu marga liti þú vilt spila með? Veldu tölu á bili 2-10: "))
    while numberOfGuesses not in range(2,10):
        numberOfGuesses = int(raw_input("Hversu margar tilraunir viltu að séu leyfðar? Veldu tölu á bili 2-10 "))
    while sameColorAnswer not in sameColorAllowedAnswers:
        sameColorAnswer = raw_input("Viltu að sami litur sé leyfður oftar en einu sinni? [y] fyrri já eða [n] fyrir nei: ")
    if sameColorAnswer in ["y","Y","já","j","J"]:
        sameColor = True      
    return numberOfGuesses,numberOfColors,sameColor

def makeColors():
    black = Color("svartur")
    green = Color("Grænn")
    brown = Color("Brúnn")
    purple = Color("Fjólublár")
    red = Color("Rauður")
    white = Color("Hvítur")
    blue = Color("Blár")
    yellow = Color("Gulur")
    colorList = [black,green,brown,purple,red,white,blue,yellow] 
    return colorList  

def main():
    colorList = makeColors()
    userIntput = greetings()
    mastermindObj = Mastermind(colorList,userIntput[0],userIntput[1],userIntput[2])

    print mastermindObj.colors
    print mastermindObj.numbersOfColors
    print mastermindObj.sameColor
    print mastermindObj.totalGuesses
    print mastermindObj.rows
    
    
main() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    