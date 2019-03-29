import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(word):
    word= word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        ans= input("Did you Mean %s instead? Enter Y if yes or N if No:" %get_close_matches(word,data.keys())[0])
        if ans=="Y" or  "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ans=="N" or "n":
            return "Sorry the word does'nt Exist"
        else:
            return "We Dont understand you."
    else:
        return "Sorry The Word does'nt Exist"

word= input("Enter the word: ")
print(translate(word))