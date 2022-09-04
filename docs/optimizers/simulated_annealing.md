# Simulated Annealing


## Introduction

Simulated annealing chooses its next possible position similar to hill climbing, but it accepts 
worse results with a probability that decreases with time.
It simulates a temperature that decreases with each iteration, similar to a material cooling down.



## About the implementation

The **simulated annealing** algorithm inherits the methods from the regular hill climbing.
Similar to stochastic hill climbing it may accept a worse position with the goal of
escaping a local optimum. The `start_temp` is a factor for the probability of accepting 
a worse position. This probability decreases over time, because of the ànnealing_rate`
decreasing the `start_temp` over time.



## Parameters

{% include 'parameters/epsilon.md' %}

{% include 'parameters/distribution.md' %}

{% include 'parameters/n_neighbours.md' %}

{% include 'parameters/n_neighbours.md' %}

{% include 'parameters/n_neighbours.md' %}

