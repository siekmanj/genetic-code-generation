# Genetic python code generator
# Written by Jonah Siekmann
# 1/9/2018


from random import *
import time
import math
import os

import threading

import genome
import fitness

MAX_CONCURRENT_THREADS = 10;

def lookForInput():
    return input("")

def initializeGenomes(num):
    genomes = []
    for i in range(0, num):
        genomes.append(genome.Genome(True));
    return genomes;

def getFittestGenomes(num, genomes):
    
    topGenomes = [];
    fitList = []
    
    for i in range(0, len(genomes)-1):
        fitList.append(genomes[i].fitness())
        
    while(len(topGenomes) < num):
        currentTopScore = 0
        for index in range(0, len(fitList)-1):
            if genomes[index] not in topGenomes:
                currentScore = fitList[index]
                currentGenome = genomes[index]
                if currentTopScore < currentScore:
                    currentTopScore = currentScore
                    currentTopGenome = currentGenome
        topGenomes.append(currentTopGenome)
    return topGenomes

def getAverageSimilarity(genome, genomes):
    average = 0
    for i in genomes:
        if i is not genome:
            average += genome.similarity(i);
    return average/len(genomes);
            
        
            
def breedGenomes(genomes): #breeds an existing pool of genomes together to make more genomes.
    
    if(genomes): #if genomes is not empty 
        
        for i in range(math.floor(len(genomes) * uniform(1, 3))): #breed a random number of the fittest genomes together
            
            genome1 = choice(genomes) #randomly selects a genome from the list of fittest genomes
            genome2 = choice(genomes) #randomly selects a second genome from the list of fittest genomes
            
            if genome1 is not genome2:
                
                child = genome1.crossbreed(genome2) #takes a random half from genome1 and genome2 to create a new genome, with a random chance for mutations.
                genomes.append(child) #appends the child to the list of all the genomes.
                
def getExistingGenomes():
    genomes = []
    for i in os.listdir("genomes"):
        existingGenome = genome.Genome(False)
        existingGenome.id = i
        file = open("genomes/" + i + "/X.genome")
        for i in file.read().split(" "):
            existingGenome.genome.append(i)
        existingGenome.fitness() #calculate fitness
        genomes.append(existingGenome)
        file.close()
    return genomes
        
def main():
    print("Looking for existing genomes...")
    genomes = getExistingGenomes()
    if len(genomes) > 0:
        print("Found " + str(len(genomes)) + " existing genomes.")
    else:
        print("Did not find any. Initializing a new pool.")
        genomes = initializeGenomes(genome.POOL_SIZE);
    cream_of_the_crop = []
   
    cycle = 0;
    while(True):
        
        start_time = time.time(); #keep track of the time this loop started at.

        seed(); #seed the random number generator

        print("Commencing breeding cycle " + str(cycle) + ".");
        
        breedGenomes(genomes);
        
        print("Resulting number of genomes in pool: " + str(len(genomes)));

        cream_of_the_crop = getFittestGenomes(genome.POOL_SIZE, genomes);
        
        top_fitness = cream_of_the_crop[0].fitness();
        bottom_fitness = cream_of_the_crop[len(cream_of_the_crop)-1].fitness();
        top_wordcount = cream_of_the_crop[0].wordcount();
        similarity_factor = getAverageSimilarity(cream_of_the_crop[0], cream_of_the_crop);
        
        print("Genetic similarity between #1 and top " + str(len(cream_of_the_crop)) + ": " + str(math.floor(100 * similarity_factor)) + "%. Highest score: " + str(math.floor(top_fitness*1000)/1000) + ". Mutation rate: " + str(math.floor(1000*cream_of_the_crop[0].mutation_rate)/1000) + ". Lowest score: " + str(math.floor(bottom_fitness*1000)/1000) + ". Mutation rate: " + str(math.floor(1000*cream_of_the_crop[len(cream_of_the_crop)-1].mutation_rate)/1000) + ". Keywords: " + str(top_wordcount) + "/" + str(genome.GENOME_LENGTH) + " (" + str(100*(top_wordcount)/genome.GENOME_LENGTH) + "%). Time elapsed since start of cycle: " + str(math.floor(time.time() - start_time)) + "seconds.");
        
        for i in genomes:
            if i not in cream_of_the_crop:
                i.removeFromPool()
                
        genomes = cream_of_the_crop
        
        for i in cream_of_the_crop:
            i.saveToFile()

            
        print(str(len(genomes)))
       
        if cycle % 20 == 0:
            print("\n\n");
            cream_of_the_crop[0].print(20)
            print("\n\n");
        cycle += 1;
        time.sleep(2)
    


            
        
        


        
        

main()
