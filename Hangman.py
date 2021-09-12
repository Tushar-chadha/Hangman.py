import random
import hangman_art 
import word_list

print(hangman_art.logo+'\n')

RandWord=random.choice(word_list.word_list)
RandWordTBC = list(RandWord)

displayWords=[]
result=''
lives=6

for i in RandWordTBC:
    displayWords.append('_')

print(hangman_art.stages[lives])
endGame=False
while not endGame:
    print(lives+' left')
    print(displayWords)
    guessed=input('Guess a alphabet: ').lower()

    for p in range(len(RandWordTBC)):
        if RandWordTBC[p] == guessed:
            displayWords[p]=guessed
        

    if '_' not in displayWords:
        endGame=True
        result='You WIN'

    if guessed not in RandWord:
            lives=lives - 1
    if lives>0:
        print('\n'+hangman_art.stages[lives]+'\n')
    elif lives==0:
        print('\n'+hangman_art.stages[0]+'\n')
        endGame=True
        result='You LOOSE'

print('\n'+result+'\n')
print(RandWord +' was the word.')



