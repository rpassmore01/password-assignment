#	name: Russell Passmore
#	class: ICS4U
#	assignment: password assignment
#	date: October 4, 2022

from math import floor
from manimlib import *
import numpy as np
import random
import datetime

numWords = 6

class PassphraseGenerator(Scene):
    def construct(self):
        intro_words = Text("""
            Passphrases can be used to simplify and 
            secure your online accounts.A passphrase 
            differs from a regular password because 
            it uses a group of words rather than 
            random characrters.A passphrase could 
            look like this: 
            "wind their abbot raise vowel maze".
            These passphrases are usually 6-8 words in 
            length, and they provide better security 
            than short passwords while being easier to 
            remember and type.
        """)

        self.play(Write(intro_words))
        self.wait(5)
        self.play(FadeOut(intro_words))

        current_date = datetime.datetime.now()

        random.seed(int(current_date.strftime("%Y%m%d%H%M%S")))

        diceRolls = []
        for i in range(0,numWords):
            currRoll = ''
            for i in range(1,6):
                currRoll += str(random.randint(1,6))
            diceRolls.append(currRoll)


        diceGroup = VGroup()
        diceGroupDict = {}

        prev = None
        for i in range(0, len(diceRolls)):
            animObject = Text(diceRolls[i])
            if i == 0:
                diceGroup.add(animObject)
                diceGroupDict[diceRolls[i]] = animObject
                prev = animObject
            else:
                animObject.next_to(prev, DOWN)
                diceGroup.add(animObject)
                diceGroupDict[diceRolls[i]] = animObject
                prev = animObject
        
        diceGroup.shift(UP*floor(len(diceRolls)/3))
        self.play(Write(diceGroup))
        self.wait()
        self.play(diceGroup.to_edge)

        file = open('diceware.txt', 'r')
        fileText = file.read()
        fileArray = fileText.split('\n')

        answers = {}

        for i in range(0, len(fileArray)):
            splitLine = fileArray[i].split('\t')
            for roll in diceRolls:
                if splitLine[0] == roll:
                    answers[i] = splitLine

        answerGroup = VGroup()

        for answer in answers:
            numberGroup = VGroup()
            wordGroup = VGroup()
            glowGroup =  VGroup()
            prevNumber = None
            firstObject = None
            answerObject = None
            numberObject = None
            wordObject = None
            answerNumber = 0
            for i in range(answer-5, answer+5):
                splitAnswer = fileArray[i].split('\t')
                numberObject = Text(f"{splitAnswer[0]}")
                wordObject = Text(f"{splitAnswer[1]}")
                if i == answer:
                    answerObject = wordObject
                    glowGroup.add(numberObject)
                    answerNumber = splitAnswer[0]
                if i == answer-5:
                    firstObject = wordObject
                    numberGroup.add(numberObject)
                    prevNumber = numberObject
                    wordGroup.add(wordObject)
                    wordObject.next_to(numberObject, RIGHT)
                else:
                    numberObject.next_to(prevNumber, DOWN)
                    wordObject.next_to(numberObject, RIGHT)
                    numberGroup.add(numberObject)
                    wordGroup.add(wordObject)
                    prevNumber = numberObject
            
            numberGroup.shift(UP*3)
            wordGroup.shift(UP*3)

            triangle = Triangle()
            triangle.set_height(0.5)
            triangle.next_to(firstObject)
            triangle.rotate((PI*210)/180)

            glowGroup.add(diceGroupDict[answerNumber])

            writeGroup = VGroup(numberGroup, wordGroup)
            self.play(Write(writeGroup, runtime = 0.5))
            self.play(FadeIn(triangle))
            self.play(triangle.next_to, answerObject)
            self.play(FadeToColor(glowGroup, BLUE))
            self.play(FadeToColor(glowGroup, WHITE))
            self.add(answerObject)
            answerGroup.add(answerObject)
            wordGroup.remove(answerObject)
            fadeOutGroup = VGroup(numberGroup, wordGroup, triangle)
            self.play(FadeOut(fadeOutGroup, runtime = 0.2))
            self.play(answerObject.next_to, diceGroupDict[answerNumber])
        
        prev = answerObject
        for object in answerGroup:
            if object != answerObject:
                self.play(object.next_to, prev)
                prev = object

        self.play(FadeOut(diceGroup))
        self.play(answerGroup.move_to, [0,0,0])

        passwordText = Text("Your passphrase is:")
        passwordText.next_to(answerGroup, UP)

        self.play(Write(passwordText))


if __name__ == '__main__':
    numWords = input()
    scene = PassphraseGenerator()
    scene.render()
