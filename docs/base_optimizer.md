# Base Optimizer

This page shows the parameters, methods and attributes that are available to any optimizer-class. You can go to the **Optimization Algorithms** section to get information about the specific parameters and explanations for each optimization algorithm.

## Parameters

The following arguments can be passed to each optimization class:

### `search_space`

- **type:** `dict`

Pass the search_space to the optimizer class to define the space were the optimization algorithm can search for the best parameters for the given objective function.



!!! example
    ```python
    ...

    search_space = {
        "x1": numpy.arange(-10, 31, 0.3),
        "x2": numpy.arange(-10, 31, 0.3),
    }

    opt = HillClimbingOptimizer(search_space)

    ...
    ```

---

### `initialize` 

- **type:** `dict`, `None`
- **default:** `{"grid": 8, "vertices": 8, "random": 4, "warm_start": []}`

An optimization run is split into the initialization phase and iteration phase. The initialization dictionary automatically determines the number of initialization steps. It is the sum if all initialization parameters in the dictionary passed to **initialize**. These parameters are evaluated in the first n iterations. After the initialization phase the optimization run continues with the given algorithm (e.g. hill-climbing). The initialize keywords are the following:

- `grid`: Initializes positions in a grid like pattern. Positions that cannot be put into a grid are randomly positioned.

- `vertices`: Initializes positions at the vertices of the search space. Positions that cannot be put into a vertices are randomly positioned.

- `random`: Number of random initialized positions

- `warm_start`: List of parameter dictionaries that marks additional start points for the optimization run.
  

---

### `random_state` 

- **type:** `int`, `None`
- **default:** `None`

Random state for random processes in the random, numpy and scipy module.

