import random
import nltk
from nltk import pos_tag, word_tokenize

def objects():
    with open('/usr/share/dict/linux.words', 'r') as myfile:
            return (myfile.readlines())

def Jeremy_Picks(words):
    return random.choice(words).rstrip()

def Jeremy_Evaluates(aWord):
    return nltk.pos_tag(word_tokenize(aWord))[0][1]

def Jeremy_Gets_An_Opinion():
    return ('worst' if (random.random() <= 0.5) else 'best')

def Jeremy_Sounds_His_Opinion(opinion, noun):
    print('Hi, my name is Jeremy Clarkson and this is the ' + opinion + ' ' + noun + '...\n   in the world')

isNoun = False
word = Jeremy_Picks(objects())
opinion = Jeremy_Gets_An_Opinion()

while(not isNoun):
    wordType = Jeremy_Evaluates(word)

    if(wordType != ('NN' or 'NNS')):
        word = Jeremy_Picks(objects())
        wordType = Jeremy_Evaluates(word)
    else:
        isNoun = True

finalVerdict = Jeremy_Sounds_His_Opinion(opinion, word)
