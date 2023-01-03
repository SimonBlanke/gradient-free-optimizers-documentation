!!! example 

    ```python
    from gradient_free_optimizers import ForestOptimizer

    ...

    opt = ForestOptimizer(search_space, xi=0.15)
    opt.search(objective_function, n_iter=100)
    ```
