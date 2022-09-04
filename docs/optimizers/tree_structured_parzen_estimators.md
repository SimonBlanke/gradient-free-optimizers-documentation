# Tree Structured Parzen Estimators


## Introduction

Tree of Parzen Estimators also chooses new positions by calculating the expected improvement. 
It does so by calculating the ratio of probability being among the best positions and 
the worst positions. Those probabilities are determined with a kernel density estimator,
that is trained on alrady evaluated positions.



## About the implementation

Similar to other sequence-model-based optimization algorithms the positions and scores 
of previous evaluations are saved as features and targets to train a machine learning algorithm.
For the tree structured parzen estimators we use two kernel density estimators that get
the training data from the best and worst positions to calculate the expected improvement.



## Parameters

{% include 'parameters/gamma_tpe.md' %}

{% include 'parameters/warm_start_smbo.md' %}

{% include 'parameters/rand_rest_p.md' %}
