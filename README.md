# genetic-code-generation
Uses evolutionary algorithms to create python code that (eventually) compiles.

Current state: Generates python keywords from random characters over the course of a few thousand breeding cycles, saves each genome to a file called X.genome.

Roadmap:
Three chromosomes are created. The first contains randomly generated characters: 

(A, T, F, a-z) 

which eventually become python keywords. 

The second creates randomly distributed special characters as well as three-letter variable names, and random numbers:

(+, -, \*, /, =, (, ), :, kgw, qpw, 1234, 152, 19) 

which eventually become arranged in a reasonable order, ie, each (, ", and \[ has a matching \], " and \), a three-letter variable is followed by an operator like =, \*, and assigned to something.


The third comes up with a Context-Free Grammar, which I still need to figure out.
