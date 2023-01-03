!!! example 

    ```python
    from gradient_free_optimizers import HillClimbingOptimizer

    ...

    opt = HillClimbingOptimizer(search_space, epsilon=0.1)
    opt.search(objective_function, n_iter=100)
    ```
