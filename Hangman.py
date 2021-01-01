import random
import string
check3=[]
man=r"""       +---+
       O   |
      /|\  |
      / \  |
         ===
"""
check2=0
tries=5
Interface=[]
words=["giraffe","information","figure",
        "biology","pension","obscure",
        "flourish","hypothesis","subway"]
word=random.choice(words)
space=''
comma=' '
for underscore in word:
    Interface.append("_")
print(comma.join(Interface))
print("This is how long the word is:",len(word),"\nStart guessing!")
while "_" in Interface:
    while True:
        check4=comma.join(check3)
        guess=input('Guess a letter or type \"check\" to show the amount of tries left \nand the how many letters are left: ')
        guess=guess.lower()
        if guess=='check':
            print('\nThis is how many tries you have left:', tries)
            print(Interface)
            continue
        if guess == guess.isalpha():
            print ('You need to print a letter in the alphabet!')
            continue
        if len(guess)!=1:
            print ('You must input 1 character!')
            continue
        if guess in check3:
            print('You have already guessed that word!'"\nThese are the letters you've guessed wrong:",check4)
            continue
        if guess in word:
            print(guess.upper(),"was a correct letter!")
            for check in word:
                if guess==check:
                    Interface[check2]=check
                check2+=1
            check2=0
            if '_' in Interface:
                print(comma.join(Interface))
            else:
                print('This is was the word:')
                print(space.join(Interface))
                print('You have won!')
                break
        else:
            print('Your guess was not in the word!')
            check3.append(guess)
            tries-=1
            print("You have this many tries left!:",tries)
        if tries==0:
            break
    if tries==0:
        print('You have lost!')
        print(man)
        break
