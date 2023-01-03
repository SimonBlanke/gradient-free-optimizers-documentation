!!! example 

    ```python
    from gradient_free_optimizers import TreeStructuredParzenEstimators

    ...

    opt = TreeStructuredParzenEstimators(search_space, gamma_tpe=0.1)
    opt.search(objective_function, n_iter=100)
    ```
