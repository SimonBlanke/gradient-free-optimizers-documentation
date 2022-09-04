# Forest Optimization

## Introduction

The forest-optimizer calculates the expected improvement of the position space with a 
tree-based model. This optimization technique is very similar to bayesian-optimization
in every part, except its model.



## About the implementation

implementation_ = """
The forest-optimizer shares most of its code base with the bayesian-optimizer. Only its model, to 
calculate the expected score and its standard deviation is different. Tree based models do not 
calculate the standard deviation by them self. A modification is necessary to determine the
standard deviation from the impurity of the trees in the ensemble.



## Parameters

{% include 'parameters/tree_regressor.md' %}

{% include 'parameters/xi.md' %}

{% include 'parameters/warm_start_smbo.md' %}

{% include 'parameters/rand_rest_p.md' %}



