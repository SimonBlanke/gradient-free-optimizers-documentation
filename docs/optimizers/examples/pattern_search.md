!!! example 

    ```python
    from gradient_free_optimizers import PatternSearch

    ...

    opt = PatternSearch(search_space, n_positions=2)
    opt.search(objective_function, n_iter=100)
    ```
