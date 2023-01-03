!!! example 

    ```python
    from gradient_free_optimizers import StochasticHillClimbingOptimizer

    ...

    opt = StochasticHillClimbingOptimizer(search_space, epsilon=0.3)
    opt.search(objective_function, n_iter=100)
    ```
