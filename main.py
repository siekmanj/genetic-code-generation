# Genetic python code generator
# Written by Jonah Siekmann
# 1/9/2018

from genome import Genome

INITIAL_GENOMES = 4;

genomes = [];

def initializeGenomes(num):
    for i in range(0, num):
        genomes.append(Genome(True));

def getFittestGenomes(num):
    topGenomes = [];
    while(len(topGenomes) < num):
        currentTopGenome = [];
        currentTopScore = 0;
        for genome in genomes:
            if genome not in topGenomes:
                currentScore = genome.fitness();
                currentGenome = genome;
                if currentTopScore < currentScore:
                    currentTopScore = currentScore;
                    currentTopGenome = currentGenome;
        topGenomes.append(currentTopGenome);
    return topGenomes

def main():
    initializeGenomes(INITIAL_GENOMES);

    inpt = input("Begin breeding?");
    while(inpt == 'yes'):
        cream_of_the_crop = getFittestGenomes(2);
        genomes.append(Genome.crossbreed(cream_of_the_crop[0], cream_of_the_crop[1]));
        print(genomes[len(genomes)-1].fitness());
        
        


        
        

main();
