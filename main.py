# Genetic python code generator
# Written by Jonah Siekmann
# 1/9/2018

from genome import Genome
from random import *
import time
import math
INITIAL_GENOMES = 30;
STABLE_GENOMES = 22;


def initializeGenomes(num):
    genomes = []
    for i in range(0, num):
        genomes.append(Genome(True));
    return genomes;

def getFittestGenomes(num, genomes):
    topGenomes = [];
    fitList = []
    print("Selecting " + str(num) + " fittest genomes of " + str(len(genomes)) + " total.");
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
        print("Found " + str(len(topGenomes)) + " fittest genomes so far: ", end="");
        for i in range(0, 5):
            print(topGenomes[len(topGenomes)-1].genome[i], end=" ");
        print("");
    return topGenomes

def printGenome(genome):
    counter = 0;
    for i in genome.genome:
        print(i + " ", end="");
        counter += 1;
        if counter % 15 == 0:
            print("");
def main():
    genomes = initializeGenomes(INITIAL_GENOMES);

    cream_of_the_crop = []
    
    counter = 0;
    
    start_t = time.time();
    
    while(True):
        elapsed_time = math.floor(time.time() - start_t);
        print("Cycle " + str(counter) + ". It has been " + str(elapsed_time) + "s since initialization.");
        print("Pausing for three seconds for readability."); 
        time.sleep(3);
        print("Breeding...");
        if(len(cream_of_the_crop) > 0):
            for i in range(0, randint(0, len(cream_of_the_crop)-1)):
                genomes.append(cream_of_the_crop[i].crossbreed(cream_of_the_crop[randint(0, len(cream_of_the_crop)-1)]));
                
        for i in range(0, randint(0, len(genomes)-1)):
            genomes.append(genomes[i].crossbreed(genomes[randint(0, len(genomes)-1)]));
        print("Breeding finished.");
        
        cream_of_the_crop = getFittestGenomes(STABLE_GENOMES, genomes);
        top_fitness = cream_of_the_crop[0].fitness();
        top_wordcount = cream_of_the_crop[0].wordcount();
        
        print("Highest scoring genome fitness was " + str(cream_of_the_crop[0].fitness()) + " with a keyword count of " + str(cream_of_the_crop[0].wordcount()) + "/1000 (" + str(100*(top_wordcount)/1000) + "%)");
        
        genomes = cream_of_the_crop;
        
        counter += 1;
        

            
        
        


        
        

main();
