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

!!! example
    ```python
    ...

    search_space = {
        "x": numpy.arange(-10, 11, 0.1),
    }

    init_para = {
        "x": 5,
    }

    initialize = {"warm_start": [init_para], "grid": 4, "vertices": 4, "random": 2}

    opt = HillClimbingOptimizer(search_space, initialize=initialize)
    opt.search(objective_function, n_iter=50)
    ...
    ```



---

### `constraints` 

- **type:** `list`, `None`
- **default:** `None`

The constraints-argument accepts a list of functions. These functions contain the same argument as the objective-function to access the parameters from the search-space and returns a boolean value. With these parameters you can set new conditions and boundries for the search-space by returning `True` or `False` depending on the parameters from the argument. If the returning value is true the position in the search-space is valid, but if it is false the position is **not** inside the "valid area" of the search-space.

Optimization algorithms will never select a position inside the constrained area of the search-space to be evaluated inside the objective-function.


!!! example
    ```python
    ...

    search_space = {
        "x1": numpy.arange(-10, 31, 0.3),
        "x2": numpy.arange(-10, 31, 0.3),
    }

    def constraint_1(para):
        # only values in 'x1' higher than -5 are valid
        return para["x1"] > -5

    constraints_list = [constraint_1]

    opt = HillClimbingOptimizer(search_space, constraints=constraints_list)

    ...
    ```


---

### `random_state` 

- **type:** `int`, `None`
- **default:** `None`

Random state for random processes in the random, numpy and scipy module.

