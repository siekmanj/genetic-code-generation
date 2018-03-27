import random
#The only thing that this class should do is generate random 1s and 0s
#The other stuff should be in an intermediary class
#character interpretations

class Genome:
	def __init__(self, genome_length):
		self.genome = []
		self.length = genome_length
		random.seed()
		for i in range(genome_length):
			self.genome.append(random.randint(0, 1))

	def sequence(self, bytelength):
		nums = []
		for i in range(0, len(self.genome), bytelength):
			codon = int("".join(str(self.genome[x]) for x in range(i, i+bytelength)), 2)
			nums.append(codon)
		return nums
