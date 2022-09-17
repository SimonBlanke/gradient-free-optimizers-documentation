# Spiral Optimization


## Introduction

The **spiral optimization**-algorithm 



## About the implementation



$$
x_i (k+1) = x^* (k) R(\theta) (x_i(k)- x^*(k))
$$




The rotation matrix used for n-dimensional optimization problems is defined as:

$$
R(\theta) = \left[ \begin{matrix}
0^{\top}_{n-1} & -1 \\
I_{n-1} & 0_{n-1}
\end{matrix} \right]
$$



## Parameters

{% include 'parameters/population.md' %}

{% include 'parameters/decay_rate_spiral.md' %}
