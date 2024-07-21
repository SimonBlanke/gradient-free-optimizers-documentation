!!! example 

    ```python
    from gradient_free_optimizers import DifferentialEvolutionOptimizer

    ...

    opt = DifferentialEvolutionOptimizer(search_space, mutation_rate=0.8)
    opt.search(objective_function, n_iter=100)
    ```
