!!! example 

    ```python
    from gradient_free_optimizers import RandomRestartHillClimbingOptimizer

    ...

    opt = RandomRestartHillClimbingOptimizer(search_space, n_iter_restart=20)
    opt.search(objective_function, n_iter=100)
    ```
