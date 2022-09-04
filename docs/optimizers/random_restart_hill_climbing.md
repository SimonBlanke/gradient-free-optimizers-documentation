# Random Restart Hill ClimbingOptimizer


## Introduction

Random restart hill climbing works by starting a hill climbing search and jumping to a random 
new position after `n_iter_restart` iterations. 
Those restarts should prevent the algorithm getting stuck in local optima.



## About the implementation

The random restart hill climbing inherits its behaviour from the regular hill climbing and 
expands it by jumping to a random position during the iteration step. 



## Parameters

{% include 'parameters/epsilon.md' %}

{% include 'parameters/distribution.md' %}

{% include 'parameters/n_neighbours.md' %}

{% include 'parameters/n_iter_restart.md' %}
