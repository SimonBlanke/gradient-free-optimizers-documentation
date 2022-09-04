# Bayesian Optimization


## Introduction

Bayesian optimization chooses new positions by calculating the expected 
improvement of every position in the search space based on a gaussian process 
that trains on already evaluated positions.



## About the implementation

The bayesian optimizer collects the information about the position and score in each 
iteration. The gaussian process regressor fits to the position (features) and score (target),
and predicts the scores of all unknown positions. This is why the bayesian optimization needs
at least one initial position. The gaussian process returns the standard deviation 
in addition to the prediction (or mean), both of which are required to 
compute the acquisition function.
The position of the best predicted score
is evaluated next. The selected position and its true score is then collected, 
restarting the cycle.



## Parameters

{% include 'parameters/gpr.md' %}

{% include 'parameters/xi.md' %}

{% include 'parameters/warm_start_smbo.md' %}

{% include 'parameters/rand_rest_p.md' %}
