#	name: Russell Passmore
#	class: ICS4U
#	assignment: password assignment
#	date: October 4, 2022

from math import floor
from manimlib import *
import numpy as np
import random
import datetime

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

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

        #self.play(Write(intro_words))
        #self.wait(5)
        #self.play(FadeOut(intro_words))

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

        for answer in answers:
            answerGroup = VGroup()
            prev = None
            firstObject = None
            answerObject = None
            for i in range(answer-5, answer+5):
                animObject = Text(f"{fileArray[i]}")
                if i == answer:
                    answerObject = animObject
                if i == answer-5:
                    firstObject = animObject
                    animObject.shift(UP*3)
                    answerGroup.add(animObject)
                    prev = animObject
                else:
                    animObject.next_to(prev, DOWN)
                    answerGroup.add(animObject)
                    prev = animObject
            print(firstObject)
            print(answerObject)
            triangle = Triangle()
            triangle.set_height(0.5)
            triangle.next_to(firstObject)
            self.play(Write(answerGroup))
            self.wait(5)
            self.play(FadeIn(triangle))
            self.play(triangle.rotate, (PI*210)/180)
            self.play(triangle.next_to, answerObject)
            self.wait(5)



if __name__ == '__main__':
    numWords = input()
    scene = PassphraseGenerator()
    scene.render()
