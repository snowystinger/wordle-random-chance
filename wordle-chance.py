#!/usr/bin/python3
import sys
import random

def filter_on_knowledge(overall_blacks, overall_greens, overall_yellows):
    def filter_curry(word):
        for idx, i in enumerate(word):
            if i in overall_blacks:
                return False
        for j in overall_greens:
            if j['value'] != word[j['index']]:
                return False
        for j in overall_yellows:
            if j not in word:
                return False
        return True
    return filter_curry

path = './csw19.txt'

word_file = open(path,'r')
words = word_file.readlines()[2:]
words = list(filter(lambda x: len(x) == 5, map(lambda x: x.replace('\n', '').lower(), words)))
word_file.close()

occurrences = {}
for word in words:
    for letter in word:
        if letter in occurrences:
            occurrences[letter] = occurrences[letter] + 1
        else:
            occurrences[letter] = 1
occurrences = dict(sorted(occurrences.items(), key=lambda item: item[1]))
top_occurrences = list(occurrences.keys())[-8:]
print(top_occurrences)
starters = []
for word in words:
    shouldContinue = False
    for letter in word:
        if word.count(letter) > 1:
            shouldContinue = True
            break
    if shouldContinue:
        continue
    for letter in word:
        if letter not in top_occurrences:
            shouldContinue = True
            break
    if shouldContinue:
        continue
    starters.append(word)

print('try the word ' + starters[random.randrange(len(starters))])

print('you have ' + str(len(words)) + ' word choices')

overall_greens = []
overall_yellows = []
overall_blacks = []
new_words = []

while True:
    guess = input('what did you guess? ').lower()
    if guess == 'done':
        break
    if guess == 'show':
        print(new_words)
        continue
    result = input('what was the result? ').lower()


    greens = [index for index, element in enumerate(result) if element == 'g']
    yellows = [index for index, element in enumerate(result) if element == 'y']
    blacks = [index for index, element in enumerate(result) if element == 'b']

    for i in greens:
        overall_greens.append({'value': guess[i], 'index': i})

    for i in yellows:
        overall_yellows.append(guess[i])

    for i in blacks:
        overall_blacks.append(guess[i])

    print(overall_greens)
    print(overall_yellows)
    print(overall_blacks)


    new_words = list(filter(filter_on_knowledge(overall_blacks, overall_greens, overall_yellows), words))

    print('you have ' + str(len(new_words)) + ' word choices')
