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
    print "---------------------------------"
    print "     Velkominn í Mastermind"
    print "---------------------------------"
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
    black = Color("Svartur")
    green = Color("Grænn")
    brown = Color("Brúnn")
    purple = Color("Fjólublár")
    red = Color("Rauður")
    white = Color("Hvítur")
    blue = Color("Blár")
    yellow = Color("Gulur")
    colorList = [black,green,brown,purple,red,white,blue,yellow] 
    return colorList  

def guessColors(colorList, numberOfColors):
    colorStrList = []
    guessRow = []
    print "Veldu " + str(numberOfColors) + " með því að skrifa nafn litar í röð aðskilið með einu bili"
    print "Litir í boði: Svartur Grænn Brúnn Fjólublár Rauður Hvítur Blár Gulur"
    print ""
    
    inputOK = False
    while not inputOK:
        inputError = False
        input = raw_input()
        userRow = input.split(" ")
        if len(userRow) != numberOfColors:
            print "ekki réttur fjöldi af litum " + str(len(userRow)) + " litir í stað " + str(numberOfColors)
            print "Veldu aftur liti: "
            print ""
            inputError = True
        for color in colorList:
            colorStrList.append(color.name)
        for color in userRow:
            if color not in colorStrList:
                print "ekki réttur litur: " + color
                print "Veldu aftur liti: "
                print ""
                inputError = True
        if not inputError:
            inputOK = True
            print "input OK" + str(inputOK)
    for color in userRow:
        guessRow.append(Color(color))
    return guessRow

        

def main():
    colorList = makeColors()
    userIntput = greetings()
    mastermindObj = Mastermind(colorList,userIntput[0],userIntput[1],userIntput[2])
    won,lost = False,False

    print mastermindObj.colors
    print mastermindObj.numbersOfColors
    print mastermindObj.sameColor
    print mastermindObj.totalGuesses
    print mastermindObj.rows
    while not won and not lost:
        guess = guessColors(colorList, userIntput[1])
        won,lost = mastermindObj.gradePlayerChoice(guess)
        if won:
            print "Þú hefur unnið"
        if lost:
            print "Þú er hefur tapað"
    
main() 
    
   
    
    
    
    
    
    
    
    
    
    
    
    