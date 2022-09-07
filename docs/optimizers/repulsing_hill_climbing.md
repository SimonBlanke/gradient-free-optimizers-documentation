# Repulsing Hill Climbing


## Introduction

The **repulsing hill climbing** optimization algorithm improves the normal hill 
climbing by adding a way to escape local optimia. If no better position is 
found within the next `n_neighbours` positions the algorithm will increase 
`epsilon` by multiplying the `repulsion_factor` for the next iteration.



## About the implementation

Similar to other hill climbing based algorithms the **repulsing hill climbing**
inherits the methods from the regular hill climbing and adds a functionality to
escape local optima. The repulsing hill climbing temporally increases `epsilon`
to jump out of the current region.



## Parameters

{% include 'parameters/epsilon.md' %}

{% include 'parameters/distribution.md' %}

{% include 'parameters/n_neighbours.md' %}

{% include 'parameters/repulsion_factor.md' %}

