from graphics import *
import random

def indexFind(word,guess):
    result = list()
    for i,x in enumerate(word):
        if x == guess:
            result.append(i)
    return result

def hangman(word, definition):
    returnStuff = {'again':0, '1st':1}

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    win = GraphWin("Hangman", 800, 550)
    win.setBackground("yellow")

    titleText = Text(Point(400,50), 'HANGMAN')
    titleText.setSize(24)
    titleText.setStyle('bold')
    titleText.draw(win)

    #Building the hangman base
    base = Line(Point(120,350),Point(230,350))
    base.draw(win)
    stand = Line(Point(175,350),Point(175,150))
    stand.draw(win)
    stand2 = Line(Point(175,150),Point(250,150))
    stand2.draw(win)
    stand3 = Line(Point(250,150),Point(250,180))
    stand3.draw(win)

    #drawing the empty lines for the word
    x1 = 150
    x2 = 180
    print(word)
    for l in range (len(word)):
        wordLine = Line(Point(x1, 420),Point(x2,420))
        wordLine.draw(win)
        x1+=40
        x2+=40

    incorrectText = Text(Point(600,300), 'Incorrect Guesses:')
    incorrectText.draw(win)

    guessCounter = 0
    textCheck = 0
    repeatCheck = 0
    invalidText = Text(Point(600,100), 'You did not enter a valid letter.')
    invalidText.setTextColor('red')
    repeatText = Text(Point(600,100), 'You already guessed this letter.')
    repeatText.setTextColor('red')
    guesses = []
    letterCount = 0
    while guessCounter < 6:
        indexes = []
        #text entry box
        textEntry = Entry(Point(600,180),10)
        textEntry.draw(win)
        guessText = Text(Point(600,150), 'Guess a letter:')
        guessText.draw(win)
        #user has to click this box to confirm the letter
        enterBox = Rectangle(Point(580,200), Point(620,220))
        enterBox.setFill('white')
        enterBox.draw(win)
        clickText = Text(Point(600,210), 'Enter')
        clickText.draw(win)
        #guessing the word
        guessWordText = Text(Point(400,250), 'Guess the word:')
        guessWordText.draw(win)
        wordEntry = Entry(Point(400,270),15)
        wordEntry.draw(win)
        #isnt drawing this
        enterBox2 = Rectangle(Point(380,260), Point(420,280))
        enterBox2.setFill('white')
        enterBox2.draw(win)
        click2 = Text(Point(400,270), 'Enter')
        click2.draw(win)

        click = win.getMouse()
        x = click.getX()
        y = click.getY()

        if 580 < x < 620 and 200 < y < 220:
            guess = textEntry.getText().lower().strip()

            #checks if the entered letter is in the alphabet
            if guess not in alphabet:
                if repeatCheck == 1:
                    repeatText.undraw()
                    repeatCheck = 0

                if textCheck == 0:
                    invalidText.draw(win)
                    textCheck = 1

            #checks if the entered letter is not a repeat
            elif guess in guesses:
                if textCheck == 1:
                    invalidText.undraw()
                    textCheck = 0

                if repeatCheck == 0:
                    repeatText.draw(win)
                    repeatCheck = 1

            #if the entered letter is in the alphabet and is not a repeat, this code will execute
            else:
                guesses.append(guess)

                if textCheck == 1:
                    invalidText.undraw()
                    textCheck = 0

                elif repeatCheck == 1:
                    repeatText.undraw()
                    repeatCheck = 0

                for letter in word:
                    if letter == guess:
                        indexes = indexFind(word,guess)

                if len(indexes) == 0:
                    guessCounter += 1
                    if guessCounter == 1:
                        guessText1 = Text(Point(550,320), guess)
                        guessText1.draw(win)
                        head = Circle(Point(250,200), 20)
                        head.draw(win)

                    elif guessCounter == 2:
                        guessText2 = Text(Point(570,320), guess)
                        guessText2.draw(win)
                        body = Line(Point(250,220),Point(250,270))
                        body.draw(win)

                    elif guessCounter == 3:
                        guessText3 = Text(Point(590,320), guess)
                        guessText3.draw(win)
                        rightArm = Line(Point(250,230),Point(265,265))
                        rightArm.draw(win)

                    elif guessCounter == 4:
                        guessText4 = Text(Point(610,320), guess)
                        guessText4.draw(win)
                        leftArm = Line(Point(250,230),Point(235,265))
                        leftArm.draw(win)

                    elif guessCounter == 5:
                        guessText5 = Text(Point(630,320), guess)
                        guessText5.draw(win)
                        rightLeg = Line(Point(250,270),Point(265,300))
                        rightLeg.draw(win)

                    elif guessCounter == 6:
                        guessText6 = Text(Point(650,320), guess)
                        guessText6.draw(win)
                        leftLeg = Line(Point(250,270),Point(235,300))
                        leftLeg.draw(win)

                else:
                    for item in indexes:
                        x = 165
                        x += 40* int(item)
                        if x == 165:
                            correctLetter = Text(Point(x,410), guess.upper())

                        else:
                            correctLetter = Text(Point(x,410), guess)

                        correctLetter.draw(win)
                        letterCount += 1
                        if letterCount == len(word):
                            guessCounter = 10


    if guessCounter == 10:
        victoryText = Text(Point(400,200), 'YOU WIN!')
        victoryText.setSize(18)
        victoryText.setStyle('bold')
        victoryText.setTextColor('green')
        victoryText.draw(win)

    else:
        loseText = Text(Point(400,200), 'YOU LOSE!')
        loseText.setSize(18)
        loseText.setStyle('bold')
        loseText.setTextColor('red')
        loseText.draw(win)

        wordText = Text(Point(400,220), 'The word was: ' + word.title())
        wordText.draw(win)

    #quitbox
    quitBox = Rectangle(Point(30, 500), Point(100,550))
    quitBox.setFill('green')
    quitBox.draw(win)
    quitorNah = Text(Point(60, 490), 'Quit')
    quitorNah.draw(win)

    #againbox
    quitBox = Rectangle(Point(710, 500), Point(780,550))
    quitBox.setFill('green')
    quitBox.draw(win)
    quitorNah = Text(Point(750, 490), 'Play Again')
    quitorNah.draw(win)

    #definition of word
    definitionText = Text(Point(400, 450), definition)
    definitionText.draw(win)

    click2 = win.getMouse()
    x2 = click2.getX()
    y2 = click2.getY()

    while True:
        if 30 < x2 < 100 and 500 < y2 < 550:
            returnStuff['again'] = 0
            win.close()
            break

        elif 710 < x2 < 780 and 500 < y2 < 550:
            returnStuff['again'] = 1
            win.close()
            break

    return returnStuff

