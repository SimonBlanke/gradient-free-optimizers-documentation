# Hill Climbing


## Introduction

Hill climbing is a very basic optimization technique, that explores the search space only localy. It starts at an initial point, which is often chosen randomly and continues to move to positions with a better solution. It has no method against getting stuck in local optima.



## About the implementation

The hill climbing algorithm is saving the current position in the search space and finds a new position by selecting a random position around it. This is done with a gaussian `distribution`. So if the position is further away the probability of getting selected is lower, but never zero. This makes the hill climbing more heuristic and a bit more adaptable. The standard deviation of the gaussian distribution in each dimension is dependend on the size of the search space in the corresponding dimension. This improves the exploration performance if the sizes of the search space dimensions are differing from each other.



## Parameters

{% include 'parameters/epsilon.md' %}


---

### `distribution`

...

  - type: string
  - default: normal
  - possible values: normal, laplace, logistic, gumbel

---

### `n_neighbours`

...

  - type: int
  - default: 3
  - typical range: 1 ... 10

---


## Characteristics

🟢 Very well adapted to convex optimization problems

🟢 Useful to do finetuning on a good initial starting position

🔴 Expect average/poor results for non-convex problems

🔵 Increase `epsilon` for better global exploration or decrease for local exploration

🔵 The `distribution` changes the behaviour of the hill climbing in multiple ways

🔵 A higher `n_neighbours` slows down the movement through the search space and improves selection of next position
