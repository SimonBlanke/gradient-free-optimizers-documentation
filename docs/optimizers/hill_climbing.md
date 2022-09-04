# Hill Climbing


## Introduction

Hill climbing is a very basic optimization technique, that explores the search space only localy. It starts at an initial point, which is often chosen randomly and continues to move to positions with a better solution. It has no method against getting stuck in local optima.



## About the implementation

The hill climbing algorithm is saving the current position in the search space and finds a new position by selecting a random position around it. This is done with a gaussian `distribution`. So if the position is further away the probability of getting selected is lower, but never zero. This makes the hill climbing more heuristic and a bit more adaptable. The standard deviation of the gaussian distribution in each dimension is dependend on the size of the search space in the corresponding dimension. This improves the exploration performance if the sizes of the search space dimensions are differing from each other.



## Parameters

{% include 'parameters/epsilon.md' %}

{% include 'parameters/distribution.md' %}

{% include 'parameters/n_neighbours.md' %}

