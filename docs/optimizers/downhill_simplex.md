# Downhill Simplex Optimizer


## Introduction

The downhill simplex optimizer works by grouping `number of dimensions + 1`-positions into a simplex.
The search space is explored by reflecting, expanding, contracting or shrinking the simplex via
the `alpha`, `gamma`, `beta` or `sigma` parameters.



## About the implementation

The **downhill simplex** algorithm works in a completly different way from the other local
hill climbing based optimizers. It is much more complex, because there are 
reflecting-, expanding-, contracting- and shrinking-steps for the iteration 
(before new score is known) and the evaluation (after new score is known). This leads
to a bigger and more complex source code than the hill climbing based algorithms.



## Parameters

{% include 'parameters/alpha.md' %}

{% include 'parameters/gamma.md' %}

{% include 'parameters/beta.md' %}

{% include 'parameters/sigma.md' %}
