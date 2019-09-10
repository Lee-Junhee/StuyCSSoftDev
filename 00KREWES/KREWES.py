KREWES = {
        'orpheus': ['Emily', 'Kevin', 'Vishwaa'],
        'rex': ['William', 'Joseph', 'Calvin'],
        'endymion': ['Grace', 'Nahi', 'Derek']
        }

import random
def randName():
    return (random.choice(KREWES[random.choice(KREWES.keys())])

print(randName())
print(randName())
print(randName())
