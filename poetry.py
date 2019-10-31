import random


def word(speech_part):
    data = {'noun': ['fossil', 'horse', 'aardvark', 'judge',
                     'chef', 'mango', 'extrovert', 'gorilla'],
            'verb': ['kicks', 'jingles', 'bounces', 'slurps',
                     'meows', 'explodes', 'curdles'],
            'adjective': ['furry', 'balding', 'incredulous',
                          'fragrant', 'exuberant', 'glistening'],
            'preposition': ['against', 'after', 'into', 'beneath',
                            'upon', 'for', 'in', 'like', 'over', 'within'],
            'adverb': ['curiously', 'extravagantly', 'tantalizingly',
                       'furiously', 'sensuously']}
    return random.choice(data[speech_part])


def make(string):
    if string[0] in ('a', 'e', 'i', 'o', 'u', 'y'):
        return 'An'
    else:
        return 'A'
        

def poem():
    adjective1 = word('adjective')
    noun1 = word('noun')
    noun2 = word('noun')
    a_or_an = make(adjective1)
    poem = f'{a_or_an} {adjective1} {noun1}\n\n{a_or_an} {adjective1} {noun1} {word("verb")}' + ' ' +\
           f'{word("preposition")} the {word("adjective")} {noun2} {word("adverb")}, the {noun1}'+\
           f' {word("verb")}\nthe {noun2} {word("verb")} {word("preposition")} a {word("adjective")} {word("noun")}\n\n\n'
    return poem


def main():
    try:
        with open ('files/poerty.txt', 'a') as file:
            file.write(poem())
    except:
        with open ('files/poetry.txt', 'w') as file:
            file.write(poem())


main()
