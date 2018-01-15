# Genetic python code generator
# Written by Jonah Siekmann
# 1/9/2018
"""
Things that receive a positive fitness score:
Newlines + 1
Indents + 3
Lines less than 100 characters long + 1
Keywords (followed by variable) + 5
    else preceded by an if + 5
    keyword + var name = something + 10
                           ^ if this is a previously declared variable + 12
    
Compilation + 60

fitness is evaluated per-line - lines with a fitness of 0 aren't included and considered inactive portions of genome

"""

from genome import Genome

genomes = [];

def main():
    
    genomes.append(Genome());
    genomes[0].fitness();
    inpt = input("Continue?");
    while(inpt == 'yes'):
        fitlist = [];
        for i in genomes:
            score = fitness(i);
            fitlist.append(score);
            print(score);
        
        

main();
