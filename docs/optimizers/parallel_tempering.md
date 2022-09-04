# Parallel Tempering


## Introduction

Parallel Tempering initializes multiple simulated annealing searches with different 
temperatures and chooses to swap those temperatures with a probability based on 
its temperature and difference of current scores.



## About the implementation

The population of the parallel tempering optimizer consists of multiple initializations
of the simulated annealing optimizer class. Each of those receives a random starting temperature.
The algorithm calculates the probability of swapping temperatures
for every combination of annealer instances. 



## Parameters

{% include 'parameters/population.md' %}

{% include 'parameters/n_iter_swap.md' %}

{% include 'parameters/rand_rest_p.md' %}
