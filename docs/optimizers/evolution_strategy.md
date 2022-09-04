# Evolution Strategy


## Introduction

Evolution strategy mutates and combines the best individuals of a population across a 
number of generations without transforming them into an array of bits 
(like genetic algorithms) but uses the real values of the positions.



## About the implementation

The mutation part of the evolution strategy optimizer is a regular hill climbing algorithm.
The crossover works by combining the best positions to get new ones. The worst positions 
are removed to preserve the number of individuals in the population.



## Parameters

{% include 'parameters/population.md' %}

{% include 'parameters/mutation_rate.md' %}

{% include 'parameters/crossover_rate.md' %}

{% include 'parameters/rand_rest_p.md' %}
