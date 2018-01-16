# Genetic python code generator
# Written by Jonah Siekmann
# 1/9/2018

from genome import *
from random import *
import time
import math



def initializeGenomes(num):
    genomes = []
    for i in range(0, num):
        genomes.append(Genome(True));
    return genomes;

def getFittestGenomes(num, genomes):
    topGenomes = [];
    fitList = []
    for i in range(0, len(genomes)-1):
        fitList.append(genomes[i].fitness());

    while(len(topGenomes) < num):
        currentTopScore = 0;
        for index in range(0, len(fitList)-1):
            if genomes[index] not in topGenomes:
                currentScore = fitList[index];
                currentGenome = genomes[index];
                if currentTopScore < currentScore:
                    currentTopScore = currentScore;
                    currentTopGenome = currentGenome;
        topGenomes.append(currentTopGenome);
    return topGenomes


def printGenome(genome):
    counter = 0;
    for i in genome.genome:
        print(i + " ", end="");
        counter += 1;
        if counter % 22 == 0:
            print("");
def main():
    genomes = initializeGenomes(INITIAL_GENOMES);

    cream_of_the_crop = []
    
    counter = 0;
    
    start_t = time.time();
    
    while(True):
        elapsed_time = math.floor(time.time() - start_t);
        print("Commencing cycle " + str(counter) + ". It has been " + str(elapsed_time) + " seconds since initialization. ", end="");
        if(len(cream_of_the_crop) > 0):
            for i in range(0, randint(0, len(cream_of_the_crop)-1)):
                genomes.append(cream_of_the_crop[i].crossbreed(cream_of_the_crop[randint(0, len(cream_of_the_crop)-1)]));
        for i in range(0, randint(0, len(genomes)-1)):
            genomes.append(genomes[i].crossbreed(genomes[randint(0, len(genomes)-1)]));
        print("Current number of genomes in pool: " + str(len(genomes)));
        
        cream_of_the_crop = getFittestGenomes(randint(STABLE_GENOMES, STABLE_GENOMES + STABLE_GENOMES*0.1), genomes);
        
        top_fitness = cream_of_the_crop[0].fitness();
        top_wordcount = cream_of_the_crop[0].wordcount();
        
        print("Genetic similarity between top two genomes: " + str(math.floor(100 * (cream_of_the_crop[0].similarity(cream_of_the_crop[1])))) + "%. ", end="");
        
        print("Highest scoring genome fitness was " + str(top_fitness) + " with a keyword count of " + str(top_wordcount) + "/1000 (" + str(100*(top_wordcount)/1000) + "%)");
        time.sleep(2);
        genomes = cream_of_the_crop;
        if counter % 500 == 0:
            print("\n\n");
            printGenome(cream_of_the_crop[0]);
            print("\n\n");
        counter += 1;
        

            
        
        


        
        

main();
