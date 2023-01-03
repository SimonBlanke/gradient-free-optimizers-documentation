!!! example 

    ```python
    from gradient_free_optimizers import SpiralOptimization

    ...

    opt = SpiralOptimization(search_space, decay_rate=1.1)
    opt.search(objective_function, n_iter=100)
    ```
