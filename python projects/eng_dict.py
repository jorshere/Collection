import json
#import os
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))
def translate(word):
    word=word.lower()    # to get all input in lower case OR you can pass it in  call function;
    if word in data:            # to check the word exist in program
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.6))>0:
        xyz=input (f"did you mean :{get_close_matches(word,data.keys())[0]},\t if Yes press 'y' else press 'n' : ")
        if xyz == 'n' or xyz=='N':
            return f"we cant able to find similar words for: {word} , please try again;"
        elif xyz =='y' or xyz=='Y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "Invaild Entry, follow as stated;"

    else:
        return "word doesn't have meaning,enter again."


while True:                         # to be in loop
    entry= input("enter word: ")
    output= translate(entry)

    if type(output) == list:
        for i in output:
            print(f". {i}")
    else:
        print(output)      