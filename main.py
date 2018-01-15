# Genetic python code generator
# Written by Jonah Siekmann
# 1/9/2018

from genome import Genome

INITIAL_GENOMES = 20;
STABLE_GENOMES = 16;


def initializeGenomes(num):
    genomes = []
    for i in range(0, num):
        genomes.append(Genome(True));
    return genomes;

def getFittestGenomes(num, genomes):
    topGenomes = [];
    
    while(len(topGenomes) < num):
        print("Found " + str(len(topGenomes)) + " fittest genomes so far: ", end="");
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
        print(topGenomes[len(topGenomes)-1].genome[0]);
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
    
    while(True):
        print("Crossbreeding.", end="");
        for i in range(0, len(cream_of_the_crop)-1):
            genomes.append(cream_of_the_crop[i].crossbreed(cream_of_the_crop[i+1]))
            genomes.append(cream_of_the_crop[i].crossbreed(cream_of_the_crop[len(cream_of_the_crop)-i-1]));
        print("\nSelecting " + str(STABLE_GENOMES) + " fittest genomes.");
        cream_of_the_crop = getFittestGenomes(STABLE_GENOMES, genomes);
                
        print("Highest score was " + str(cream_of_the_crop[0].fitness()) + ".");
        
        counter = 0;
        genomes = cream_of_the_crop;
        

            
        
        


        
        

main();
