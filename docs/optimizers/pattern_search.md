# Pattern Search


## Introduction

The pattern search works by initializing a cross-shaped collection of positions in the 
search space. When all positions in the cross are evaluated the center of the cross moves
to the best position. This leads to new positions inside the cross that have not been
evaluated. If non of the positions have a better score than the center position the cross
shrinks by the `reduction`-factor creating new positions inside the cross.



## About the implementation

Similar to a population based optimization algorithm the pattern search has a list of information 
about the positions and their scores to form the pattern. 
As the pattern moves through the search space this information gets updated.



## Parameters

{% include 'parameters/n_positions.md' %}

{% include 'parameters/pattern_size.md' %}

{% include 'parameters/reduction.md' %}
