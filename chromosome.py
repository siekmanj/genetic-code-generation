import random

class Chromosome:
	def __init__(self, length):
		random.seed()

		self.chromosome = []
		self.length = length

		for i in range(length):
			self.chromosome.append(random.randint(0, 1)) #assign a random number

	def crossbreed(self, partner, chance_of_mutation):
		offspring = Chromosome(0) #create a new chromosome with 0 bits

		if(self.length != partner.length): #if the length of the parent chromosome is greater than its partner
			return offspring #if the lengths don't match, return the empty offspring
		else:
			offspring.length = self.length #set the length of the offspring

			for i in range(self.length): #50/50 chance of a bit coming from either parent
				if(random.randint(0, 1) == 0):
					offspring.chromosome.append(self.chromosome[i])
				else:
					offspring.chromosome.append(partner.chromosome[i])

			if(random.randint(0, chance_of_mutation) < 1): #1 in X chance of a mutation
				if offspring[i] == 1:
					offspring[i] == 0
				else:
					offspring[i] == 1
					
		return offspring
