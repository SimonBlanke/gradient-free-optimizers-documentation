!!! example 

    ```python
    from gradient_free_optimizers import PowellsMethod

    ...

    opt = PowellsMethod(search_space, iters_p_dim=15)
    opt.search(objective_function, n_iter=100)
    ```
