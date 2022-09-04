# Stochastic Hill Climbing


## Introduction

Stochastic hill climbing extends the normal hill climbing by a simple method against getting 
stuck in local optima. It has a parameter `p_accept` you can set, 
that determines the probability to 
accept worse solutions as a next position. 
This should enable the stochastic hill climbing to find better solutions in
a non-convex optimization problem over many iterations.


## About the implementation

The stochastic hill climbing inherits the behaviour of the regular hill climbing algorithm and
adds its additional functionality after the evaluation of the score is done. 
The stochastic part of the algorithm gets activated of the new score is not better than
the previous one.



## Parameters

{% include 'parameters/epsilon.md' %}

{% include 'parameters/distribution.md' %}

{% include 'parameters/n_neighbours.md' %}

{% include 'parameters/p_accept.md' %}


