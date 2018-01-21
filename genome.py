import time
from random import *
from fitness import *
characters = ['T', 'F', 'N', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']; 
MIN_WORD_LEN = 2;
MAX_WORD_LEN = 8;
GENOME_LENGTH = 250;

INITIAL_GENOMES = 100;
STABLE_GENOMES = 100;

MUTATION_RATE = 0.3; #up to 15.5% of words in a genome can be altered during a crossbreed.


    
class Genome:
    """This class represents a genome."""
    def __init__(self, init): 
        self.genome = [];
        self.mutation_rate = MUTATION_RATE;
        self.mutations = 0;
        if(init): #If init is true, then we need to populate this genome with random characters (this is only true at start of simulation)
            seed();
            for i in range(0, GENOME_LENGTH): #populate entire genome
                wordLength = randint(MIN_WORD_LEN, MAX_WORD_LEN); #each word can be a random length.
                word = "";
                for i in range(0, wordLength):
                    word += choice(characters);
                self.genome.append(word);

    def crossbreed(self, genome2, mutation): #takes two existing genomes, and inserts a word from one of two parents into every slot.
        new_genome = Genome(False); #initialize Genome object with False to tell it not to bother filling its own genome with random words, as we'll do that next.
        new_genome.mutation_rate = mutation;
        seed();
        new_genome.mutations = 0;
        for i in range(0, GENOME_LENGTH): #population entire genome of new offspring
            if randint(0, 1) == 1: #50/50 chance of any word coming from either parent
                new_genome.genome.append(self.genome[i]); 
            else:
                new_genome.genome.append(genome2.genome[i]);
        for word in range(0, len(new_genome.genome)-1):
            if(randint(0, 100) < new_genome.mutation_rate * 100): #random chance of a character in a word mutating into something else.
                mutation = list(new_genome.genome[word]);
                randomChar = randint(0, len(new_genome.genome[word])-1)
                if randint(0, 1) == 1: # 50% chance that the mutation will be a character replacement or deletion
                    if randint(0, 1) == 1:
                        mutation[randomChar] = choice(characters);
                        new_genome.mutations+=1;
                    elif len(new_genome.genome[word]) > MIN_WORD_LEN:
                        del mutation[randomChar];
                        new_genome.mutations+=1;

                else:
                    if randint(0, 1) == 1 and len(new_genome.genome[word]) < MAX_WORD_LEN: # 25% chance that the mutation will lengthen the string by one character
                        mutation.append(choice(characters));
                        new_genome.mutations+=1;
                       
                    elif len(new_genome.genome[word]) > MIN_WORD_LEN: # 25% chance that the mutation will shorten the string by one character.
                        mutation.pop(); 
                        new_genome.mutations+=1;
                new_genome.genome[word] = ''.join(str(c) for c in mutation);
        return new_genome;
    def getMutations(self):
        return self.mutations
    def print(self):
        counter = 0;
        for i in self.genome:
            print(i, end=" ");
            if counter == 15:
                print("");
        print("\n");
    def similarity(self, genome): #returns the average word similarity of two genomes. May reveal something about genetic diversity (?)
        averageSimilarity = 0;
        for i in range(GENOME_LENGTH):
            averageSimilarity += wordSimilarity(self.genome[i], genome.genome[i]); #wordSimilarity returns a number between 1 and 0 depending on how similar the two words are.
        return averageSimilarity/GENOME_LENGTH; #return the average of the word similarities.

    
    def fitness(self):
        return evaluateFitness(self.genome)/GENOME_LENGTH;
    
    def wordcount(self):
        return numberOfKeywords(self.genome);