#list with various words pertaining to nanotechnology
words = ['nanotechnology', 'science', 'nanometre' , 'strength', 'chemistry',
         'small', 'molecule', 'light' , 'weight', 'technology', 'materials',
         'property', 'physics', 'engineering', 'matter', 'waterloo', 'nanobot',
         'reaction', 'structure', 'cells']

definitions = {
    'nanotechnology' : 'The field concerning objects that are between 1-100 nanometres. ',
    'science'  : 'Nanotechnology is a new field of science.',
    'nanometre': 'A nanometre is a billionth of a metre. (10^-9)',
    'strength' : 'Nano materials have higher strength than regular materials.',
    'chemistry': 'High level chemistry plays a big role in Nanoscience.',
    'small'    : 'Nano is an extremly small scale that is used in Nanotechnology.',
    'molecule' : 'Nanotechnology is researched and conducted at the molecular level.',
    'light'    : 'Nano materials give increased control of the light spectrum.',
    'weight'   : 'Nano materials have an extremly small weight.',
    'technology':'Lots of new technology is being created thanks to Nanoscience.',
    'materials': 'Nano materials have enhanced properties that are very useful.',
    'property' : 'Nano materials have enhances properties that are very useful.',
    'physics'  : 'A high understanding of physics is required to study Nanotechnology.',
    'engineering' : 'Nanotechnology has recently become a new strand of engineering.',
    'matter'   : 'The structure of matter can be manipulated and modified using Nanotechnology.',
    'waterloo' : 'Waterloo is the only university in Canada to have a specialized Nanotechnology undergraduate degree.',
    'nanobot'  : 'Nanobots are extremly small machines used in Nanotechnology to perform certain tasks.',
    'reaction' : 'Nano materials can have greater chemecial reactivity than other materials.',
    'structure': 'Nanoscience looks at the structre of molecules to find ways to manipulate them.',
    'cells'    : 'Nanotechnology is conducted at a scale much smaller than a single cell.'}



#picks a random word from the list
word = random.choice(words)

#gets the defintion of the chosen word from the dictionary of definitions for each word
definition = definitions[word]

#this variable ensures it opens the game the first time
initialCall = 1
#stores the returnValue for the first call
returnValue = hangman(word, definition)

#sets the initialCall to 0 after first call
if returnValue['1st']==1:
    initialCall=0

#Calls the game function again if user wishes
while initialCall == 1 or returnValue['again'] == 1:
    word = random.choice(words)
    definition = definitions[word]
    returnValue = hangman(word, definition)