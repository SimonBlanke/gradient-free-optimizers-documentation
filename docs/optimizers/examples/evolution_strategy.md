!!! example 

    ```python
    from gradient_free_optimizers import EvolutionStrategyOptimizer

    ...

    opt = EvolutionStrategyOptimizer(search_space, population=15)
    opt.search(objective_function, n_iter=100)
    ```
