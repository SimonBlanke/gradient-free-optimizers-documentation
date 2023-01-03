!!! example 

    ```python
    from gradient_free_optimizers import BayesianOptimizer

    ...

    opt = BayesianOptimizer(search_space, xi=0.15)
    opt.search(objective_function, n_iter=100)
    ```
