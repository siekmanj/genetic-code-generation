# Fitness Evaluation for a genetic python code generator
# Written by Jonah Siekmann
# 1/9/2018
"""
Things that receive a positive fitness score:
Newlines + 1
Indents + 3
Lines less than 100 characters long + 1
Keywords (followed by variable) + 5
    else preceded by an if + 5
    keyword + var name = something + 10
                           ^ if this is a previously declared variable + 12
    
Compilation + 60

fitness is evaluated per-line - lines with a fitness of 0 aren't included and considered inactive portions of genome

"""

import keyword as k

from random import *

MAX_WORD_LEN = 8;
MIN_WORD_LEN = 2;
INITIAL_GENOMES = 2;
MUTATION_RATE = 5;
MAX_NUMBER_OF_MUTATIONS = 50;
characters = ['T', 'F', 'N', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

genomes = [];

def fitness(word):
    highestScore = 0;
    for i in range(0, len(k.kwlist)-1):        #for every keyword in the list of keywords
        currentScore = 0;                      #initialize temp score
        for j in range(0, len(k.kwlist[i])-1): #for each char in the keyword
            if len(word) > j:                  #if the length of the word is shorter than the index of the current character in the keyword, abort
              if k.kwlist[i][j] == word[j]:
                currentScore += 1;
        if(currentScore > highestScore):
            highestScore = currentScore
    return highestScore

def main():
    for i in range(0, INITIAL_GENOMES):
        genome = [];
        for i in range(0, 1000):
            l = randint(MIN_WORD_LEN, MAX_WORD_LEN);
            temp = "";
            for i in range(0, l):
                char = randint(0, len(characters)-1);
                temp += characters[char];
            genome.append(temp);
        genomes.append(genome);
    
    while(input("cont? ") != "n"):

        
def crossbreed(genome1, genome2):
    new_genome = [];
    for i in range(0, 500):
        new_genome.append(genome1[randint(0, 1000)]);
        new_genome.append(genome2[randint(0, 1000)]);
    for i in range(0, randint(0, MAX_NUMBER_OF_MUTATIONS)):
        if(randint(0, 100) < MUTATION_RATE):
            new_genome[randint(0, 1000)] = characters[randint(0, len(characters))];
    return new_genome;
main();
