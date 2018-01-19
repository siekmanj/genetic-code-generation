# Genetic python code generator
# Written by Jonah Siekmann
# 1/9/2018

from genome import *
from random import *
import time
import math

import threading
import queue
import fitness
def lookForInput():
    return input("");

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

def getAverageSimilarity(genome, genomes):
    average = 0;
    for i in genomes:
        if i is not genome:
            average += genome.similarity(i);
    return average/len(genomes);

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
    numGenomes = STABLE_GENOMES;
    mutation_rate = .12
    counter = 0;
    start_t = time.time();
    threading.Thread(target=lookForInput).start();
                         
    while(True):
        elapsed_time = math.floor(time.time() - start_t);
        print("Commencing cycle " + str(counter) + ". It has been " + str(elapsed_time) + " seconds since initialization. Mutation rate: " + str(mutation_rate), end=". ");
        if(len(cream_of_the_crop) > 0):
            for i in range(0, randint(0, len(cream_of_the_crop)-1)):
                genomes.append(cream_of_the_crop[i].crossbreed(cream_of_the_crop[randint(0, len(cream_of_the_crop)-1)], mutation_rate));
        for i in range(0, randint(0, len(genomes)-1)):
            genomes.append(genomes[i].crossbreed(genomes[randint(0, len(genomes)-1)], mutation_rate));
        print("Current number of genomes in pool: " + str(len(genomes)));

        cream_of_the_crop = getFittestGenomes(randint(numGenomes, math.floor(numGenomes + numGenomes*0.1)), genomes);

        top_fitness = cream_of_the_crop[0].fitness();
        top_wordcount = cream_of_the_crop[0].wordcount();
        similarity_factor = getAverageSimilarity(cream_of_the_crop[0], cream_of_the_crop);
        
        
        if(similarity_factor > .3 and mutation_rate < .50):
            mutation_rate += 0.005;
        if(similarity_factor < .3 and mutation_rate > .12):
            mutation_rate -= 0.005;
        

        print("Genetic similarity between #1 and top " + str(len(cream_of_the_crop)) + ": " + str(math.floor(100 * similarity_factor)) + "%. ", end="");
        for i in cream_of_the_crop:
            i.print();
        print("Highest score was 0." + str(math.floor(1000*top_fitness)) + " with a keyword count of " + str(top_wordcount) + "/1000 (" + str(100*(top_wordcount)/1000) + "%)");
        time.sleep(2);
        genomes = cream_of_the_crop;
        if counter % 20 == 0:
            print("\n\n");
            printGenome(cream_of_the_crop[0]);
            print("\n\n");
        counter += 1;
        print("threads: ", threading.active_count());
        if threading.active_count() < 2:
            inpt = input("Enter values for mutation rate and fitness pool size: ").split();
            valid = False;
            while not valid:
                try:
                    mutation_rate = float(inpt[0]);
                    numGenomes = int(inpt[1]);
                    if mutation_rate > .5 or mutation_rate < 0 or numGenomes <16 or numGenomes > 1000:
                        raise OutOfBoundsException("nope");
                    valid = True;
                except:
                    inpt = input("Invalid input. First arg must be 0 < float < 1, second one must be 16 < int <: ");
                
            threading.Thread(target=lookForInput).start();

    


            
        
        


        
        

main();
