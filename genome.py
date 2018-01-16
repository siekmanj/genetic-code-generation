import time
from random import *
from fitness import evaluateFitness
from fitness import numberOfKeywords
characters = ['T', 'F', 'N', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']; 
MIN_WORD_LEN = 2;
MAX_WORD_LEN = 8;
GENOME_LENGTH = 1000;
MUTATION_RATE = 5;
MAX_NUMBER_OF_MUTATIONS = 50;
    
class Genome:
    """This class represents a genome."""
    def __init__(self, init): 
        self.genome = [];
        if(init):
            seed();
            for i in range(0, GENOME_LENGTH):
                wordLength = randint(MIN_WORD_LEN, MAX_WORD_LEN);
                word = "";
                for i in range(0, wordLength):
                    char = randint(0, len(characters)-1);
                    word += characters[char];
                self.genome.append(word);

    def crossbreed(self, genome2): #takes two existing genomes, and inserts a word from one of two parents into every slot.
        new_genome = Genome(False);
        seed();
        for i in range(0, GENOME_LENGTH):
            if randint(0, 1) == 1:    #50/50 chance of word coming from either parent
                new_genome.genome.append(self.genome[i]); 
            else:
                new_genome.genome.append(genome2.genome[i]);
        for i in range(0, randint(0, MAX_NUMBER_OF_MUTATIONS)): #chance of random mutation - replace a random character from a random word with another random character
            if(randint(0, 100) < MUTATION_RATE):
                randomIndex = randint(0, GENOME_LENGTH-1);
                mutation = list(new_genome.genome[randomIndex])
                mutation[randint(0, len(new_genome.genome[randomIndex])-1)] = characters[randint(0, len(characters)-1)];
                new_genome.genome[randomIndex] = mutation;
        return new_genome;
    
    def fitness(self):
        return evaluateFitness(self.genome);
    
    def wordcount(self):
        return numberOfKeywords(self.genome);