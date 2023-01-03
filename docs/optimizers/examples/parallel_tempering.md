!!! example 

    ```python
    from gradient_free_optimizers import ParallelTemperingOptimizer

    ...

    opt = ParallelTemperingOptimizer(search_space, population=20)
    opt.search(objective_function, n_iter=100)
    ```
