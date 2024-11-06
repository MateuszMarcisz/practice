import string

import numpy as np
# Add an import here

text = np.array(['Th   Is', '{Is', 'Al+mOst', 'A}', 'nOr m   Al!!!', 'sEnt578EncE', '-nOw'])  # Do not change this.


def remove_extra_stuff(txt):
    return np.char.translate(txt, str.maketrans('IAOLE', 'iaole', string.punctuation + string.whitespace + string.digits))


if __name__ == '__main__':
    for word in remove_extra_stuff(text):
        print(word, end=" ")
