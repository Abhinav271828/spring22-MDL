---
title: Machine, Data and Learning (CS7.301)
subtitle: |
          | Spring 2022, IIIT Hyderabad
          | 10 Feb, Thursday (Lecture 9)
author: Taught by Prof. Vikram Pudi
---

# Solving Problems by Searching (contd.)
## Informed Search Algorithms
Best-first search is an informed search algorithm which uses an *evaluation function* $f(n)$ for each node. This function quantifies the "desirability" of a node. Thus the most desirable unexpanded node is followed.  

One special case of this is greedy best-first search, where $f(n)$ is defined to be a heuristic $h(n)$ estimating the cost from $n$ to the goal. This algorithm is neither complete nor optimal. It has time and space complexity $O(b^m)$, but this can be improved by the choice of heuristic.  

$A^*$ search is another special case of best-first search. The evaluation function here incorporates the cost of the path up to the current node, *i.e.*, $f(n) = g(n) + h(n)$, where $g(n)$ is the cost of the node and $h(n)$ is the estimated cost from $n$ to the goal.  
It is complete (unless there are infinitely many nodes $n$ such that $f(n) \leq f(G)$) and optimal. Its time is exponential.

## Heuristics
A heuristic $h(n)$ is *admissible* if it is bounded by the true cost to reach the goal from $n$, *i.e.*, it never overestimates the cost. In other words, it is optimistic.  

It can be proved that if $h(n)$ is admissible, then $A^*$ using tree search is optimal.  
Let $G$ be the optimal goal and suppose some suboptimal goal $G'$ has been generated in the fringe. Let $n$ be an unexpanded node in the fringe.  
Then we have $f(G') > f(G)$, and $h(n) \leq h^*(n)$, the true cost. Adding $g(n)$ to both sides, we have $g(n) + h(n) \leq g(n) + h^*(n)$. This means that $f(n) \leq f(G)$, which in turn means $f(n) < f(G')$. Thus $G'$ will never be expanded.  

Furthermore, a heuristic is consistent if for every node $n$, and every child $n'$ of $n$ generated by $a$,
$$h(n) \leq c(n,a,n') + h(n')$$
holds, where $c$ is the cost function for a step. If $h(n)$ is consistent, then $f(n') > f(n)$, *i.e.*, $f(n)$ is non-decreasing.  

It can be shown that if $h(n)$ is consistent, then $A^*$ using graph search is optimal.  

A heuristic $h_1(n)$ is dominated by another $h_2(n)$ is $h_2(n) \geq h_1(n)$ for all $n$, and both are admissible. This means that $h_2(n)$ is better for a search.