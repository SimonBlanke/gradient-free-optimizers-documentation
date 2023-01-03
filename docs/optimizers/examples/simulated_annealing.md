!!! example 

    ```python
    from gradient_free_optimizers import SimulatedAnnealingOptimizer

    ...

    opt = SimulatedAnnealingOptimizer(search_space, annealing_rate=0.999)
    opt.search(objective_function, n_iter=100)
    ```
