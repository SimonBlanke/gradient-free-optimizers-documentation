!!! example 

    ```python
    from gradient_free_optimizers import GeneticAlgorithmOptimizer

    ...

    opt = GeneticAlgorithmOptimizer(search_space, mutation_rate=0.4, n_parents=3)
    opt.search(objective_function, n_iter=100)
    ```
