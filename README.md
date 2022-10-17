# Passphrase Generator #
This is for a school project.   
This project uses manim to visualize the creation of passphrases using diceware. Each line in the diceware file contains a 6 digit string of numbers that each correspond to six dye rolls. It is in the following format:

| Dice Rolls  | Word |
| ------------- | ------------- |
| 44441  | ore  |
| 44442  | organ  |
| 44443  | orgy  |
| 44444  | orin  |


 There is one word for each group of six rolls. The idea is that you roll a dye six times for every word you want to add to your passphrase, and write down each roll. You then find the corresponding string of dye rolls that matches your six dye rolls, and write the word that you find down. For this visualization there are always six words in each passphrase. 