# Genetic Algorithm


## Introduction

A genetic algorithm mimics natural selection by evolving a population of candidate solutions through processes akin to biological reproduction and mutation. Each candidate is evaluated using a fitness function, and the best-performing solutions are selected to create new candidates through crossover and mutation. This iterative process enables the algorithm to explore and exploit the solution space, making it particularly useful for complex or discontinuous landscapes where gradient-based methods fail.


## About the implementation



## Parameters

{% include 'parameters/population.md' %}

{% include 'optimizers/genetic_algorithm/mutation_rate.md' %}

{% include 'optimizers/genetic_algorithm/crossover_rate.md' %}

{% include 'optimizers/genetic_algorithm/n_parents.md' %}

{% include 'optimizers/genetic_algorithm/offspring.md' %}
