import keyword as k;

def evaluateFitness(genome):
    print("FUCK");
    overallScore = 0;
    for word in genome:
        highestScore = 0;
        for i in range(0, len(k.kwlist)-1):        #for every keyword in the list of keywords
            currentScore = 0;                      #initialize temp score
            for j in range(0, len(k.kwlist[i])-1): #for each char in the keyword
                if len(word) > j:                  #if the length of the word is shorter than the index of the current character in the keyword, abort
                  if k.kwlist[i][j] == word[j]:    #if the character at that position in the keyword matches the position in the randomly generated word
                    currentScore += 1;             #increment the fitness score
            if(currentScore > highestScore):       #we don't want multiple keywords to increment the same fitness score
                highestScore = currentScore
        overallScore += highestScore;
    return overallScore