import json
from difflib import get_close_matches
from tkinter import messagebox
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        msg="Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]
        res = messagebox.askquestion(title="Suggestion", message=msg)
        if res == "yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif res == "no":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

