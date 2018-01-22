import time
import math
from random import *
from fitness import *

characters = ['T', 'F', 'N', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
POOL_SIZE = 500 #number of genomes to keep after culling the unfit
MIN_WORD_LEN = 2
MAX_WORD_LEN = 8
GENOME_LENGTH = 50
MUTATION_RATE = 0.155 #percentage of words in a genome which can be altered during a crossbreed.



    
class Genome:
    """This class represents a genome."""
    def __init__(self, init): 
        
        self.genome = []
        self.mutation_rate = MUTATION_RATE
        
        if(init): #If init is true, then we need to populate this genome with random characters (this is only needed at start of simulation
            
            seed() #seed the random number generator
            
            for i in range(0, GENOME_LENGTH): #populate entire genome
                
                word = ""
                wordLength = randint(MIN_WORD_LEN, MAX_WORD_LEN) #get a random word length
                for i in range(0, wordLength): 
                    word += choice(characters) #append random characters to the word
                    
                self.genome.append(word) #append the random word to the genome
    
            self.fitness_score = evaluateFitness(self.genome)/GENOME_LENGTH
        
        self.fitness_score = .1
                
    def crossbreed(self, other_genome): #takes two existing genomes, and inserts a word from one of two parents into every slot.
        
        seed() #seed the random number generator
        new_genome = Genome(False) #initialize Genome object with False to keep it from filling its genome with random words.
        #new_genome.mutation_rate =  0.125*(1 / (1 + math.exp(-(1/((self.fitness() + other_genome.fitness())/2))))) #multiply mutation rate by inverse parent's averaged fitness;
        new_genome.mutation_rate = 0.05 / ((self.fitness() + other_genome.fitness())/2)
        for i in range(0, GENOME_LENGTH): #population entire genome of new offspring

            if randint(0, 1) == 0: #50/50 chance of any word coming from either parent
                new_genome.genome.append(self.genome[i]) #insert a word from parent 1
            else:
                new_genome.genome.append(other_genome.genome[i]) #insert a word from parent 2
                        
        for word in range(0, len(new_genome.genome)-1): #iterate through every word so that each one has an equal chance of being mutated
            if(randint(0, 100) < new_genome.mutation_rate * 100): #random chance of a character in a word mutating into something else

                mutation = list(new_genome.genome[word])
                mutation_type = randint(1, 3)
                
                if mutation_type == 1: #33% chance that the mutation will be a character replacement
                    mutation[randint(0, len(new_genome.genome[word])-1)] = choice(characters) #replace a random character in the word with another random character
                    
                elif mutation_type == 2 and len(new_genome.genome[word]) > MIN_WORD_LEN: #33% chance that the mutation will be a character deletion
                    del mutation[randint(0, len(new_genome.genome[word])-1)] #delete a random character from the word
                    
                elif mutation_type == 3 and len(new_genome.genome[word]) < MAX_WORD_LEN: # 33% chance that the mutation will be a character insertion
                    mutation.insert(randint(0, len(new_genome.genome[word])), choice(characters)) #insert a random character into the word
                            
                new_genome.genome[word] = ''.join(str(c) for c in mutation) #re-insert the mutated word back into the genome
                
        self.fitness_score = evaluateFitness(self.genome)/GENOME_LENGTH
        return new_genome
    
    
    def print(self, wordsPerLine): #prints a genome
        
        for i in range(len(self.genome)-1):

            print(self.genome[i] + " ", end="")

            if i % wordsPerLine == 0 and i >= wordsPerLine:
                
                print("")
                
                
    def similarity(self, genome): #returns the average word similarity of two genomes. May reveal something about genetic diversity (?)
        
        averageSimilarity = 0
        
        for i in range(GENOME_LENGTH):
            
            averageSimilarity += wordSimilarity(self.genome[i], genome.genome[i]) #wordSimilarity returns a number between 1 and 0 depending on how similar the two words are.
            
        return averageSimilarity/GENOME_LENGTH #return the average of the word similarities.

    
    def fitness(self):
        return self.fitness_score #evaluateFitness(self.genome)/GENOME_LENGTH
    
    def wordcount(self):
        return numberOfKeywords(self.genome)
    
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))