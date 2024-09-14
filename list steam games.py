import os
import random

print("Hellom, why don't we list a handfull of games \n")
path = "/Program Files (x86)/Steam/steamapps/common"
pog = os.listdir(path)
print(pog, "\n")
print("Now lets do our best to atttempt to grab a random fun game from that. \n")

pogGame = random.choice(pog)

print("Your random game is: \n", ">>> ", pogGame, " <<<")

input("Press enter to exit")