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
import math
from genome import *


SHORT_TO_LONG_KEYWORD_RATIO = 0.32

def evaluateFitness(genome):
    overallScore = 0;
    for word in genome:
        temp = "";
        highestScore = 0;
        for keyword in k.kwlist: #for every keyword in the list of keywords
            currentScore = wordSimilarity(word, keyword) * math.sqrt(len(keyword) * SHORT_TO_LONG_KEYWORD_RATIO)
            if(currentScore > highestScore):       #we don't want multiple keywords to increment the same fitness score
                temp = keyword
                highestScore = currentScore
           
        overallScore += highestScore;
    return overallScore

def numberOfKeywords(genome):
    wordCount = 0;
    for word in genome:
        for i in k.kwlist:
            if i == word:
                wordCount += 1;
    return wordCount;

def wordSimilarity(word1, word2):
    smallWord = "";
    bigWord = "";
    if(len(word1) > len(word2)):
        smallWord = word2;
        bigWord = word1;
    else:
        smallWord = word1;
        bigWord = word2;
    longestRun = 0;
    for i in range(0, len(smallWord)-1):
        indexSmall = 0;
        indexBig = 0;
        run = 0;
        while(i + indexSmall < len(smallWord) and indexBig < len(bigWord)):
            if smallWord[i + indexSmall] == bigWord[indexBig]:
                run += 1;
                indexSmall += 1;    
                if run > longestRun:
                    longestRun = run;
            else:
                run = 0;
                indexSmall = 0;
            indexBig += 1;
    return longestRun/len(bigWord);

def min(word1, word2):
    if(len(word1) < len(word2)):
        return word1
    else:
        return word2
    
def max(word1, word2):
    if(len(word1) > len(word2)):
        return word1
    else:
        return word2
    
    
    """

in def ssert del yiel def asseF inj miasser elif uels fr TFals from zglobv not elsf in is or is
for while xclasg aise raise eFals break rom if if in ceptrg pass dhile retuwg Falsl fpor and cnallyx dcl
pssekf rom None from fglob or onek for
"""