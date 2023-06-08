from random import shuffle
import os

os.system("cls")

def shuffle_word(word):
    list_word = list(word)
    shuffle(list_word)
    newWord = ''.join(list_word)

    return newWord
    

def shuffle_multipleWords(word):
    newWord = ""
    arr_words = word.split(' ')
    arrWordContainer = []
    for new_word in arr_words:
        arrWordContainer.append(shuffle_word(new_word))
    
    for new_word in arrWordContainer:
            newWord = newWord + ' ' + new_word
    
    return newWord

def start():
    print("- Enter a Word -")
    word = input().lower()
    newWord = shuffle_word(word)

    if(' ' in word):
        newWord = shuffle_multipleWords(word)
    
    print(f'{newWord}\n')

    while(True):
        print("- Do you want to reshuffle? (y/n) -")
        reshuffle_ans = input()
        if(reshuffle_ans.lower() == 'y' or reshuffle_ans.lower() == 'yes'):
            newWord = shuffle_word(newWord)
            if(' ' in word):
                newWord = shuffle_multipleWords(word)
        
            print(f'{newWord}\n')

        elif (reshuffle_ans.lower() == 'n' or reshuffle_ans.lower() == 'no'): 
            break
        else:
            print('Kindly select yes or no\n')
        

## MAIN CODE ##
start()
while(True):
    print("\n- Want to shuffle a new Word? (y/n)-")
    newShuffle = input()
    print(newShuffle.lower() == 'y' or newShuffle.lower() == 'yes')
    if(newShuffle.lower() == 'y' or newShuffle.lower() == 'yes'):
        os.system("cls")
        start()
    elif (newShuffle.lower() == 'n' or newShuffle.lower() == 'no'): 
            break
    else:
        print('Kindly select yes or no')