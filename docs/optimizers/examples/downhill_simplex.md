!!! example 

    ```python
    from gradient_free_optimizers import DownhillSimplexOptimizer

    ...

    opt = DownhillSimplexOptimizer(search_space, alpha=0.5)
    opt.search(objective_function, n_iter=100)
    ```
