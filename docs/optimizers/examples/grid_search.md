!!! example 

    ```python
    from gradient_free_optimizers import GridSearchOptimizer

    ...

    opt = GridSearchOptimizer(search_space, step_size=3)
    opt.search(objective_function, n_iter=100)
    ```
