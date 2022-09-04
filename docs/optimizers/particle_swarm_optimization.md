# Particle Swarm Optimization


## Introduction

Particle swarm optimization works by initializing a number of positions in the search space,
which move according to their own ineratia, the attraction to their own known best positions
and the global best position.



## About the implementation

The particle swarm optimizer initializes multiple particle classes, which inherit from
the hill-climbing class. In the current version all movement-calculations are contained in
the particle class. Particles have a velocity, which they maintain even without attraction
to other particles via `cognitive_weight` or `social_weight`.



## Parameters

{% include 'parameters/population.md' %}

{% include 'parameters/inertia.md' %}

{% include 'parameters/cognitive_weight.md' %}

{% include 'parameters/social_weight.md' %}

{% include 'parameters/rand_rest_p.md' %}
