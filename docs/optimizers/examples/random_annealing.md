!!! example 

    ```python
    from gradient_free_optimizers import RandomAnnealingOptimizer

    ...

    opt = RandomAnnealingOptimizer(search_space, epsilon=0.2)
    opt.search(objective_function, n_iter=100)
    ```
