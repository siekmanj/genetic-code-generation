import keyword as k;
import math
from genome import *


SHORT_TO_LONG_KEYWORD_RATIO = 0.32

#return the sum fitness of a genome
def evaluateFitness(genome):
    overallScore = 0;
    for word in genome:
        highestScore = 0;
        for keyword in k.kwlist: #for every keyword in the list of keywords
            currentScore = wordSimilarity(word, keyword) * math.sqrt(len(keyword) * SHORT_TO_LONG_KEYWORD_RATIO) #multiplying by the square root of length makes longer keywords score higher than shorter ones while still allowing shorter keywords to be represented proportionally
            if(currentScore > highestScore):       #we don't want multiple keywords to increment the same fitness score
                highestScore = currentScore
           
        overallScore += highestScore;
    return overallScore

#returns the number of keywords in a list
def numberOfKeywords(genome):
    wordCount = 0;
    for word in genome:
        for i in k.kwlist:
            if i == word:
                wordCount += 1;
    return wordCount;

#returns number between 0 and 1 of how similar two words are to each other. "in" and "if" returns 0.5. "ni" and "if" also return 0.5, because they are length 2 and have 1 letter in common.
def wordSimilarity(word1, word2):
    smallWord = min(word1, word2);
    bigWord = max(word1, word2);
    
    longestRun = 0;
    for i in range(len(smallWord)-1):
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

#returns the longer of two words
def min(word1, word2):
    if(len(word1) < len(word2)):
        return word1
    else:
        return word2

#returns the shorter of two words
def max(word1, word2):
    if(len(word1) > len(word2)):
        return word1
    else:
        return word2
    
    