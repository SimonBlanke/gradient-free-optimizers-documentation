!!! example 

    ```python
    from gradient_free_optimizers import LipschitzOptimizer

    ...

    opt = LipschitzOptimizer(search_space)
    opt.search(objective_function, n_iter=100)
    ```
