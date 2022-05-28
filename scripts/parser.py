import json
import os
import random

with open(os.path.join('data', 'database1.json'), 'r', encoding='utf-8') as f:
    DATA = json.load(f)


def getData():
    randomNumber = random.choice([i + 1 for i in range(len(DATA))])
    chosenDATA = DATA[str(randomNumber)]
    auth = chosenDATA['author']
    quote = chosenDATA['quote']
    text = f'{quote} — {auth}'
    return text
