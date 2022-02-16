---
title: Machine, Data and Learning (CS7.301)
subtitle: |
          | Spring 2022, IIIT Hyderabad
          | 10 Feb, Thursday (Lecture 9)
author: Taught by Prof. Vikram Pudi
---

# Solving Problems by Searching
## Informed Search Algorithms (contd.)
We can use as an admissible heuristic for a problem the cost of a solution to the relaxed problem.  

Another class of informed search algorithms are local search algorithms. These are used for problems that require us to find a configuration satisfying some constraints, like the $n$-queens problem. The path to the goal is irrelevant in these cases.  

Hill-climbing search is a strategy that continually finds a local maximum, and uses this to reach the peak. However, this has the disadvantage that it might get stuck in a local maximum.  

Simulated annealing search is a way to escape the local maxima. It allows some undesirable moves, but it gradually decreases their frequency. If the "temperature" $T$ decreases slowly enough, then simulated annealing will find a global optimum with probability approaching 1.  

Local beam search is another such algorithm. It keeps track of $k$ states rather than just one, and picks the $k$ best states out of all the successors of these $k$ states.  

Genetic algorithms are another class of search algorithms. They form successor states by combining two parent states, starting with $k$ randomly generated states. There is a fitness function that lets us evaluate the states.  
We can also incorporate random mutations.