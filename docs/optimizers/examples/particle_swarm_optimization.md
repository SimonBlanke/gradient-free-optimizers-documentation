!!! example 

    ```python
    from gradient_free_optimizers import ParticleSwarmOptimizer

    ...

    opt = ParticleSwarmOptimizer(search_space, population=5)
    opt.search(objective_function, n_iter=100)
    ```
