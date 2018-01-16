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
import keyword as k;
from genome import *

def evaluateFitness(genome):
    overallScore = 0;
    for word in genome:
        highestScore = 0;
        for i in range(0, len(k.kwlist)-1): #for every keyword in the list of keywords
            currentScore = 0;                                   
            for j in range(0, len(k.kwlist[i])-1): #for each char in the keyword
                if len(word) > j and k.kwlist[i][j] == word[j]: #stops index out of bounds from happening, checks if the char at this position matches keyword in same position.
                    currentScore += 1;
                #elif j != 0 and (word[j] == "F" or word[j] == "T" or word[j] == "N"): #If we're NOT at the start of the word and there is a capital letter, we punish fitness score.
                #    currentScore -= 1;
            if(k.kwlist[i] == word):
                currentScore += 25;
            if(currentScore > highestScore):       #we don't want multiple keywords to increment the same fitness score
                highestScore = currentScore
        overallScore += highestScore;
    return overallScore

def numberOfKeywords(genome):
    wordCount = 0;
    for word in genome:
        for i in range(0, len(k.kwlist)-1):
            if k.kwlist[i] == word:
                wordCount += 1;
    return wordCount;

def wordSimilarity(word1, word2):
    similarityScore = 0;
    for i in range(0, len(word1)-1):
        if i < len(word2)-1:
            if word1[i] == word2[i]:
                similarityScore += 1;
    similarityScore /= max(len(word1), len(word2));
    return similarityScore;
         